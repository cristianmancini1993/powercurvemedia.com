#!/usr/bin/env python3
"""Generate TrimOne landing + thank-you pages for RO, CZ, HU, SK, PL."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IT_INDEX = ROOT / "it" / "trimone" / "index.html"
IT_THANKYOU = ROOT / "it" / "trimone" / "thank-you.html"
WEBHOOK = "https://hook.eu2.make.com/ut8j6klzjnsa9tspsaszuppyttaqyaxm"
UID = "019f60bd-7f67-709f-a69c-8041b92c05ba"
CPA_EUR = 21

GEOS = [
    {
        "geo": "ro",
        "lang": "ro",
        "offer": "151",
        "price": 399,
        "currency": "RON",
        "was": "1.299 RON",
        "now": "399 RON",
        "cta_price": "399 RON",
    },
    {
        "geo": "cz",
        "lang": "cs",
        "offer": "152",
        "price": 1999,
        "currency": "CZK",
        "was": "6.599 Kč",
        "now": "1.999 Kč",
        "cta_price": "1.999 Kč",
    },
    {
        "geo": "hu",
        "lang": "hu",
        "offer": "153",
        "price": 29999,
        "currency": "HUF",
        "was": "99.999 Ft",
        "now": "29.999 Ft",
        "cta_price": "29.999 Ft",
    },
    {
        "geo": "sk",
        "lang": "sk",
        "offer": "154",
        "price": 79.99,
        "currency": "EUR",
        "was": "249,99 €",
        "now": "79,99 €",
        "cta_price": "79,99 €",
    },
    {
        "geo": "pl",
        "lang": "pl",
        "offer": "155",
        "price": 349,
        "currency": "PLN",
        "was": "999 zł",
        "now": "349 zł",
        "cta_price": "349 zł",
    },
]


def price_js(price: float | int) -> str:
    if isinstance(price, float) and not price.is_integer():
        return f"{price:.2f}"
    if float(price) == int(price):
        return str(int(price))
    return f"{float(price):.2f}"


T: dict[str, dict[str, str | list]] = {
    "ro": {
        "title": "TrimOne™ — Motocoasă Fără Fir 3000W | -70% Doar Azi",
        "meta_desc": "TrimOne™: motocoasă cu baterie ultra-ușoară de 1,2 kg cu 2 baterii 60V. Putere 3000W, livrare gratuită 24h, plată la livrare.",
        "og_title": "TrimOne™ — Motocoasă fără fir | -70% Doar Azi",
        "og_desc": "Taie, finisează și modelează cu precizie milimetrică. 2 baterii 60V incluse. Plată la livrare.",
        "img_alt": "TrimOne motocoasă fără fir",
        "topbar": "DOAR AZI: -70% + LIVRARE GRATUITĂ ÎN 24H — PLATĂ LA LIVRARE",
        "rating": "Peste <strong>15.000</strong> clienți mulțumiți în România",
        "gift": "🎁 CADOU: 1 baterie litiu-ion 60V extra!",
        "h1_hl": "Grădina pe care ai visat-o mereu, în câteva minute și fără niciun efort",
        "lead": "Taie, finisează și modelează cu precizie milimetrică. Uită de oboseala uneltelor vechi: cu o greutate de doar <strong>1,2 kg</strong> și <strong>2 baterii litiu-ion de 60V</strong>, îngrijirea gazonului devine rapidă și plăcută.",
        "cta_hero": "DA, VREAU TRIMONE™ →",
        "form_note": "🔒 Fără plată în avans · Plătești doar la livrare",
        "f1t": "Livrare gratuită", "f1d": "24/48 ore în toată România",
        "f2t": "Plată la livrare", "f2d": "Plătești doar când primești",
        "f3t": "4 ani garanție", "f3d": "Protecție completă inclusă",
        "f4t": "14 zile retur", "f4d": "Mulțumit sau banii înapoi",
        "eyebrow": "De ce TrimOne™",
        "reasons_h2": "4 motive pentru care vei schimba modul în care îți îngrijești grădina",
        "r1t": "Dublă autonomie: 2 baterii 60V", "r1p": "Folosești una în timp ce cealaltă se încarcă. Lucrezi fără întreruperi — grădina ta nu așteaptă.",
        "r2t": "Putere 3000W fără fir", "r2p": "Motorul Brushless™ oferă forța unei motocoase pe benzină. Taie oriunde, fără cabluri încurcate și fără să cauți priza.",
        "r3t": "Gata în 3 secunde", "r3p": "Introdu bateria, apasă butonul și ești gata. Mâner telescopic și cap rotativ 180° ajung acolo unde altele nu pot.",
        "r4t": "Greutate record — 1,2 kg", "r4p": "Proiectat pentru a fi ridicat cu o singură mână. Putere silențioasă, zero emisii — protejează-ți spatele și lucra ore fără să te obosești.",
        "countdown": "⏰ Reducerea -70% expiră în",
        "cd_h": "Ore", "cd_m": "Min", "cd_s": "Sec",
        "stock_l": "Disponibilitate în stoc", "stock_r": "Au rămas doar 3 bucăți!",
        "live_word": "persoane", "live_suffix": "vizualizează această ofertă acum",
        "order_h2": "Completează formularul pentru a comanda",
        "order_p": "Introdu datele tale mai jos — te contactăm pentru confirmare. Pregătește <strong>{price}</strong> numerar pentru curier.",
        "lbl_name": "Nume și prenume*", "lbl_tel": "Număr de telefon*", "lbl_addr": "Adresă de livrare*",
        "ph_name": "Ion Popescu", "ph_tel": "+40 712 345 678", "ph_addr": "Str. Victoriei 10, București 010001",
        "cta_form": "DA, COMAND TRIMONE™ CU {price}",
        "reviews_eyebrow": "Recenzii", "reviews_h2": "Ce spun clienții noștri",
        "rev_alt": "Recenzie client TrimOne",
        "rev1": "«M-am săturat să mă lupt cu vechea motocoasă pe benzină, grea și zgomotoasă. TrimOne™ cântărește foarte puțin — o ridic cu o mână! — și taie iarba înaltă fără ezitare. Mânerul telescopic mă permite să lucrez în picioare. O achiziție pe care o repet!»",
        "rev2": "«Cel mai bun lucru sunt cele două baterii incluse: folosesc una în timp ce cealaltă se încarcă. Cu peria de oțel am curățat aleile de buruieni. Foarte practică și capul rotativ pentru margini.»",
        "rev3": "«Locuiesc într-un cartier și nu voiam să deranjez vecinii duminica dimineața. TrimOne™ este incredibil de silențios, dar are o putere neașteptată. Recomand tuturor!»",
        "verified_m": "Client verificat", "verified_f": "Clientă verificată",
        "kit_eyebrow": "În cutie", "kit_h2": "Kitul tău complet TrimOne™",
        "kit_alt": "Kit complet TrimOne",
        "kit_items": [
            "1× TrimOne™ Professional — corp ultra-ușor (1,2 kg) cu motor Brushless",
            "2× baterii litiu-ion 60V (1 CADOU) — dublă autonomie",
            "1× încărcător ultra-rapid",
            "1× disc dințat din oțel călit — crengi și tufișuri",
            "2× lame Precision-Cut din oțel inox",
            "1× cap multifilament pentru finisarea marginilor",
            "1× perie rotativă din oțel (CADOU) — alei și rosturi",
            "Garanție oficială de 4 ani",
        ],
        "faq_h2": "Întrebări frecvente",
        "faqs": [
            ("Cât durează bateria TrimOne™?", "Fiecare baterie oferă aproximativ 30–40 de minute de lucru continuu. În kit găsești 2 baterii — autonomie totală de peste o oră."),
            ("Este greu de montat sau folosit?", "Deloc. Montajul durează mai puțin de 2 minute. Introdu bateria, reglează mânerul telescopic și ești gata."),
            ("Poate tăia și crengi mici?", "Da, sistemul 4-în-1 este foarte versatil. Lamele din oțel taie tufișuri mici, peria rotativă îndepărtează buruienile."),
            ("Este zgomotos? Pot folosi în bloc?", "Motorul Brushless este extrem de silențios față de modelele pe benzină. Poți lucra oricând fără să deranjezi vecinii."),
            ("Ce se întâmplă dacă am o problemă?", "Oferim 4 ani garanție și asistență dedicată. Ai 14 zile pentru retur simplu dacă nu ești mulțumit."),
            ("Care sunt termenele și costurile de livrare?", "Livrarea este complet gratuită în toată România! Comanda este procesată în 24 de ore și livrată în 24/48 ore lucrătoare."),
        ],
        "footer_tag": "Produse utile pentru viața de zi cu zi, livrare în 24–48 ore cu plată la livrare.",
        "footer_info": "Informații", "footer_contact": "Contact",
        "footer_about": "Despre noi", "footer_contact_link": "Contactează-ne",
        "footer_privacy": "Politica de Confidențialitate", "footer_terms": "Termeni și Condiții",
        "footer_cookie": "Politica Cookie-uri", "footer_ship": "Politica de Livrare", "footer_refund": "Politica de Returnare",
        "footer_rights": "Toate drepturile rezervate.",
        "ty_title": "Comandă înregistrată — Așteaptă apelul de confirmare | TrimOne™",
        "ty_desc": "Comanda ta TrimOne™ a fost înregistrată. Mai rămâne un ultim pas: răspunde la apelul de confirmare.",
        "ty_h1": "Comanda ta a fost înregistrată cu succes!",
        "ty_sub": "Perfect — comanda ta TrimOne™ este în procesare. Mai rămâne doar <strong>un ultim pas</strong> pentru finalizare și expediere.",
        "ty_hero_alt": "Echipa powercurvemedia: call center și logistică COD",
        "ty_eyebrow": "👇 Ce trebuie să faci acum",
        "ty_action_t": "📞 Răspunde la apelul de confirmare",
        "ty_action_b": "Un operator te va contacta <strong>în următoarele ore</strong> pentru a confirma comanda.",
        "ty_warn": "Dacă nu răspunzi la apel, comanda va fi anulată automat.",
        "ty_hours_h": "🕒 Program de contact",
        "ty_hours": "<strong>Luni – Sâmbătă</strong> · 9:00 – 18:00",
        "ty_next_h": "📋 Ce urmează",
        "ty_s1": "Răspunde la apel și <strong>confirmă datele tale</strong>",
        "ty_s2": "Comanda va fi expediată în <strong>24–48 de ore</strong>",
        "ty_s3": "Livrare la domiciliu și <strong>plată la livrare ({price})</strong>",
        "ty_b1": "🔒 Plată la livrare", "ty_b2": "🛡️ Garanție 4 ani", "ty_b3": "🔐 Protecție SSL",
        "cookie_text": "Folosim cookie-uri tehnice și de terți pentru a îmbunătăți experiența ta.",
        "cookie_accept": "Accept", "cookie_learn": "Află mai mult",
    },
    "cz": {
        "title": "TrimOne™ — Akumulátorový Křovinořez 3000W | -70% Jen Dnes",
        "meta_desc": "TrimOne™: ultralehký akumulátorový křovinořez 1,2 kg se 2 bateriemi 60V. Výkon 3000W, doprava zdarma 24h, platba na dobírku.",
        "og_title": "TrimOne™ — Křovinořez bez kabelu | -70% Jen Dnes",
        "og_desc": "Stříhejte, upravujte a tvarujte s milimetrovou přesností. 2 baterie 60V v balení. Platba na dobírku.",
        "img_alt": "TrimOne akumulátorový křovinořez",
        "topbar": "JEN DNES: -70% + DOPRAVA ZDARMA DO 24H — PLATBA NA DOBÍRKU",
        "rating": "Více než <strong>15 000</strong> spokojených zákazníků v Česku",
        "gift": "🎁 ZDARMA: 1 extra lithiová baterie 60V!",
        "h1_hl": "Zahrada, o které jste vždy snili, během pár minut a bez námahy",
        "lead": "Stříhejte, upravujte a tvarujte s milimetrovou přesností. Zapomeňte na staré nářadí: s hmotností pouhých <strong>1,2 kg</strong> a <strong>2 lithiovými bateriemi 60V</strong> je péče o trávník rychlá a snadná.",
        "cta_hero": "ANO, CHCI TRIMONE™ →",
        "form_note": "🔒 Bez platby předem · Platíte až při převzetí",
        "f1t": "Doprava zdarma", "f1d": "24/48 hodin po celé ČR",
        "f2t": "Platba na dobírku", "f2d": "Platíte až kurýrovi",
        "f3t": "4 roky záruky", "f3d": "Kompletní ochrana v ceně",
        "f4t": "14 dní na vrácení", "f4d": "Spokojeni nebo vrácení peněz",
        "eyebrow": "Proč TrimOne™",
        "reasons_h2": "4 důvody, proč změníte způsob péče o zahradu",
        "r1t": "Dvojitá výdrž: 2 baterie 60V", "r1p": "Jednu používáte, druhá se nabíjí. Pracujete bez přestávek — vaše zahrada nečeká.",
        "r2t": "Výkon 3000W bez kabelu", "r2p": "Motor Brushless™ má sílu benzínového křovinořezu. Stříhejte kdekoli bez zamotaných kabelů a bez hledání zásuvky.",
        "r3t": "Připraven za 3 sekundy", "r3p": "Vložte baterii, stiskněte tlačítko a jste připraveni. Teleskopická rukojeť a hlava 180° dosáhnou tam, kde jiné nářadí nestačí.",
        "r4t": "Rekordní lehkost — 1,2 kg", "r4p": "Navržen pro zvednutí jednou rukou. Tichý výkon, nulové emise — chraňte záda a pracujte hodiny bez únavy.",
        "countdown": "⏰ Sleva -70% končí za",
        "cd_h": "Hod", "cd_m": "Min", "cd_s": "Sek",
        "stock_l": "Dostupnost skladem", "stock_r": "Zbývají jen 3 kusy!",
        "live_word": "lidí", "live_suffix": "si právě prohlíží tuto nabídku",
        "order_h2": "Vyplňte formulář pro objednávku",
        "order_p": "Vyplňte údaje níže — ozveme se vám pro potvrzení. Připravte si <strong>{price}</strong> v hotovosti pro kurýra.",
        "lbl_name": "Jméno a příjmení*", "lbl_tel": "Telefonní číslo*", "lbl_addr": "Doručovací adresa*",
        "ph_name": "Jan Novák", "ph_tel": "+420 601 234 567", "ph_addr": "Václavské nám. 1, 110 00 Praha",
        "cta_form": "ANO, OBJEDNÁVÁM TRIMONE™ ZA {price}",
        "reviews_eyebrow": "Recenze", "reviews_h2": "Co říkají naši zákazníci",
        "rev_alt": "Recenze zákazníka TrimOne",
        "rev1": "«Měl jsem dost boje se starým benzínovým křovinořezem, těžkým a hlučným. TrimOne™ váží velmi málo — zvedám ho jednou rukou! — a bez váhání seká vysokou trávu. Teleskopická rukojeť mi umožňuje pracovat vestoje. Nákup, který bych zopakoval!»",
        "rev2": "«Nejlepší jsou dvě baterie v balení: jednu používám, zatímco se druhá nabíjí. Ocelovým kartáčem jsem vyčistil chodník od plevele. Velmi praktická otočná hlava pro okraje trávníku.»",
        "rev3": "«Bydlím v řadovce a nechtěla jsem rušit sousedy v neděli ráno. TrimOne™ je neuvěřitelně tichý, ale má sílu, kterou od akumulátorového nářadí nečekáte. Doporučuji!»",
        "verified_m": "Ověřený zákazník", "verified_f": "Ověřená zákaznice",
        "kit_eyebrow": "V balení", "kit_h2": "Váš kompletní kit TrimOne™",
        "kit_alt": "Kompletní kit TrimOne",
        "kit_items": [
            "1× TrimOne™ Professional — ultralehké tělo (1,2 kg) s motorem Brushless",
            "2× lithiové baterie 60V (1 ZDARMA) — dvojitá výdrž",
            "1× ultra-rychlé nabíječky",
            "1× ozubený kotouč z kalené oceli — větve a keře",
            "2× čepele Precision-Cut z nerezové oceli",
            "1× multifilamentová hlava pro okraje",
            "1× rotační ocelový kartáč (ZDARMA) — chodníky a spáry",
            "Oficiální 4letá záruka",
        ],
        "faq_h2": "Často kladené otázky",
        "faqs": [
            ("Jak dlouho vydrží baterie TrimOne™?", "Každá baterie zaručuje přibližně 30–40 minut nepřetržité práce. V balení jsou 2 baterie — celková výdrž přes hodinu."),
            ("Je složité ho sestavit nebo používat?", "Vůbec ne. Sestavení trvá méně než 2 minuty. Vložte baterii, nastavte teleskopickou rukojeť a jste připraveni."),
            ("Umí řezat i malé větve?", "Díky systému 4-v-1 je velmi univerzální. Ocelové čepele řežou keře, rotační kartáč odstraňuje plevel."),
            ("Je hlučný? Mohu ho používat v bytovce?", "Motor Brushless je extrémně tichý oproti benzínovým modelům. Můžete pracovat kdykoli bez rušení sousedů."),
            ("Co když budu mít problém s produktem?", "Nabízíme 4 roky záruky a podporu. Máte 14 dní na snadné vrácení."),
            ("Jaké jsou termíny a náklady doručení?", "Doručení je zcela zdarma po celé ČR! Objednávka je zpracována do 24 hodin a doručena do 24/48 hodin."),
        ],
        "footer_tag": "Užitečné produkty pro každodenní život, doručení za 24–48 hodin s platbou na dobírku.",
        "footer_info": "Informace", "footer_contact": "Kontakt",
        "footer_about": "O nás", "footer_contact_link": "Kontaktujte nás",
        "footer_privacy": "Zásady ochrany osobních údajů", "footer_terms": "Obchodní podmínky",
        "footer_cookie": "Zásady cookies", "footer_ship": "Zásady doručení", "footer_refund": "Zásady vrácení",
        "footer_rights": "Všechna práva vyhrazena.",
        "ty_title": "Objednávka přijata — Čekejte na potvrzovací hovor | TrimOne™",
        "ty_desc": "Vaše objednávka TrimOne™ byla zaregistrována. Zbývá poslední krok: přijměte potvrzovací hovor.",
        "ty_h1": "Vaše objednávka byla úspěšně zaregistrována!",
        "ty_sub": "Skvělé — vaše objednávka TrimOne™ se zpracovává. Zbývá jen <strong>poslední krok</strong> k dokončení a odeslání.",
        "ty_hero_alt": "Tým powercurvemedia: call centrum a logistika COD",
        "ty_eyebrow": "👇 Co teď udělat",
        "ty_action_t": "📞 Přijměte potvrzovací hovor",
        "ty_action_b": "Náš operátor vás kontaktuje <strong>v následujících hodinách</strong> pro potvrzení objednávky.",
        "ty_warn": "Pokud hovor nepřijmete, objednávka bude automaticky zrušena.",
        "ty_hours_h": "🕒 Kontaktní hodiny",
        "ty_hours": "<strong>Pondělí – Sobota</strong> · 9:00 – 18:00",
        "ty_next_h": "📋 Co bude dál",
        "ty_s1": "Přijměte hovor a <strong>potvrďte své údaje</strong>",
        "ty_s2": "Objednávka bude odeslána do <strong>24–48 hodin</strong>",
        "ty_s3": "Doručení domů a <strong>platba na dobírku ({price})</strong>",
        "ty_b1": "🔒 Platba na dobírku", "ty_b2": "🛡️ Záruka 4 roky", "ty_b3": "🔐 Ochrana SSL",
        "cookie_text": "Používáme technické a analytické cookies pro zlepšení vašeho zážitku.",
        "cookie_accept": "Přijímám", "cookie_learn": "Zjistit více",
    },
    "hu": {
        "title": "TrimOne™ — Vezeték Nélküli Fűkasza 3000W | -70% Csak Ma",
        "meta_desc": "TrimOne™: ultrakönnyű akkumulátoros fűkasza 1,2 kg, 2× 60V batteriával. 3000W teljesítmény, ingyenes szállítás 24h, utánvétes fizetés.",
        "og_title": "TrimOne™ — Vezeték nélküli fűkasza | -70% Csak Ma",
        "og_desc": "Vágjon, formáljon és precízen dolgozzon. 2× 60V batteria a csomagban. Utánvétes fizetés.",
        "img_alt": "TrimOne vezeték nélküli fűkasza",
        "topbar": "MA CSAK: -70% + INGYENES SZÁLLÍTÁS 24H — UTÁNVÉTES FIZETÉS",
        "rating": "Több mint <strong>15 000</strong> elégedett vásárló Magyarországon",
        "gift": "🎁 AJÁNDÉK: 1 extra 60V lítium-ion batteria!",
        "h1_hl": "Az álmaid kertje, percek alatt és erőfeszítés nélkül",
        "lead": "Vágjon, formáljon és dolgozzon milliméteres pontossággal. Felejtse el a régi szerszámok fáradalmát: mindössze <strong>1,2 kg</strong> súllyal és <strong>2× 60V lítium-ion batteriával</strong> a gyepápolás gyors és könnyű élmény.",
        "cta_hero": "IGEN, KÉREM A TRIMONE™-T →",
        "form_note": "🔒 Nincs előleg · Csak átvételkor fizet",
        "f1t": "Ingyenes szállítás", "f1d": "24/48 óra Magyarországon",
        "f2t": "Utánvétes fizetés", "f2d": "Csak átvételkor fizet",
        "f3t": "4 év garancia", "f3d": "Teljes körű védelem",
        "f4t": "14 napos visszaküldés", "f4d": "Elégedett vagy visszatérítés",
        "eyebrow": "Miért TrimOne™",
        "reasons_h2": "4 ok, amiért megváltoztatja a kertgondozást",
        "r1t": "Dupla üzemidő: 2× 60V batteria", "r1p": "Az egyiket használja, míg a másik tölt. Folyamatos munka — a kert nem vár.",
        "r2t": "3000W vezeték nélkül", "r2p": "A Brushless™ motor benzines fűkasza erejét adja. Vágjon bárhol, kábelek és konnektor nélkül.",
        "r3t": "3 másodperc és kész", "r3p": "Batteria be, gomb meg — már dolgozhat. Teleszkópos kar és 180°-os fej elér oda, ahol más nem.",
        "r4t": "Rekord súly — 1,2 kg", "r4p": "Egy kézzel emelhető. Csendes, nulla kibocsátás — óvja a hátát, dolgozzon órákig fáradtság nélkül.",
        "countdown": "⏰ A -70% kedvezmény lejár",
        "cd_h": "Óra", "cd_m": "Perc", "cd_s": "Mp",
        "stock_l": "Raktárkészlet", "stock_r": "Már csak 3 darab maradt!",
        "live_word": "ember", "live_suffix": "nézi ezt az ajánlatot most",
        "order_h2": "Töltse ki az űrlapot a rendeléshez",
        "order_p": "Adja meg az adatait — felhívjuk a megerősítéshez. Készítsen <strong>{price}</strong> készpénzt a futárnak.",
        "lbl_name": "Teljes név*", "lbl_tel": "Telefonszám*", "lbl_addr": "Szállítási cím*",
        "ph_name": "Kovács István", "ph_tel": "+36 30 123 4567", "ph_addr": "Andrássy út 12, Budapest 1061",
        "cta_form": "IGEN, RENDELEM A TRIMONE™-T {price}",
        "reviews_eyebrow": "Vélemények", "reviews_h2": "Mit mondanak vásárlóink",
        "rev_alt": "TrimOne vásárlói vélemény",
        "rev1": "«Elegem volt a régi benzines fűkaszával, nehéz és zajos. A TrimOne™ szinte semmit nyom — egy kézzel emelem! — és magas füvet is könnyen vág. A teleszkópos karral állva dolgozhatok. Ezerszer megvenném!»",
        "rev2": "«A két batteria a legjobb: az egyiket használom, míg a másik tölt. Acélkefével kitisztítottam a járdát a fű közül. A forgatható fej praktikus a szélekhez.»",
        "rev3": "«Sorházban lakom, nem akartam zavarni a szomszédokat vasárnap reggel. A TrimOne™ hihetetlenül csendes, de olyan erős, amit batteriás géptől nem vársz. Mindenkinek ajánlom!»",
        "verified_m": "Ellenőrzött vásárló", "verified_f": "Ellenőrzött vásárló",
        "kit_eyebrow": "A csomagban", "kit_h2": "A teljes TrimOne™ készlet",
        "kit_alt": "Teljes TrimOne készlet",
        "kit_items": [
            "1× TrimOne™ Professional — ultrakönnyű test (1,2 kg) Brushless motorral",
            "2× 60V lítium-ion batteria (1 AJÁNDÉK) — dupla üzemidő",
            "1× ultra-gyors töltő",
            "1× edzett acél fogazott tárcsa — ágak és cserjék",
            "2× Precision-Cut rozsdamentes acél penge",
            "1× multifilament fej a szélekhez",
            "1× forgó acélkefe (AJÁNDÉK) — járdák és fugák",
            "Hivatalos 4 év garancia",
        ],
        "faq_h2": "Gyakori kérdések",
        "faqs": [
            ("Mennyi ideig tart a batteria?", "Minden batteria kb. 30–40 perc folyamatos munkát biztosít. A készletben 2 batteria van — összesen több mint egy óra üzemidő."),
            ("Nehéz összeszerelni vagy használni?", "Egyáltalán nem. Összeszerelés kevesebb mint 2 perc. Batteria be, teleszkópos kar állítás — kész."),
            ("Vág kis ágakat is?", "A 4-in-1 rendszer nagyon univerzális. Acél pengék kis cserjéket vágnak, a forgó kefe eltávolítja a füvet a járdáról."),
            ("Zajos? Használhatom társasházban?", "A Brushless motor rendkívül csendes a benzines gépeknél. Bármikor dolgozhat anélkül, hogy zavarná a szomszédokat."),
            ("Mi van, ha probléma van a termékkel?", "4 év garanciát és dedikált támogatást kínálunk. 14 nap egyszerű visszaküldés, ha nem elégedett."),
            ("Milyen a szállítás ideje és költsége?", "A szállítás teljesen ingyenes Magyarországon! Rendelés 24 órán belül feldolgozva, kiszállítás 24/48 munkanapon belül."),
        ],
        "footer_tag": "Hasznos termékek a mindennapokhoz, 24–48 órás szállítás utánvéttel.",
        "footer_info": "Információ", "footer_contact": "Kapcsolat",
        "footer_about": "Rólunk", "footer_contact_link": "Kapcsolatfelvétel",
        "footer_privacy": "Adatvédelmi irányelvek", "footer_terms": "Általános szerződési feltételek",
        "footer_cookie": "Cookie szabályzat", "footer_ship": "Szállítási szabályzat", "footer_refund": "Visszatérítési szabályzat",
        "footer_rights": "Minden jog fenntartva.",
        "ty_title": "Rendelés rögzítve — Várja a megerősítő hívást | TrimOne™",
        "ty_desc": "TrimOne™ rendelésed rögzítve. Utolsó lépés: fogadja a megerősítő hívást.",
        "ty_h1": "Rendelésed sikeresen rögzítve!",
        "ty_sub": "Rendben — TrimOne™ rendelésed feldolgozás alatt. Már csak <strong>egy utolsó lépés</strong> a befejezéshez és szállításhoz.",
        "ty_hero_alt": "A powercurvemedia csapata: call center és COD logisztika",
        "ty_eyebrow": "👇 Mit kell tenned most",
        "ty_action_t": "📞 Fogadd a megerősítő hívást",
        "ty_action_b": "Operátorunk <strong>a következő órákban</strong> felhív a rendelés megerősítéséhez.",
        "ty_warn": "Ha nem veszed fel a hívást, a rendelés automatikusan törlődik.",
        "ty_hours_h": "🕒 Elérhetőség",
        "ty_hours": "<strong>Hétfő – Szombat</strong> · 9:00 – 18:00",
        "ty_next_h": "📋 Mi következik",
        "ty_s1": "Fogadd a hívást és <strong>erősítsd meg az adataidat</strong>",
        "ty_s2": "Rendelésed <strong>24–48 órán</strong> belül feladva",
        "ty_s3": "Házhozszállítás és <strong>utánvétes fizetés ({price})</strong>",
        "ty_b1": "🔒 Utánvétes fizetés", "ty_b2": "🛡️ 4 év garancia", "ty_b3": "🔐 SSL védelem",
        "cookie_text": "Technikai és harmadik féltől származó cookie-kat használunk a jobb élményhez.",
        "cookie_accept": "Elfogadom", "cookie_learn": "További információ",
    },
    "sk": {
        "title": "TrimOne™ — Akumulátorový Krovinorez 3000W | -70% Len Dnes",
        "meta_desc": "TrimOne™: ultralight akumulátorový krovinorez 1,2 kg so 2 batériami 60V. Výkon 3000W, doprava zdarma 24h, platba na dobierku.",
        "og_title": "TrimOne™ — Krovinorez bez kábla | -70% Len Dnes",
        "og_desc": "Strihajte, upravujte a tvarujte s milimetrovou presnosťou. 2 batérie 60V v balení. Platba na dobierku.",
        "img_alt": "TrimOne akumulátorový krovinorez",
        "topbar": "LEN DNES: -70% + DOPRAVA ZDARMA DO 24H — PLATBA NA DOBIERKU",
        "rating": "Viac ako <strong>15 000</strong> spokojných zákazníkov na Slovensku",
        "gift": "🎁 ZDARMA: 1 extra lítiová batéria 60V!",
        "h1_hl": "Záhrada, o ktorej ste vždy snívali, za pár minút a bez námahy",
        "lead": "Strihajte, upravujte a tvarujte s milimetrovou presnosťou. Zabudnite na staré náradie: s hmotnosťou len <strong>1,2 kg</strong> a <strong>2 lítiovými batériami 60V</strong> je starostlivosť o trávnik rýchlá a jednoduchá.",
        "cta_hero": "ÁNO, CHCEM TRIMONE™ →",
        "form_note": "🔒 Bez platby vopred · Platíte až pri prevzatí",
        "f1t": "Doprava zdarma", "f1d": "24/48 hodín na celom Slovensku",
        "f2t": "Platba na dobierku", "f2d": "Platíte až kuriérovi",
        "f3t": "4 roky záruky", "f3d": "Kompletná ochrana v cene",
        "f4t": "14 dní na vrátenie", "f4d": "Spokojní alebo vrátenie peňazí",
        "eyebrow": "Prečo TrimOne™",
        "reasons_h2": "4 dôvody, prečo zmeníte spôsob starostlivosti o záhradu",
        "r1t": "Dvojitá výdrž: 2 batérie 60V", "r1p": "Jednu používate, druhá sa nabíja. Pracujete bez prestávok — vaša záhrada nečaká.",
        "r2t": "Výkon 3000W bez kábla", "r2p": "Motor Brushless™ má silu benzínového krovinorezu. Strihajte kdekoľvek bez zamotaných káblov a bez hľadania zásuvky.",
        "r3t": "Pripravený za 3 sekundy", "r3p": "Vložte batériu, stlačte tlačidlo a ste pripravení. Teleskopická rukoväť a hlava 180° dosiahnu tam, kde iné náradie nestačí.",
        "r4t": "Rekordná ľahkosť — 1,2 kg", "r4p": "Navrhnutý na zdvihnutie jednou rukou. Tichý výkon, nulové emisie — chráňte chrbát a pracujte hodiny bez únavy.",
        "countdown": "⏰ Zľava -70% končí za",
        "cd_h": "Hod", "cd_m": "Min", "cd_s": "Sek",
        "stock_l": "Dostupnosť na sklade", "stock_r": "Zostávajú len 3 kusy!",
        "live_word": "ľudí", "live_suffix": "si práve prezerá túto ponuku",
        "order_h2": "Vyplňte formulár pre objednávku",
        "order_p": "Vyplňte údaje nižšie — ozveme sa vám pre potvrdenie. Pripravte si <strong>{price}</strong> v hotovosti pre kuriéra.",
        "lbl_name": "Meno a priezvisko*", "lbl_tel": "Telefónne číslo*", "lbl_addr": "Doručovacia adresa*",
        "ph_name": "Ján Novák", "ph_tel": "+421 901 234 567", "ph_addr": "Hlavná 15, 811 01 Bratislava",
        "cta_form": "ÁNO, OBJEDNÁVAM TRIMONE™ ZA {price}",
        "reviews_eyebrow": "Recenzie", "reviews_h2": "Čo hovoria naši zákazníci",
        "rev_alt": "Recenzia zákazníka TrimOne",
        "rev1": "«Už som sa nechcel trápiť so starým benzínovým krovinorezom, ťažkým a hlučným. TrimOne™ váži veľmi málo — zdvihám ho jednou rukou! — a bez váhania seká vysokú trávu. Teleskopická rukoväť mi umožňuje pracovať v stoji. Kúpa, ktorú by som zopakoval!»",
        "rev2": "«Najlepšie sú dve batérie v balení: jednu používam, zatiaľ čo sa druhá nabíja. Oceľovou kefou som vyčistil chodník od buriny. Veľmi praktická otočná hlava pre okraje trávnika.»",
        "rev3": "«Bývam v radovej zástavbe a nechcela som rušiť susedov v nedeľu ráno. TrimOne™ je neuveriteľne tichý, ale má silu, ktorú od akumulátorového náradia nečakáte. Odporúčam!»",
        "verified_m": "Overený zákazník", "verified_f": "Overená zákazníka",
        "kit_eyebrow": "V balení", "kit_h2": "Váš kompletný kit TrimOne™",
        "kit_alt": "Kompletný kit TrimOne",
        "kit_items": [
            "1× TrimOne™ Professional — ultralight telo (1,2 kg) s motorom Brushless",
            "2× lítiové batérie 60V (1 ZDARMA) — dvojitá výdrž",
            "1× ultra-rýchlá nabíjačka",
            "1× ozubený kotúč z kalenej ocele — vetvy a kere",
            "2× čepele Precision-Cut z nehrdzavejúcej ocele",
            "1× multifilamentová hlava pre okraje",
            "1× rotačná oceľová kefa (ZDARMA) — chodníky a spáry",
            "Oficiálna 4-ročná záruka",
        ],
        "faq_h2": "Často kladené otázky",
        "faqs": [
            ("Ako dlho vydrží batéria TrimOne™?", "Každá batéria zaručuje približne 30–40 minút nepretržitej práce. V balení sú 2 batérie — celková výdrž viac ako hodinu."),
            ("Je zložité ho zostaviť alebo používať?", "Vôbec nie. Zostavenie trvá menej ako 2 minúty. Vložte batériu, nastavte teleskopickú rukoväť a ste pripravení."),
            ("Zvláda aj malé vetvy?", "Vďaka systému 4-v-1 je veľmi univerzálny. Oceľové čepele režú kere, rotačná kefa odstraňuje burinu."),
            ("Je hlučný? Môžem ho používať v bytovke?", "Motor Brushless je extrémne tichý oproti benzínovým modelom. Môžete pracovať kedykoľvek bez rušenia susedov."),
            ("Čo ak budem mať problém s produktom?", "Ponúkame 4 roky záruky a podporu. Máte 14 dní na jednoduché vrátenie."),
            ("Aké sú termíny a náklady doručenia?", "Doručenie je úplne zdarma na celom Slovensku! Objednávka je spracovaná do 24 hodín a doručená do 24/48 hodín."),
        ],
        "footer_tag": "Užitočné produkty pre každodenný život, doručenie za 24–48 hodín s platbou na dobierku.",
        "footer_info": "Informácie", "footer_contact": "Kontakt",
        "footer_about": "O nás", "footer_contact_link": "Kontaktujte nás",
        "footer_privacy": "Zásady ochrany osobných údajov", "footer_terms": "Obchodné podmienky",
        "footer_cookie": "Zásady cookies", "footer_ship": "Zásady doručenia", "footer_refund": "Zásady vrátenia",
        "footer_rights": "Všetky práva vyhradené.",
        "ty_title": "Objednávka prijatá — Čakajte na potvrdzovací hovor | TrimOne™",
        "ty_desc": "Vaša objednávka TrimOne™ bola zaregistrovaná. Zostáva posledný krok: prijmite potvrdzovací hovor.",
        "ty_h1": "Vaša objednávka bola úspešne zaregistrovaná!",
        "ty_sub": "Skvelé — vaša objednávka TrimOne™ sa spracováva. Zostáva len <strong>posledný krok</strong> k dokončení a odoslaniu.",
        "ty_hero_alt": "Tím powercurvemedia: call centrum a logistika COD",
        "ty_eyebrow": "👇 Čo teraz urobiť",
        "ty_action_t": "📞 Prijmite potvrdzovací hovor",
        "ty_action_b": "Náš operátor vás kontaktuje <strong>v nasledujúcich hodinách</strong> pre potvrdenie objednávky.",
        "ty_warn": "Ak hovor neprijmete, objednávka bude automaticky zrušená.",
        "ty_hours_h": "🕒 Kontaktné hodiny",
        "ty_hours": "<strong>Pondelok – Sobota</strong> · 9:00 – 18:00",
        "ty_next_h": "📋 Čo bude ďalej",
        "ty_s1": "Prijmite hovor a <strong>potvrďte svoje údaje</strong>",
        "ty_s2": "Objednávka bude odoslaná do <strong>24–48 hodín</strong>",
        "ty_s3": "Doručenie domov a <strong>platba na dobierku ({price})</strong>",
        "ty_b1": "🔒 Platba na dobierku", "ty_b2": "🛡️ Záruka 4 roky", "ty_b3": "🔐 Ochrana SSL",
        "cookie_text": "Používame technické a analytické cookies pre zlepšenie vášho zážitku.",
        "cookie_accept": "Prijímam", "cookie_learn": "Zistiť viac",
    },
    "pl": {
        "title": "TrimOne™ — Bezprzewodowa Podkaszarka 3000W | -70% Tylko Dziś",
        "meta_desc": "TrimOne™: ultralekka podkaszarka akumulatorowa 1,2 kg z 2 bateriami 60V. Moc 3000W, darmowa dostawa 24h, płatność przy odbiorze.",
        "og_title": "TrimOne™ — Podkaszarka bezprzewodowa | -70% Tylko Dziś",
        "og_desc": "Przycinaj, równaj i kształtuj z milimetrową precyzją. 2 baterie 60V w zestawie. Płatność przy odbiorze.",
        "img_alt": "TrimOne bezprzewodowa podkaszarka",
        "topbar": "TYLKO DZIŚ: -70% + DARMOWA DOSTAWA W 24H — PŁATNOŚĆ PRZY ODBIORZE",
        "rating": "Ponad <strong>15 000</strong> zadowolonych klientów w Polsce",
        "gift": "🎁 GRATIS: 1 dodatkowa bateria litowo-jonowa 60V!",
        "h1_hl": "Ogród, o którym zawsze marzyłeś, w kilka minut i bez wysiłku",
        "lead": "Przycinaj, równaj i kształtuj z milimetrową precyzją. Zapomnij o trudzie ze starymi narzędziami: dzięki wadze zaledwie <strong>1,2 kg</strong> i <strong>2 bateriom litowo-jonowym 60V</strong> pielęgnacja trawnika staje się szybką i łatwą przyjemnością.",
        "cta_hero": "TAK, CHCĘ TRIMONE™ →",
        "form_note": "🔒 Bez zaliczki · Płacisz tylko przy odbiorze",
        "f1t": "Darmowa dostawa", "f1d": "24/48 godzin w całej Polsce",
        "f2t": "Płatność przy odbiorze", "f2d": "Płacisz dopiero po otrzymaniu",
        "f3t": "4 lat gwarancji", "f3d": "Pełna ochrona w zestawie",
        "f4t": "14 dni na zwrot", "f4d": "Zadowolony lub zwrot pieniędzy",
        "eyebrow": "Dlaczego TrimOne™",
        "reasons_h2": "4 powody, dla których zmienisz sposób pielęgnacji ogrodu",
        "r1t": "Podwójna autonomia: 2 baterie 60V", "r1p": "Jedną używasz, druga się ładuje. Pracujesz bez przerw — ogród nie czeka.",
        "r2t": "Moc 3000W bez kabla", "r2p": "Silnik Brushless™ daje siłę spalinowej podkaszarki. Pracuj wszędzie bez plątających się kabli i szukania gniazdka.",
        "r3t": "Gotowy w 3 sekundy", "r3p": "Włóż baterię, naciśnij przycisk — gotowe. Teleskopowa rączka i głowica 180° docierają tam, gdzie inne narzędzia nie sięgają.",
        "r4t": "Rekordowa lekkość — 1,2 kg", "r4p": "Zaprojektowany do podnoszenia jedną ręką. Cichy, zero emisji — chroń plecy i pracuj godzinami bez zmęczenia.",
        "countdown": "⏰ Rabat -70% wygasa za",
        "cd_h": "Godz", "cd_m": "Min", "cd_s": "Sek",
        "stock_l": "Dostępność w magazynie", "stock_r": "Pozostały tylko 3 sztuki!",
        "live_word": "osób", "live_suffix": "ogląda teraz tę ofertę",
        "order_h2": "Wypełnij formularz, aby zamówić",
        "order_p": "Podaj dane poniżej — skontaktujemy się w celu potwierdzenia. Przygotuj <strong>{price}</strong> gotówki dla kuriera.",
        "lbl_name": "Imię i nazwisko*", "lbl_tel": "Numer telefonu*", "lbl_addr": "Adres dostawy*",
        "ph_name": "Jan Kowalski", "ph_tel": "+48 512 345 678", "ph_addr": "ul. Marszałkowska 10, 00-590 Warszawa",
        "cta_form": "TAK, ZAMAWIAM TRIMONE™ ZA {price}",
        "reviews_eyebrow": "Opinie", "reviews_h2": "Co mówią nasi klienci",
        "rev_alt": "Opinia klienta TrimOne",
        "rev1": "«Miałem dość walki ze starą spalinową podkaszarką, ciężką i głośną. TrimOne™ waży bardzo mało — podnoszę jedną ręką! — i bez wahania tnie wysoką trawę. Teleskopowa rączka pozwala pracować na stojąco. Kupiłbym ponownie!»",
        "rev2": "«Najlepsze są dwie baterie w zestawie: jedną używam, druga się ładuje. Szczotką stalową wyczyściłem chodnik z chwastów. Bardzo praktyczna obrotowa głowica do krawędzi trawnika.»",
        "rev3": "«Mieszkam w szeregowcu i nie chciałam przeszkadzać sąsiadom w niedzielę rano. TrimOne™ jest niesamowicie cichy, ale ma moc, której nie spodziewasz się od akumulatorowego narzędzia. Polecam!»",
        "verified_m": "Zweryfikowany klient", "verified_f": "Zweryfikowana klientka",
        "kit_eyebrow": "W zestawie", "kit_h2": "Twój kompletny zestaw TrimOne™",
        "kit_alt": "Kompletny zestaw TrimOne",
        "kit_items": [
            "1× TrimOne™ Professional — ultralekka obudowa (1,2 kg) z silnikiem Brushless",
            "2× baterie litowo-jonowe 60V (1 GRATIS) — podwójna autonomia",
            "1× ultra-szybka ładowarka",
            "1× tarcza zębata ze stali hartowanej — gałęzie i krzewy",
            "2× ostrza Precision-Cut ze stali nierdzewnej",
            "1× głowica wieloliniowa do krawędzi",
            "1× obrotowa szczotka stalowa (GRATIS) — chodniki i fugy",
            "Oficjalna 4-letnia gwarancja",
        ],
        "faq_h2": "Najczęściej zadawane pytania",
        "faqs": [
            ("Jak długo działa bateria TrimOne™?", "Każda bateria zapewnia około 30–40 minut ciągłej pracy. W zestawie są 2 baterie — łączna autonomia ponad godziny."),
            ("Czy trudno go zmontować lub używać?", "Wcale nie. Montaż zajmuje mniej niż 2 minuty. Włóż baterię, ustaw teleskopową rączkę i gotowe."),
            ("Czy tnie też małe gałęzie?", "System 4-w-1 jest bardzo uniwersalny. Ostrza ze stali tną małe krzewy, obrotowa szczotka usuwa chwasty z chodnika."),
            ("Czy jest głośny? Mogę używać w bloku?", "Silnik Brushless jest bardzo cichy w porównaniu z modelami spalinowymi. Możesz pracować o każdej porze bez przeszkadzania sąsiadom."),
            ("Co jeśli mam problem z produktem?", "Oferujemy 4 lat gwarancji i wsparcie. Masz 14 dni na prosty zwrot, jeśli nie jesteś zadowolony."),
            ("Jakie są terminy i koszty dostawy?", "Dostawa jest całkowicie darmowa w całej Polsce! Zamówienie przetwarzane w 24 godziny, dostawa w 24/48 godzin roboczych."),
        ],
        "footer_tag": "Przydatne produkty na co dzień, dostawa w 24–48 godzin z płatnością przy odbiorze.",
        "footer_info": "Informacje", "footer_contact": "Kontakt",
        "footer_about": "O nas", "footer_contact_link": "Skontaktuj się",
        "footer_privacy": "Polityka prywatności", "footer_terms": "Regulamin",
        "footer_cookie": "Polityka cookies", "footer_ship": "Polityka wysyłki", "footer_refund": "Polityka zwrotów",
        "footer_rights": "Wszelkie prawa zastrzeżone.",
        "ty_title": "Zamówienie przyjęte — Czekaj na rozmowę potwierdzającą | TrimOne™",
        "ty_desc": "Twoje zamówienie TrimOne™ zostało zarejestrowane. Pozostał ostatni krok: odbierz rozmowę potwierdzającą.",
        "ty_h1": "Twoje zamówienie zostało pomyślnie zarejestrowane!",
        "ty_sub": "Świetnie — zamówienie TrimOne™ jest w realizacji. Pozostał tylko <strong>ostatni krok</strong> do finalizacji i wysyłki.",
        "ty_hero_alt": "Zespół powercurvemedia: call center i logistyka COD",
        "ty_eyebrow": "👇 Co musisz teraz zrobić",
        "ty_action_t": "📞 Odbierz rozmowę potwierdzającą",
        "ty_action_b": "Nasz operator skontaktuje się z Tobą <strong>w ciągu kilku godzin</strong>, aby potwierdzić zamówienie.",
        "ty_warn": "Jeśli nie odbierzesz rozmowy, zamówienie zostanie automatycznie anulowane.",
        "ty_hours_h": "🕒 Godziny kontaktu",
        "ty_hours": "<strong>Poniedziałek – Sobota</strong> · 9:00 – 18:00",
        "ty_next_h": "📋 Co dalej",
        "ty_s1": "Odbierz rozmowę i <strong>potwierdź swoje dane</strong>",
        "ty_s2": "Zamówienie zostanie wysłane w ciągu <strong>24–48 godzin</strong>",
        "ty_s3": "Dostawa do domu i <strong>płatność przy odbiorze ({price})</strong>",
        "ty_b1": "🔒 Płatność przy odbiorze", "ty_b2": "🛡️ Gwarancja 4 lat", "ty_b3": "🔐 Ochrona SSL",
        "cookie_text": "Używamy plików cookie technicznych i analitycznych, aby poprawić Twoje doświadczenie.",
        "cookie_accept": "Akceptuję", "cookie_learn": "Dowiedz się więcej",
    },
}


def fmt(tr: dict, key: str, price: str) -> str:
    val = tr[key]
    return val.replace("{price}", price) if isinstance(val, str) else val


def build_faq_html(tr: dict) -> str:
    items = []
    for q, a in tr["faqs"]:
        items.append(
            f"  <div class=\"faq-item\">\n"
            f"    <button class=\"faq-q\" type=\"button\"><span>{q}</span><span class=\"arrow\">▾</span></button>\n"
            f"    <div class=\"faq-a\"><p>{a}</p></div>\n"
            f"  </div>"
        )
    return "\n".join(items)


def build_kit_items_html(tr: dict) -> str:
    return "\n".join(f"        <li>{item}</li>" for item in tr["kit_items"])


def apply_index(html: str, g: dict, tr: dict) -> str:
    geo = g["geo"]
    lang = g["lang"]
    offer = g["offer"]
    was = g["was"]
    now = g["now"]
    cta_price = g["cta_price"]
    thankyou = f"https://powercurvemedia.com/{geo}/trimone/thank-you.html"
    live_js = (
        f"el.innerHTML = '<strong>' + count + ' {tr['live_word']}</strong> "
        f"{tr['live_suffix']}';"
    )

    html = html.replace('lang="it"', f'lang="{lang}"', 1)
    html = html.replace("https://powercurvemedia.com/it/trimone/", f"https://powercurvemedia.com/{geo}/trimone/")
    html = html.replace('href="/it/', f'href="/{geo}/')

    pairs: list[tuple[str, str]] = [
        ("TrimOne™ — Decespugliatore Senza Filo 3000W | -70% Solo Oggi", tr["title"]),
        (
            'content="TrimOne™: decespugliatore a batteria ultraleggero da 1,2 kg con 2 batterie 60V. Potenza 3000W, spedizione gratuita 24/48h, pagamento alla consegna."',
            f'content="{tr["meta_desc"]}"',
        ),
        ("TrimOne™ — Decespugliatore senza filo | -70% Solo Oggi", tr["og_title"]),
        (
            'content="Taglia, rifila e modella con precisione millimetrica. 2 batterie 60V incluse. Pagamento alla consegna."',
            f'content="{tr["og_desc"]}"',
        ),
        ("TrimOne decespugliatore senza filo", tr["img_alt"]),
        (
            "SOLO OGGI: -70% + CONSEGNA GRATUITA IN 24H — PAGAMENTO ALLA CONSEGNA",
            tr["topbar"],
        ),
        (
            "Oltre <strong>15.000</strong> clienti soddisfatti in Italia",
            tr["rating"],
        ),
        ("🎁 IN REGALO: 1 batteria agli ioni di litio 60V extra!", tr["gift"]),
        (
            "<h1>TrimOne™<br><span class=\"hl\">Il giardino che hai sempre sognato, in pochi minuti e senza alcuno sforzo</span></h1>",
            f"<h1>TrimOne™<br><span class=\"hl\">{tr['h1_hl']}</span></h1>",
        ),
        (
            "Taglia, rifila e modella con precisione millimetrica. Dimentica la fatica degli attrezzi vecchi: con un peso di soli <strong>1,2 kg</strong> e <strong>2 batterie agli ioni di litio da 60V</strong>, curare il prato diventa un piacere veloce e facile.",
            tr["lead"],
        ),
        ("249 €", was),
        ("79 €", now),
        ("SÌ, VOGLIO TRIMONE™ →", tr["cta_hero"]),
        ("🔒 Nessun anticipo · Paghi solo alla consegna", tr["form_note"]),
        ("<h4>Spedizione gratuita</h4><p>24/48 ore in tutta Italia</p>", f"<h4>{tr['f1t']}</h4><p>{tr['f1d']}</p>"),
        ("<h4>Pagamento alla consegna</h4><p>Paghi solo quando ricevi</p>", f"<h4>{tr['f2t']}</h4><p>{tr['f2d']}</p>"),
        ("<h4>4 anni di garanzia</h4><p>Protezione completa inclusa</p>", f"<h4>{tr['f3t']}</h4><p>{tr['f3d']}</p>"),
        ("<h4>14 giorni per il reso</h4><p>Soddisfatto o rimborso</p>", f"<h4>{tr['f4t']}</h4><p>{tr['f4d']}</p>"),
        ("<span class=\"eyebrow\">Perché TrimOne™</span>", f"<span class=\"eyebrow\">{tr['eyebrow']}</span>"),
        (
            "<h2>4 motivi per cui cambierai il modo di curare il giardino</h2>",
            f"<h2>{tr['reasons_h2']}</h2>",
        ),
        ("<h3>Doppia autonomia: 2 batterie 60V</h3><p>Ne usi una mentre l'altra si ricarica. Lavori senza interruzioni — il tuo giardino non aspetta.</p>", f"<h3>{tr['r1t']}</h3><p>{tr['r1p']}</p>"),
        ("<h3>Potenza 3000W senza filo</h3><p>Il motore Brushless™ offre la forza di un decespugliatore a scoppio. Taglia ovunque, senza cavi aggrovigliati e senza cercare la presa.</p>", f"<h3>{tr['r2t']}</h3><p>{tr['r2p']}</p>"),
        ("<h3>Pronto in 3 secondi</h3><p>Inserisci la batteria, premi il pulsante e sei operativo. Manico telescopico e testa girevole a 180° raggiungono dove gli altri attrezzi si fermano.</p>", f"<h3>{tr['r3t']}</h3><p>{tr['r3p']}</p>"),
        ("<h3>Leggerezza record — 1,2 kg</h3><p>Progettato per essere sollevato con una mano. Potenza silenziosa, zero emissioni — proteggi la schiena e lavora per ore senza stancarti.</p>", f"<h3>{tr['r4t']}</h3><p>{tr['r4p']}</p>"),
        ("⏰ Lo sconto -70% scade tra", tr["countdown"]),
        ("<div class=\"lbl\">Ore</div>", f"<div class=\"lbl\">{tr['cd_h']}</div>"),
        ("<div class=\"lbl\">Min</div>", f"<div class=\"lbl\">{tr['cd_m']}</div>"),
        ("<div class=\"lbl\">Sec</div>", f"<div class=\"lbl\">{tr['cd_s']}</div>"),
        ("<span class=\"left\">Disponibilità in magazzino</span>", f"<span class=\"left\">{tr['stock_l']}</span>"),
        ("<span class=\"right\">Solo 3 pezzi rimasti!</span>", f"<span class=\"right\">{tr['stock_r']}</span>"),
        ("<strong>16 persone</strong> stanno guardando questa offerta ora", f"<strong>16 {tr['live_word']}</strong> {tr['live_suffix']}"),
        ("<h2>Compila il modulo per ordinare</h2>", f"<h2>{tr['order_h2']}</h2>"),
        (
            "Inserisci i tuoi dati qui sotto: ti contatteremo per confermare l'ordine. Tieni pronti <strong>79 €</strong> in contanti per il corriere.",
            fmt(tr, "order_p", now),
        ),
        ("<label for=\"name\">Nome e cognome*</label>", f"<label for=\"name\">{tr['lbl_name']}</label>"),
        ("placeholder=\"Mario Rossi\"", f'placeholder="{tr["ph_name"]}"'),
        ("<label for=\"tel\">Numero di telefono*</label>", f"<label for=\"tel\">{tr['lbl_tel']}</label>"),
        ("placeholder=\"+39 312 345 6789\"", f'placeholder="{tr["ph_tel"]}"'),
        ("<label for=\"street-address\">Indirizzo di consegna*</label>", f"<label for=\"street-address\">{tr['lbl_addr']}</label>"),
        ("placeholder=\"Via Roma 45, Interno 12, 00100 Roma\"", f'placeholder="{tr["ph_addr"]}"'),
        (
            'value="https://powercurvemedia.com/it/trimone/thank-you.html"',
            f'value="{thankyou}"',
        ),
        ("SÌ, ORDINO TRIMONE™ A 79€", fmt(tr, "cta_form", cta_price)),
        ("<span class=\"eyebrow\">Recensioni</span>", f"<span class=\"eyebrow\">{tr['reviews_eyebrow']}</span>"),
        ("<h2>Cosa dicono i nostri clienti</h2>", f"<h2>{tr['reviews_h2']}</h2>"),
        ("alt=\"Recensione cliente TrimOne\"", f'alt="{tr["rev_alt"]}"'),
        ("«Ero stanco di lottare con il vecchio decespugliatore a scoppio, pesante e rumoroso. TrimOne™ pesa pochissimo — lo sollevo con una mano! — e taglia l'erba alta senza esitazione. Il manico telescopico mi permette di lavorare in piedi, senza piegarmi. Un acquisto che rifarei mille volte!»", tr["rev1"]),
        ("«Il meglio sono le due batterie incluse: ne uso una mentre l'altra si ricarica, così non mi fermo mai. Con la spazzola in acciaio ho pulito il vialetto dalle erbacce tra le mattonelle e sembra nuovo. Molto pratica anche la testa girevole per rifinire i bordi del prato lungo il marciapiede.»", tr["rev2"]),
        ("«Vivo in una villetta a schiera e non volevo disturbare i vicini la domenica mattina. TrimOne™ è incredibilmente silenzioso, ma ha una potenza che non ti aspetti da un attrezzo a batteria. Le lame in plastica sono perfette per rifinire intorno ai fiori senza danneggiarli. Lo consiglio a chiunque voglia un giardino curato senza stress!»", tr["rev3"]),
        ("<div class=\"name\">Marco R.</div><div class=\"loc\">Cliente verificato</div>", f"<div class=\"name\">Marco R.</div><div class=\"loc\">{tr['verified_m']}</div>"),
        ("<div class=\"name\">Elena B.</div><div class=\"loc\">Cliente verificata</div>", f"<div class=\"name\">Elena B.</div><div class=\"loc\">{tr['verified_f']}</div>"),
        ("<div class=\"name\">Francesca T.</div><div class=\"loc\">Cliente verificata</div>", f"<div class=\"name\">Francesca T.</div><div class=\"loc\">{tr['verified_f']}</div>"),
        ("<span class=\"eyebrow\">Nella confezione</span>", f"<span class=\"eyebrow\">{tr['kit_eyebrow']}</span>"),
        ("<h2>Il tuo kit completo TrimOne™</h2>", f"<h2>{tr['kit_h2']}</h2>"),
        ("alt=\"Kit completo TrimOne\"", f'alt="{tr["kit_alt"]}"'),
        ("<h2>Domande frequenti</h2>", f"<h2>{tr['faq_h2']}</h2>"),
        (
            "Prodotti utili per la vita quotidiana, consegna in 24-48 ore con pagamento alla consegna.",
            tr["footer_tag"],
        ),
        (">Informazioni<", f">{tr['footer_info']}<"),
        (">Chi siamo<", f">{tr['footer_about']}<"),
        (">Contattaci<", f">{tr['footer_contact_link']}<"),
        (">Privacy Policy<", f">{tr['footer_privacy']}<"),
        (">Termini e Condizioni<", f">{tr['footer_terms']}<"),
        (">Cookie Policy<", f">{tr['footer_cookie']}<"),
        (">Politica di Spedizione<", f">{tr['footer_ship']}<"),
        (">Politica di Rimborso<", f">{tr['footer_refund']}<"),
        (">Contatti<", f">{tr['footer_contact']}<"),
        ("Tutti i diritti riservati", tr["footer_rights"].rstrip(".")),
    ]

    for old, new in sorted(pairs, key=lambda x: len(x[0]), reverse=True):
        html = html.replace(old, new)

    html = html.replace(
        f'<input name="offer" type="hidden" value="TODO" />',
        f'<input name="offer" type="hidden" value="{offer}" />',
    )
    html = html.replace(
        f'<input name="lp" type="hidden" value="TODO" />',
        f'<input name="lp" type="hidden" value="{offer}" />',
    )

    kit_old = re.search(r"<ul>\n(?:        <li>.*\n)+      </ul>", html, re.S)
    if kit_old:
        kit_new = f"<ul>\n{build_kit_items_html(tr)}\n      </ul>"
        html = html.replace(kit_old.group(0), kit_new, 1)

    faq_old = re.search(
        r"<section class=\"faq wrap\">.*?</section>",
        html,
        re.S,
    )
    if faq_old:
        faq_new = (
            f"<section class=\"faq wrap\">\n"
            f"  <div class=\"section-heading\">\n"
            f"    <h2>{tr['faq_h2']}</h2>\n"
            f"  </div>\n"
            f"{build_faq_html(tr)}\n"
            f"</section>"
        )
        html = html.replace(faq_old.group(0), faq_new, 1)

    html = html.replace(
        "el.innerHTML = '<strong>' + count + ' persone</strong> stanno guardando questa offerta ora';",
        live_js,
    )

    return html


def apply_thankyou(html: str, g: dict, tr: dict) -> str:
    geo = g["geo"]
    lang = g["lang"]
    price = g["price"]
    currency = g["currency"]
    cta_price = g["cta_price"]
    pj = price_js(price)
    cpa_js = f"{CPA_EUR}.0"

    html = html.replace('lang="it"', f'lang="{lang}"', 1)
    html = html.replace('href="/it/', f'href="/{geo}/')
    html = html.replace("'value': 79.90,", f"'value': {cpa_js},")
    html = html.replace("'value': 1.0,", f"'value': {cpa_js},")

    html = re.sub(
        r"window\.SITE_CONFIG = \{.*?\n\};",
        (
            "window.SITE_CONFIG = {\n"
            f"  GEO: '{geo}',\n"
            f"  PRODUCT_SLUG: 'trimone',\n"
            f"  CURRENCY: '{currency}',\n"
            f"  PRICE: {pj},\n"
            "  META_PIXEL_ID: '',\n"
            "  GOOGLE_TAG_ID: '',\n"
            "  GOOGLE_ADS_CONVERSION_ID: '',\n"
            "  TY_CONVERSION_LABEL: '',\n"
            f"  COOKIE_TEXT: {json.dumps(tr['cookie_text'], ensure_ascii=False)},\n"
            f"  COOKIE_ACCEPT: {json.dumps(tr['cookie_accept'], ensure_ascii=False)},\n"
            f"  COOKIE_LEARN: {json.dumps(tr['cookie_learn'], ensure_ascii=False)}\n"
            "};"
        ),
        html,
        count=1,
        flags=re.S,
    )

    html = html.replace(
        "if (window.trackPurchase) window.trackPurchase(79, 'EUR');",
        f"if (window.trackPurchase) window.trackPurchase({pj}, '{currency}');",
    )

    pairs = [
        (
            "Ordine ricevuto — Attendi la chiamata di conferma | TrimOne™",
            tr["ty_title"],
        ),
        (
            'content="Il tuo ordine TrimOne™ è stato registrato. Manca solo un ultimo passaggio: rispondi alla chiamata di conferma del nostro operatore."',
            f'content="{tr["ty_desc"]}"',
        ),
        ("Il tuo ordine è stato registrato con successo!", tr["ty_h1"]),
        (
            "Perfetto — il tuo ordine TrimOne™ è in elaborazione. Manca solo <strong>un ultimo passaggio</strong> per completarlo e far partire la spedizione.",
            tr["ty_sub"],
        ),
        (
            "Il team powercurvemedia al lavoro: call center e logistica COD",
            tr["ty_hero_alt"],
        ),
        ("👇 Cosa devi fare adesso", tr["ty_eyebrow"]),
        ("📞 Rispondi alla chiamata di conferma", tr["ty_action_t"]),
        (
            "Un nostro operatore ti contatterà <strong>nelle prossime ore</strong> per confermare il tuo ordine.",
            tr["ty_action_b"],
        ),
        (
            "Se non rispondi alla chiamata, l'ordine verrà automaticamente annullato.",
            tr["ty_warn"],
        ),
        ("🕒 Orari di contatto", tr["ty_hours_h"]),
        ("<strong>Lunedì – Sabato</strong> · 9:00 – 18:00", tr["ty_hours"]),
        ("📋 Cosa succede dopo", tr["ty_next_h"]),
        (
            "Rispondi alla chiamata e <strong>conferma i tuoi dati</strong>",
            tr["ty_s1"],
        ),
        (
            "Il tuo ordine verrà spedito entro <strong>24–48 ore</strong>",
            tr["ty_s2"],
        ),
        (
            "Consegna a domicilio e <strong>pagamento alla consegna (79 €)</strong>",
            fmt(tr, "ty_s3", cta_price),
        ),
        ("🔒 Pagamento alla consegna", tr["ty_b1"]),
        ("🛡️ Garanzia 4 anni", tr["ty_b2"]),
        ("🔐 Protezione SSL", tr["ty_b3"]),
        (">Informazioni<", f">{tr['footer_info']}<"),
        (">Chi siamo<", f">{tr['footer_about']}<"),
        (">Contattaci<", f">{tr['footer_contact_link']}<"),
        (">Privacy Policy<", f">{tr['footer_privacy']}<"),
        (">Termini e Condizioni<", f">{tr['footer_terms']}<"),
        (">Cookie Policy<", f">{tr['footer_cookie']}<"),
        (">Politica di Spedizione<", f">{tr['footer_ship']}<"),
        (">Politica di Rimborso<", f">{tr['footer_refund']}<"),
        (">Contatti<", f">{tr['footer_contact']}<"),
        ("Tutti i diritti riservati", tr["footer_rights"].rstrip(".")),
    ]
    for old, new in sorted(pairs, key=lambda x: len(x[0]), reverse=True):
        html = html.replace(old, new)

    return html


def main() -> list[Path]:
    index_tpl = IT_INDEX.read_text(encoding="utf-8")
    thank_tpl = IT_THANKYOU.read_text(encoding="utf-8")
    created: list[Path] = []

    for g in GEOS:
        geo = g["geo"]
        tr = T[geo]
        out_dir = ROOT / geo / "trimone"
        out_dir.mkdir(parents=True, exist_ok=True)

        index_path = out_dir / "index.html"
        index_path.write_text(apply_index(index_tpl, g, tr), encoding="utf-8")
        created.append(index_path)

        ty_path = out_dir / "thank-you.html"
        ty_path.write_text(apply_thankyou(thank_tpl, g, tr), encoding="utf-8")
        created.append(ty_path)

        print(f"  {geo}/trimone/index.html")
        print(f"  {geo}/trimone/thank-you.html")

    return created


if __name__ == "__main__":
    print("Generating TrimOne pages...")
    files = main()
    print(f"Done — {len(files)} files written.")
