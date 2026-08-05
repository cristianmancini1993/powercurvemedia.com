#!/usr/bin/env python3
"""Generate Breezon landing + thank-you pages for CZ, RO, HU, SK."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

GEOS = [
    {
        "geo": "cz", "lang": "cs", "offer": "102",
        "price": 2499, "currency": "CZK",
        "was": "8.330 Kč", "now": "2.499 Kč", "cpa": 17,
    },
    {
        "geo": "ro", "lang": "ro", "offer": "308",
        "price": 499, "currency": "RON",
        "was": "1.663 Lei", "now": "499 Lei", "cpa": 17,
    },
    {
        "geo": "hu", "lang": "hu", "offer": "309",
        "price": 36499, "currency": "HUF",
        "was": "121.663 Ft", "now": "36.499 Ft", "cpa": 17,
    },
    {
        "geo": "sk", "lang": "sk", "offer": "310",
        "price": 99, "currency": "EUR",
        "was": "330 €", "now": "99 €", "cpa": 17,
    },
]

T = {
    "cz": {
        "title": "Breezon™ — Přenosná klimatizace 18 000 BTU bez hadice | -70%",
        "description": "Breezon™: přenosná klimatizace 18 000 BTU chlad/teplo, bez venkovní hadice a bez instalace. Vytápí a chladí až 145 m², HEPA filtry, platba na dobírku.",
        "topbar": "🔥 SLEVA 70 % + DOPRAVA ZDARMA — PLATBA NA DOBÍRKU 🔥",
        "rating": "Průměrné hodnocení: <strong>4,8 / 5</strong> · Na základě více než <strong>25 000</strong> skutečných recenzí",
        "gift": "🚚 Rychlé doručení do 24/48 hodin + Garance spokojenosti nebo vrácení peněz",
        "h1": "První klimatizace <span class=\"hl\">18 000 BTU</span> bez venkovní hadice: vytápí a chladí až <span class=\"hl\">145 m²</span> během pár minut",
        "lead": "<strong>Breezon™</strong> vám zajistí pohodlné klima doma bez venkovní jednotky a složité instalace. Technologie <strong>Smart Climate AI</strong>, filtry <strong>HEPA</strong>, pouze <strong>18 dB</strong> v nočním režimu — a platíte až při doručení.",
        "hero_alt": "Breezon přenosná klimatizace 18 000 BTU",
        "cta": "OBJEDNAT NYNÍ! →",
        "form_note": "🔒 Bez platby předem · Platba na dobírku · Doručení 24/48 h",
        "f1h": "Chlazení a topení", "f1p": "Vytápí a chladí až 145 m²",
        "f2h": "Bez venkovní hadice", "f2p": "Žádné motory venku, nulová instalace",
        "f3h": "Ultra tichý provoz", "f3p": "26 dB max. · 18 dB noční režim",
        "f4h": "Platba na dobírku", "f4p": "Pohodlně, bezpečně, bez zálohy",
        "urgency": "⏰ Nabídka -70 % platí pouze dnes",
        "cd_h": "Hod", "cd_m": "Min", "cd_s": "Sek",
        "stock_l": "Dostupnost", "stock_r": "Zbývá jen pár kusů!",
        "live": "<strong>{n} lidí</strong> si právě prohlíží Breezon",
        "form_h": "Vyplňte objednávkový formulář",
        "form_p": "Ozveme se vám a potvrdíme detaily doručení.",
        "name_l": "Jméno a příjmení*", "name_ph": "Jan Novák",
        "phone_l": "Telefonní číslo*", "phone_ph": "+420 601 234 567",
        "addr_l": "Doručovací adresa*", "addr_ph": "Václavské nám. 1, 110 00 Praha",
        "submit": "Potvrdit objednávku",
        "w1e": "01 — V létě chladno, v zimě teplo",
        "w1h": "Ideální klima za pár minut, bez hadic a instalace",
        "w1t": ["18 000 BTU", "Až 145 m²", "Plug & Play"],
        "w1p": "Díky výkonu <strong>18 000 BTU</strong> <strong>Breezon™</strong> vytápí a chladí prostory až <strong>145 m²</strong>. Bez hadice do okna, bez venkovní jednotky: zapojte do zásuvky a nastavte teplotu na ovladači, displeji nebo v telefonu.",
        "w1i": "Ideální pro domov, kancelář nebo pokoj pro hosty: přesuňte ho kamkoli potřebujete.",
        "w2e": "02 — Čistý vzduch a vyvážená vlhkost",
        "w2h": "HEPA filtry a Smart Climate AI pro zdravé pohodlí",
        "w2t": ["HEPA filtr", "Aktivní uhlí", "Climate AI"],
        "w2p": "Technologie <strong>Smart Climate AI</strong> sleduje kvalitu vzduchu a vlhkost a automaticky se přizpůsobuje, aby předcházela plísním a zápachu. Filtr <strong>HEPA</strong> a předfiltr zachytí prach, alergeny a nečistoty.",
        "w2i": "Omyvatelné a opakovaně použitelné filtry na roky — žádné průběžné náklady na výměnu.",
        "w3e": "03 — Ticho v noci a nižší účty",
        "w3h": "Pouze 18 dB v noci a optimalizovaná spotřeba",
        "w3t": ["26 dB max.", "18 dB noc", "Smart AI"],
        "w3p": "<strong>Breezon™</strong> je navržen pro maximální pohodlí s ultranízkou hlučností: <strong>26 dB</strong> na plný výkon a pouze <strong>18 dB</strong> v nočním režimu. Smart Climate AI optimalizuje výkon a ventilaci a snižuje plýtvání.",
        "w3i": "Méně hluku, méně spotřeby, více odpočinku — ideální i do ložnice.",
        "cmp_label": "Nejpraktičtější volba pro klima ve vaší domácnosti",
        "cmp_h": "Breezon™ vs. tradiční klimatizace",
        "cmp_rows": [
            ("Instalace", "Venkovní jednotka, vrtání, technici", "Plug & Play, žádné práce"),
            ("Hadice / odvod", "Hadice do okna nutná", "Bez venkovní hadice"),
            ("Výkon", "Často omezený / asymetrický", "18 000 BTU chlad/teplo"),
            ("Pokrytí", "Typicky jedna ložnice", "Až 145 m²"),
            ("Hluk", "Rušivý v noci", "Až 18 dB noční režim"),
            ("Vzduch", "Základní filtry", "Omyvatelné HEPA + uhlí"),
            ("Cena", "8.330 Kč", "Jen 2.499 Kč"),
        ],
        "cmp_th1": "Pevná / přenosná s hadicí",
        "rev_h": "Recenze zákazníků",
        "rev_sub": "★ 4,8/5 · Ověřený nákup · Kontrolované recenze",
        "reviews": [
            ("Konečně bez hadice v okně", "«Konečně přenosná klimatizace bez otravné hadice! Snadno ji přesouvám z místnosti do místnosti a doma je vždy ideální teplota. V zimě rychle topí a v létě chladí bez vysoké spotřeby. Už si bez ní nedokážu představit život!»", "Tomáš N.", "review-1"),
            ("Čerstvý, suchý a tichý vzduch", "«Vždycky jsem nesnášel vlhké horko doma, ale s Breezon je vzduch konečně svěží a suchý. Používám ho i v zimě na vytápění obýváku. Snadné ovládání, super tichý a bez instalace.»", "Petr K.", "review-2"),
            ("Velmi praktický s aplikací a ovladačem", "«Skvělé ovládání přes aplikaci i dálkový ovladač. Můžu ho zapnout ještě cestou domů a vše je připravené. V nočním režimu ho skoro vůbec neslyším.»", "Lucie M.", "review-3"),
        ],
        "verified": "Ověřený nákup",
        "kit_eye": "Co dostanete s Breezon",
        "kit_h": "Kompletní sada Breezon™",
        "kit_items": [
            "<strong>1× Breezon</strong> inteligentní klimatizace chlad/teplo 18 000 BTU",
            "Dálkový ovladač + smart ovládání přes aplikaci",
            "3× omyvatelné předfiltry s aktivním uhlím (2 zdarma)",
            "3× omyvatelné HEPA filtry (2 zdarma)",
            "Nádoba na kondenzát 10 litrů",
            "Český manuál · 30denní záruka · Doručení 24/48 h na dobírku",
        ],
        "faq_h": "Často kladené otázky",
        "faqs": [
            ("Vyžaduje Breezon složitou instalaci?", "Ne. Nepotřebujete venkovní jednotku ani klasickou hadici do okna. Zapojte do zásuvky a zvolte požadovanou teplotu."),
            ("Opravdu zvládne vytápět a chladit velké prostory?", "Ano. S 18 000 BTU je Breezon navržen pro vytápění a chlazení prostor až 145 m² během pár minut."),
            ("Je hlučný v noci?", "Ne. Noční režim automaticky snižuje hlučnost a intenzitu (až na 18 dB) pro pohodlnější spánek."),
            ("Mohu platit na dobírku?", "Ano. Zaplatíte kurýrovi při doručení. Mějte připraveno <strong>2.499 Kč</strong>."),
            ("Co když nebudu spokojen/a?", "Máte 30denní garanci spokojenosti nebo vrácení peněz. Náš zákaznický servis vám pomůže s vrácením a podporou."),
        ],
        "footer_tag": "Užitečné produkty pro každodenní život, doručení do 24–48 hodin s platbou na dobírku.",
        "footer_info": "Informace", "footer_about": "O nás", "footer_del": "Doručení",
        "footer_ship": "Zásady doručení", "footer_refund": "Zásady vrácení",
        "footer_home": "Domů", "footer_contact": "Kontaktujte nás",
        "footer_copy": "Všechna práva vyhrazena.",
        "submitting": "Odesílání...",
        "ty_title": "Objednávka přijata — Vyčkejte na potvrzovací hovor | Breezon™",
        "ty_desc": "Vaše objednávka Breezon™ byla zaregistrována. Poslední krok: přijměte potvrzovací hovor.",
        "ty_h": "Vaše objednávka byla úspěšně zaregistrována!",
        "ty_sub": "Skvělé — objednávka Breezon™ se zpracovává. Zbývá jen <strong>poslední krok</strong> před odesláním.",
        "ty_eye": "👇 Co musíte udělat teď",
        "ty_act_h": "📞 Přijměte potvrzovací hovor",
        "ty_act_p": "Náš operátor vás bude kontaktovat <strong>do několika hodin</strong>, aby potvrdil objednávku.",
        "ty_warn": "Pokud hovor nepřijmete, objednávka se automaticky zruší.",
        "ty_hours_h": "🕒 Hodiny kontaktu",
        "ty_hours": "<strong>Pondělí – Sobota</strong> · 9:00 – 18:00",
        "ty_next_h": "📋 Co bude následovat",
        "ty_steps": [
            "Při hovoru <strong>potvrďte své údaje</strong>",
            "Objednávka bude odeslána do <strong>24–48 hodin</strong>",
            "Doručení domů a <strong>platba na dobírku</strong>",
        ],
        "ty_b1": "🔒 Platba na dobírku", "ty_b2": "🛡️ 30denní záruka", "ty_b3": "🔐 SSL ochrana",
    },
    "ro": {
        "title": "Breezon™ — Aer condiționat portabil 18.000 BTU fără furtun | -70%",
        "description": "Breezon™: climatizator portabil 18.000 BTU rece/cald, fără furtun exterior și fără instalare. Încălzește și răcește până la 145 m², filtre HEPA, plată ramburs.",
        "topbar": "🔥 REDUCERE 70% + LIVRARE GRATUITĂ — PLATĂ RAMBURS 🔥",
        "rating": "Evaluare medie: <strong>4,8 / 5</strong> · Pe baza a peste <strong>25.000</strong> de recenzii reale",
        "gift": "🚚 Livrare rapidă în 24/48 ore + Garanție de satisfacție sau ramburs",
        "h1": "Primul climatizator de <span class=\"hl\">18.000 BTU</span> fără furtun exterior: încălzește și răcește până la <span class=\"hl\">145 m²</span> în câteva minute",
        "lead": "<strong>Breezon™</strong> climatizează casa fără unitate exterioară și fără instalări complicate. Tehnologie <strong>Smart Climate AI</strong>, filtre <strong>HEPA</strong>, doar <strong>18 dB</strong> în modul noapte — și plătiți doar la livrare.",
        "hero_alt": "Breezon aer condiționat portabil 18.000 BTU",
        "cta": "COMANDĂ ACUM! →",
        "form_note": "🔒 Fără plată în avans · Plată ramburs · Livrare 24/48h",
        "f1h": "Rece și cald", "f1p": "Încălzește și răcește până la 145 m²",
        "f2h": "Zero furtun exterior", "f2p": "Fără motoare afară, zero instalare",
        "f3h": "Ultra silențios", "f3p": "26 dB max. · 18 dB mod noapte",
        "f4h": "Plată ramburs", "f4p": "Comod, sigur, fără avans",
        "urgency": "⏰ Oferta -70% activă doar azi",
        "cd_h": "Ore", "cd_m": "Min", "cd_s": "Sec",
        "stock_l": "Disponibilitate", "stock_r": "Au rămas puține unități!",
        "live": "<strong>{n} persoane</strong> vizualizează Breezon acum",
        "form_h": "Completați formularul de comandă",
        "form_p": "Vă vom contacta pentru a confirma detaliile livrării.",
        "name_l": "Nume și prenume*", "name_ph": "Andrei Popescu",
        "phone_l": "Număr de telefon*", "phone_ph": "+40 721 234 567",
        "addr_l": "Adresa de livrare*", "addr_ph": "Str. Victoriei 10, București",
        "submit": "Confirmă comanda",
        "w1e": "01 — Răcoare vara, căldură iarna",
        "w1h": "Climă perfectă în câteva minute, fără furtunuri sau instalări",
        "w1t": ["18.000 BTU", "Până la 145 m²", "Plug & Play"],
        "w1p": "Datorită puterii de <strong>18.000 BTU</strong>, <strong>Breezon™</strong> încălzește și răcește spații de până la <strong>145 m²</strong>. Fără furtun la fereastră, fără unitate exterioară: conectați la priză și setați temperatura de pe telecomandă, ecran sau smartphone.",
        "w1i": "Ideal pentru casă, birou sau cameră de oaspeți: mutați-l oriunde aveți nevoie.",
        "w2e": "02 — Aer curat și umiditate echilibrată",
        "w2h": "Filtre HEPA și Smart Climate AI pentru confort sănătos",
        "w2t": ["Filtru HEPA", "Cărbune activ", "Climate AI"],
        "w2p": "Tehnologia <strong>Smart Climate AI</strong> monitorizează calitatea aerului și umiditatea, ajustându-se automat pentru a preveni mucegaiul și mirosurile. Filtrul <strong>HEPA</strong> și prefiltrul rețin praf, alergeni și poluanți.",
        "w2i": "Filtre lavabile și reutilizabile ani de zile — fără costuri continue de înlocuire.",
        "w3e": "03 — Liniște noaptea și facturi mai mici",
        "w3h": "Doar 18 dB noaptea și consum optimizat",
        "w3t": ["26 dB max.", "18 dB noapte", "Smart AI"],
        "w3p": "<strong>Breezon™</strong> este conceput pentru confort maxim cu zgomot ultra-redus: <strong>26 dB</strong> la putere maximă și doar <strong>18 dB</strong> în modul noapte. Smart Climate AI optimizează puterea și ventilația, reducând risipa.",
        "w3i": "Mai puțin zgomot, mai puțin consum, mai multă odihnă — perfect și în dormitor.",
        "cmp_label": "Cea mai practică alegere pentru climatizarea casei",
        "cmp_h": "Breezon™ vs. climatizatoare tradiționale",
        "cmp_rows": [
            ("Instalare", "Unitate exterioară, găuri, tehnicieni", "Plug & Play, zero lucrări"),
            ("Furtun / evacuare", "Furtun la fereastră obligatoriu", "Fără furtun exterior"),
            ("Putere", "Adesea limitată / asimetrică", "18.000 BTU rece/cald"),
            ("Acoperire", "De obicei un dormitor", "Până la 145 m²"),
            ("Zgomot", "Deranjant noaptea", "Până la 18 dB mod noapte"),
            ("Aer", "Filtre de bază", "HEPA + cărbune lavabil"),
            ("Preț", "1.663 Lei", "Doar 499 Lei"),
        ],
        "cmp_th1": "Fix / portabil cu furtun",
        "rev_h": "Recenzii clienți",
        "rev_sub": "★ 4,8/5 · Cumpărare verificată · Recenzii verificate",
        "reviews": [
            ("În sfârșit fără furtun la fereastră", "«În sfârșit un climatizator portabil fără furtunul enervant! Îl mut ușor din cameră în cameră și casa are mereu temperatura perfectă. Iarna încălzește repede, vara răcește fără consum excesiv. Nu mai pot trăi fără el!»", "Andrei P.", "review-1"),
            ("Aer proaspăt, uscat și silențios", "«Am urât mereu căldura umedă acasă, dar cu Breezon aerul este în sfârșit proaspăt și uscat. Îl folosesc și iarna pentru living. Ușor de folosit, super silențios, fără instalare.»", "Mihai R.", "review-2"),
            ("Foarte practic cu aplicație și telecomandă", "«Foarte comod cu aplicația și telecomanda. Îl pot porni înainte să ajung acasă și totul e gata. În modul noapte abia se aude.»", "Elena M.", "review-3"),
        ],
        "verified": "Cumpărare verificată",
        "kit_eye": "Ce primiți cu Breezon",
        "kit_h": "Kit complet Breezon™",
        "kit_items": [
            "<strong>1× Breezon</strong> climatizator inteligent rece/cald 18.000 BTU",
            "Telecomandă + control smart prin aplicație",
            "3× pre-filtre cu cărbune activ lavabile (2 cadou)",
            "3× filtre HEPA lavabile (2 cadou)",
            "Tavă de condens 10 litri",
            "Manual în română · Garanție 30 zile · Livrare 24/48h ramburs",
        ],
        "faq_h": "Întrebări frecvente",
        "faqs": [
            ("Breezon necesită instalări complicate?", "Nu. Nu sunt necesare unități exterioare sau furtunul clasic la fereastră. Conectați la priză și alegeți temperatura dorită."),
            ("Poate încălzi și răci spații mari?", "Da. Cu 18.000 BTU, Breezon este conceput să încălzească și răcească spații de până la 145 m² în câteva minute."),
            ("Face zgomot noaptea?", "Nu. Modul noapte reduce automat zgomotul și intensitatea (până la 18 dB) pentru odihnă mai confortabilă."),
            ("Pot plăti ramburs?", "Da. Plătiți curierului la livrare. Aveți pregătiți <strong>499 Lei</strong>."),
            ("Ce se întâmplă dacă nu sunt mulțumit?", "Aveți 30 de zile garanție de satisfacție sau ramburs. Suportul nostru vă ajută cu returul și asistența."),
        ],
        "footer_tag": "Produse utile pentru viața de zi cu zi, livrare în 24–48 ore cu plată ramburs.",
        "footer_info": "Informații", "footer_about": "Despre noi", "footer_del": "Livrare",
        "footer_ship": "Politica de livrare", "footer_refund": "Politica de retur",
        "footer_home": "Acasă", "footer_contact": "Contactați-ne",
        "footer_copy": "Toate drepturile rezervate.",
        "submitting": "Se trimite...",
        "ty_title": "Comandă primită — Așteptați apelul de confirmare | Breezon™",
        "ty_desc": "Comanda dvs. Breezon™ a fost înregistrată. Ultimul pas: răspundeți la apelul de confirmare.",
        "ty_h": "Comanda dvs. a fost înregistrată cu succes!",
        "ty_sub": "Excelent — comanda Breezon™ este în procesare. Mai rămâne <strong>un ultim pas</strong> înainte de expediere.",
        "ty_eye": "👇 Ce trebuie să faceți acum",
        "ty_act_h": "📞 Răspundeți la apelul de confirmare",
        "ty_act_p": "Operatorul nostru vă va contacta <strong>în câteva ore</strong> pentru a confirma comanda.",
        "ty_warn": "Dacă nu răspundeți la apel, comanda va fi anulată automat.",
        "ty_hours_h": "🕒 Ore de contact",
        "ty_hours": "<strong>Luni – Sâmbătă</strong> · 9:00 – 18:00",
        "ty_next_h": "📋 Ce urmează",
        "ty_steps": [
            "La apel, <strong>confirmați datele</strong>",
            "Comanda se expediază în <strong>24–48 ore</strong>",
            "Livrare acasă și <strong>plată ramburs</strong>",
        ],
        "ty_b1": "🔒 Plată ramburs", "ty_b2": "🛡️ Garanție 30 zile", "ty_b3": "🔐 Protejat SSL",
    },
    "hu": {
        "title": "Breezon™ — Hordozható klíma 18 000 BTU cső nélkül | -70%",
        "description": "Breezon™: hordozható 18 000 BTU meleg/hideg klíma, külső cső és telepítés nélkül. Fűt és hűt akár 145 m²-ig, HEPA szűrők, utánvétes fizetés.",
        "topbar": "🔥 70% KEDVEZMÉNY + INGYENES SZÁLLÍTÁS — UTÁNVÉTES FIZETÉS 🔥",
        "rating": "Átlagos értékelés: <strong>4,8 / 5</strong> · Több mint <strong>25 000</strong> valódi vélemény alapján",
        "gift": "🚚 Gyors szállítás 24/48 órán belül + Elégedettségi garancia vagy visszatérítés",
        "h1": "Az első <span class=\"hl\">18 000 BTU</span> klíma külső cső nélkül: fűt és hűt akár <span class=\"hl\">145 m²</span>-ig percek alatt",
        "lead": "A <strong>Breezon™</strong> otthonát klimatizálja külső egység és bonyolult telepítés nélkül. <strong>Smart Climate AI</strong> technológia, <strong>HEPA</strong> szűrők, mindössze <strong>18 dB</strong> éjszakai módban — és csak átvételkor fizet.",
        "hero_alt": "Breezon hordozható klíma 18 000 BTU",
        "cta": "RENDELJEN MOST! →",
        "form_note": "🔒 Előleg nélkül · Utánvét · 24/48 órás szállítás",
        "f1h": "Hűtés és fűtés", "f1p": "Fűt és hűt akár 145 m²-ig",
        "f2h": "Nulla külső cső", "f2p": "Nincs kültéri motor, nulla telepítés",
        "f3h": "Ultra csendes", "f3p": "26 dB max. · 18 dB éjszakai mód",
        "f4h": "Utánvétes fizetés", "f4p": "Kényelmes, biztonságos, előleg nélkül",
        "urgency": "⏰ -70% ajánlat csak ma érvényes",
        "cd_h": "Óra", "cd_m": "Perc", "cd_s": "Mp",
        "stock_l": "Elérhetőség", "stock_r": "Már csak kevés darab maradt!",
        "live": "<strong>{n} ember</strong> nézi éppen a Breezont",
        "form_h": "Töltse ki a rendelési űrlapot",
        "form_p": "Felvesszük Önnel a kapcsolatot a szállítás részleteinek megerősítéséhez.",
        "name_l": "Teljes név*", "name_ph": "Kovács Gábor",
        "phone_l": "Telefonszám*", "phone_ph": "+36 30 123 4567",
        "addr_l": "Szállítási cím*", "addr_ph": "Andrássy út 10, 1061 Budapest",
        "submit": "Rendelés megerősítése",
        "w1e": "01 — Nyáron hűvös, télen meleg",
        "w1h": "Tökéletes klíma percek alatt, csövek és telepítés nélkül",
        "w1t": ["18 000 BTU", "Akár 145 m²", "Plug & Play"],
        "w1p": "Az <strong>18 000 BTU</strong> teljesítménynek köszönhetően a <strong>Breezon™</strong> akár <strong>145 m²</strong>-ig fűt és hűt. Ablakcső nélkül, külső egység nélkül: csatlakoztassa és állítsa be a hőmérsékletet távirányítóról, kijelzőről vagy okostelefonról.",
        "w1i": "Ideális otthonra, irodára vagy vendégszobára: vigye oda, ahová szüksége van.",
        "w2e": "02 — Tiszta levegő és kiegyensúlyozott páratartalom",
        "w2h": "HEPA szűrők és Smart Climate AI az egészséges komfortért",
        "w2t": ["HEPA szűrő", "Aktív szén", "Climate AI"],
        "w2p": "A <strong>Smart Climate AI</strong> technológia figyeli a levegő minőségét és a páratartalmat, automatikusan alkalmazkodva a penész és szagok megelőzésére. A <strong>HEPA</strong> szűrő és előszűrő megfogja a port, allergéneket és szennyeződéseket.",
        "w2i": "Mosható, újrahasználható szűrők évekig — nincs folyamatos csere költség.",
        "w3e": "03 — Csendes éjszakák, alacsonyabb számlák",
        "w3h": "Csak 18 dB éjjel és optimalizált fogyasztás",
        "w3t": ["26 dB max.", "18 dB éjjel", "Smart AI"],
        "w3p": "A <strong>Breezon™</strong> maximális komfortra készült ultracsendes működéssel: <strong>26 dB</strong> teljes teljesítménynél és mindössze <strong>18 dB</strong> éjszakai módban. A Smart Climate AI optimalizálja a teljesítményt és a szellőzést, csökkentve a pazarlást.",
        "w3i": "Kevesebb zaj, kevesebb fogyasztás, több pihenés — hálószobába is tökéletes.",
        "cmp_label": "A legpraktikusabb választás otthona klimatizálásához",
        "cmp_h": "Breezon™ vs. hagyományos klímák",
        "cmp_rows": [
            ("Telepítés", "Kültéri egység, furatok, szerelők", "Plug & Play, nulla munka"),
            ("Cső / elvezetés", "Ablakcső kötelező", "Külső cső nélkül"),
            ("Teljesítmény", "Gyakran korlátozott / aszimmetrikus", "18 000 BTU hideg/meleg"),
            ("Lefedettség", "Tipikusan egy hálószoba", "Akár 145 m²"),
            ("Zaj", "Zavaró éjjel", "Akár 18 dB éjszakai mód"),
            ("Levegő", "Alap szűrők", "Mosható HEPA + szén"),
            ("Ár", "121.663 Ft", "Csak 36.499 Ft"),
        ],
        "cmp_th1": "Fix / hordozható csővel",
        "rev_h": "Vásárlói vélemények",
        "rev_sub": "★ 4,8/5 · Ellenőrzött vásárlás · Ellenőrzött vélemények",
        "reviews": [
            ("Végre nincs ablakcső", "«Végre egy hordozható klíma cső nélkül! Könnyen mozgatom szobáról szobára, és otthon mindig tökéletes a hőmérséklet. Télen gyorsan fűt, nyáron hűt anélkül, hogy sokat fogyasztana. Nélküle már el sem tudom képzelni!»", "Gábor T.", "review-1"),
            ("Friss, száraz és csendes levegő", "«Mindig utáltam a párás meleget otthon, de a Breezonnal végre friss és száraz a levegő. Télen a nappali fűtésére is használom. Könnyű kezelni, szuper csendes, telepítés nélkül.»", "Zsuzsa K.", "review-2"),
            ("Nagyon praktikus app-pal és távirányítóval", "«Nagyon kényelmes az app és a távirányító. Hazafelé bekapcsolhatom, és minden kész. Éjszakai módban alig hallani.»", "Péter M.", "review-3"),
        ],
        "verified": "Ellenőrzött vásárlás",
        "kit_eye": "Mit kap a Breezonnal",
        "kit_h": "Teljes Breezon™ készlet",
        "kit_items": [
            "<strong>1× Breezon</strong> okos meleg/hideg klíma 18 000 BTU",
            "Távirányító + okos app vezérlés",
            "3× mosható aktív szén előszűrő (2 ajándék)",
            "3× mosható HEPA szűrő (2 ajándék)",
            "10 literes kondenzvíz tálca",
            "Magyar kézikönyv · 30 napos garancia · 24/48 órás utánvétes szállítás",
        ],
        "faq_h": "Gyakori kérdések",
        "faqs": [
            ("A Breezon bonyolult telepítést igényel?", "Nem. Nincs szükség külső egységre vagy klasszikus ablakcsőre. Csatlakoztassa és válassza ki a kívánt hőmérsékletet."),
            ("Tényleg fűt és hűt nagy tereket?", "Igen. 18 000 BTU-val a Breezon akár 145 m²-es tereket fűt és hűt percek alatt."),
            ("Zajos éjjel?", "Nem. Az éjszakai mód automatikusan csökkenti a zajt és az intenzitást (akár 18 dB-re) a kényelmesebb pihenésért."),
            ("Fizethetek utánvéttel?", "Igen. Az futárnak fizet átvételkor. Készítsen elő <strong>36.499 Ft</strong>-ot."),
            ("Mi van, ha nem vagyok elégedett?", "30 napos elégedettségi garancia vagy visszatérítés. Ügyfélszolgálatunk segít a visszaküldésben és támogatásban."),
        ],
        "footer_tag": "Hasznos mindennapi termékek, 24–48 órás szállítás utánvéttel.",
        "footer_info": "Információ", "footer_about": "Rólunk", "footer_del": "Szállítás",
        "footer_ship": "Szállítási feltételek", "footer_refund": "Visszatérítési feltételek",
        "footer_home": "Főoldal", "footer_contact": "Kapcsolat",
        "footer_copy": "Minden jog fenntartva.",
        "submitting": "Küldés...",
        "ty_title": "Rendelés fogadva — Várja a megerősítő hívást | Breezon™",
        "ty_desc": "Breezon™ rendelését rögzítettük. Utolsó lépés: fogadja a megerősítő hívást.",
        "ty_h": "Rendelését sikeresen rögzítettük!",
        "ty_sub": "Remek — a Breezon™ rendelés feldolgozás alatt van. Már csak <strong>egy utolsó lépés</strong> van a szállítás előtt.",
        "ty_eye": "👇 Mit kell tennie most",
        "ty_act_h": "📞 Fogadja a megerősítő hívást",
        "ty_act_p": "Munkatársunk <strong>néhány órán belül</strong> felveszi Önnel a kapcsolatot a rendelés megerősítéséhez.",
        "ty_warn": "Ha nem veszi fel a hívást, a rendelés automatikusan törlődik.",
        "ty_hours_h": "🕒 Elérhetőségi idő",
        "ty_hours": "<strong>Hétfő – Szombat</strong> · 9:00 – 18:00",
        "ty_next_h": "📋 Mi következik",
        "ty_steps": [
            "A hívás során <strong>erősítse meg adatait</strong>",
            "A rendelés <strong>24–48 órán</strong> belül feladásra kerül",
            "Házhozszállítás és <strong>utánvétes fizetés</strong>",
        ],
        "ty_b1": "🔒 Utánvét", "ty_b2": "🛡️ 30 napos garancia", "ty_b3": "🔐 SSL védelem",
    },
    "sk": {
        "title": "Breezon™ — Prenosná klimatizácia 18 000 BTU bez hadice | -70%",
        "description": "Breezon™: prenosná klimatizácia 18 000 BTU chlad/teplo, bez vonkajšej hadice a bez inštalácie. Vyhrieva a chladí až 145 m², HEPA filtre, platba pri prevzatí.",
        "topbar": "🔥 ZĽAVA 70 % + DOPRAVA ZDARMA — PLATBA PRI PREVZATÍ 🔥",
        "rating": "Priemerné hodnotenie: <strong>4,8 / 5</strong> · Na základe viac ako <strong>25 000</strong> skutočných recenzií",
        "gift": "🚚 Rýchle doručenie do 24/48 hodín + Garancia spokojnosti alebo vrátenie peňazí",
        "h1": "Prvá klimatizácia <span class=\"hl\">18 000 BTU</span> bez vonkajšej hadice: vyhrieva a chladí až <span class=\"hl\">145 m²</span> za pár minút",
        "lead": "<strong>Breezon™</strong> vám zabezpečí pohodlné klima doma bez vonkajšej jednotky a zložitej inštalácie. Technológia <strong>Smart Climate AI</strong>, filtre <strong>HEPA</strong>, len <strong>18 dB</strong> v nočnom režime — a platíte až pri doručení.",
        "hero_alt": "Breezon prenosná klimatizácia 18 000 BTU",
        "cta": "OBJEDNAŤ TERAZ! →",
        "form_note": "🔒 Bez platby vopred · Platba pri prevzatí · Doručenie 24/48 h",
        "f1h": "Chladenie a kúrenie", "f1p": "Vyhrieva a chladí až 145 m²",
        "f2h": "Bez vonkajšej hadice", "f2p": "Žiadne motory vonku, nulová inštalácia",
        "f3h": "Ultra tichý", "f3p": "26 dB max. · 18 dB nočný režim",
        "f4h": "Platba pri prevzatí", "f4p": "Pohodlne, bezpečne, bez zálohy",
        "urgency": "⏰ Ponuka -70 % platí len dnes",
        "cd_h": "Hod", "cd_m": "Min", "cd_s": "Sek",
        "stock_l": "Dostupnosť", "stock_r": "Zostáva len pár kusov!",
        "live": "<strong>{n} ľudí</strong> si práve prezerá Breezon",
        "form_h": "Vyplňte objednávkový formulár",
        "form_p": "Ozveme sa vám a potvrdíme detaily doručenia.",
        "name_l": "Meno a priezvisko*", "name_ph": "Martin Kováč",
        "phone_l": "Telefónne číslo*", "phone_ph": "+421 901 234 567",
        "addr_l": "Doručovacia adresa*", "addr_ph": "Hlavná 10, 811 01 Bratislava",
        "submit": "Potvrdiť objednávku",
        "w1e": "01 — V lete chladno, v zime teplo",
        "w1h": "Ideálne klima za pár minút, bez hadíc a inštalácie",
        "w1t": ["18 000 BTU", "Až 145 m²", "Plug & Play"],
        "w1p": "Vďaka výkonu <strong>18 000 BTU</strong> <strong>Breezon™</strong> vyhrieva a chladí priestory až <strong>145 m²</strong>. Bez hadice do okna, bez vonkajšej jednotky: zapojte do zásuvky a nastavte teplotu na ovládači, displeji alebo v telefóne.",
        "w1i": "Ideálne pre domov, kanceláriu alebo izbu pre hostí: presuňte ho kam potrebujete.",
        "w2e": "02 — Čistý vzduch a vyvážená vlhkosť",
        "w2h": "HEPA filtre a Smart Climate AI pre zdravé pohodlie",
        "w2t": ["HEPA filter", "Aktívne uhlie", "Climate AI"],
        "w2p": "Technológia <strong>Smart Climate AI</strong> sleduje kvalitu vzduchu a vlhkosť a automaticky sa prispôsobuje, aby predchádzala plesniam a zápachu. Filter <strong>HEPA</strong> a predfilter zachytia prach, alergény a nečistoty.",
        "w2i": "Umývateľné a opakovane použiteľné filtre na roky — žiadne priebežné náklady na výmenu.",
        "w3e": "03 — Ticho v noci a nižšie účty",
        "w3h": "Len 18 dB v noci a optimalizovaná spotreba",
        "w3t": ["26 dB max.", "18 dB noc", "Smart AI"],
        "w3p": "<strong>Breezon™</strong> je navrhnutý pre maximálne pohodlie s ultranízkou hlučnosťou: <strong>26 dB</strong> na plný výkon a len <strong>18 dB</strong> v nočnom režime. Smart Climate AI optimalizuje výkon a ventiláciu a znižuje plytvanie.",
        "w3i": "Menej hluku, menej spotreby, viac odpočinku — ideálne aj do spálne.",
        "cmp_label": "Najpraktickejšia voľba pre klima vo vašej domácnosti",
        "cmp_h": "Breezon™ vs. tradičné klimatizácie",
        "cmp_rows": [
            ("Inštalácia", "Vonkajšia jednotka, vŕtanie, technici", "Plug & Play, žiadne práce"),
            ("Hadica / odvod", "Hadica do okna nutná", "Bez vonkajšej hadice"),
            ("Výkon", "Často obmedzený / asymetrický", "18 000 BTU chlad/teplo"),
            ("Pokrytie", "Typicky jedna izba", "Až 145 m²"),
            ("Hluk", "Rušivý v noci", "Až 18 dB nočný režim"),
            ("Vzduch", "Základné filtre", "Umývateľné HEPA + uhlie"),
            ("Cena", "330 €", "Len 99 €"),
        ],
        "cmp_th1": "Pevná / prenosná s hadicou",
        "rev_h": "Recenzie zákazníkov",
        "rev_sub": "★ 4,8/5 · Overený nákup · Kontrolované recenzie",
        "reviews": [
            ("Konečne bez hadice v okne", "«Konečne prenosná klimatizácia bez otravnej hadice! Ľahko ju presúvam z izby do izby a doma je vždy ideálna teplota. V zime rýchlo kúri a v lete chladí bez vysokej spotreby. Už si bez nej neviem predstaviť život!»", "Martin K.", "review-1"),
            ("Čerstvý, suchý a tichý vzduch", "«Vždy som nenávidel vlhké horúčavy doma, ale s Breezon je vzduch konečne svieži a suchý. Používam ho aj v zime na kúrenie obývačky. Jednoduché ovládanie, super tichý a bez inštalácie.»", "Lucia H.", "review-2"),
            ("Veľmi praktický s aplikáciou a ovládačom", "«Veľmi pohodlné ovládanie cez aplikáciu aj diaľkový ovládač. Môžem ho zapnúť ešte cestou domov a všetko je pripravené. V nočnom režime ho takmer nepočujem.»", "Peter S.", "review-3"),
        ],
        "verified": "Overený nákup",
        "kit_eye": "Čo dostanete s Breezon",
        "kit_h": "Kompletná sada Breezon™",
        "kit_items": [
            "<strong>1× Breezon</strong> inteligentná klimatizácia chlad/teplo 18 000 BTU",
            "Diaľkový ovládač + smart ovládanie cez aplikáciu",
            "3× umývateľné predfiltre s aktívnym uhlím (2 zdarma)",
            "3× umývateľné HEPA filtre (2 zdarma)",
            "Nádoba na kondenzát 10 litrov",
            "Slovenský manuál · 30-dňová záruka · Doručenie 24/48 h pri prevzatí",
        ],
        "faq_h": "Často kladené otázky",
        "faqs": [
            ("Vyžaduje Breezon zložitú inštaláciu?", "Nie. Nepotrebujete vonkajšiu jednotku ani klasickú hadicu do okna. Zapojte do zásuvky a zvoľte požadovanú teplotu."),
            ("Naozaj zvládne vyhrievať a chladiť veľké priestory?", "Áno. S 18 000 BTU je Breezon navrhnutý na vyhrievanie a chladenie priestorov až 145 m² za pár minút."),
            ("Je hlučný v noci?", "Nie. Nočný režim automaticky znižuje hlučnosť a intenzitu (až na 18 dB) pre pohodlnejší spánok."),
            ("Môžem platiť pri prevzatí?", "Áno. Zaplatíte kuriérovi pri doručení. Majte pripravených <strong>99 €</strong>."),
            ("Čo ak nebudem spokojný/á?", "Máte 30-dňovú garanciu spokojnosti alebo vrátenie peňazí. Náš zákaznícky servis vám pomôže s vrátením a podporou."),
        ],
        "footer_tag": "Užitočné produkty pre každodenný život, doručenie do 24–48 hodín s platbou pri prevzatí.",
        "footer_info": "Informácie", "footer_about": "O nás", "footer_del": "Doručenie",
        "footer_ship": "Zásady doručenia", "footer_refund": "Zásady vrátenia",
        "footer_home": "Domov", "footer_contact": "Kontaktujte nás",
        "footer_copy": "Všetky práva vyhradené.",
        "submitting": "Odosielanie...",
        "ty_title": "Objednávka prijatá — Počkajte na potvrdzovací hovor | Breezon™",
        "ty_desc": "Vaša objednávka Breezon™ bola zaregistrovaná. Posledný krok: prijmite potvrdzovací hovor.",
        "ty_h": "Vaša objednávka bola úspešne zaregistrovaná!",
        "ty_sub": "Skvelé — objednávka Breezon™ sa spracováva. Zostáva len <strong>posledný krok</strong> pred odoslaním.",
        "ty_eye": "👇 Čo musíte urobiť teraz",
        "ty_act_h": "📞 Prijmite potvrdzovací hovor",
        "ty_act_p": "Náš operátor vás bude kontaktovať <strong>do niekoľkých hodín</strong>, aby potvrdil objednávku.",
        "ty_warn": "Ak hovor neprijmete, objednávka sa automaticky zruší.",
        "ty_hours_h": "🕒 Hodiny kontaktu",
        "ty_hours": "<strong>Pondelok – Sobota</strong> · 9:00 – 18:00",
        "ty_next_h": "📋 Čo bude nasledovať",
        "ty_steps": [
            "Počas hovoru <strong>potvrďte svoje údaje</strong>",
            "Objednávka bude odoslaná do <strong>24–48 hodín</strong>",
            "Doručenie domov a <strong>platba pri prevzatí</strong>",
        ],
        "ty_b1": "🔒 Platba pri prevzatí", "ty_b2": "🛡️ 30-dňová záruka", "ty_b3": "🔐 SSL ochrana",
    },
}


def tags_html(tags: list[str]) -> str:
    return "".join(f'<span class="tag">{t}</span>' for t in tags)


def cmp_table(tr: dict) -> str:
    rows = ""
    for label, bad, good in tr["cmp_rows"]:
        rows += f"<tr><td>{label}</td><td>{bad}</td><td class=\"win\">{good}</td></tr>\n    "
    return f"""<table>
    <tr><th></th><th>{tr['cmp_th1']}</th><th class="highlight">Breezon™</th></tr>
    {rows}</table>"""


def reviews_html(tr: dict, geo: str) -> str:
    blocks = []
    for title, quote, author, img in tr["reviews"]:
        v = "4" if img == "review-2" else "3"
        blocks.append(f"""      <div class="testimonial">
        <img decoding="async" class="t-photo" src="/assets/img/reviews/breezon/{img}.png?v={v}" alt="Breezon — {author} ✅ — {tr['verified']}" loading="lazy" onerror="this.src='/assets/img/placeholder.svg'">
        <div class="t-body">
          <div class="stars">★★★★★</div>
          <h4>{title}</h4>
          <p>«{quote[1:-1] if quote.startswith('«') else quote}»</p>
          <div class="author-row"><div class="author">{author} ✅ — {tr['verified']}</div></div>
        </div>
      </div>""")
    return "\n".join(blocks)


def faq_html(tr: dict) -> str:
    items = []
    for q, a in tr["faqs"]:
        items.append(f"""  <div class="faq-item"><button class="faq-q" type="button"><span>{q}</span><span class="arrow">▾</span></button>
    <div class="faq-a"><p>{a}</p></div></div>""")
    return "\n".join(items)


def kit_items_html(tr: dict) -> str:
    return "\n".join(f"        <li>{item}</li>" for item in tr["kit_items"])


def landing_html(g: dict, tr: dict) -> str:
    geo, lang, offer = g["geo"], g["lang"], g["offer"]
    slug_path = f"breezon/{offer}"
    canonical = f"https://powercurvemedia.com/{geo}/breezon/{offer}/"
    price_js = int(g["price"]) if float(g["price"]) == int(g["price"]) else g["price"]
    rev_blocks = []
    for title, quote, author, img in tr["reviews"]:
        v = "4" if img == "review-2" else "3"
        rev_blocks.append(f"""      <div class="testimonial">
        <img decoding="async" class="t-photo" src="/assets/img/reviews/breezon/{img}.png?v={v}" alt="Breezon — {author} ✅ — {tr['verified']}" loading="lazy" onerror="this.src='/assets/img/placeholder.svg'">
        <div class="t-body">
          <div class="stars">★★★★★</div>
          <h4>{title}</h4>
          <p>{quote}</p>
          <div class="author-row"><div class="author">{author} ✅ — {tr['verified']}</div></div>
        </div>
      </div>""")
    reviews_block = "\n".join(rev_blocks)

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-18294109732"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'AW-18294109732');
</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>{tr['title']}</title>
<meta name="description" content="{tr['description']}">
<meta name="contact" content="info@powercurvemedia.com">
<meta name="theme-color" content="#14181f">
<link rel="canonical" href="{canonical}">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/climaone-landing.css">
<script>
window.SITE_CONFIG = {{
  GEO: '{geo}',
  PRODUCT_SLUG: '{slug_path}',
  CURRENCY: '{g['currency']}',
  PRICE: {price_js},
  OFFER_NAME: 'Breezon {offer} {geo.upper()}',
  LP_ID: '{geo}-breezon-{offer}',
  FORM_ENDPOINT: 'https://TODO-network-endpoint.com/api/lead',
  SUBMITTING_LABEL: '{tr['submitting']}'
}};
</script>
<script src="/assets/js/tracking.js" defer></script>
<script src="/assets/js/form-handler.js" defer></script>
</head>
<body>

<div class="topbar">{tr['topbar']}</div>

<div class="rating-strip wrap">
  <div class="stars">★★★★★</div>
  <div class="rating-text">{tr['rating']}</div>
</div>

<section class="hero wrap">
  <div class="hero-copy">
    <span class="gift-strip">{tr['gift']}</span>
    <h1>{tr['h1']}</h1>
    <p class="lead">{tr['lead']}</p>
    <div class="hero-image hero-image-mobile-only">
      <img decoding="async" src="/assets/img/products/breezon/hero.png?v=3" alt="{tr['hero_alt']}" width="560" height="560" loading="eager" fetchpriority="high" onerror="this.src='/assets/img/placeholder.svg'">
    </div>
    <div class="price-block">
      <span class="was">{g['was']}</span>
      <span class="now">{g['now']}</span>
      <span class="pct">-70%</span>
    </div>
    <a href="#order-form" class="cta-btn">{tr['cta']}</a>
    <p class="form-note">{tr['form_note']}</p>
  </div>
  <div class="hero-image hero-image-desktop-only">
    <img decoding="async" src="/assets/img/products/breezon/hero.png?v=3" alt="{tr['hero_alt']}" width="560" height="560" loading="eager" fetchpriority="high" onerror="this.src='/assets/img/placeholder.svg'">
  </div>
</section>

<div class="wrap">
  <div class="feature-row">
    <div class="feature-item"><div class="ico">❄️</div><h4>{tr['f1h']}</h4><p>{tr['f1p']}</p></div>
    <div class="feature-item"><div class="ico">🚫</div><h4>{tr['f2h']}</h4><p>{tr['f2p']}</p></div>
    <div class="feature-item"><div class="ico">🔇</div><h4>{tr['f3h']}</h4><p>{tr['f3p']}</p></div>
    <div class="feature-item"><div class="ico">💳</div><h4>{tr['f4h']}</h4><p>{tr['f4p']}</p></div>
  </div>
</div>

<section class="order-section" id="order-form">
  <div class="wrap">
    <div class="urgency-strip">
      <div class="countdown-row">
        <div class="countdown-label">{tr['urgency']}</div>
        <div class="countdown-timer" id="countdownTimer">
          <div class="box"><div class="num" id="cd-h">00</div><div class="lbl">{tr['cd_h']}</div></div>
          <div class="sep">:</div>
          <div class="box"><div class="num" id="cd-m">14</div><div class="lbl">{tr['cd_m']}</div></div>
          <div class="sep">:</div>
          <div class="box"><div class="num" id="cd-s">59</div><div class="lbl">{tr['cd_s']}</div></div>
        </div>
      </div>
      <div class="stock-row">
        <div class="stock-label"><span class="left">{tr['stock_l']}</span><span class="right">{tr['stock_r']}</span></div>
        <div class="stock-bar"><div class="stock-bar-fill"></div></div>
      </div>
      <div class="live-row">
        <span class="dot"></span>
        <span id="liveCount">{tr['live'].replace('{n}', '41')}</span>
      </div>
    </div>

    <div class="order-card">
      <h2>{tr['form_h']}</h2>
      <p>{tr['form_p']}</p>
      <form class="cod-form order-form" novalidate>
        <div class="cod-form__field">
          <label class="cod-form__label" for="name">{tr['name_l']}</label>
          <input id="name" class="cod-form__input" type="text" name="name" autocomplete="name" placeholder="{tr['name_ph']}" required minlength="3">
        </div>
        <div class="cod-form__field">
          <label class="cod-form__label" for="phone">{tr['phone_l']}</label>
          <input id="phone" class="cod-form__input" type="tel" name="phone" autocomplete="tel" placeholder="{tr['phone_ph']}" required>
        </div>
        <div class="cod-form__field">
          <label class="cod-form__label" for="address">{tr['addr_l']}</label>
          <input id="address" class="cod-form__input" type="text" name="address" autocomplete="street-address" placeholder="{tr['addr_ph']}" required minlength="10">
        </div>
        <div style="margin-top:10px;text-align:center">
          <button name="submit" type="submit">{tr['submit']}</button>
        </div>
        <p class="form-note">{tr['form_note']}</p>
      </form>
    </div>
  </div>
</section>

<section class="why-block wrap">
  <div class="why-grid">
    <div class="why-img"><img decoding="async" src="/assets/img/products/breezon/desc-1.png?v=3" alt="{tr['hero_alt']}" loading="lazy" onerror="this.src='/assets/img/placeholder.svg'"></div>
    <div>
      <div class="num-eyebrow">{tr['w1e']}</div>
      <h3>{tr['w1h']}</h3>
      <div class="tag-row">{tags_html(tr['w1t'])}</div>
      <p>{tr['w1p']}</p>
      <p class="italic">{tr['w1i']}</p>
    </div>
  </div>
</section>

<section class="why-block wrap">
  <div class="why-grid">
    <div class="why-img"><img decoding="async" src="/assets/img/products/breezon/desc-2.png?v=3" alt="Breezon HEPA" loading="lazy" onerror="this.src='/assets/img/placeholder.svg'"></div>
    <div>
      <div class="num-eyebrow">{tr['w2e']}</div>
      <h3>{tr['w2h']}</h3>
      <div class="tag-row">{tags_html(tr['w2t'])}</div>
      <p>{tr['w2p']}</p>
      <p class="italic">{tr['w2i']}</p>
    </div>
  </div>
</section>

<section class="why-block wrap" style="border-bottom:none;">
  <div class="why-grid">
    <div class="why-img"><img decoding="async" src="/assets/img/products/breezon/desc-3.png?v=3" alt="Breezon night mode" loading="lazy" onerror="this.src='/assets/img/placeholder.svg'"></div>
    <div>
      <div class="num-eyebrow">{tr['w3e']}</div>
      <h3>{tr['w3h']}</h3>
      <div class="tag-row">{tags_html(tr['w3t'])}</div>
      <p>{tr['w3p']}</p>
      <p class="italic">{tr['w3i']}</p>
    </div>
  </div>
</section>

<section class="compare wrap">
  <div class="section-label">{tr['cmp_label']}</div>
  <h2>{tr['cmp_h']}</h2>
  {cmp_table(tr)}
</section>

<section class="testimonials">
  <div class="wrap">
    <div class="section-heading">
      <h2>{tr['rev_h']}</h2>
      <span class="eyebrow" style="display:block;margin-top:8px;color:#5b6472;font-weight:600;text-transform:none;letter-spacing:0;font-size:14px;">{tr['rev_sub']}</span>
    </div>
    <div class="t-grid">
{reviews_block}
    </div>
  </div>
</section>

<section class="kit-section wrap">
  <div class="section-heading">
    <span class="eyebrow">{tr['kit_eye']}</span>
    <h2>{tr['kit_h']}</h2>
  </div>
  <div class="kit-box">
    <img decoding="async" src="/assets/img/products/breezon/kit.png?v=3" alt="Breezon kit" loading="lazy" onerror="this.src='/assets/img/placeholder.svg'">
    <div class="kit-content">
      <div class="price-block" style="margin-bottom:16px;">
        <span class="was">{g['was']}</span>
        <span class="now">{g['now']}</span>
        <span class="pct">-70%</span>
      </div>
      <ul>
{kit_items_html(tr)}
      </ul>
      <a href="#order-form" class="cta-btn">{tr['cta']}</a>
    </div>
  </div>
</section>

<section class="faq wrap">
  <div class="section-heading">
    <h2>{tr['faq_h']}</h2>
  </div>
{faq_html(tr)}
</section>

<footer class="site-footer">
  <div class="wrap">
    <div>
      <a href="/" class="site-footer__brand" aria-label="powercurvemedia.com home">
        <span style="font-size:22px;font-weight:800;color:#fff;">powercurve<span style="color:#16a34a;">media</span></span>
      </a>
      <p class="site-footer__tagline">{tr['footer_tag']}</p>
      <p class="site-footer__address">Global Health Distribution S.r.l. — Piazza San Marco 5, 25063 Gardone Val Trompia, Italia</p>
      <p class="site-footer__email"><a href="mailto:info@powercurvemedia.com">info@powercurvemedia.com</a></p>
    </div>
    <div>
      <h3>{tr['footer_info']}</h3>
      <ul>
        <li><a href="/{geo}/privacy-policy.html">Privacy Policy</a></li>
        <li><a href="/{geo}/terms-conditions.html">Terms</a></li>
        <li><a href="/{geo}/cookie-policy.html">Cookie Policy</a></li>
      </ul>
    </div>
    <div>
      <h3>{tr['footer_about']}</h3>
      <ul>
        <li><a href="/">{tr['footer_home']}</a></li>
        <li><a href="/{geo}/">{geo.upper()}</a></li>
        <li><a href="mailto:info@powercurvemedia.com">{tr['footer_contact']}</a></li>
      </ul>
    </div>
    <div>
      <h3>{tr['footer_del']}</h3>
      <ul>
        <li><a href="/{geo}/shipping-policy.html">{tr['footer_ship']}</a></li>
        <li><a href="/{geo}/refund-policy.html">{tr['footer_refund']}</a></li>
      </ul>
    </div>
  </div>
  <p class="site-footer__copy">© <span data-year>2026</span> powercurvemedia.com – {tr['footer_copy']}</p>
</footer>

<script src="/assets/js/breezon-landing-{geo}.js" defer></script>
<script>
  document.querySelectorAll('[data-year]').forEach(function (el) {{
    el.textContent = String(new Date().getFullYear());
  }});
</script>
</body>
</html>
"""


def thankyou_html(g: dict, tr: dict) -> str:
    geo, lang, offer = g["geo"], g["lang"], g["offer"]
    price_js = int(g["price"]) if float(g["price"]) == int(g["price"]) else g["price"]
    steps = "\n".join(f"        <li>{s}</li>" for s in tr["ty_steps"])
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-18294109732"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'AW-18294109732');
</script>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{tr['ty_title']}</title>
<meta name="description" content="{tr['ty_desc']}">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/climaone-landing.css">
<style>
body {{ background: #f7f9fb; font-family: 'Poppins', sans-serif; }}
.ty-page {{ max-width: 540px; margin: 0 auto; padding: 1.5rem 1rem 3rem; }}
.ty-logo {{ text-align: center; padding: 1rem 0 0.5rem; font-size: 22px; font-weight: 800; }}
.ty-check {{ width: 64px; height: 64px; border-radius: 9999px; background: #fff; border: 2px solid #1f9d55; display: flex; align-items: center; justify-content: center; margin: 1rem auto 1.5rem; font-size: 2rem; color: #1f9d55; font-weight: 800; }}
.ty-headline {{ font-size: 1.625rem; font-weight: 800; line-height: 1.2; text-align: center; margin-bottom: 0.875rem; }}
.ty-subhead {{ text-align: center; color: #5b6472; font-size: 1rem; line-height: 1.5; margin-bottom: 1.5rem; max-width: 440px; margin-left: auto; margin-right: auto; }}
.ty-action {{ background: #f0fdf4; border: 1.5px solid #86efac; border-radius: 12px; padding: 1.25rem; margin-bottom: 1rem; }}
.ty-action__eyebrow {{ font-size: 0.7rem; font-weight: 800; letter-spacing: 0.15em; text-transform: uppercase; color: #15803d; margin-bottom: 0.625rem; text-align: center; }}
.ty-action__title {{ font-size: 1.25rem; font-weight: 800; text-align: center; margin-bottom: 0.625rem; }}
.ty-action__body, .ty-action__warning {{ text-align: center; color: #5b6472; font-size: 0.95rem; line-height: 1.5; }}
.ty-action__warning {{ color: #15803d; font-weight: 700; }}
.ty-box {{ background: #fff; border: 1px solid #e7eaee; border-radius: 8px; margin-bottom: 0.75rem; overflow: hidden; }}
.ty-box__header {{ padding: 0.625rem 1rem; background: #f7f9fb; border-bottom: 1px solid #e7eaee; font-size: 0.7rem; font-weight: 800; text-transform: uppercase; color: #5b6472; }}
.ty-box__body {{ padding: 0.75rem 1rem; font-size: 0.95rem; }}
.ty-steps-list {{ list-style: none; padding: 0; margin: 0; counter-reset: ty-step; }}
.ty-steps-list li {{ display: flex; gap: 0.625rem; padding: 0.625rem 0; border-bottom: 1px solid #e7eaee; font-size: 0.9rem; counter-increment: ty-step; }}
.ty-steps-list li::before {{ content: counter(ty-step) "."; font-weight: 800; color: #16a34a; }}
.ty-trust {{ display: flex; gap: 0.5rem; flex-wrap: wrap; justify-content: center; margin-top: 1.25rem; }}
.ty-trust__badge {{ background: #fff; border: 1px solid #e7eaee; border-radius: 9999px; padding: 0.4rem 0.875rem; font-size: 0.75rem; font-weight: 600; color: #5b6472; }}
</style>
<script>
window.SITE_CONFIG = {{
  GEO: '{geo}',
  PRODUCT_SLUG: 'breezon/{offer}',
  OFFER_NAME: 'Breezon {offer} {geo.upper()}',
  LP_ID: '{geo}-breezon-{offer}',
  CONVERSION_VALUE: {g['cpa']},
  CONVERSION_CURRENCY: 'EUR'
}};
</script>
<script src="/assets/js/tracking.js" defer></script>
</head>
<body>
<div class="ty-logo"><a href="/" style="color:inherit;text-decoration:none;">powercurve<span style="color:#16a34a;">media</span></a></div>
<main class="ty-page">
  <div class="ty-check">✓</div>
  <h1 class="ty-headline">{tr['ty_h']}</h1>
  <p class="ty-subhead">{tr['ty_sub']}</p>
  <section class="ty-action">
    <div class="ty-action__eyebrow">{tr['ty_eye']}</div>
    <h2 class="ty-action__title">{tr['ty_act_h']}</h2>
    <p class="ty-action__body">{tr['ty_act_p']}</p>
    <p class="ty-action__warning">{tr['ty_warn']}</p>
  </section>
  <section class="ty-box">
    <div class="ty-box__header">{tr['ty_hours_h']}</div>
    <div class="ty-box__body">{tr['ty_hours']}</div>
  </section>
  <section class="ty-box">
    <div class="ty-box__header">{tr['ty_next_h']}</div>
    <div class="ty-box__body"><ol class="ty-steps-list">
{steps}
    </ol></div>
  </section>
  <div class="ty-trust">
    <span class="ty-trust__badge">{tr['ty_b1']}</span>
    <span class="ty-trust__badge">{tr['ty_b2']}</span>
    <span class="ty-trust__badge">{tr['ty_b3']}</span>
  </div>
</main>
<script>
  (function () {{
    if (!window.gtag) return;
    var p = new URLSearchParams(window.location.search);
    gtag('event', 'conversion', {{
      'send_to': 'AW-18294109732/3Pa8COOx7dUcEOv3tatE',
      'value': {g['cpa']},
      'currency': 'EUR',
      'transaction_id': p.get('subid') || ('df_' + Date.now())
    }});
  }})();
</script>
</body>
</html>
"""


def js_file(geo: str, live_tpl: str) -> str:
    return f"""(function () {{
  const end = Date.now() + 15 * 60 * 1000;
  function tick() {{
    const diff = Math.max(0, end - Date.now());
    const h = Math.floor(diff / 3600000);
    const m = Math.floor((diff % 3600000) / 60000);
    const s = Math.floor((diff % 60000) / 1000);
    const hEl = document.getElementById('cd-h');
    const mEl = document.getElementById('cd-m');
    const sEl = document.getElementById('cd-s');
    if (hEl) hEl.textContent = String(h).padStart(2, '0');
    if (mEl) mEl.textContent = String(m).padStart(2, '0');
    if (sEl) sEl.textContent = String(s).padStart(2, '0');
    if (diff > 0) setTimeout(tick, 1000);
  }}
  tick();
}})();

(function () {{
  let count = 41;
  const el = document.getElementById('liveCount');
  if (!el) return;
  const tpl = {live_tpl!r};
  setInterval(function () {{
    count += (Math.random() > 0.5 ? 1 : -1) * Math.ceil(Math.random() * 2);
    count = Math.min(52, Math.max(34, count));
    el.innerHTML = tpl.replace('{{n}}', String(count));
  }}, 2000);
}})();

document.querySelectorAll('.faq-item').forEach(function (item) {{
  var btn = item.querySelector('.faq-q');
  if (!btn) return;
  btn.addEventListener('click', function () {{
    var isOpen = item.classList.contains('open');
    document.querySelectorAll('.faq-item.open').forEach(function (i) {{
      i.classList.remove('open');
    }});
    if (!isOpen) item.classList.add('open');
  }});
}});
"""


def main() -> None:
    for g in GEOS:
        geo = g["geo"]
        tr = T[geo]
        out_dir = ROOT / geo / "breezon" / g["offer"]
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "index.html").write_text(landing_html(g, tr), encoding="utf-8")
        (out_dir / "thank-you.html").write_text(thankyou_html(g, tr), encoding="utf-8")
        js_path = ROOT / "assets" / "js" / f"breezon-landing-{geo}.js"
        js_path.write_text(js_file(geo, tr["live"]), encoding="utf-8")
        print(f"Generated {out_dir}")


if __name__ == "__main__":
    main()
