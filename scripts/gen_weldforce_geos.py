#!/usr/bin/env python3
"""Generate WeldForce 800 landing + thank-you pages for SI, RO, PL, HU, CZ, SK."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IT_DIR = ROOT / "it" / "weldforce-800"
SITEMAP = ROOT / "sitemap.xml"
PRODUCT_SLUG = "weldforce-800"
LASTMOD = "2026-07-19"

GEOS = [
    {
        "geo": "si",
        "lang": "sl",
        "price": 99.99,
        "currency": "EUR",
        "price_disp": "99,99 €",
        "old_disp": "333 €",
        "cpa": 19,
        "country": "Sloveniji",
        "country_adj": "slovenski",
    },
    {
        "geo": "ro",
        "lang": "ro",
        "price": 549,
        "currency": "RON",
        "price_disp": "549 RON",
        "old_disp": "1.830 RON",
        "cpa": 19,
        "country": "România",
        "country_adj": "română",
    },
    {
        "geo": "pl",
        "lang": "pl",
        "price": 439,
        "currency": "PLN",
        "price_disp": "439 zł",
        "old_disp": "1.463 zł",
        "cpa": 21,
        "country": "Polsce",
        "country_adj": "polski",
    },
    {
        "geo": "hu",
        "lang": "hu",
        "price": 36999,
        "currency": "HUF",
        "price_disp": "36.999 Ft",
        "old_disp": "123.330 Ft",
        "cpa": 21,
        "country": "Magyarországon",
        "country_adj": "magyar",
    },
    {
        "geo": "cz",
        "lang": "cs",
        "price": 2449,
        "currency": "CZK",
        "price_disp": "2.449 Kč",
        "old_disp": "8.163 Kč",
        "cpa": 21,
        "country": "Česku",
        "country_adj": "český",
    },
    {
        "geo": "sk",
        "lang": "sk",
        "price": 99.99,
        "currency": "EUR",
        "price_disp": "99,99 €",
        "old_disp": "333 €",
        "cpa": 21,
        "country": "Slovensku",
        "country_adj": "slovenský",
    },
]


def price_schema(price: float | int) -> str:
    if isinstance(price, float) and not price.is_integer():
        return f"{price:.2f}"
    return str(int(price)) if float(price) == int(price) else f"{float(price):.2f}"


def price_js(price: float | int) -> str:
    if isinstance(price, float) and not price.is_integer():
        return f"{price:.2f}"
    if float(price) == int(price):
        return str(int(price))
    return f"{float(price):.2f}"


# ---------------------------------------------------------------------------
# Full UI translations (Italian source → native)
# ---------------------------------------------------------------------------

T = {
    "si": {
        "meta_title": "WeldForce 800™ — Profesionalni varilec 8 v 1 brez jeklenke | -70% samo danes",
        "meta_desc": "WeldForce 800™: profesionalni varilec 8 v 1 (laser, MIG brez plina, TIG, elektroda). Deluje na vtičnici 220V. Vari aluminij, litino, jeklo, železo in inox. Plačilo ob dostavi, pošiljanje 24/48h.",
        "og_title": "WeldForce 800™ — Varilec 8 v 1 | -70% samo danes",
        "og_desc": "Profesionalni varilec 8 v 1 brez jeklenke. Vtičnica 220V, samodejni nadzor. Plačilo ob dostavi.",
        "schema_name": "WeldForce 800™ — Profesionalni varilec 8 v 1",
        "schema_desc": "Profesionalni varilec 8 v 1: laser, MIG brez plina, TIG, elektroda, točkovno varjenje in rezanje. Deluje na vtičnici 220V. Vari aluminij, litino, jeklo, železo in inox.",
        "submitting": "Pošiljanje...",
        "cookie_text": "Uporabljamo tehnične in piškotke tretjih oseb za izboljšanje vaše izkušnje in za analitiko.",
        "cookie_accept": "Sprejmi",
        "cookie_learn": "Izvedi več",
        "banner": "🔥 SAMO DANES: -70% + PLAČILO OB DOSTAVI 🔥",
        "rating": '<strong>4,8/5</strong> — Več kot <strong>8.700</strong> preverjenih ocen',
        "guarantee_line": "🛡️ Garancija 2 leti + Dostava v 24-48h",
        "hero_title": "Profesionalni varilec 8 v 1 ⚡ Samodejno vari vsak material",
        "hero_sub": 'Več kot 8.700 ljudi je že zamenjalo stare varilce: ena kompaktna naprava za lasersko varjenje, MIG brez plina, TIG in elektrodo. <strong>Deluje na običajni vtičnici 220V</strong> in vari aluminij, litino, jeklo, železo in inox — tudi pod vodo.',
        "hero_alt": "WeldForce 800™ — profesionalni varilec 8 v 1 brez jeklenke",
        "hero_img_title": "WeldForce 800™ Varilec 8 v 1",
        "offer_label": "POSEBNA PONUDBA -70%",
        "cta": "DA, ŽELIM WeldForce 800™ →",
        "no_advance": "🔒 Brez predplačila · Brez kartice · Plačate šele ob dostavi",
        "trust_ship_t": "Dostava v 24-48h",
        "trust_ship_s": "Hitra pošiljka po vsej Sloveniji",
        "trust_pay_t": "Plačilo ob dostavi",
        "trust_pay_s": "Plačate šele, ko prejmete",
        "trust_gar_t": "Garancija 2 leti",
        "trust_gar_s": "Uradna kritje vključeno",
        "trust_ret_t": "Vračilo 30 dni",
        "trust_ret_s": "Enostavno in brezplačno vračilo",
        "countdown_aria": "Časovno omejena ponudba",
        "countdown_label": "⏰ Ponudba -70% poteče čez",
        "ore": "Ur",
        "min": "Min",
        "sec": "Sek",
        "watching": 'Razpoložljivost: <strong>Zadnji kosi na voljo</strong> · <strong>38 oseb</strong> trenutno gleda ta varilec',
        "form_title": "Dokončajte naročilo",
        "form_sub": "Izpolnite spodnji obrazec, naša ekipa vas bo kontaktirala za potrditev vseh podrobnosti.",
        "label_name": "Ime in priimek *",
        "ph_name": "Npr. Janez Novak",
        "err_name": "Vnesite ime in priimek (vsaj 3 znake)",
        "label_phone": "Telefonska številka *",
        "ph_phone": "Npr. 031 123 456",
        "err_phone": "Vnesite veljavno telefonsko številko",
        "label_addr": "Naslov za dostavo *",
        "ph_addr": "Ulica, hišna št., mesto, poštna št.",
        "err_addr": "Vnesite celoten naslov (vsaj 10 znakov)",
        "confirm_btn": "POTRDI NAROČILO",
        "f1_label": "01 — Ena naprava za vsako delo",
        "f1_title": "8 funkcij v eni kompaktni napravi",
        "f1_c1": "Lasersko varjenje",
        "f1_c2": "MIG brez plina",
        "f1_c3": "TIG in elektroda",
        "f1_p1": "Z WeldForce 800™ prehajate z enega dela na drugega brez menjave stroja: <strong>laser, MIG brez plina, TIG, elektroda, točkovno varjenje in rezanje</strong> so že vgrajeni. Poleg tega <strong>lasersko čiščenje</strong> odstrani rjo, barvo in okside s kovin v nekaj prehodih.",
        "f1_p2": "Manj opreme za nakup in shranjevanje: vse, kar potrebujete, imate v enem kompaktnem ohišju, pripravljenem v delavnici ali garaži.",
        "f1_alt": "Varilec 8 v 1 z več funkcijami",
        "f2_label": "02 — Samodejni nadzor, brez industrijske namestitve",
        "f2_title": "Sistem zazna material in vse nastavi sam",
        "f2_c1": "Standardna vtičnica 220V",
        "f2_c2": "Samodejna nastavitev",
        "f2_c3": "Primerno za začetnike",
        "f2_p1": "Elektronika WeldForce 800™ samodejno prilagodi tok, moč in podajanje žice glede na obdelovanec. Tako zmanjšate prežganine in prazne zagone, tudi če varite le ob vikendih.",
        "f2_p2": "Ni potrebe po liniji 380V: vtaknite vtič v <strong>hišno vtičnico 220V</strong> in začnite takoj — od garaže do vogala delavnice.",
        "f2_alt": "Sistem samodejnega nadzora, vtičnica 220V",
        "f3_label": "03 — Vari vsak material, tudi pod vodo",
        "f3_title": "Aluminij, litina, jeklo, železo, inox — brez omejitev",
        "f3_c1": "Zahtevni materiali",
        "f3_c2": "Uporaba tudi pod vodo",
        "f3_c3": "Zaščita pred preobremenitvijo",
        "f3_p1": "Obvlada zahtevne zlitine in težke razmere — <strong>aluminij, litino, inox in železo</strong> — in ostane stabilen tudi tam, kjer se mnogi tradicionalni varilci ustavijo, <strong>vključno z uporabo v vlažnih okoljih / pod vodo</strong>.",
        "f3_p2": "Serijsko zaščite proti pregrevanju in preobremenitvi; v embalaži so že klešče, kabli in bistveni dodatki, brez nakupa delov posebej.",
        "f3_alt": "Varjenje aluminija, jekla in inoxa tudi pod vodo",
        "cmp_sub": "Neposredna primerjava",
        "cmp_title": "Tradicionalni varilec proti WeldForce 800™",
        "cmp_trad": "Tradicionalni",
        "cmp_r1a": "Vrsta varjenja",
        "cmp_r1b": "Samo ena vrsta",
        "cmp_r1c": "8 v 1: laser, MIG, TIG, elektroda, točkovno",
        "cmp_r2a": "Rezanje in čiščenje",
        "cmp_r2b": "Ni vključeno",
        "cmp_r2c": "Lasersko rezanje in čiščenje vključeno",
        "cmp_r3a": "Nastavitev",
        "cmp_r3b": "Ročna in zapletena",
        "cmp_r3c": "Samodejna in pametna",
        "cmp_r4a": "Enostavnost uporabe",
        "cmp_r4b": "Težko za začetnike",
        "cmp_r4c": "Enostavno tudi brez izkušenj",
        "cmp_r5a": "Zahtevni materiali",
        "cmp_r5b": "Omejene zmogljivosti",
        "cmp_r5c": "Aluminij, litina, inox brez težav",
        "cmp_r6a": "Napajanje",
        "cmp_r6b": "Pogosto zahteva industrijski 380V",
        "cmp_r6c": "Standardna vtičnica 220V",
        "rev_title": "Več kot 8.700 zadovoljnih strank. Odkrijte, zakaj izberejo WeldForce 800™.",
        "rev1_t": "Močan in enostaven tudi za začetnike.",
        "rev1_p": "»Pričakoval sem nekaj zapletenega, a po dveh poskusih sem zavaril kos iz aluminija in enega iz inoxa. Dobra moč in jasni ukazi.«",
        "rev1_a": "Andrej P. — Ljubljana, Preverjena stranka",
        "rev1_alt": "WeldForce 800 v uporabi na kosu aluminija",
        "rev2_t": "Pripravljen za uporabo, brez industrijske namestitve.",
        "rev2_p": "»Priključil sem ga na vtičnico v garaži in v petih minutah sem že delal. Brez čudne namestitve: popoln za domača dela.«",
        "rev2_a": "Marko D. — Maribor, Preverjena stranka",
        "rev2_alt": "WeldForce 800 priključen na standardno vtičnico v garaži",
        "rev3_t": "Lasersko čiščenje je neverjetno.",
        "rev3_p": "»Na zarjavelih kosih lasersko čiščenje naredi razliko: v nekaj minutah je površina spet uporabna, brez ur s krtačo.«",
        "rev3_a": "Luka L. — Celje, Preverjena stranka",
        "rev3_alt": "Lasersko čiščenje zarjavelega kosa",
        "pkg_sub": "V embalaži",
        "pkg_title": "Kompletni komplet WeldForce 800™, pripravljen za uporabo",
        "pkg_alt": "Kompletni komplet WeldForce 800",
        "pkg_li1": "Varilec 8 v 1 — laser, MIG brez plina, TIG, elektroda, točkovno varjenje in rezanje",
        "pkg_li2": "Klešče in kabli v kompletu — nobenega dodatka za nakup posebej",
        "pkg_li3": "Sistem samodejnega nadzora — zazna material in sam nastavi moč",
        "pkg_li4": "Funkcija laserskega čiščenja — odstrani rjo in oksidacijo",
        "pkg_li5": "Primerno tudi za delo pod vodo",
        "pkg_li6": "Vgrajena zaščita pred preobremenitvijo in pregrevanjem",
        "pkg_li7": "<strong>Uradna garancija 2 leti</strong>",
        "faq_title": "Pogosta vprašanja",
        "faq1_q": "Kdaj prispe?",
        "faq1_a": "Dostava poteka v 24–48 delovnih urah. Kontaktiramo vas v nekaj urah za potrditev naročila in podrobnosti dostave.",
        "faq2_q": "Ali lahko plačam ob dostavi?",
        "faq2_a": "Da, plačate v gotovini neposredno kurirju, ko prejmete paket. Pripravite {price}.",
        "faq3_q": "Ali potrebujem industrijski tok 380V?",
        "faq3_a": "Ne, deluje na običajni vtičnici 220V: priključite in takoj začnete delati — doma, v garaži ali v delavnici.",
        "faq4_q": "Ali jo lahko uporabljam, tudi če nimam izkušenj z varjenjem?",
        "faq4_a": "Da, sistem samodejnega nadzora zazna material in sam nastavi moč, tok in hitrost žice ter prepreči napake tudi začetnikom.",
        "faq5_q": "Kaj pa, če nisem zadovoljen?",
        "faq5_a": "Imate 30 dni časa za brezplačno vračilo in polno vračilo denarja, brez vprašanj.",
        "footer_blurb": "Uporabni izdelki za vsakdanje življenje, dostava v 24–48 urah s plačilom ob dostavi.",
        "footer_info": "Informacije",
        "footer_about": "O nas",
        "footer_contact_link": "Stik",
        "footer_privacy": "Politika zasebnosti",
        "footer_terms": "Pogoji uporabe",
        "footer_cookie": "Politika piškotkov",
        "footer_ship": "Politika dostave",
        "footer_refund": "Politika vračila",
        "footer_contacts": "Kontakt",
        "footer_country": "Italija",
        "footer_rights": "Vse pravice pridržane",
        "popups": [
            {"initial": "A", "name": "Andrej P.", "image": "/assets/img/reviews/arcforce/popup-1.png", "message": " je pravkar naročil WeldForce 800™", "time": "pred 2 minutama, Ljubljana"},
            {"initial": "M", "name": "Marko D.", "image": "/assets/img/reviews/arcforce/popup-2.png", "message": " je pravkar potrdil naročilo", "time": "pred 5 minutami, Maribor"},
            {"initial": "L", "name": "Luka L.", "image": "/assets/img/reviews/arcforce/popup-3.png", "message": " je pravkar kupil WeldForce 800™", "time": "pred 8 minutami, Celje"},
            {"initial": "N", "name": "Nejc R.", "image": "/assets/img/reviews/arcforce/popup-1.png", "message": " je zaključil naročilo", "time": "pred 12 minutami, Koper"},
            {"initial": "G", "name": "Gregor B.", "image": "/assets/img/reviews/arcforce/popup-2.png", "message": " je pravkar naročil (dostava jutri)", "time": "pred 18 minutami, Kranj"},
            {"initial": "S", "name": "Simon M.", "image": "/assets/img/reviews/arcforce/popup-3.png", "message": " je potrdil svoje naročilo", "time": "pred 24 minutami, Novo mesto"},
        ],
        # thank-you
        "ty_title": "Naročilo prejeto — Počakajte na potrditveni klic | WeldForce 800™",
        "ty_desc": "Vaše naročilo WeldForce 800™ je bilo registrirano. Ostaja le še zadnji korak: odgovorite na potrditveni klic našega operaterja.",
        "ty_headline": "Vaše naročilo je bilo uspešno registrirano!",
        "ty_subhead": "Odlično — vaše naročilo WeldForce 800™ se obdeluje. Ostaja le še <strong>zadnji korak</strong> za dokončanje in začetek pošiljanja.",
        "ty_alt": "Ekipa powercurvemedia pri delu: klicni center in logistika COD",
        "ty_eyebrow": "👇 Kaj morate storiti zdaj",
        "ty_action_title": "📞 Odgovorite na potrditveni klic",
        "ty_action_body": 'Naš operater vas bo kontaktiral <strong>v naslednjih urah</strong> za potrditev naročila.',
        "ty_warning": "Če ne odgovorite na klic, bo naročilo samodejno preklicano.",
        "ty_hours_h": "🕒 Urniki stika",
        "ty_hours": "<strong>Ponedeljek – Sobota</strong> · 9:00 – 18:00",
        "ty_next_h": "📋 Kaj sledi",
        "ty_s1": 'Odgovorite na klic in <strong>potrdite svoje podatke</strong>',
        "ty_s2": 'Vaše naročilo bo odposlano v <strong>24–48 urah</strong>',
        "ty_s3": 'Dostava na dom in <strong>plačilo ob dostavi</strong>',
        "ty_b1": "🔒 Plačilo ob dostavi",
        "ty_b2": "🛡️ Garancija 24 mesecev",
        "ty_b3": "🔐 Zaščita SSL",
        "ty_footer_addr": "Piazza San Marco 5 — 25063 Gardone Val Trompia",
    },
    "ro": {
        "meta_title": "WeldForce 800™ — Aparat de sudură profesional 8 în 1 fără butelie | -70% doar azi",
        "meta_desc": "WeldForce 800™: aparat de sudură profesional 8 în 1 (laser, MIG fără gaz, TIG, electrod). Funcționează la priza 220V. Sudează aluminiu, fontă, oțel, fier și inox. Plata la livrare, expediere 24/48h.",
        "og_title": "WeldForce 800™ — Aparat de sudură 8 în 1 | -70% doar azi",
        "og_desc": "Aparat de sudură profesional 8 în 1 fără butelie. Priză 220V, control automat. Plata la livrare.",
        "schema_name": "WeldForce 800™ — Aparat de sudură profesional 8 în 1",
        "schema_desc": "Aparat de sudură profesional 8 în 1: laser, MIG fără gaz, TIG, electrod, puncte și tăiere. Funcționează la priza 220V. Sudează aluminiu, fontă, oțel, fier și inox.",
        "submitting": "Se trimite...",
        "cookie_text": "Folosim cookie-uri tehnice și de terți pentru a îmbunătăți experiența ta și pentru analiză.",
        "cookie_accept": "Accept",
        "cookie_learn": "Află mai mult",
        "banner": "🔥 DOAR AZI: -70% + PLATA LA LIVRARE 🔥",
        "rating": '<strong>4,8/5</strong> — Peste <strong>8.700</strong> recenzii verificate',
        "guarantee_line": "🛡️ Garanție 2 ani + Livrare în 24-48h",
        "hero_title": "Aparat de sudură profesional 8 în 1 ⚡ Sudează automat orice material",
        "hero_sub": 'Peste 8.700 de persoane și-au înlocuit deja vechile aparate de sudură: un singur dispozitiv compact pentru sudură laser, MIG fără gaz, TIG și electrod. <strong>Funcționează la priza normală de 220V</strong> și sudează aluminiu, fontă, oțel, fier și inox — chiar și sub apă.',
        "hero_alt": "WeldForce 800™ — aparat de sudură profesional 8 în 1 fără butelie",
        "hero_img_title": "WeldForce 800™ Aparat de sudură 8 în 1",
        "offer_label": "OFERTĂ SPECIALĂ -70%",
        "cta": "DA, VREAU WeldForce 800™ →",
        "no_advance": "🔒 Fără avans · Fără card · Plătești doar la livrare",
        "trust_ship_t": "Livrare în 24-48h",
        "trust_ship_s": "Expediere rapidă în toată România",
        "trust_pay_t": "Plata la livrare",
        "trust_pay_s": "Plătești doar când primești",
        "trust_gar_t": "Garanție 2 ani",
        "trust_gar_s": "Acoperire oficială inclusă",
        "trust_ret_t": "Retur 30 de zile",
        "trust_ret_s": "Rambursare simplă și gratuită",
        "countdown_aria": "Ofertă pe timp limitat",
        "countdown_label": "⏰ Oferta -70% expiră în",
        "ore": "Ore",
        "min": "Min",
        "sec": "Sec",
        "watching": 'Disponibilitate: <strong>Ultimele bucăți disponibile</strong> · <strong>38 de persoane</strong> privesc acum acest aparat',
        "form_title": "Finalizează comanda",
        "form_sub": "Completează formularul de mai jos, echipa noastră te va contacta pentru a confirma toate detaliile.",
        "label_name": "Nume și prenume *",
        "ph_name": "Ex. Ion Popescu",
        "err_name": "Introdu numele și prenumele (cel puțin 3 caractere)",
        "label_phone": "Număr de telefon *",
        "ph_phone": "Ex. 07xx xxx xxx",
        "err_phone": "Introdu un număr de telefon valid",
        "label_addr": "Adresa de livrare *",
        "ph_addr": "Stradă, nr., oraș, cod poștal",
        "err_addr": "Introdu o adresă completă (cel puțin 10 caractere)",
        "confirm_btn": "CONFIRMĂ COMANDA",
        "f1_label": "01 — Un singur dispozitiv pentru orice lucrare",
        "f1_title": "8 funcții într-un singur dispozitiv compact",
        "f1_c1": "Sudură laser",
        "f1_c2": "MIG fără gaz",
        "f1_c3": "TIG și electrod",
        "f1_p1": "Cu WeldForce 800™ treci de la o lucrare la alta fără să schimbi aparatul: <strong>laser, MIG fără gaz, TIG, electrod, puncte și tăiere</strong> sunt deja integrate. În plus, <strong>curățarea laser</strong> îndepărtează rugina, vopseaua și oxizii de pe metale în câteva treceri.",
        "f1_p2": "Mai puțină echipă de cumpărat și de depozitat: ai tot ce îți trebuie într-un singur corp compact, gata în atelier sau în garaj.",
        "f1_alt": "Aparat de sudură 8 în 1 cu funcții multiple",
        "f2_label": "02 — Control automat, fără instalare industrială",
        "f2_title": "Sistemul detectează materialul și reglează totul singur",
        "f2_c1": "Priză standard 220V",
        "f2_c2": "Reglare automată",
        "f2_c3": "Potrivit pentru începători",
        "f2_p1": "Electronica WeldForce 800™ adaptează singură curentul, puterea și avansul sârmei în funcție de piesă. Astfel reduci arsurile și repornirile în gol, chiar dacă sudezi doar în weekend.",
        "f2_p2": "Fără linie de 380V: bagi stecherul în <strong>priza de acasă de 220V</strong> și începi imediat, de la boxul auto până în colțul atelierului.",
        "f2_alt": "Sistem de control automat, priză 220V",
        "f3_label": "03 — Sudează orice material, chiar și sub apă",
        "f3_title": "Aluminiu, fontă, oțel, fier, inox — fără limite",
        "f3_c1": "Materiale dificile",
        "f3_c2": "Utilizare și sub apă",
        "f3_c3": "Protecție la suprasarcină",
        "f3_p1": "Gestionează aliaje dificile și situații grele — <strong>aluminiu, fontă, inox și fier</strong> — și rămâne stabil chiar și unde multe aparate tradiționale se opresc, <strong>inclusiv în medii umede / sub apă</strong>.",
        "f3_p2": "Protecții anti-supraîncălzire și anti-suprasarcină din fabrică; în cutie găsești deja clești, cabluri și accesorii esențiale, fără să cumperi piese separat.",
        "f3_alt": "Sudură pe aluminiu, oțel și inox chiar și sub apă",
        "cmp_sub": "Comparație directă",
        "cmp_title": "Aparat tradițional vs WeldForce 800™",
        "cmp_trad": "Tradițional",
        "cmp_r1a": "Tip de sudură",
        "cmp_r1b": "Un singur tip",
        "cmp_r1c": "8 în 1: laser, MIG, TIG, electrod, puncte",
        "cmp_r2a": "Tăiere și curățare",
        "cmp_r2b": "Neinclus",
        "cmp_r2c": "Tăiere și curățare laser incluse",
        "cmp_r3a": "Reglare",
        "cmp_r3b": "Manuală și complexă",
        "cmp_r3c": "Automată și inteligentă",
        "cmp_r4a": "Ușurință în utilizare",
        "cmp_r4b": "Greu pentru începători",
        "cmp_r4c": "Ușor chiar și fără experiență",
        "cmp_r5a": "Materiale dificile",
        "cmp_r5b": "Performanțe limitate",
        "cmp_r5c": "Aluminiu, fontă, inox fără probleme",
        "cmp_r6a": "Alimentare",
        "cmp_r6b": "Adesea necesită 380V industrial",
        "cmp_r6c": "Priză standard 220V",
        "rev_title": "Peste 8.700 de clienți mulțumiți. Descoperă de ce aleg WeldForce 800™.",
        "rev1_t": "Puternic și ușor chiar și pentru începători.",
        "rev1_p": "«Mă așteptam la ceva complicat, dar după două încercări am sudat o piesă din aluminiu și una din inox. Putere bună și comenzi clare.»",
        "rev1_a": "Andrei P. — București, Client verificat",
        "rev1_alt": "WeldForce 800 folosit pe o piesă din aluminiu",
        "rev2_t": "Gata de utilizare, fără instalare industrială.",
        "rev2_p": "«L-am conectat la priza din garaj și în cinci minute lucram deja. Fără instalări ciudate: perfect pentru treburile de acasă.»",
        "rev2_a": "Mihai D. — Cluj-Napoca, Client verificat",
        "rev2_alt": "WeldForce 800 conectat la o priză standard în garaj",
        "rev3_t": "Curățarea laser este incredibilă.",
        "rev3_p": "«Pe piesele ruginite curățarea laser face diferența: în câteva minute suprafața e din nou prelucrabilă, fără ore cu peria.»",
        "rev3_a": "Florin L. — Timișoara, Client verificat",
        "rev3_alt": "Curățare laser pe o piesă rugină",
        "pkg_sub": "În cutie",
        "pkg_title": "Kit complet WeldForce 800™, gata de utilizare",
        "pkg_alt": "Kit complet WeldForce 800",
        "pkg_li1": "Aparat de sudură 8 în 1 — laser, MIG fără gaz, TIG, electrod, puncte și tăiere",
        "pkg_li2": "Clești și cabluri complete — fără accesorii de cumpărat separat",
        "pkg_li3": "Sistem de control automat — detectează materialul și reglează puterea singur",
        "pkg_li4": "Funcție de curățare laser — îndepărtează rugina și oxidarea",
        "pkg_li5": "Potrivit și pentru lucrări sub apă",
        "pkg_li6": "Protecție integrată la suprasarcină și supraîncălzire",
        "pkg_li7": "<strong>Garanție oficială de 2 ani</strong>",
        "faq_title": "Întrebări frecvente",
        "faq1_q": "Când ajunge?",
        "faq1_a": "Livrarea are loc în 24–48 de ore lucrătoare. Te contactăm în câteva ore pentru a confirma comanda și detaliile de livrare.",
        "faq2_q": "Pot plăti la livrare?",
        "faq2_a": "Da, plătești cash direct curierului când primești coletul. Pregătește {price}.",
        "faq3_q": "Am nevoie de curent industrial de 380V?",
        "faq3_a": "Nu, funcționează la priza normală de 220V: îl conectezi și începi imediat să lucrezi, acasă, în garaj sau în atelier.",
        "faq4_q": "Îl pot folosi chiar dacă nu am experiență în sudură?",
        "faq4_a": "Da, sistemul de control automat detectează materialul și reglează singur puterea, curentul și viteza sârmei, evitând erorile chiar și pentru începători.",
        "faq5_q": "Ce se întâmplă dacă nu sunt mulțumit?",
        "faq5_a": "Ai 30 de zile pentru a-l returna gratuit și a primi rambursarea completă, fără întrebări.",
        "footer_blurb": "Produse utile pentru viața de zi cu zi, livrare în 24–48 de ore cu plata la livrare.",
        "footer_info": "Informații",
        "footer_about": "Despre noi",
        "footer_contact_link": "Contactează-ne",
        "footer_privacy": "Politica de Confidențialitate",
        "footer_terms": "Termeni și Condiții",
        "footer_cookie": "Politica Cookie-uri",
        "footer_ship": "Politica de Livrare",
        "footer_refund": "Politica de Returnare",
        "footer_contacts": "Contact",
        "footer_country": "Italia",
        "footer_rights": "Toate drepturile rezervate",
        "popups": [
            {"initial": "A", "name": "Andrei P.", "image": "/assets/img/reviews/arcforce/popup-1.png", "message": " a comandat tocmai WeldForce 800™", "time": "acum 2 minute, București"},
            {"initial": "M", "name": "Mihai D.", "image": "/assets/img/reviews/arcforce/popup-2.png", "message": " a confirmat tocmai comanda", "time": "acum 5 minute, Cluj-Napoca"},
            {"initial": "F", "name": "Florin L.", "image": "/assets/img/reviews/arcforce/popup-3.png", "message": " a cumpărat tocmai WeldForce 800™", "time": "acum 8 minute, Timișoara"},
            {"initial": "L", "name": "Lucian R.", "image": "/assets/img/reviews/arcforce/popup-1.png", "message": " a finalizat comanda", "time": "acum 12 minute, Iași"},
            {"initial": "G", "name": "George B.", "image": "/assets/img/reviews/arcforce/popup-2.png", "message": " a comandat tocmai (livrare mâine)", "time": "acum 18 minute, Constanța"},
            {"initial": "S", "name": "Stefan M.", "image": "/assets/img/reviews/arcforce/popup-3.png", "message": " a confirmat comanda sa", "time": "acum 24 minute, Brașov"},
        ],
        "ty_title": "Comandă primită — Așteaptă apelul de confirmare | WeldForce 800™",
        "ty_desc": "Comanda ta WeldForce 800™ a fost înregistrată. Mai rămâne un ultim pas: răspunde la apelul de confirmare al operatorului nostru.",
        "ty_headline": "Comanda ta a fost înregistrată cu succes!",
        "ty_subhead": "Perfect — comanda ta WeldForce 800™ este în procesare. Mai rămâne doar <strong>un ultim pas</strong> pentru a o finaliza și a porni expedierea.",
        "ty_alt": "Echipa powercurvemedia la lucru: call center și logistică COD",
        "ty_eyebrow": "👇 Ce trebuie să faci acum",
        "ty_action_title": "📞 Răspunde la apelul de confirmare",
        "ty_action_body": 'Un operator te va contacta <strong>în următoarele ore</strong> pentru a confirma comanda.',
        "ty_warning": "Dacă nu răspunzi la apel, comanda va fi anulată automat.",
        "ty_hours_h": "🕒 Program de contact",
        "ty_hours": "<strong>Luni – Sâmbătă</strong> · 9:00 – 18:00",
        "ty_next_h": "📋 Ce urmează",
        "ty_s1": 'Răspunde la apel și <strong>confirmă datele tale</strong>',
        "ty_s2": 'Comanda ta va fi expediată în <strong>24–48 de ore</strong>',
        "ty_s3": 'Livrare la domiciliu și <strong>plata la livrare</strong>',
        "ty_b1": "🔒 Plata la livrare",
        "ty_b2": "🛡️ Garanție 24 luni",
        "ty_b3": "🔐 Protecție SSL",
        "ty_footer_addr": "Piazza San Marco 5 — 25063 Gardone Val Trompia",
    },
    "pl": {
        "meta_title": "WeldForce 800™ — Profesjonalna spawarka 8 w 1 bez butli | -70% tylko dziś",
        "meta_desc": "WeldForce 800™: profesjonalna spawarka 8 w 1 (laser, MIG bez gazu, TIG, elektroda). Działa z gniazdka 220V. Spawa aluminium, żeliwo, stal, żelazo i inox. Płatność przy odbiorze, wysyłka 24/48h.",
        "og_title": "WeldForce 800™ — Spawarka 8 w 1 | -70% tylko dziś",
        "og_desc": "Profesjonalna spawarka 8 w 1 bez butli. Gniazdko 220V, automatyczna kontrola. Płatność przy odbiorze.",
        "schema_name": "WeldForce 800™ — Profesjonalna spawarka 8 w 1",
        "schema_desc": "Profesjonalna spawarka 8 w 1: laser, MIG bez gazu, TIG, elektroda, punktowe i cięcie. Działa z gniazdka 220V. Spawa aluminium, żeliwo, stal, żelazo i inox.",
        "submitting": "Wysyłanie...",
        "cookie_text": "Używamy technicznych plików cookie i plików cookie stron trzecich w celu poprawy doświadczenia i analizy.",
        "cookie_accept": "Akceptuję",
        "cookie_learn": "Dowiedz się więcej",
        "banner": "🔥 TYLKO DZIŚ: -70% + PŁATNOŚĆ PRZY ODBIORZE 🔥",
        "rating": '<strong>4,8/5</strong> — Ponad <strong>8.700</strong> zweryfikowanych opinii',
        "guarantee_line": "🛡️ Gwarancja 2 lata + Dostawa w 24-48h",
        "hero_title": "Profesjonalna spawarka 8 w 1 ⚡ Spawa automatycznie każdy materiał",
        "hero_sub": 'Ponad 8.700 osób już wymieniło stare spawarki: jedno kompaktowe urządzenie do spawania laserowego, MIG bez gazu, TIG i elektrodą. <strong>Działa ze zwykłego gniazdka 220V</strong> i spawa aluminium, żeliwo, stal, żelazo i inox — nawet pod wodą.',
        "hero_alt": "WeldForce 800™ — profesjonalna spawarka 8 w 1 bez butli",
        "hero_img_title": "WeldForce 800™ Spawarka 8 w 1",
        "offer_label": "OFERTA SPECJALNA -70%",
        "cta": "TAK, CHCĘ WeldForce 800™ →",
        "no_advance": "🔒 Bez zaliczki · Bez karty · Płacisz dopiero przy odbiorze",
        "trust_ship_t": "Dostawa w 24-48h",
        "trust_ship_s": "Szybka wysyłka w całej Polsce",
        "trust_pay_t": "Płatność przy odbiorze",
        "trust_pay_s": "Płacisz dopiero gdy odbierzesz",
        "trust_gar_t": "Gwarancja 2 lata",
        "trust_gar_s": "Oficjalne pokrycie w cenie",
        "trust_ret_t": "Zwrot 30 dni",
        "trust_ret_s": "Prosty i bezpłatny zwrot",
        "countdown_aria": "Oferta ograniczona czasowo",
        "countdown_label": "⏰ Oferta -70% kończy się za",
        "ore": "Godz",
        "min": "Min",
        "sec": "Sek",
        "watching": 'Dostępność: <strong>Ostatnie sztuki dostępne</strong> · <strong>38 osób</strong> ogląda teraz tę spawarkę',
        "form_title": "Dokończ zamówienie",
        "form_sub": "Wypełnij formularz poniżej, nasz zespół skontaktuje się z Tobą, aby potwierdzić wszystkie szczegóły.",
        "label_name": "Imię i nazwisko *",
        "ph_name": "Np. Jan Kowalski",
        "err_name": "Wpisz imię i nazwisko (co najmniej 3 znaki)",
        "label_phone": "Numer telefonu *",
        "ph_phone": "Np. 500 123 456",
        "err_phone": "Wpisz prawidłowy numer telefonu",
        "label_addr": "Adres dostawy *",
        "ph_addr": "Ulica, nr, miasto, kod pocztowy",
        "err_addr": "Wpisz pełny adres (co najmniej 10 znaków)",
        "confirm_btn": "POTWIERDŹ ZAMÓWIENIE",
        "f1_label": "01 — Jedno urządzenie do każdej pracy",
        "f1_title": "8 funkcji w jednym kompaktowym urządzeniu",
        "f1_c1": "Spawanie laserowe",
        "f1_c2": "MIG bez gazu",
        "f1_c3": "TIG i elektroda",
        "f1_p1": "Z WeldForce 800™ przechodzisz z jednej pracy na drugą bez zmiany maszyny: <strong>laser, MIG bez gazu, TIG, elektroda, punktowe i cięcie</strong> są już zintegrowane. Dodatkowo <strong>czyszczenie laserowe</strong> usuwa rdzę, farbę i tlenki z metali w kilku przejściach.",
        "f1_p2": "Mniej sprzętu do kupienia i przechowywania: wszystko, czego potrzebujesz, masz w jednej kompaktowej obudowie, gotowej w warsztacie lub garażu.",
        "f1_alt": "Spawarka 8 w 1 z wieloma funkcjami",
        "f2_label": "02 — Automatyczna kontrola, bez instalacji przemysłowej",
        "f2_title": "System wykrywa materiał i reguluje wszystko sam",
        "f2_c1": "Standardowe gniazdko 220V",
        "f2_c2": "Automatyczna regulacja",
        "f2_c3": "Odpowiednia dla początkujących",
        "f2_p1": "Elektronika WeldForce 800™ sama dostosowuje prąd, moc i podawanie drutu do elementu. Dzięki temu mniej przepaleń i pustych startów — nawet jeśli spawasz tylko w weekendy.",
        "f2_p2": "Bez linii 380V: włączasz wtyczkę do <strong>domowego gniazdka 220V</strong> i od razu zaczynasz — od garażu po kąt warsztatu.",
        "f2_alt": "System automatycznej kontroli, gniazdko 220V",
        "f3_label": "03 — Spawa każdy materiał, nawet pod wodą",
        "f3_title": "Aluminium, żeliwo, stal, żelazo, inox — bez ograniczeń",
        "f3_c1": "Trudne materiały",
        "f3_c2": "Użycie także pod wodą",
        "f3_c3": "Ochrona przed przeciążeniem",
        "f3_p1": "Radzi sobie z trudnymi stopami i sytuacjami — <strong>aluminium, żeliwo, inox i żelazo</strong> — i pozostaje stabilna nawet tam, gdzie wiele tradycyjnych spawarek się zatrzymuje, <strong>w tym w wilgotnych środowiskach / pod wodą</strong>.",
        "f3_p2": "Ochrona przed przegrzaniem i przeciążeniem w standardzie; w pudełku znajdziesz już szczypce, kable i niezbędne akcesoria, bez dokupywania części.",
        "f3_alt": "Spawanie aluminium, stali i inoxu także pod wodą",
        "cmp_sub": "Bezpośrednie porównanie",
        "cmp_title": "Tradycyjna spawarka vs WeldForce 800™",
        "cmp_trad": "Tradycyjna",
        "cmp_r1a": "Rodzaj spawania",
        "cmp_r1b": "Tylko jeden typ",
        "cmp_r1c": "8 w 1: laser, MIG, TIG, elektroda, punktowe",
        "cmp_r2a": "Cięcie i czyszczenie",
        "cmp_r2b": "Nieujęte",
        "cmp_r2c": "Cięcie i czyszczenie laserowe w zestawie",
        "cmp_r3a": "Regulacja",
        "cmp_r3b": "Ręczna i skomplikowana",
        "cmp_r3c": "Automatyczna i inteligentna",
        "cmp_r4a": "Łatwość użycia",
        "cmp_r4b": "Trudna dla początkujących",
        "cmp_r4c": "Łatwa nawet bez doświadczenia",
        "cmp_r5a": "Trudne materiały",
        "cmp_r5b": "Ograniczone osiągi",
        "cmp_r5c": "Aluminium, żeliwo, inox bez problemów",
        "cmp_r6a": "Zasilanie",
        "cmp_r6b": "Często wymaga przemysłowego 380V",
        "cmp_r6c": "Standardowe gniazdko 220V",
        "rev_title": "Ponad 8.700 zadowolonych klientów. Zobacz, dlaczego wybierają WeldForce 800™.",
        "rev1_t": "Mocna i łatwa nawet dla początkujących.",
        "rev1_p": "«Spodziewałem się czegoś skomplikowanego, a po dwóch próbach zespawałem element z aluminium i jeden z inoxu. Dobra moc i czytelne sterowanie.»",
        "rev1_a": "Andrzej P. — Warszawa, Zweryfikowany klient",
        "rev1_alt": "WeldForce 800 użyta na elemencie z aluminium",
        "rev2_t": "Gotowa do użycia, bez instalacji przemysłowej.",
        "rev2_p": "«Podłączyłem do gniazdka w garażu i w pięć minut już pracowałem. Bez dziwnych instalacji: idealna do domowych prac.»",
        "rev2_a": "Michał D. — Kraków, Zweryfikowany klient",
        "rev2_alt": "WeldForce 800 podłączona do standardowego gniazdka w garażu",
        "rev3_t": "Czyszczenie laserowe jest niesamowite.",
        "rev3_p": "«Na zardzewiałych elementach czyszczenie laserowe robi różnicę: w kilka minut powierzchnia znów nadaje się do obróbki, bez godzin z szczotką.»",
        "rev3_a": "Piotr L. — Gdańsk, Zweryfikowany klient",
        "rev3_alt": "Czyszczenie laserowe zardzewiałego elementu",
        "pkg_sub": "W zestawie",
        "pkg_title": "Kompletny zestaw WeldForce 800™, gotowy do użycia",
        "pkg_alt": "Kompletny zestaw WeldForce 800",
        "pkg_li1": "Spawarka 8 w 1 — laser, MIG bez gazu, TIG, elektroda, punktowe i cięcie",
        "pkg_li2": "Szczypce i kompletne kable — żadnych akcesoriów do dokupienia",
        "pkg_li3": "System automatycznej kontroli — wykrywa materiał i sam reguluje moc",
        "pkg_li4": "Funkcja czyszczenia laserowego — usuwa rdzę i utlenienie",
        "pkg_li5": "Nadaje się także do prac pod wodą",
        "pkg_li6": "Wbudowana ochrona przed przeciążeniem i przegrzaniem",
        "pkg_li7": "<strong>Oficjalna gwarancja 2 lata</strong>",
        "faq_title": "Często zadawane pytania",
        "faq1_q": "Kiedy dotrze?",
        "faq1_a": "Dostawa następuje w ciągu 24–48 godzin roboczych. Skontaktujemy się w ciągu kilku godzin, aby potwierdzić zamówienie i szczegóły dostawy.",
        "faq2_q": "Czy mogę zapłacić przy odbiorze?",
        "faq2_a": "Tak, płacisz gotówką bezpośrednio kurierowi przy odbiorze paczki. Przygotuj {price}.",
        "faq3_q": "Czy potrzebuję prądu przemysłowego 380V?",
        "faq3_a": "Nie, działa ze zwykłego gniazdka 220V: podłączasz i od razu zaczynasz pracę — w domu, w garażu lub w warsztacie.",
        "faq4_q": "Czy mogę jej używać, nawet jeśli nie mam doświadczenia w spawaniu?",
        "faq4_a": "Tak, system automatycznej kontroli wykrywa materiał i sam reguluje moc, prąd i prędkość drutu, unikając błędów nawet u początkujących.",
        "faq5_q": "A jeśli nie będę zadowolony?",
        "faq5_a": "Masz 30 dni na bezpłatny zwrot i pełny zwrot pieniędzy, bez pytań.",
        "footer_blurb": "Przydatne produkty do codziennego życia, dostawa w 24–48 godzin z płatnością za pobraniem.",
        "footer_info": "Informacje",
        "footer_about": "O nas",
        "footer_contact_link": "Kontakt",
        "footer_privacy": "Polityka prywatności",
        "footer_terms": "Regulamin",
        "footer_cookie": "Polityka cookies",
        "footer_ship": "Polityka dostawy",
        "footer_refund": "Polityka zwrotów",
        "footer_contacts": "Kontakt",
        "footer_country": "Włochy",
        "footer_rights": "Wszelkie prawa zastrzeżone",
        "popups": [
            {"initial": "A", "name": "Andrzej P.", "image": "/assets/img/reviews/arcforce/popup-1.png", "message": " właśnie zamówił WeldForce 800™", "time": "2 minuty temu, Warszawa"},
            {"initial": "M", "name": "Michał D.", "image": "/assets/img/reviews/arcforce/popup-2.png", "message": " właśnie potwierdził zamówienie", "time": "5 minut temu, Kraków"},
            {"initial": "P", "name": "Piotr L.", "image": "/assets/img/reviews/arcforce/popup-3.png", "message": " właśnie kupił WeldForce 800™", "time": "8 minut temu, Gdańsk"},
            {"initial": "L", "name": "Łukasz R.", "image": "/assets/img/reviews/arcforce/popup-1.png", "message": " zakończył zamówienie", "time": "12 minut temu, Wrocław"},
            {"initial": "G", "name": "Grzegorz B.", "image": "/assets/img/reviews/arcforce/popup-2.png", "message": " właśnie zamówił (dostawa jutro)", "time": "18 minut temu, Poznań"},
            {"initial": "S", "name": "Szymon M.", "image": "/assets/img/reviews/arcforce/popup-3.png", "message": " potwierdził swoje zamówienie", "time": "24 minuty temu, Łódź"},
        ],
        "ty_title": "Zamówienie przyjęte — Czekaj na rozmowę potwierdzającą | WeldForce 800™",
        "ty_desc": "Twoje zamówienie WeldForce 800™ zostało zarejestrowane. Pozostał tylko ostatni krok: odbierz rozmowę potwierdzającą od naszego operatora.",
        "ty_headline": "Twoje zamówienie zostało pomyślnie zarejestrowane!",
        "ty_subhead": "Świetnie — Twoje zamówienie WeldForce 800™ jest przetwarzane. Pozostał już tylko <strong>ostatni krok</strong> do jego ukończenia i wysyłki.",
        "ty_alt": "Zespół powercurvemedia w pracy: call center i logistyka pobraniowa",
        "ty_eyebrow": "👇 Co masz teraz zrobić",
        "ty_action_title": "📞 Odbierz rozmowę potwierdzającą",
        "ty_action_body": 'Nasz operator skontaktuje się z Tobą <strong>w ciągu najbliższych godzin</strong> w celu potwierdzenia zamówienia.',
        "ty_warning": "Jeśli nie odbierzesz telefonu, zamówienie zostanie automatycznie anulowane.",
        "ty_hours_h": "🕒 Godziny kontaktu",
        "ty_hours": "<strong>Poniedziałek – Sobota</strong> · 9:00 – 18:00",
        "ty_next_h": "📋 Co się stanie dalej",
        "ty_s1": 'Odbierz telefon i <strong>potwierdź swoje dane</strong>',
        "ty_s2": 'Twoje zamówienie zostanie wysłane w ciągu <strong>24–48 godzin</strong>',
        "ty_s3": 'Dostawa do domu i <strong>płatność za pobraniem</strong>',
        "ty_b1": "🔒 Płatność za pobraniem",
        "ty_b2": "🛡️ Gwarancja 24 miesiące",
        "ty_b3": "🔐 Ochrona SSL",
        "ty_footer_addr": "Piazza San Marco 5 — 25063 Gardone Val Trompia",
    },
}

T_EXTRA = {
    "hu": {
        "meta_title": "WeldForce 800™ — Professzionális 8 az 1-ben hegesztő palack nélkül | -70% csak ma",
        "meta_desc": "WeldForce 800™: professzionális 8 az 1-ben hegesztő (lézer, gáz nélküli MIG, TIG, elektróda). 220V-os aljzattal működik. Alumíniumot, öntöttvasat, acélt, vasat és inoxot hegeszt. Fizetés átvételkor, szállítás 24/48h.",
        "og_title": "WeldForce 800™ — 8 az 1-ben hegesztő | -70% csak ma",
        "og_desc": "Professzionális 8 az 1-ben hegesztő palack nélkül. 220V-os aljzat, automatikus vezérlés. Fizetés átvételkor.",
        "schema_name": "WeldForce 800™ — Professzionális 8 az 1-ben hegesztő",
        "schema_desc": "Professzionális 8 az 1-ben hegesztő: lézer, gáz nélküli MIG, TIG, elektróda, ponthegesztés és vágás. 220V-os aljzattal működik. Alumíniumot, öntöttvasat, acélt, vasat és inoxot hegeszt.",
        "submitting": "Küldés folyamatban...",
        "cookie_text": "Technikai és harmadik féltől származó sütiket használunk az élmény javítása és elemzés céljából.",
        "cookie_accept": "Elfogadom",
        "cookie_learn": "Tudj meg többet",
        "banner": "🔥 CSAK MA: -70% + FIZETÉS ÁTVÉTELKOR 🔥",
        "rating": '<strong>4,8/5</strong> — Több mint <strong>8.700</strong> ellenőrzött értékelés',
        "guarantee_line": "🛡️ 2 év garancia + Kézbesítés 24-48 órán belül",
        "hero_title": "Professzionális 8 az 1-ben hegesztő ⚡ Automatikusan hegeszt minden anyagot",
        "hero_sub": 'Több mint 8.700 ember cserélte már le a régi hegesztőjét: egy kompakt készülék lézerhegesztéshez, gáz nélküli MIG-hez, TIG-hez és elektródához. <strong>A szokásos 220V-os aljzattal működik</strong>, és alumíniumot, öntöttvasat, acélt, vasat és inoxot hegeszt — akár víz alatt is.',
        "hero_alt": "WeldForce 800™ — professzionális 8 az 1-ben hegesztő palack nélkül",
        "hero_img_title": "WeldForce 800™ 8 az 1-ben hegesztő",
        "offer_label": "KÜLÖNLEGES AJÁNLAT -70%",
        "cta": "IGEN, KÉREM a WeldForce 800™-at →",
        "no_advance": "🔒 Nincs előleg · Nincs bankkártya · Csak átvételkor fizet",
        "trust_ship_t": "Kézbesítés 24-48 óra",
        "trust_ship_s": "Gyors szállítás egész Magyarországon",
        "trust_pay_t": "Fizetés átvételkor",
        "trust_pay_s": "Csak akkor fizet, amikor megkapja",
        "trust_gar_t": "2 év garancia",
        "trust_gar_s": "Hivatalos fedezet benne van",
        "trust_ret_t": "30 napos visszaküldés",
        "trust_ret_s": "Egyszerű és ingyenes visszatérítés",
        "countdown_aria": "Időkorlátozott ajánlat",
        "countdown_label": "⏰ A -70%-os ajánlat lejár",
        "ore": "Óra",
        "min": "Perc",
        "sec": "Mp",
        "watching": 'Elérhetőség: <strong>Utolsó darabok</strong> · <strong>38 ember</strong> nézi most ezt a hegesztőt',
        "form_title": "Fejezze be a rendelését",
        "form_sub": "Töltse ki az alábbi űrlapot, csapatunk felveszi Önnel a kapcsolatot az összes részlet megerősítéséhez.",
        "label_name": "Teljes név *",
        "ph_name": "Pl. Kovács János",
        "err_name": "Adja meg a teljes nevét (legalább 3 karakter)",
        "label_phone": "Telefonszám *",
        "ph_phone": "Pl. 06 30 123 4567",
        "err_phone": "Adjon meg érvényes telefonszámot",
        "label_addr": "Szállítási cím *",
        "ph_addr": "Utca, házszám, város, irányítószám",
        "err_addr": "Adjon meg teljes címet (legalább 10 karakter)",
        "confirm_btn": "RENDELÉS MEGERŐSÍTÉSE",
        "f1_label": "01 — Egy készülék minden munkához",
        "f1_title": "8 funkció egy kompakt készülékben",
        "f1_c1": "Lézerhegesztés",
        "f1_c2": "Gáz nélküli MIG",
        "f1_c3": "TIG és elektróda",
        "f1_p1": "A WeldForce 800™-mal gépcseré nélkül vált egyik munkáról a másikra: <strong>lézer, gáz nélküli MIG, TIG, elektróda, ponthegesztés és vágás</strong> már beépítve. Emellett a <strong>lézeres tisztítás</strong> néhány menetben eltávolítja a rozsdát, festéket és oxidokat a fémekről.",
        "f1_p2": "Kevesebb berendezés vásárlása és tárolása: minden, amire szüksége van, egy kompakt házban van, készen a műhelyben vagy a garázsban.",
        "f1_alt": "8 az 1-ben hegesztő több funkcióval",
        "f2_label": "02 — Automatikus vezérlés, ipari telepítés nélkül",
        "f2_title": "A rendszer érzékeli az anyagot és mindent magától állít",
        "f2_c1": "Standard 220V-os aljzat",
        "f2_c2": "Automatikus szabályozás",
        "f2_c3": "Kezdőknek is alkalmas",
        "f2_p1": "A WeldForce 800™ elektronikája magától igazítja az áramot, a teljesítményt és a huzalelőtolást a darabhoz. Így kevesebb az átégés és az üres indítás — még akkor is, ha csak hétvégén hegeszt.",
        "f2_p2": "Nincs szükség 380V-os vonalra: dugja be a <strong>házi 220V-os aljzatba</strong>, és azonnal kezdhet — a garázstól a műhely sarkáig.",
        "f2_alt": "Automatikus vezérlőrendszer, 220V-os aljzat",
        "f3_label": "03 — Minden anyagot hegeszt, akár víz alatt is",
        "f3_title": "Alumínium, öntöttvas, acél, vas, inox — határok nélkül",
        "f3_c1": "Nehéz anyagok",
        "f3_c2": "Használat víz alatt is",
        "f3_c3": "Túlterhelés elleni védelem",
        "f3_p1": "Kezeli a nehéz ötvözeteket és helyzeteket — <strong>alumínium, öntöttvas, inox és vas</strong> — és stabil marad ott is, ahol sok hagyományos hegesztő megáll, <strong>beleértve a nedves környezetet / víz alatti használatot</strong>.",
        "f3_p2": "Gyárilag túlmelegedés- és túlterhelés-védelem; a dobozban már megtalálja a fogókat, kábeleket és alapvető tartozékokat, külön alkatrészvásárlás nélkül.",
        "f3_alt": "Hegesztés alumíniumon, acélon és inoxon akár víz alatt",
        "cmp_sub": "Közvetlen összehasonlítás",
        "cmp_title": "Hagyományos hegesztő vs WeldForce 800™",
        "cmp_trad": "Hagyományos",
        "cmp_r1a": "Hegesztés típusa",
        "cmp_r1b": "Csak egy típus",
        "cmp_r1c": "8 az 1-ben: lézer, MIG, TIG, elektróda, pont",
        "cmp_r2a": "Vágás és tisztítás",
        "cmp_r2b": "Nem tartozék",
        "cmp_r2c": "Lézeres vágás és tisztítás benne",
        "cmp_r3a": "Beállítás",
        "cmp_r3b": "Kézi és bonyolult",
        "cmp_r3c": "Automatikus és intelligens",
        "cmp_r4a": "Használhatóság",
        "cmp_r4b": "Nehéz kezdőknek",
        "cmp_r4c": "Könnyű tapasztalat nélkül is",
        "cmp_r5a": "Nehéz anyagok",
        "cmp_r5b": "Korlátozott teljesítmény",
        "cmp_r5c": "Alumínium, öntöttvas, inox gond nélkül",
        "cmp_r6a": "Tápellátás",
        "cmp_r6b": "Gyakran ipari 380V-ot igényel",
        "cmp_r6c": "Standard 220V-os aljzat",
        "rev_title": "Több mint 8.700 elégedett vásárló. Tudja meg, miért választják a WeldForce 800™-at.",
        "rev1_t": "Erős és könnyű akár kezdőknek is.",
        "rev1_p": "«Valami bonyolultra számítottam, de két próba után összehegesztettem egy alumínium és egy inox darabot. Jó teljesítmény és egyértelmű kezelés.»",
        "rev1_a": "András P. — Budapest, Ellenőrzött vásárló",
        "rev1_alt": "WeldForce 800 alumínium darabon",
        "rev2_t": "Azonnal használható, ipari telepítés nélkül.",
        "rev2_p": "«Bedugtam a garázs aljzatába, és öt perc múlva már dolgoztam. Nincs furcsa telepítés: tökéletes otthoni munkákhoz.»",
        "rev2_a": "Mihály D. — Debrecen, Ellenőrzött vásárló",
        "rev2_alt": "WeldForce 800 standard aljzatra csatlakoztatva a garázsban",
        "rev3_t": "A lézeres tisztítás hihetetlen.",
        "rev3_p": "«Rozsdás darabokon a lézeres tisztítás számít: néhány perc alatt újra megmunkálható a felület, órákig tartó kefélés nélkül.»",
        "rev3_a": "László L. — Szeged, Ellenőrzött vásárló",
        "rev3_alt": "Lézeres tisztítás rozsdás darabon",
        "pkg_sub": "A csomagban",
        "pkg_title": "Teljes WeldForce 800™ készlet, használatra kész",
        "pkg_alt": "Teljes WeldForce 800 készlet",
        "pkg_li1": "8 az 1-ben hegesztő — lézer, gáz nélküli MIG, TIG, elektróda, ponthegesztés és vágás",
        "pkg_li2": "Fogók és teljes kábelkészlet — nincs külön tartozékvásárlás",
        "pkg_li3": "Automatikus vezérlőrendszer — érzékeli az anyagot és magától állítja a teljesítményt",
        "pkg_li4": "Lézeres tisztítási funkció — eltávolítja a rozsdát és oxidációt",
        "pkg_li5": "Víz alatti munkákhoz is alkalmas",
        "pkg_li6": "Beépített túlterhelés- és túlmelegedés-védelem",
        "pkg_li7": "<strong>Hivatalos 2 év garancia</strong>",
        "faq_title": "Gyakori kérdések",
        "faq1_q": "Mikor érkezik?",
        "faq1_a": "A kézbesítés 24–48 munkanapon belüli órában történik. Néhány órán belül felvesszük Önnel a kapcsolatot a rendelés és a szállítási részletek megerősítéséhez.",
        "faq2_q": "Fizethetek átvételkor?",
        "faq2_a": "Igen, készpénzzel fizet közvetlenül a futárnak, amikor átveszi a csomagot. Tartsa készenlétben: {price}.",
        "faq3_q": "Szükségem van ipari 380V-os áramra?",
        "faq3_a": "Nem, a szokásos 220V-os aljzattal működik: bedugja, és azonnal dolgozhat otthon, a garázsban vagy a műhelyben.",
        "faq4_q": "Használhatom akkor is, ha nincs hegesztési tapasztalatom?",
        "faq4_a": "Igen, az automatikus vezérlés érzékeli az anyagot, és magától állítja a teljesítményt, áramot és huzalsebességet, így a kezdők is elkerülik a hibákat.",
        "faq5_q": "Mi van, ha nem vagyok elégedett?",
        "faq5_a": "30 napja van ingyenesen visszaküldeni és teljes visszatérítést kapni, kérdések nélkül.",
        "footer_blurb": "Hasznos termékek a mindennapi élethez, kézbesítés 24–48 óra alatt utánvétes fizetéssel.",
        "footer_info": "Információ",
        "footer_about": "Rólunk",
        "footer_contact_link": "Kapcsolat",
        "footer_privacy": "Adatvédelmi szabályzat",
        "footer_terms": "Általános szerződési feltételek",
        "footer_cookie": "Cookie szabályzat",
        "footer_ship": "Szállítási feltételek",
        "footer_refund": "Visszaküldési szabályzat",
        "footer_contacts": "Kapcsolat",
        "footer_country": "Olaszország",
        "footer_rights": "Minden jog fenntartva",
        "popups": [
            {"initial": "A", "name": "András P.", "image": "/assets/img/reviews/arcforce/popup-1.png", "message": " éppen most rendelte a WeldForce 800™-at", "time": "2 perce, Budapest"},
            {"initial": "M", "name": "Mihály D.", "image": "/assets/img/reviews/arcforce/popup-2.png", "message": " éppen most erősítette meg a rendelést", "time": "5 perce, Debrecen"},
            {"initial": "L", "name": "László L.", "image": "/assets/img/reviews/arcforce/popup-3.png", "message": " éppen most vásárolta a WeldForce 800™-at", "time": "8 perce, Szeged"},
            {"initial": "P", "name": "Péter R.", "image": "/assets/img/reviews/arcforce/popup-1.png", "message": " befejezte a rendelést", "time": "12 perce, Pécs"},
            {"initial": "G", "name": "Gábor B.", "image": "/assets/img/reviews/arcforce/popup-2.png", "message": " éppen most rendelt (szállítás holnap)", "time": "18 perce, Győr"},
            {"initial": "S", "name": "Sándor M.", "image": "/assets/img/reviews/arcforce/popup-3.png", "message": " megerősítette a rendelését", "time": "24 perce, Miskolc"},
        ],
        "ty_title": "Rendelés megérkezett — Várja a megerősítő hívást | WeldForce 800™",
        "ty_desc": "A WeldForce 800™ rendelése regisztrálva lett. Már csak egy utolsó lépés van hátra: válaszoljon operátorunk megerősítő hívására.",
        "ty_headline": "A rendelése sikeresen regisztrálva lett!",
        "ty_subhead": "Tökéletes — a WeldForce 800™ rendelése feldolgozás alatt áll. Csak <strong>egy utolsó lépés</strong> van hátra a befejezéséhez és a szállítás megkezdéséhez.",
        "ty_alt": "A powercurvemedia csapata munka közben: call center és COD logisztika",
        "ty_eyebrow": "👇 Mit kell most tennie",
        "ty_action_title": "📞 Válaszoljon a megerősítő hívásra",
        "ty_action_body": 'Operátorunk <strong>a következő órákban</strong> felveszi Önnel a kapcsolatot a rendelés megerősítéséhez.',
        "ty_warning": "Ha nem válaszol a hívásra, a rendelés automatikusan törlődik.",
        "ty_hours_h": "🕒 Kapcsolattartási idő",
        "ty_hours": "<strong>Hétfő – Szombat</strong> · 9:00 – 18:00",
        "ty_next_h": "📋 Mi történik ezután",
        "ty_s1": 'Válaszoljon a hívásra és <strong>erősítse meg adatait</strong>',
        "ty_s2": 'Rendelése <strong>24–48 órán belül</strong> kerül feladásra',
        "ty_s3": 'Házhozszállítás és <strong>fizetés átvételkor</strong>',
        "ty_b1": "🔒 Fizetés átvételkor",
        "ty_b2": "🛡️ 24 hónap garancia",
        "ty_b3": "🔐 SSL védelem",
        "ty_footer_addr": "Piazza San Marco 5 — 25063 Gardone Val Trompia",
    },
    "cz": {
        "meta_title": "WeldForce 800™ — Profesionální svářečka 8 v 1 bez lahve | -70% jen dnes",
        "meta_desc": "WeldForce 800™: profesionální svářečka 8 v 1 (laser, MIG bez plynu, TIG, elektroda). Funguje ze zásuvky 220V. Svařuje hliník, litinu, ocel, železo a inox. Platba na dobírku, doručení 24/48h.",
        "og_title": "WeldForce 800™ — Svářečka 8 v 1 | -70% jen dnes",
        "og_desc": "Profesionální svářečka 8 v 1 bez lahve. Zásuvka 220V, automatické řízení. Platba na dobírku.",
        "schema_name": "WeldForce 800™ — Profesionální svářečka 8 v 1",
        "schema_desc": "Profesionální svářečka 8 v 1: laser, MIG bez plynu, TIG, elektroda, bodové svařování a řezání. Funguje ze zásuvky 220V. Svařuje hliník, litinu, ocel, železo a inox.",
        "submitting": "Odesílání...",
        "cookie_text": "Používáme technické soubory cookie a soubory cookie třetích stran ke zlepšení vašeho zážitku a k analýze.",
        "cookie_accept": "Přijmout",
        "cookie_learn": "Zjistit více",
        "banner": "🔥 JEN DNES: -70% + PLATBA NA DOBÍRKU 🔥",
        "rating": '<strong>4,8/5</strong> — Více než <strong>8.700</strong> ověřených recenzí',
        "guarantee_line": "🛡️ Záruka 2 roky + Doručení do 24-48h",
        "hero_title": "Profesionální svářečka 8 v 1 ⚡ Automaticky svaří každý materiál",
        "hero_sub": 'Více než 8.700 lidí už vyměnilo své staré svářečky: jedno kompaktní zařízení pro laserové svařování, MIG bez plynu, TIG a elektrodu. <strong>Funguje z běžné zásuvky 220V</strong> a svařuje hliník, litinu, ocel, železo a inox — i pod vodou.',
        "hero_alt": "WeldForce 800™ — profesionální svářečka 8 v 1 bez lahve",
        "hero_img_title": "WeldForce 800™ Svářečka 8 v 1",
        "offer_label": "SPECIÁLNÍ NABÍDKA -70%",
        "cta": "ANO, CHCI WeldForce 800™ →",
        "no_advance": "🔒 Bez zálohy · Bez karty · Platíte až při doručení",
        "trust_ship_t": "Doručení do 24-48h",
        "trust_ship_s": "Rychlá doprava po celé ČR",
        "trust_pay_t": "Platba na dobírku",
        "trust_pay_s": "Platíte až když převzmete",
        "trust_gar_t": "Záruka 2 roky",
        "trust_gar_s": "Oficiální krytí v ceně",
        "trust_ret_t": "Vrácení 30 dní",
        "trust_ret_s": "Jednoduchá a bezplatná refundace",
        "countdown_aria": "Časově omezená nabídka",
        "countdown_label": "⏰ Nabídka -70% končí za",
        "ore": "Hod",
        "min": "Min",
        "sec": "Sek",
        "watching": 'Dostupnost: <strong>Poslední kusy skladem</strong> · <strong>38 lidí</strong> právě sleduje tuto svářečku',
        "form_title": "Dokončete objednávku",
        "form_sub": "Vyplňte formulář níže, náš tým vás kontaktuje pro potvrzení všech detailů.",
        "label_name": "Jméno a příjmení *",
        "ph_name": "Např. Jan Novák",
        "err_name": "Zadejte jméno a příjmení (alespoň 3 znaky)",
        "label_phone": "Telefonní číslo *",
        "ph_phone": "Např. 777 123 456",
        "err_phone": "Zadejte platné telefonní číslo",
        "label_addr": "Dodací adresa *",
        "ph_addr": "Ulice, číslo, město, PSČ",
        "err_addr": "Zadejte úplnou adresu (alespoň 10 znaků)",
        "confirm_btn": "POTVRDIT OBJEDNÁVKU",
        "f1_label": "01 — Jedno zařízení na každou práci",
        "f1_title": "8 funkcí v jednom kompaktním zařízení",
        "f1_c1": "Laserové svařování",
        "f1_c2": "MIG bez plynu",
        "f1_c3": "TIG a elektroda",
        "f1_p1": "S WeldForce 800™ přecházíte z jedné práce na druhou bez výměny stroje: <strong>laser, MIG bez plynu, TIG, elektroda, bodové svařování a řezání</strong> jsou už integrované. Navíc <strong>laserové čištění</strong> odstraní rez, barvu a oxidy z kovů v několika průchodech.",
        "f1_p2": "Méně vybavení ke koupi a uskladnění: vše potřebné máte v jednom kompaktním těle, připraveném v dílně nebo garáži.",
        "f1_alt": "Svářečka 8 v 1 s více funkcemi",
        "f2_label": "02 — Automatické řízení, bez průmyslové instalace",
        "f2_title": "Systém detekuje materiál a vše nastaví sám",
        "f2_c1": "Standardní zásuvka 220V",
        "f2_c2": "Automatické nastavení",
        "f2_c3": "Vhodné pro začátečníky",
        "f2_p1": "Elektronika WeldForce 800™ sama přizpůsobí proud, výkon a posuv drátu podle obrobku. Tak snížíte propálení a prázdné starty — i když svařujete jen o víkendech.",
        "f2_p2": "Bez linky 380V: zasunete zástrčku do <strong>domácí zásuvky 220V</strong> a hned začnete — od garáže po roh dílny.",
        "f2_alt": "Systém automatického řízení, zásuvka 220V",
        "f3_label": "03 — Svaří každý materiál, i pod vodou",
        "f3_title": "Hliník, litina, ocel, železo, inox — bez omezení",
        "f3_c1": "Náročné materiály",
        "f3_c2": "Použití i pod vodou",
        "f3_c3": "Ochrana proti přetížení",
        "f3_p1": "Zvládá náročné slitiny a situace — <strong>hliník, litinu, inox a železo</strong> — a zůstává stabilní i tam, kde se mnoho tradičních svářeček zastaví, <strong>včetně vlhkého prostředí / pod vodou</strong>.",
        "f3_p2": "Ochrana proti přehřátí a přetížení v základu; v krabici už najdete kleště, kabely a základní příslušenství, bez dokupování dílů.",
        "f3_alt": "Svařování hliníku, oceli a inoxu i pod vodou",
        "cmp_sub": "Přímé srovnání",
        "cmp_title": "Tradiční svářečka vs WeldForce 800™",
        "cmp_trad": "Tradiční",
        "cmp_r1a": "Typ svařování",
        "cmp_r1b": "Jen jeden typ",
        "cmp_r1c": "8 v 1: laser, MIG, TIG, elektroda, bodové",
        "cmp_r2a": "Řezání a čištění",
        "cmp_r2b": "Nezahrnuto",
        "cmp_r2c": "Laserové řezání a čištění v balení",
        "cmp_r3a": "Nastavení",
        "cmp_r3b": "Ruční a složité",
        "cmp_r3c": "Automatické a inteligentní",
        "cmp_r4a": "Snadnost použití",
        "cmp_r4b": "Těžké pro začátečníky",
        "cmp_r4c": "Snadné i bez zkušeností",
        "cmp_r5a": "Náročné materiály",
        "cmp_r5b": "Omezený výkon",
        "cmp_r5c": "Hliník, litina, inox bez problémů",
        "cmp_r6a": "Napájení",
        "cmp_r6b": "Často vyžaduje průmyslových 380V",
        "cmp_r6c": "Standardní zásuvka 220V",
        "rev_title": "Více než 8.700 spokojených zákazníků. Zjistěte, proč volí WeldForce 800™.",
        "rev1_t": "Výkonná a snadná i pro začátečníky.",
        "rev1_p": "«Čekal jsem něco složitého, ale po dvou pokusech jsem svařil kus z hliníku a jeden z inoxu. Dobrý výkon a jasné ovládání.»",
        "rev1_a": "Andrej P. — Praha, Ověřený zákazník",
        "rev1_alt": "WeldForce 800 použitá na hliníkovém kusu",
        "rev2_t": "Připravená k použití, bez průmyslové instalace.",
        "rev2_p": "«Zapojil jsem ji do zásuvky v garáži a za pět minut už jsem pracoval. Žádná divná instalace: ideální na domácí práce.»",
        "rev2_a": "Michal D. — Brno, Ověřený zákazník",
        "rev2_alt": "WeldForce 800 zapojená do standardní zásuvky v garáži",
        "rev3_t": "Laserové čištění je úžasné.",
        "rev3_p": "«Na zrezivělých kusech laserové čištění dělá rozdíl: za pár minut je povrch znovu zpracovatelný, bez hodin s kartáčem.»",
        "rev3_a": "Lukáš L. — Ostrava, Ověřený zákazník",
        "rev3_alt": "Laserové čištění zrezivělého kusu",
        "pkg_sub": "V balení",
        "pkg_title": "Kompletní sada WeldForce 800™, připravená k použití",
        "pkg_alt": "Kompletní sada WeldForce 800",
        "pkg_li1": "Svářečka 8 v 1 — laser, MIG bez plynu, TIG, elektroda, bodové svařování a řezání",
        "pkg_li2": "Kleště a kompletní kabely — žádné příslušenství dokupovat zvlášť",
        "pkg_li3": "Systém automatického řízení — detekuje materiál a sám nastaví výkon",
        "pkg_li4": "Funkce laserového čištění — odstraňuje rez a oxidaci",
        "pkg_li5": "Vhodné i pro práce pod vodou",
        "pkg_li6": "Integrovaná ochrana proti přetížení a přehřátí",
        "pkg_li7": "<strong>Oficiální záruka 2 roky</strong>",
        "faq_title": "Často kladené otázky",
        "faq1_q": "Kdy dorazí?",
        "faq1_a": "Doručení probíhá do 24–48 pracovních hodin. Kontaktujeme vás během několika hodin pro potvrzení objednávky a detailů doručení.",
        "faq2_q": "Mohu platit na dobírku?",
        "faq2_a": "Ano, platíte hotově přímo kurýrovi při převzetí balíku. Připravte si {price}.",
        "faq3_q": "Potřebuji průmyslový proud 380V?",
        "faq3_a": "Ne, funguje z běžné zásuvky 220V: zapojíte a hned začnete pracovat — doma, v garáži nebo v dílně.",
        "faq4_q": "Mohu ji používat, i když nemám zkušenosti se svařováním?",
        "faq4_a": "Ano, systém automatického řízení detekuje materiál a sám nastaví výkon, proud a rychlost drátu, takže se začátečníci vyhnou chybám.",
        "faq5_q": "Co když nebudu spokojen?",
        "faq5_a": "Máte 30 dní na bezplatné vrácení a plnou refundaci, bez otázek.",
        "footer_blurb": "Užitečné produkty pro každodenní život, doručení do 24–48 hodin s platbou na dobírku.",
        "footer_info": "Informace",
        "footer_about": "O nás",
        "footer_contact_link": "Kontaktujte nás",
        "footer_privacy": "Zásady ochrany osobních údajů",
        "footer_terms": "Obchodní podmínky",
        "footer_cookie": "Zásady cookies",
        "footer_ship": "Doprava",
        "footer_refund": "Vrácení zboží",
        "footer_contacts": "Kontakt",
        "footer_country": "Itálie",
        "footer_rights": "Všechna práva vyhrazena",
        "popups": [
            {"initial": "A", "name": "Andrej P.", "image": "/assets/img/reviews/arcforce/popup-1.png", "message": " právě objednal WeldForce 800™", "time": "před 2 minutami, Praha"},
            {"initial": "M", "name": "Michal D.", "image": "/assets/img/reviews/arcforce/popup-2.png", "message": " právě potvrdil objednávku", "time": "před 5 minutami, Brno"},
            {"initial": "L", "name": "Lukáš L.", "image": "/assets/img/reviews/arcforce/popup-3.png", "message": " právě koupil WeldForce 800™", "time": "před 8 minutami, Ostrava"},
            {"initial": "P", "name": "Petr R.", "image": "/assets/img/reviews/arcforce/popup-1.png", "message": " dokončil objednávku", "time": "před 12 minutami, Plzeň"},
            {"initial": "G", "name": "Martin B.", "image": "/assets/img/reviews/arcforce/popup-2.png", "message": " právě objednal (doručení zítra)", "time": "před 18 minutami, Liberec"},
            {"initial": "S", "name": "Tomáš M.", "image": "/assets/img/reviews/arcforce/popup-3.png", "message": " potvrdil svou objednávku", "time": "před 24 minutami, Olomouc"},
        ],
        "ty_title": "Objednávka přijata — Vyčkejte na potvrzovací hovor | WeldForce 800™",
        "ty_desc": "Vaše objednávka WeldForce 800™ byla zaregistrována. Zbývá jen poslední krok: odpovězte na potvrzovací hovor našeho operátora.",
        "ty_headline": "Vaše objednávka byla úspěšně zaregistrována!",
        "ty_subhead": "Skvělé — vaše objednávka WeldForce 800™ se zpracovává. Zbývá už jen <strong>poslední krok</strong> k jejímu dokončení a expedici.",
        "ty_alt": "Tým powercurvemedia při práci: call centrum a logistika dobírky",
        "ty_eyebrow": "👇 Co máte nyní udělat",
        "ty_action_title": "📞 Odpovězte na potvrzovací hovor",
        "ty_action_body": 'Náš operátor vás bude kontaktovat <strong>v nejbližších hodinách</strong> pro potvrzení objednávky.',
        "ty_warning": "Pokud na hovor neodpovíte, objednávka bude automaticky zrušena.",
        "ty_hours_h": "🕒 Hodiny kontaktu",
        "ty_hours": "<strong>Pondělí – Sobota</strong> · 9:00 – 18:00",
        "ty_next_h": "📋 Co bude dál",
        "ty_s1": 'Odpovězte na hovor a <strong>potvrďte své údaje</strong>',
        "ty_s2": 'Vaše objednávka bude odeslána do <strong>24–48 hodin</strong>',
        "ty_s3": 'Doručení domů a <strong>platba na dobírku</strong>',
        "ty_b1": "🔒 Platba na dobírku",
        "ty_b2": "🛡️ Záruka 24 měsíců",
        "ty_b3": "🔐 Ochrana SSL",
        "ty_footer_addr": "Piazza San Marco 5 — 25063 Gardone Val Trompia",
    },
    "sk": {
        "meta_title": "WeldForce 800™ — Profesionálna zváračka 8 v 1 bez fľaše | -70% len dnes",
        "meta_desc": "WeldForce 800™: profesionálna zváračka 8 v 1 (laser, MIG bez plynu, TIG, elektróda). Funguje zo zásuvky 220V. Zvára hliník, liatinu, oceľ, železo a inox. Platba na dobierku, doručenie 24/48h.",
        "og_title": "WeldForce 800™ — Zváračka 8 v 1 | -70% len dnes",
        "og_desc": "Profesionálna zváračka 8 v 1 bez fľaše. Zásuvka 220V, automatické riadenie. Platba na dobierku.",
        "schema_name": "WeldForce 800™ — Profesionálna zváračka 8 v 1",
        "schema_desc": "Profesionálna zváračka 8 v 1: laser, MIG bez plynu, TIG, elektróda, bodové zváranie a rezanie. Funguje zo zásuvky 220V. Zvára hliník, liatinu, oceľ, železo a inox.",
        "submitting": "Odosielanie...",
        "cookie_text": "Používame technické súbory cookie a súbory cookie tretích strán na zlepšenie vášho zážitku a na analýzu.",
        "cookie_accept": "Prijať",
        "cookie_learn": "Zistiť viac",
        "banner": "🔥 LEN DNES: -70% + PLATBA NA DOBIERKU 🔥",
        "rating": '<strong>4,8/5</strong> — Viac ako <strong>8.700</strong> overených recenzií',
        "guarantee_line": "🛡️ Záruka 2 roky + Doručenie do 24-48h",
        "hero_title": "Profesionálna zváračka 8 v 1 ⚡ Automaticky zvára každý materiál",
        "hero_sub": 'Viac ako 8.700 ľudí už vymenilo svoje staré zváračky: jedno kompaktné zariadenie na laserové zváranie, MIG bez plynu, TIG a elektródu. <strong>Funguje z bežnej zásuvky 220V</strong> a zvára hliník, liatinu, oceľ, železo a inox — aj pod vodou.',
        "hero_alt": "WeldForce 800™ — profesionálna zváračka 8 v 1 bez fľaše",
        "hero_img_title": "WeldForce 800™ Zváračka 8 v 1",
        "offer_label": "ŠPECIÁLNA PONUKA -70%",
        "cta": "ÁNO, CHCEM WeldForce 800™ →",
        "no_advance": "🔒 Bez zálohy · Bez karty · Platíte až pri doručení",
        "trust_ship_t": "Doručenie do 24-48h",
        "trust_ship_s": "Rýchla doprava po celom Slovensku",
        "trust_pay_t": "Platba na dobierku",
        "trust_pay_s": "Platíte až keď prevezmete",
        "trust_gar_t": "Záruka 2 roky",
        "trust_gar_s": "Oficiálne krytie v cene",
        "trust_ret_t": "Vrátenie 30 dní",
        "trust_ret_s": "Jednoduchá a bezplatná refundácia",
        "countdown_aria": "Časovo obmedzená ponuka",
        "countdown_label": "⏰ Ponuka -70% končí o",
        "ore": "Hod",
        "min": "Min",
        "sec": "Sek",
        "watching": 'Dostupnosť: <strong>Posledné kusy na sklade</strong> · <strong>38 ľudí</strong> práve sleduje túto zváračku',
        "form_title": "Dokončite objednávku",
        "form_sub": "Vyplňte formulár nižšie, náš tím vás kontaktuje na potvrdenie všetkých detailov.",
        "label_name": "Meno a priezvisko *",
        "ph_name": "Napr. Ján Novák",
        "err_name": "Zadajte meno a priezvisko (aspoň 3 znaky)",
        "label_phone": "Telefónne číslo *",
        "ph_phone": "Napr. 0901 123 456",
        "err_phone": "Zadajte platné telefónne číslo",
        "label_addr": "Dodacia adresa *",
        "ph_addr": "Ulica, číslo, mesto, PSČ",
        "err_addr": "Zadajte úplnú adresu (aspoň 10 znakov)",
        "confirm_btn": "POTVRDIŤ OBJEDNÁVKU",
        "f1_label": "01 — Jedno zariadenie na každú prácu",
        "f1_title": "8 funkcií v jednom kompaktnom zariadení",
        "f1_c1": "Laserové zváranie",
        "f1_c2": "MIG bez plynu",
        "f1_c3": "TIG a elektróda",
        "f1_p1": "S WeldForce 800™ prechádzate z jednej práce na druhú bez výmeny stroja: <strong>laser, MIG bez plynu, TIG, elektróda, bodové zváranie a rezanie</strong> sú už integrované. Navyše <strong>laserové čistenie</strong> odstráni hrdzu, farbu a oxidy z kovov v niekoľkých prechodoch.",
        "f1_p2": "Menej vybavenia na kúpu a uskladnenie: všetko potrebné máte v jednom kompaktnom tele, pripravenom v dielni alebo garáži.",
        "f1_alt": "Zváračka 8 v 1 s viacerými funkciami",
        "f2_label": "02 — Automatické riadenie, bez priemyselnej inštalácie",
        "f2_title": "Systém deteguje materiál a všetko nastaví sám",
        "f2_c1": "Štandardná zásuvka 220V",
        "f2_c2": "Automatické nastavenie",
        "f2_c3": "Vhodné pre začiatočníkov",
        "f2_p1": "Elektronika WeldForce 800™ sama prispôsobí prúd, výkon a posuv drôtu podľa obrobku. Tak znížite prepálenia a prázdne štarty — aj keď zvárate len cez víkendy.",
        "f2_p2": "Bez linky 380V: zasuniete zástrčku do <strong>domácej zásuvky 220V</strong> a hneď začnete — od garáže po roh dielne.",
        "f2_alt": "Systém automatického riadenia, zásuvka 220V",
        "f3_label": "03 — Zvára každý materiál, aj pod vodou",
        "f3_title": "Hliník, liatina, oceľ, železo, inox — bez obmedzení",
        "f3_c1": "Náročné materiály",
        "f3_c2": "Použitie aj pod vodou",
        "f3_c3": "Ochrana proti preťaženiu",
        "f3_p1": "Zvláda náročné zliatiny a situácie — <strong>hliník, liatinu, inox a železo</strong> — a zostáva stabilná aj tam, kde sa mnohé tradičné zváračky zastavia, <strong>vrátane vlhkého prostredia / pod vodou</strong>.",
        "f3_p2": "Ochrana proti prehriatiu a preťaženiu v základe; v krabici už nájdete kliešte, káble a základné príslušenstvo, bez dokupovania dielov.",
        "f3_alt": "Zváranie hliníka, ocele a inoxu aj pod vodou",
        "cmp_sub": "Priame porovnanie",
        "cmp_title": "Tradičná zváračka vs WeldForce 800™",
        "cmp_trad": "Tradičná",
        "cmp_r1a": "Typ zvárania",
        "cmp_r1b": "Len jeden typ",
        "cmp_r1c": "8 v 1: laser, MIG, TIG, elektróda, bodové",
        "cmp_r2a": "Rezanie a čistenie",
        "cmp_r2b": "Nezahrnuté",
        "cmp_r2c": "Laserové rezanie a čistenie v balení",
        "cmp_r3a": "Nastavenie",
        "cmp_r3b": "Ručné a zložité",
        "cmp_r3c": "Automatické a inteligentné",
        "cmp_r4a": "Jednoduchosť použitia",
        "cmp_r4b": "Ťažké pre začiatočníkov",
        "cmp_r4c": "Jednoduché aj bez skúseností",
        "cmp_r5a": "Náročné materiály",
        "cmp_r5b": "Obmedzený výkon",
        "cmp_r5c": "Hliník, liatina, inox bez problémov",
        "cmp_r6a": "Napájanie",
        "cmp_r6b": "Často vyžaduje priemyselných 380V",
        "cmp_r6c": "Štandardná zásuvka 220V",
        "rev_title": "Viac ako 8.700 spokojných zákazníkov. Zistite, prečo volia WeldForce 800™.",
        "rev1_t": "Výkonná a jednoduchá aj pre začiatočníkov.",
        "rev1_p": "«Čakal som niečo zložité, ale po dvoch pokusoch som zváril kus z hliníka a jeden z inoxu. Dobrý výkon a jasné ovládanie.»",
        "rev1_a": "Andrej P. — Bratislava, Overený zákazník",
        "rev1_alt": "WeldForce 800 použitá na hliníkovom kuse",
        "rev2_t": "Pripravená na použitie, bez priemyselnej inštalácie.",
        "rev2_p": "«Zapojil som ju do zásuvky v garáži a za päť minút som už pracoval. Žiadna divná inštalácia: ideálna na domáce práce.»",
        "rev2_a": "Michal D. — Košice, Overený zákazník",
        "rev2_alt": "WeldForce 800 zapojená do štandardnej zásuvky v garáži",
        "rev3_t": "Laserové čistenie je úžasné.",
        "rev3_p": "«Na zhrdzavených kusoch laserové čistenie robí rozdiel: za pár minút je povrch znova spracovateľný, bez hodín s kefou.»",
        "rev3_a": "Lukáš L. — Prešov, Overený zákazník",
        "rev3_alt": "Laserové čistenie zhrdzaveného kusu",
        "pkg_sub": "V balení",
        "pkg_title": "Kompletná sada WeldForce 800™, pripravená na použitie",
        "pkg_alt": "Kompletná sada WeldForce 800",
        "pkg_li1": "Zváračka 8 v 1 — laser, MIG bez plynu, TIG, elektróda, bodové zváranie a rezanie",
        "pkg_li2": "Kliešte a kompletné káble — žiadne príslušenstvo dokupovať zvlášť",
        "pkg_li3": "Systém automatického riadenia — deteguje materiál a sám nastaví výkon",
        "pkg_li4": "Funkcia laserového čistenia — odstraňuje hrdzu a oxidáciu",
        "pkg_li5": "Vhodné aj na práce pod vodou",
        "pkg_li6": "Integrovaná ochrana proti preťaženiu a prehriatiu",
        "pkg_li7": "<strong>Oficiálna záruka 2 roky</strong>",
        "faq_title": "Často kladené otázky",
        "faq1_q": "Kedy dorazí?",
        "faq1_a": "Doručenie prebieha do 24–48 pracovných hodín. Kontaktujeme vás počas niekoľkých hodín na potvrdenie objednávky a detailov doručenia.",
        "faq2_q": "Môžem platiť na dobierku?",
        "faq2_a": "Áno, platíte hotovosťou priamo kuriérovi pri prevzatí balíka. Pripravte si {price}.",
        "faq3_q": "Potrebujem priemyselný prúd 380V?",
        "faq3_a": "Nie, funguje z bežnej zásuvky 220V: zapojíte a hneď začnete pracovať — doma, v garáži alebo v dielni.",
        "faq4_q": "Môžem ju používať, aj keď nemám skúsenosti so zváraním?",
        "faq4_a": "Áno, systém automatického riadenia deteguje materiál a sám nastaví výkon, prúd a rýchlosť drôtu, takže sa začiatočníci vyhnú chybám.",
        "faq5_q": "Čo ak nebudem spokojný?",
        "faq5_a": "Máte 30 dní na bezplatné vrátenie a plnú refundáciu, bez otázok.",
        "footer_blurb": "Užitočné produkty pre každodenný život, doručenie do 24–48 hodín s platbou na dobierku.",
        "footer_info": "Informácie",
        "footer_about": "O nás",
        "footer_contact_link": "Kontaktujte nás",
        "footer_privacy": "Zásady ochrany osobných údajov",
        "footer_terms": "Obchodné podmienky",
        "footer_cookie": "Zásady cookies",
        "footer_ship": "Doprava",
        "footer_refund": "Vrátenie tovaru",
        "footer_contacts": "Kontakt",
        "footer_country": "Taliansko",
        "footer_rights": "Všetky práva vyhradené",
        "popups": [
            {"initial": "A", "name": "Andrej P.", "image": "/assets/img/reviews/arcforce/popup-1.png", "message": " práve objednal WeldForce 800™", "time": "pred 2 minútami, Bratislava"},
            {"initial": "M", "name": "Michal D.", "image": "/assets/img/reviews/arcforce/popup-2.png", "message": " práve potvrdil objednávku", "time": "pred 5 minútami, Košice"},
            {"initial": "L", "name": "Lukáš L.", "image": "/assets/img/reviews/arcforce/popup-3.png", "message": " práve kúpil WeldForce 800™", "time": "pred 8 minútami, Prešov"},
            {"initial": "P", "name": "Peter R.", "image": "/assets/img/reviews/arcforce/popup-1.png", "message": " dokončil objednávku", "time": "pred 12 minútami, Žilina"},
            {"initial": "G", "name": "Martin B.", "image": "/assets/img/reviews/arcforce/popup-2.png", "message": " práve objednal (doručenie zajtra)", "time": "pred 18 minútami, Nitra"},
            {"initial": "S", "name": "Tomáš M.", "image": "/assets/img/reviews/arcforce/popup-3.png", "message": " potvrdil svoju objednávku", "time": "pred 24 minútami, Banská Bystrica"},
        ],
        "ty_title": "Objednávka prijatá — Počkajte na potvrdzovací hovor | WeldForce 800™",
        "ty_desc": "Vaša objednávka WeldForce 800™ bola zaregistrovaná. Zostáva len posledný krok: odpovedzte na potvrdzovací hovor nášho operátora.",
        "ty_headline": "Vaša objednávka bola úspešne zaregistrovaná!",
        "ty_subhead": "Skvelé — vaša objednávka WeldForce 800™ sa spracováva. Zostáva už len <strong>posledný krok</strong> k jej dokončeniu a expedícii.",
        "ty_alt": "Tím powercurvemedia pri práci: call centrum a logistika dobierky",
        "ty_eyebrow": "👇 Čo máte teraz urobiť",
        "ty_action_title": "📞 Odpovedzte na potvrdzovací hovor",
        "ty_action_body": 'Náš operátor vás bude kontaktovať <strong>v najbližších hodinách</strong> pre potvrdenie objednávky.',
        "ty_warning": "Ak na hovor neodpoviete, objednávka bude automaticky zrušená.",
        "ty_hours_h": "🕒 Hodiny kontaktu",
        "ty_hours": "<strong>Pondelok – Sobota</strong> · 9:00 – 18:00",
        "ty_next_h": "📋 Čo bude ďalej",
        "ty_s1": 'Odpovedzte na hovor a <strong>potvrďte svoje údaje</strong>',
        "ty_s2": 'Vaša objednávka bude odoslaná do <strong>24–48 hodín</strong>',
        "ty_s3": 'Doručenie domov a <strong>platba na dobierku</strong>',
        "ty_b1": "🔒 Platba na dobierku",
        "ty_b2": "🛡️ Záruka 24 mesiacov",
        "ty_b3": "🔐 Ochrana SSL",
        "ty_footer_addr": "Piazza San Marco 5 — 25063 Gardone Val Trompia",
    },
}

def apply_landing(html: str, g: dict, tr: dict) -> str:
    geo = g["geo"]
    lang = g["lang"]
    price = g["price"]
    currency = g["currency"]
    price_disp = g["price_disp"]
    old_disp = g["old_disp"]
    ps = price_schema(price)
    pj = price_js(price)
    offer = f"WeldForce 800 {geo.upper()}"
    lp_id = f"{geo}-weldforce-800-v1"
    base = f"https://powercurvemedia.com/{geo}/weldforce-800/"

    html = html.replace('lang="it"', f'lang="{lang}"', 1)
    html = html.replace(
        "WeldForce 800™ — Saldatrice Professionale 8 in 1 Senza Bombola | -70% Solo Oggi",
        tr["meta_title"],
    )
    html = html.replace(
        'content="WeldForce 800™: saldatrice professionale 8 in 1 (laser, MIG senza gas, TIG, elettrodo). Funziona con presa 220V. Salda alluminio, ghisa, acciaio, ferro e inox. Pagamento alla consegna, spedizione 24/48h."',
        f'content="{tr["meta_desc"]}"',
    )
    html = html.replace("https://powercurvemedia.com/it/weldforce-800/", base)
    html = html.replace(
        'content="WeldForce 800™ — Saldatrice 8 in 1 | -70% Solo Oggi"',
        f'content="{tr["og_title"]}"',
    )
    html = html.replace(
        'content="Saldatrice professionale 8 in 1 senza bombola. Presa 220V, controllo automatico. Pagamento alla consegna."',
        f'content="{tr["og_desc"]}"',
    )
    html = html.replace(
        '"name": "WeldForce 800™ — Saldatrice Professionale 8 in 1"',
        f'"name": "{tr["schema_name"]}"',
    )
    html = html.replace(
        '"description": "Saldatrice professionale 8 in 1: laser, MIG senza gas, TIG, elettrodo, punti e taglio. Funziona con presa 220V. Salda alluminio, ghisa, acciaio, ferro e inox."',
        f'"description": "{tr["schema_desc"]}"',
    )
    html = html.replace('"price": "129.00"', f'"price": "{ps}"')
    html = html.replace('"priceCurrency": "EUR"', f'"priceCurrency": "{currency}"')

    # SITE_CONFIG block
    html = re.sub(
        r"window\.SITE_CONFIG = \{.*?\n\};",
        (
            "window.SITE_CONFIG = {\n"
            f"  GEO: '{geo}',\n"
            f"  PRODUCT_SLUG: 'weldforce-800',\n"
            f"  CURRENCY: '{currency}',\n"
            f"  PRICE: {pj},\n"
            f"  OFFER_NAME: '{offer}',\n"
            f"  LP_ID: '{lp_id}',\n"
            "  META_PIXEL_ID: '',\n"
            "  GOOGLE_TAG_ID: '',\n"
            "  GOOGLE_ADS_CONVERSION_ID: '',\n"
            "  GOOGLE_ADS_CONVERSION_LABEL: '',\n"
            "  TY_CONVERSION_LABEL: '',\n"
            "  NETWORK_PIXEL_URL: '',\n"
            "  FORM_ENDPOINT: 'https://TODO-network-endpoint.com/api/lead',\n"
            f"  SUBMITTING_LABEL: {json.dumps(tr['submitting'], ensure_ascii=False)},\n"
            f"  COOKIE_TEXT: {json.dumps(tr['cookie_text'], ensure_ascii=False)},\n"
            f"  COOKIE_ACCEPT: {json.dumps(tr['cookie_accept'], ensure_ascii=False)},\n"
            f"  COOKIE_LEARN: {json.dumps(tr['cookie_learn'], ensure_ascii=False)}\n"
            "};"
        ),
        html,
        count=1,
        flags=re.S,
    )

    popups_js = json.dumps(tr["popups"], ensure_ascii=False, indent=2)
    html = re.sub(
        r"window\.POPUP_PURCHASES = \[.*?\];",
        f"window.POPUP_PURCHASES = {popups_js};",
        html,
        count=1,
        flags=re.S,
    )

    # FAQ cash amount BEFORE display-price mass replace (Italian uses "129€")
    html = html.replace(
        "Sì, paghi in contanti direttamente al corriere quando ricevi il pacco. Tieni pronti 129€.",
        tr["faq2_a"].format(price=price_disp),
    )

    # Display prices (all occurrences)
    html = html.replace("430 €", old_disp)
    html = html.replace("129 €", price_disp)
    html = html.replace("129€", price_disp.replace(" ", ""))

    # Path prefixes
    html = html.replace('href="/it/', f'href="/{geo}/')
    html = html.replace("/it/weldforce-800/", f"/{geo}/weldforce-800/")

    # UI copy — order matters for overlapping strings
    pairs = [
        ("🔥 SOLO OGGI: -70% + PAGAMENTO ALLA CONSEGNA 🔥", tr["banner"]),
        ("<strong>4,8/5</strong> — Oltre <strong>8.700</strong> recensioni verificate", tr["rating"]),
        ("🛡️ Garanzia 2 anni + Consegna in 24-48h", tr["guarantee_line"]),
        ("Saldatrice Professionale 8 in 1 ⚡ Salda Automaticamente Ogni Materiale", tr["hero_title"]),
        (
            'Oltre 8.700 persone hanno già sostituito i loro vecchi saldatori: un solo dispositivo compatto per saldatura laser, MIG senza gas, TIG e ad elettrodo. <strong>Funziona con la normale presa da 220V</strong> e salda alluminio, ghisa, acciaio, ferro e inox — anche sott\'acqua.',
            tr["hero_sub"],
        ),
        ("WeldForce 800™ — saldatrice professionale 8 in 1 senza bombola", tr["hero_alt"]),
        ("WeldForce 800™ Saldatrice 8 in 1", tr["hero_img_title"]),
        ("OFFERTA SPECIALE -70%", tr["offer_label"]),
        ("SÌ, VOGLIO WeldForce 800™ →", tr["cta"]),
        ("🔒 Nessun anticipo · Nessuna carta · Paghi solo alla consegna", tr["no_advance"]),
        ("Consegna in 24-48h", tr["trust_ship_t"]),
        ("Spedizione rapida in tutta Italia", tr["trust_ship_s"]),
        ("Pagamento alla consegna", tr["trust_pay_t"]),
        ("Paghi solo quando ricevi", tr["trust_pay_s"]),
        ("Garanzia 2 anni", tr["trust_gar_t"]),
        ("Copertura ufficiale inclusa", tr["trust_gar_s"]),
        ("Reso 30 giorni", tr["trust_ret_t"]),
        ("Rimborso semplice e gratuito", tr["trust_ret_s"]),
        ('aria-label="Offerta a tempo"', f'aria-label="{tr["countdown_aria"]}"'),
        ("⏰ Offerta -70% scade tra", tr["countdown_label"]),
        ("<small>Ore</small>", f"<small>{tr['ore']}</small>"),
        ("<small>Min</small>", f"<small>{tr['min']}</small>"),
        ("<small>Sec</small>", f"<small>{tr['sec']}</small>"),
        (
            "Disponibilità: <strong>Ultimi pezzi disponibili</strong> · <strong>38 persone</strong> stanno guardando questa saldatrice ora",
            tr["watching"],
        ),
        ("Completa il tuo ordine", tr["form_title"]),
        (
            "Compila il modulo qui sotto, il nostro team ti contatterà per confermare tutti i dettagli.",
            tr["form_sub"],
        ),
        ("Nome e cognome *", tr["label_name"]),
        ("Es. Mario Rossi", tr["ph_name"]),
        ("Inserisci nome e cognome (almeno 3 caratteri)", tr["err_name"]),
        ("Numero di telefono *", tr["label_phone"]),
        ("Es. 333 1234567", tr["ph_phone"]),
        ("Inserisci un numero di telefono valido", tr["err_phone"]),
        ("Indirizzo di consegna *", tr["label_addr"]),
        ("Via, civico, città, CAP", tr["ph_addr"]),
        ("Inserisci un indirizzo completo (almeno 10 caratteri)", tr["err_addr"]),
        ("CONFERMA L'ORDINE", tr["confirm_btn"]),
        ("01 — Un solo dispositivo per ogni lavoro", tr["f1_label"]),
        ("8 funzioni in un unico dispositivo compatto", tr["f1_title"]),
        ("Saldatura laser", tr["f1_c1"]),
        ("MIG senza gas", tr["f1_c2"]),
        ("TIG ed elettrodo", tr["f1_c3"]),
        (
            "Con WeldForce 800™ passi da un lavoro all'altro senza cambiare macchina: <strong>laser, MIG no-gas, TIG, elettrodo, punti e taglio</strong> sono già integrati. In più, la <strong>pulizia laser</strong> toglie ruggine, vernice e ossidi dai metalli in pochi passaggi.",
            tr["f1_p1"],
        ),
        (
            "Meno attrezzature da comprare e da riporre: tieni tutto ciò che ti serve in un solo corpo compatto, pronto in officina o in garage.",
            tr["f1_p2"],
        ),
        ("Saldatrice 8 in 1 con funzioni multiple", tr["f1_alt"]),
        ("02 — Controllo automatico, nessuna installazione industriale", tr["f2_label"]),
        ("Il sistema rileva il materiale e regola tutto da solo", tr["f2_title"]),
        ("Presa standard 220V", tr["f2_c1"]),
        ("Regolazione automatica", tr["f2_c2"]),
        ("Adatto ai principianti", tr["f2_c3"]),
        (
            "L'elettronica di WeldForce 800™ adatta da sola corrente, potenza e avanzamento del filo in base al pezzo. Così riduci bruciature e ripartenze a vuoto, anche se saldi solo nei weekend.",
            tr["f2_p1"],
        ),
        (
            "Niente linea a 380V: inserisci la spina nella <strong>presa di casa a 220V</strong> e parti subito, dal box auto all'angolo dell'officina.",
            tr["f2_p2"],
        ),
        ("Sistema di controllo automatico presa 220V", tr["f2_alt"]),
        ("03 — Salda ogni materiale, anche sott'acqua", tr["f3_label"]),
        ("Alluminio, ghisa, acciaio, ferro, inox — senza limiti", tr["f3_title"]),
        ("Materiali difficili", tr["f3_c1"]),
        ("Uso anche sott'acqua", tr["f3_c2"]),
        ("Protezione da sovraccarico", tr["f3_c3"]),
        (
            "Gestisce leghe ostiche e situazioni difficili — <strong>alluminio, ghisa, inox e ferro</strong> — e resta stabile anche dove molti saldatori tradizionali si fermano, <strong>compreso l'uso in ambienti umidi / sott'acqua</strong>.",
            tr["f3_p1"],
        ),
        (
            "Protezioni anti-surriscaldamento e anti-sovraccarico di serie; in scatola trovi già pinze, cavi e accessori essenziali, senza dover comprare pezzi a parte.",
            tr["f3_p2"],
        ),
        ("Saldatura su alluminio acciaio e inox anche sott'acqua", tr["f3_alt"]),
        ("Confronto diretto", tr["cmp_sub"]),
        ("Saldatore tradizionale vs WeldForce 800™", tr["cmp_title"]),
        (">Tradizionale<", f">{tr['cmp_trad']}<"),
        ("Tipo di saldatura", tr["cmp_r1a"]),
        ("Solo un tipo", tr["cmp_r1b"]),
        ("8 in 1: laser, MIG, TIG, elettrodo, punti", tr["cmp_r1c"]),
        ("Taglio e pulizia", tr["cmp_r2a"]),
        ("Non incluso", tr["cmp_r2b"]),
        ("Taglio e pulizia laser inclusi", tr["cmp_r2c"]),
        ("Regolazione", tr["cmp_r3a"]),
        ("Manuale e complessa", tr["cmp_r3b"]),
        ("Automatica e intelligente", tr["cmp_r3c"]),
        ("Facilità d'uso", tr["cmp_r4a"]),
        ("Difficile per principianti", tr["cmp_r4b"]),
        ("Facile anche senza esperienza", tr["cmp_r4c"]),
        ("Materiali difficili", tr["cmp_r5a"]),
        ("Prestazioni limitate", tr["cmp_r5b"]),
        ("Alluminio, ghisa, inox senza problemi", tr["cmp_r5c"]),
        ("Alimentazione", tr["cmp_r6a"]),
        ("Spesso richiede 380V industriale", tr["cmp_r6b"]),
        ("Presa standard 220V", tr["cmp_r6c"]),
        (
            "Oltre 8.700 clienti soddisfatti. Scopri perché scelgono WeldForce 800™.",
            tr["rev_title"],
        ),
        ("Potente e facile anche per chi inizia.", tr["rev1_t"]),
        (
            "«Mi aspettavo qualcosa di complicato, invece dopo due prove ho chiuso un pezzo in alluminio e uno in inox. Potenza buona e comandi chiari.»",
            tr["rev1_p"],
        ),
        ("Andrea P. — Milano, Cliente verificato", tr["rev1_a"]),
        ("WeldForce 800 usata su un pezzo in alluminio", tr["rev1_alt"]),
        ("Pronto all'uso, nessuna installazione industriale.", tr["rev2_t"]),
        (
            "«L'ho collegata alla presa del garage e in cinque minuti stavo già lavorando. Nessuna installazione strana: perfetta per i lavoretti di casa.»",
            tr["rev2_p"],
        ),
        ("Michele D. — Torino, Cliente verificato", tr["rev2_a"]),
        ("WeldForce 800 collegata a una presa standard in garage", tr["rev2_alt"]),
        ("La pulizia laser è incredibile.", tr["rev3_t"]),
        (
            "«Sui pezzi arrugginiti la pulizia laser fa la differenza: in pochi minuti la superficie torna lavorabile, senza stare ore con la spazzola.»",
            tr["rev3_p"],
        ),
        ("Fabio L. — Napoli, Cliente verificato", tr["rev3_a"]),
        ("Pulizia laser su un pezzo arrugginito", tr["rev3_alt"]),
        ("Nella confezione", tr["pkg_sub"]),
        ("Kit completo WeldForce 800™, pronto all'uso", tr["pkg_title"]),
        ('alt="Kit completo WeldForce 800"', f'alt="{tr["pkg_alt"]}"'),
        (
            "Saldatrice 8 in 1 — laser, MIG senza gas, TIG, elettrodo, punti e taglio",
            tr["pkg_li1"],
        ),
        (
            "Pinze e cavi completi — nessun accessorio da comprare a parte",
            tr["pkg_li2"],
        ),
        (
            "Sistema di controllo automatico — rileva il materiale e regola la potenza da solo",
            tr["pkg_li3"],
        ),
        (
            "Funzione di pulizia laser — rimuove ruggine e ossidazione",
            tr["pkg_li4"],
        ),
        ("Adatta anche a lavorazioni sott'acqua", tr["pkg_li5"]),
        (
            "Protezione integrata da sovraccarico e surriscaldamento",
            tr["pkg_li6"],
        ),
        ("<strong>Garanzia ufficiale di 2 anni</strong>", tr["pkg_li7"]),
        ("Domande frequenti", tr["faq_title"]),
        ("Quando arriva?", tr["faq1_q"]),
        (
            "La consegna avviene entro 24-48 ore lavorative. Ti contattiamo entro poche ore per confermare l'ordine e i dettagli di consegna.",
            tr["faq1_a"],
        ),
        ("Posso pagare alla consegna?", tr["faq2_q"]),
        ("Serve la corrente industriale a 380V?", tr["faq3_q"]),
        (
            "No, funziona con la normale presa da 220V: la colleghi e inizi subito a lavorare, a casa, in garage o in officina.",
            tr["faq3_a"],
        ),
        (
            "Posso usarla anche se non ho esperienza di saldatura?",
            tr["faq4_q"],
        ),
        (
            "Sì, il sistema di controllo automatico rileva il materiale e regola da solo potenza, corrente e velocità del filo, evitando errori anche ai principianti.",
            tr["faq4_a"],
        ),
        ("E se non sono soddisfatto?", tr["faq5_q"]),
        (
            "Hai 30 giorni di tempo per restituirla gratuitamente e ricevere il rimborso completo, senza domande.",
            tr["faq5_a"],
        ),
        (
            "Prodotti utili per la vita quotidiana, consegna in 24-48 ore con pagamento alla consegna.",
            tr["footer_blurb"],
        ),
        (">Informazioni<", f">{tr['footer_info']}<"),
        (">Chi siamo<", f">{tr['footer_about']}<"),
        (">Contattaci<", f">{tr['footer_contact_link']}<"),
        (">Privacy Policy<", f">{tr['footer_privacy']}<"),
        (">Termini e Condizioni<", f">{tr['footer_terms']}<"),
        (">Cookie Policy<", f">{tr['footer_cookie']}<"),
        (">Politica di Spedizione<", f">{tr['footer_ship']}<"),
        (">Politica di Rimborso<", f">{tr['footer_refund']}<"),
        (">Contatti<", f">{tr['footer_contacts']}<"),
        ("25063 Gardone Val Trompia, Italia", f"25063 Gardone Val Trompia, {tr['footer_country']}"),
        ("Tutti i diritti riservati", tr["footer_rights"]),
    ]

    for old, new in sorted(pairs, key=lambda x: len(x[0]), reverse=True):
        html = html.replace(old, new)

    return html


def apply_thankyou(html: str, g: dict, tr: dict) -> str:
    geo = g["geo"]
    lang = g["lang"]
    price = g["price"]
    currency = g["currency"]
    cpa = g["cpa"]
    pj = price_js(price)
    cpa_js = f"{cpa:.1f}" if isinstance(cpa, float) else f"{cpa}.0" if isinstance(cpa, int) else str(cpa)
    if isinstance(cpa, int):
        cpa_js = f"{cpa}.0"

    html = html.replace('lang="it"', f'lang="{lang}"', 1)
    html = html.replace(
        "Ordine ricevuto — Attendi la chiamata di conferma | WeldForce 800™",
        tr["ty_title"],
    )
    html = html.replace(
        'content="Il tuo ordine WeldForce 800™ è stato registrato. Manca solo un ultimo passaggio: rispondi alla chiamata di conferma del nostro operatore."',
        f'content="{tr["ty_desc"]}"',
    )

    # Main conversion snippet (top) — CPA in EUR
    html = html.replace("'value': 129.00,", f"'value': {cpa_js},")
    # keep currency EUR for gtag conversion
    # trackPurchase local
    html = html.replace(
        "if (window.trackPurchase) window.trackPurchase(129.00, 'EUR');",
        f"if (window.trackPurchase) window.trackPurchase({pj}, '{currency}');",
    )

    html = re.sub(
        r"window\.SITE_CONFIG = \{.*?\n\};",
        (
            "window.SITE_CONFIG = {\n"
            f"  GEO: '{geo}',\n"
            f"  PRODUCT_SLUG: 'weldforce-800',\n"
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

    # Second conversion value → CPA
    html = html.replace("'value': 1.0,", f"'value': {cpa_js},")

    html = html.replace('href="/it/', f'href="/{geo}/')

    pairs = [
        ("Il tuo ordine è stato registrato con successo!", tr["ty_headline"]),
        (
            "Perfetto — il tuo ordine è in elaborazione. Manca solo <strong>un ultimo passaggio</strong> per completarlo e far partire la spedizione.",
            tr["ty_subhead"],
        ),
        (
            "Il team powercurvemedia al lavoro: call center e logistica COD",
            tr["ty_alt"],
        ),
        ("👇 Cosa devi fare adesso", tr["ty_eyebrow"]),
        ("📞 Rispondi alla chiamata di conferma", tr["ty_action_title"]),
        (
            "Un nostro operatore ti contatterà <strong>nelle prossime ore</strong> per confermare il tuo ordine.",
            tr["ty_action_body"],
        ),
        (
            "Se non rispondi alla chiamata, l'ordine verrà automaticamente annullato.",
            tr["ty_warning"],
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
            "Consegna a domicilio e <strong>pagamento alla consegna</strong>",
            tr["ty_s3"],
        ),
        ("🔒 Pagamento alla consegna", tr["ty_b1"]),
        ("🛡️ Garanzia 24 mesi", tr["ty_b2"]),
        ("🔐 Protezione SSL", tr["ty_b3"]),
        (">Informazioni<", f">{tr['footer_info']}<"),
        (">Chi siamo<", f">{tr['footer_about']}<"),
        (">Contattaci<", f">{tr['footer_contact_link']}<"),
        (">Privacy Policy<", f">{tr['footer_privacy']}<"),
        (">Termini e Condizioni<", f">{tr['footer_terms']}<"),
        (">Cookie Policy<", f">{tr['footer_cookie']}<"),
        (">Politica di Spedizione<", f">{tr['footer_ship']}<"),
        (">Politica di Rimborso<", f">{tr['footer_refund']}<"),
        (">Contatti<", f">{tr['footer_contacts']}<"),
        (
            "Piazza San Marco 5 — 25063 Gardone Val Trompia",
            tr["ty_footer_addr"],
        ),
        ("Tutti i diritti riservati", tr["footer_rights"]),
    ]
    for old, new in sorted(pairs, key=lambda x: len(x[0]), reverse=True):
        html = html.replace(old, new)

    return html


def write_json(geo: str, g: dict, tr: dict) -> list[Path]:
    out_dir = ROOT / "content" / geo / "products" / PRODUCT_SLUG
    out_dir.mkdir(parents=True, exist_ok=True)
    landing = {
        "product": {
            "name": "WeldForce 800™",
            "full_name": tr["schema_name"],
            "slug": PRODUCT_SLUG,
            "price": price_schema(g["price"]),
            "price_old": g["old_disp"],
            "discount": "-70%",
            "currency": g["currency"],
        },
        "hero": {
            "badge": tr["banner"],
            "title": tr["hero_title"],
            "subtitle": re.sub(r"<[^>]+>", "", tr["hero_sub"]),
        },
        "cta": tr["cta"],
        "form_title": tr["form_title"],
        "cpa": g["cpa"],
    }
    thankyou = {
        "title": tr["ty_title"],
        "headline": tr["ty_headline"],
        "price": g["price"],
        "currency": g["currency"],
        "cpa": g["cpa"],
        "cpa_currency": "EUR",
    }
    paths = []
    for name, data in (("landing.json", landing), ("thank-you.json", thankyou)):
        p = out_dir / name
        p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        paths.append(p)
    return paths


def update_sitemap(geos: list[dict]) -> list[str]:
    xml = SITEMAP.read_text(encoding="utf-8")
    added = []
    insert_at = xml.find("</urlset>")
    if insert_at < 0:
        raise RuntimeError("sitemap.xml missing </urlset>")
    chunk = ""
    for g in geos:
        loc = f"https://powercurvemedia.com/{g['geo']}/weldforce-800/"
        if loc in xml:
            continue
        entry = (
            f"  <url><loc>{loc}</loc>"
            f"<lastmod>{LASTMOD}</lastmod>"
            f"<changefreq>weekly</changefreq>"
            f"<priority>0.95</priority></url>\n"
        )
        chunk += entry
        added.append(loc)
    if chunk:
        xml = xml[:insert_at] + chunk + xml[insert_at:]
        SITEMAP.write_text(xml, encoding="utf-8")
    return added


def main() -> None:
    # Merge translation dicts
    translations = dict(T)
    translations.update(T_EXTRA)

    index_tpl = (IT_DIR / "index.html").read_text(encoding="utf-8")
    ty_tpl = (IT_DIR / "thank-you.html").read_text(encoding="utf-8")

    created: list[Path] = []
    for g in GEOS:
        geo = g["geo"]
        tr = translations[geo]
        out_dir = ROOT / geo / PRODUCT_SLUG
        out_dir.mkdir(parents=True, exist_ok=True)

        index_html = apply_landing(index_tpl, g, tr)
        ty_html = apply_thankyou(ty_tpl, g, tr)

        index_path = out_dir / "index.html"
        ty_path = out_dir / "thank-you.html"
        index_path.write_text(index_html, encoding="utf-8")
        ty_path.write_text(ty_html, encoding="utf-8")
        created.extend([index_path, ty_path])
        created.extend(write_json(geo, g, tr))

    sitemap_added = update_sitemap(GEOS)

    print("=== Files created ===")
    for p in created:
        print(f"  {p.relative_to(ROOT)}")

    print("\n=== Verification (price_disp + GEO) ===")
    for g in GEOS:
        geo = g["geo"]
        index_path = ROOT / geo / PRODUCT_SLUG / "index.html"
        text = index_path.read_text(encoding="utf-8")
        ok_price = g["price_disp"] in text
        ok_geo = f"GEO: '{geo}'" in text
        ok_old = g["old_disp"] in text
        status = "OK" if (ok_price and ok_geo and ok_old) else "FAIL"
        print(
            f"  [{status}] {geo}: price_disp={ok_price} old_disp={ok_old} GEO={ok_geo} "
            f"→ {g['price_disp']}"
        )

    print("\n=== Sitemap ===")
    if sitemap_added:
        for u in sitemap_added:
            print(f"  + {u}")
    else:
        print("  (all entries already present)")

    print("\n=== Landing URLs ===")
    for g in GEOS:
        print(f"  https://powercurvemedia.com/{g['geo']}/weldforce-800/")
        print(f"  https://powercurvemedia.com/{g['geo']}/weldforce-800/thank-you.html")


if __name__ == "__main__":
    main()

