#!/usr/bin/env python3
"""Generate OneStart landing + thank-you pages for PL, SK, HU, SI, RO, CZ."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from onestart_geo_translations import T

ROOT = Path(__file__).resolve().parents[1]
IT_LANDING = ROOT / "it" / "onestart" / "landing.html"
WEBHOOK = "https://hook.eu2.make.com/ut8j6klzjnsa9tspsaszuppyttaqyaxm"
UID = "019f60bd-7f67-709f-a69c-8041b92c05ba"
FORM_ACTION = "https://offers.unbreakable-offers.com/forms/html/"
UNBREAKABLE_JS = "https://offers.unbreakable-offers.com/forms/html/js-v2/"
TMFP_SCRIPT = "https://offers.unbreakable-offers.com/forms/tmfp/"
CONVERSION_SEND_TO = "AW-18294109732/3Pa8COOx7dUcEOv3tatE"

GEOS = [
    {
        "geo": "pl", "lang": "pl", "offer": "172",
        "key": "d364a21b82734088cce05e459b8940c5531bd5dc",
        "price": 299, "currency": "PLN",
        "was": "999 zł", "now": "299 zł", "save": "700 zł", "cpa": 19,
    },
    {
        "geo": "sk", "lang": "sk", "offer": "173",
        "key": "58bfd9cea9584836e1db2573208dd8c694e0c64f",
        "price": 69.99, "currency": "EUR",
        "was": "249,99 €", "now": "69,99 €", "save": "180 €", "cpa": 19,
    },
    {
        "geo": "hu", "lang": "hu", "offer": "174",
        "key": "1bb118a445cb0838b13410e1303777e7cafc7fe5",
        "price": 25999, "currency": "HUF",
        "was": "84.999 Ft", "now": "25.999 Ft", "save": "59.000 Ft", "cpa": 19,
    },
    {
        "geo": "si", "lang": "sl", "offer": "175",
        "key": "bea38e323f18979798be2320cd957841f4482b24",
        "price": 69.99, "currency": "EUR",
        "was": "249,99 €", "now": "69,99 €", "save": "180 €", "cpa": 19,
    },
    {
        "geo": "ro", "lang": "ro", "offer": "176",
        "key": "c5932c58845eac72c770707c2bc3591918cd0016",
        "price": 379, "currency": "RON",
        "was": "1.259 RON", "now": "379 RON", "save": "880 RON", "cpa": 18,
    },
    {
        "geo": "cz", "lang": "cs", "offer": "177",
        "key": "784c01a643ef14d368fccbc3da133bdab7cbd7d1",
        "price": 1749, "currency": "CZK",
        "was": "5.999 Kč", "now": "1.749 Kč", "save": "4.250 Kč", "cpa": 19,
    },
]


def price_js(price: float | int) -> str:
    if isinstance(price, float) and not price.is_integer():
        return f"{price:.2f}"
    if float(price) == int(price):
        return str(int(price))
    return f"{float(price):.2f}"


def geo_upper(geo: str) -> str:
    return geo.upper()


def fmt(tr: dict, key: str, **kwargs: str) -> str:
    val = tr[key]
    if isinstance(val, str):
        for k, v in kwargs.items():
            val = val.replace("{" + k + "}", v)
    return val


def build_tags_html(tags: list[str]) -> str:
    return "".join(f'<span class="tag">{t}</span>' for t in tags)


def build_cmp_table(tr: dict) -> str:
    rows = [
        f'    <tr><th></th><th>{tr["cmp_th1"]}</th>'
        f'<th class="highlight">{tr["cmp_th2"]}</th></tr>'
    ]
    for label, bad, good in tr["cmp_rows"]:
        rows.append(
            f'    <tr><td>{label}</td><td>{bad}</td><td class="win">{good}</td></tr>'
        )
    return (
        f'<section class="compare wrap">\n'
        f'  <div class="section-label">{tr["cmp_label"]}</div>\n'
        f'  <h2>{tr["cmp_h2"]}</h2>\n'
        f'  <table>\n'
        + "\n".join(rows)
        + "\n  </table>\n"
        f"</section>"
    )


def build_faq_html(tr: dict, now: str) -> str:
    items = []
    for q, a in tr["faqs"]:
        answer = a.replace("{now}", now) if isinstance(a, str) else a
        items.append(
            f'  <div class="faq-item"><button class="faq-q" type="button">'
            f"<span>{q}</span><span class=\"arrow\">▾</span></button>\n"
            f'    <div class="faq-a"><p>{answer}</p></div></div>'
        )
    return (
        f'<section class="faq wrap">\n'
        f'  <div class="section-heading">\n'
        f'    <h2>{tr["faq_h2"]}</h2>\n'
        f"  </div>\n"
        + "\n".join(items)
        + "\n</section>"
    )


def build_kit_html(tr: dict, was: str, now: str) -> str:
    items = "\n".join(f"        <li>{item}</li>" for item in tr["kit_items"])
    return (
        f'<section class="kit-section wrap">\n'
        f'  <div class="section-heading">\n'
        f'    <span class="eyebrow">{tr["kit_eyebrow"]}</span>\n'
        f'    <h2>{tr["kit_h2"]}</h2>\n'
        f"  </div>\n"
        f'  <div class="kit-box">\n'
        f'    <img decoding="async" src="/assets/img/products/onestart/kit.png" '
        f'alt="{tr["kit_alt"]}" loading="lazy" onerror="this.src=\'/assets/img/placeholder.svg\'">\n'
        f'    <div class="kit-content">\n'
        f'      <div class="price-block" style="margin-bottom:16px;">\n'
        f'        <span class="was">{was}</span>\n'
        f'        <span class="now">{now}</span>\n'
        f'        <span class="pct">-70%</span>\n'
        f"      </div>\n"
        f"      <ul>\n{items}\n      </ul>\n"
        f'      <a href="#order-form" class="cta-btn">{tr["cta_hero"]}</a>\n'
        f"    </div>\n"
        f"  </div>\n"
        f"</section>"
    )


def build_form_html(g: dict, tr: dict) -> str:
    geo = g["geo"]
    offer = g["offer"]
    thankyou = f"https://powercurvemedia.com/{geo}/onestart/{offer}/thank-you.html"
    lbl_postal = tr.get("lbl_postal", "Postal code:")
    ph_postal = tr.get("ph_postal", lbl_postal)
    return (
        f'<form class="tm-order-form" action="{FORM_ACTION}" method="post">\n'
        f'        <label for="name">{tr["lbl_name"]}</label>\n'
        f'        <input id="name" type="text" name="name" autocomplete="name" '
        f'placeholder="{tr["ph_name"]}" required>\n'
        f'        <label for="tel">{tr["lbl_tel"]}</label>\n'
        f'        <input id="tel" type="tel" name="tel" autocomplete="tel" '
        f'placeholder="{tr["ph_tel"]}" required>\n'
        f'        <label for="street-address">{tr["lbl_addr"]}</label>\n'
        f'        <input id="street-address" type="text" name="street-address" '
        f'autocomplete="street-address" placeholder="{tr["ph_addr"]}" required>\n'
        f'        <label for="postal-code">{lbl_postal}</label>\n'
        f'        <input id="postal-code" type="text" name="postal-code" '
        f'autocomplete="postal-code" placeholder="{ph_postal}">\n'
        f'        <input name="uid" type="hidden" value="{UID}" />\n'
        f'        <input name="offer" type="hidden" value="{offer}" />\n'
        f'        <input name="lp" type="hidden" value="{offer}" />\n'
        f'        <input name="thankyoupage" type="hidden" value="{thankyou}"/>\n'
        f'        <input name="webhook" type="hidden" value="{WEBHOOK}"/>\n'
        f'        <input name="_key" type="hidden" value="{g["key"]}" />\n'
        f'        <div style="margin-top: 10px; text-align: center">\n'
        f'          <button name="submit" type="submit" class="cta-btn">{tr["cta_form"]}</button>\n'
        f'        </div>\n'
        f'        <p class="form-note">{tr["form_note"]}</p>\n'
        f'        <script src="{UNBREAKABLE_JS}" async></script>\n'
        f"      </form>"
    )


def build_site_config(g: dict, tr: dict) -> str:
    geo = g["geo"]
    offer = g["offer"]
    return (
        "window.SITE_CONFIG = {\n"
        f"  GEO: '{geo}',\n"
        f"  PRODUCT_SLUG: 'onestart',\n"
        f"  CURRENCY: '{g['currency']}',\n"
        f"  PRICE: {price_js(g['price'])},\n"
        f"  OFFER_NAME: 'OneStart 4250A {geo_upper(geo)}',\n"
        f"  LP_ID: '{geo}-onestart-{offer}',\n"
        f"  FORM_ENDPOINT: '{FORM_ACTION}',\n"
        f"  SUBMITTING_LABEL: {json.dumps(tr['submitting'], ensure_ascii=False)}\n"
        "};"
    )


def apply_landing(html: str, g: dict, tr: dict) -> str:
    geo = g["geo"]
    lang = g["lang"]
    offer = g["offer"]
    was = g["was"]
    now = g["now"]
    save = g["save"]
    live_tpl = tr["live_template"].replace('"', "&quot;")

    html = html.replace('lang="it"', f'lang="{lang}"', 1)
    html = html.replace(
        'href="https://powercurvemedia.com/it/onestart/landing.html"',
        f'href="https://powercurvemedia.com/{geo}/onestart/{offer}/"',
    )
    html = html.replace('href="/it/', f'href="/{geo}/')

    html = re.sub(
        r"window\.SITE_CONFIG = \{.*?\n\};",
        build_site_config(g, tr),
        html,
        count=1,
        flags=re.S,
    )
    html = html.replace('<script src="/assets/js/form-handler.js" defer></script>\n', "")

    form_old = re.search(
        r'<form class="cod-form order-form" novalidate>.*?</form>',
        html,
        re.S,
    )
    if form_old:
        html = html.replace(form_old.group(0), build_form_html(g, tr), 1)

    pairs: list[tuple[str, str]] = [
        (
            "OneStart™ 4250A — Avviatore di emergenza | -70% Solo oggi",
            tr["title"],
        ),
        (
            'content="OneStart™ 4250A: avviatore portatile da 4250A per auto, moto, camper e furgoni. Cavi retrattili da 6 metri, power bank integrato e protezione antiscintilla. Spedizione gratuita e pagamento alla consegna."',
            f'content="{tr["meta_desc"]}"',
        ),
        (
            "🚚 SPEDIZIONE GRATUITA — PAGAMENTO ALLA CONSEGNA 🚚",
            tr["topbar"],
        ),
        (
            "<strong>4,9/5</strong> — Oltre <strong>12.000 automobilisti soddisfatti</strong>",
            tr["rating"],
        ),
        (
            "⚡ Avviatore di emergenza 4250A — Kit completo incluso",
            tr["gift"],
        ),
        (
            "<h1>Non restare bloccato con la batteria scarica. <span class=\"hl\">Avvia il tuo veicolo in pochi secondi</span></h1>",
            f"<h1>{tr['h1']}</h1>",
        ),
        (
            "Con <strong>OneStart™ 4250A</strong> riavvii auto, moto, camper, furgoni e trattori <strong>senza chiedere aiuto</strong>, senza aspettare il carro attrezzi e senza perdere ore per una batteria morta.",
            tr["lead"],
        ),
        (
            "❤️ Risparmi 137 € — Offerta limitata",
            fmt(tr, "save_note", save=save),
        ),
        (
            "SÌ, VOGLIO ONESTART™ — PAGAMENTO ALLA CONSEGNA →",
            tr["cta_hero"],
        ),
        (
            "🔒 Nessun anticipo · Nessuna carta · Paghi solo quando ricevi",
            tr["form_note"],
        ),
        (
            'alt="OneStart 4250A avviatore di emergenza con accessori"',
            f'alt="{tr["hero_alt"]}"',
        ),
        (
            "<h4>Potenza 4250A</h4><p>Avvio anche a batteria scarica</p>",
            f"<h4>{tr['f1t']}</h4><p>{tr['f1d']}</p>",
        ),
        (
            "<h4>Per ogni veicolo</h4><p>Auto, moto, camper e furgoni</p>",
            f"<h4>{tr['f2t']}</h4><p>{tr['f2d']}</p>",
        ),
        (
            "<h4>Fino a 30 avviamenti</h4><p>Una carica per molte emergenze</p>",
            f"<h4>{tr['f3t']}</h4><p>{tr['f3d']}</p>",
        ),
        (
            "<h4>Protezione intelligente</h4><p>Antiscintilla e anti errore</p>",
            f"<h4>{tr['f4t']}</h4><p>{tr['f4d']}</p>",
        ),
        (
            "🔥 Offerta speciale · Solo per oggi: 59 € <s>196 €</s> · -70%",
            fmt(tr, "countdown", now=now, was=was),
        ),
        ("<div class=\"lbl\">Ore</div>", f"<div class=\"lbl\">{tr['cd_h']}</div>"),
        ("<div class=\"lbl\">Min</div>", f"<div class=\"lbl\">{tr['cd_m']}</div>"),
        ("<div class=\"lbl\">Sec</div>", f"<div class=\"lbl\">{tr['cd_s']}</div>"),
        (
            "<span class=\"left\">Disponibilità</span>",
            f"<span class=\"left\">{tr['stock_l']}</span>",
        ),
        (
            "<span class=\"right\">Solo 9 pezzi rimasti</span>",
            f"<span class=\"right\">{tr['stock_r']}</span>",
        ),
        ("<h2>Completa il tuo ordine</h2>", f"<h2>{tr['order_h2']}</h2>"),
        (
            "Compila il modulo qui sotto: il nostro team ti contatterà per confermare tutti i dettagli.",
            tr["order_p"],
        ),
        (
            "<div class=\"num-eyebrow\">01 — La soluzione quando resti a piedi</div>",
            f"<div class=\"num-eyebrow\">{tr['w1_eyebrow']}</div>",
        ),
        (
            "<h3>⚡ Riaccendi il motore anche a batteria completamente scarica</h3>",
            f"<h3>{tr['w1_h']}</h3>",
        ),
        (
            '<div class="tag-row"><span class="tag">4250A</span><span class="tag">Auto e camper</span><span class="tag">Avvio in pochi secondi</span></div>',
            f'<div class="tag-row">{build_tags_html(tr["w1_tags"])}</div>',
        ),
        (
            "<strong>OneStart™ 4250A fa ripartire auto, moto, camper, furgoni, camion, trattori e barche</strong> in autonomia, anche con la batteria a zero.",
            tr["w1_p1"],
        ),
        (
            "Niente chiamate al soccorso stradale, niente attese per un passante disponibile: risolvi da solo, sul posto.",
            tr["w1_p2"],
        ),
        (
            'alt="OneStart avvio con batteria scarica"',
            f'alt="{tr["w1_alt"]}"',
        ),
        (
            "<div class=\"num-eyebrow\">02 — Zero grovigli, zero perdite di tempo</div>",
            f"<div class=\"num-eyebrow\">{tr['w2_eyebrow']}</div>",
        ),
        (
            "<h3>🔌 6 metri di cavi retrattili pronti quando servono</h3>",
            f"<h3>{tr['w2_h']}</h3>",
        ),
        (
            '<div class="tag-row"><span class="tag">6 metri</span><span class="tag">Retrattili</span><span class="tag">Sempre in ordine</span></div>',
            f'<div class="tag-row">{build_tags_html(tr["w2_tags"])}</div>',
        ),
        (
            "<strong>Il sistema di avvolgimento automatico dei cavi da 6 metri rende il collegamento alla batteria immediato,</strong> senza cavi ammassati nel bagagliaio.",
            tr["w2_p1"],
        ),
        (
            "Un gesto per estrarli, un gesto per riporli: tutto resta al suo posto in pochi secondi.",
            tr["w2_p2"],
        ),
        (
            'alt="OneStart cavi retrattili automatici"',
            f'alt="{tr["w2_alt"]}"',
        ),
        (
            "<div class=\"num-eyebrow\">03 — Massima sicurezza a ogni collegamento</div>",
            f"<div class=\"num-eyebrow\">{tr['w3_eyebrow']}</div>",
        ),
        (
            "<h3>🛡️ Aggancia i cavi senza pensieri e senza rischi</h3>",
            f"<h3>{tr['w3_h']}</h3>",
        ),
        (
            '<div class="tag-row"><span class="tag">Antiscintilla</span><span class="tag">Anti errore</span><span class="tag">IP68</span></div>',
            f'<div class="tag-row">{build_tags_html(tr["w3_tags"])}</div>',
        ),
        (
            "<strong>Il sistema di sicurezza integrato previene scintille, inversioni di polarità, cortocircuiti e surriscaldamenti</strong> a ogni avviamento.",
            tr["w3_p1"],
        ),
        (
            "Certificato IP68: resiste a pioggia, polvere, gelo e caldo estremo, in ogni stagione dell'anno.",
            tr["w3_p2"],
        ),
        (
            'alt="OneStart protezione intelligente IP68"',
            f'alt="{tr["w3_alt"]}"',
        ),
        (
            "<span class=\"eyebrow\">Recensioni dei clienti</span>",
            f"<span class=\"eyebrow\">{tr['rev_eyebrow']}</span>",
        ),
        (
            "<h2>Recensioni verificate su OneStart™</h2>",
            f"<h2>{tr['rev_h2']}</h2>",
        ),
        (
            'alt="Recensione OneStart 1"',
            f'alt="{tr["rev1_alt"]}"',
        ),
        ("<h4>Un salvavita in macchina</h4>", f"<h4>{tr['rev1_h']}</h4>"),
        (
            "«Batteria del furgone a zero in pieno inverno. Ho collegato OneStart™ e il motore è partito al primo tentativo. Da allora non lo tolgo più dal bagagliaio.»",
            tr["rev1_p"],
        ),
        (
            "<div class=\"author\">Marco Bianchi — ✅ Acquisto verificato</div>",
            f"<div class=\"author\">{tr['rev1_a']}</div>",
        ),
        (
            'alt="Recensione OneStart 2"',
            f'alt="{tr["rev2_alt"]}"',
        ),
        ("<h4>Praticissimo da usare</h4>", f"<h4>{tr['rev2_h']}</h4>"),
        (
            "«Il cavo che si riavvolge da solo è geniale: prima perdevo minuti a districare i vecchi cavi. Sul camper l'ho collegato e siamo ripartiti in un attimo.»",
            tr["rev2_p"],
        ),
        (
            "<div class=\"author\">Giovanni Conti — ✅ Acquisto verificato</div>",
            f"<div class=\"author\">{tr['rev2_a']}</div>",
        ),
        (
            'alt="Recensione OneStart 3"',
            f'alt="{tr["rev3_alt"]}"',
        ),
        ("<h4>Vale ogni centesimo</h4>", f"<h4>{tr['rev3_h']}</h4>"),
        (
            "«Costruzione solida, display leggibile anche di notte grazie alla torcia integrata, e il power bank mi ha tolto dai guai durante un lungo viaggio.»",
            tr["rev3_p"],
        ),
        (
            "<div class=\"author\">Francesco Ricci — ✅ Acquisto verificato</div>",
            f"<div class=\"author\">{tr['rev3_a']}</div>",
        ),
        (
            "Prodotti utili per la vita quotidiana, consegna in 24-48 ore con pagamento alla consegna.",
            tr["footer_tag"],
        ),
        (">Link utili<", f">{tr['footer_links']}<"),
        (">Chi siamo<", f">{tr['footer_about']}<"),
        (">Consegna<", f">{tr['footer_delivery']}<"),
        (">Home Page<", f">{tr['footer_home']}<"),
        (">Italia<", f">{tr['footer_geo']}<"),
        (">Contattaci<", f">{tr['footer_contact']}<"),
        (">Privacy Policy<", f">{tr['footer_privacy']}<"),
        (">Termini e condizioni<", f">{tr['footer_terms']}<"),
        (">Cookie Policy<", f">{tr['footer_cookie']}<"),
        (">Politica di spedizione<", f">{tr['footer_ship']}<"),
        (">Politica di reso<", f">{tr['footer_refund']}<"),
        (
            "© 2026 powercurvemedia.com – Tutti i diritti riservati.",
            f"© 2026 powercurvemedia.com – {tr['footer_rights']}",
        ),
    ]

    for old, new in sorted(pairs, key=lambda x: len(x[0]), reverse=True):
        html = html.replace(old, new)

    html = html.replace("196 €", was)
    html = html.replace("59 €", now)
    html = html.replace("137 €", save)

    html = html.replace(
        '<span id="liveCount"><strong>42 persone</strong> stanno guardando questo avviatore ora</span>',
        f'<span id="liveCount" data-live-template="{live_tpl}"></span>',
    )
    html = html.replace(
        '<script src="/assets/js/onestart-landing-it.js" defer></script>',
        '<script src="/assets/js/onestart-landing.js" defer></script>\n'
        f'<script src="{TMFP_SCRIPT}" crossorigin="anonymous" defer></script>',
    )

    cmp_old = re.search(r'<section class="compare wrap">.*?</section>', html, re.S)
    if cmp_old:
        html = html.replace(cmp_old.group(0), build_cmp_table(tr), 1)

    kit_old = re.search(r'<section class="kit-section wrap">.*?</section>', html, re.S)
    if kit_old:
        html = html.replace(kit_old.group(0), build_kit_html(tr, was, now), 1)

    faq_old = re.search(r'<section class="faq wrap">.*?</section>', html, re.S)
    if faq_old:
        html = html.replace(faq_old.group(0), build_faq_html(tr, now), 1)

    return html


def build_thankyou(g: dict, tr: dict) -> str:
    geo = g["geo"]
    lang = g["lang"]
    cpa = g["cpa"]
    cpa_js = f"{cpa}.0"

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
<title>{tr["ty_title"]}</title>
<meta name="description" content="{tr["ty_desc"]}">
<meta name="contact" content="info@powercurvemedia.com">
<meta name="theme-color" content="#1f9d55">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/climaone-landing.css">
<style>
body {{ background: #f7f9fb; font-family: 'Poppins', sans-serif; }}
.ty-page {{ max-width: 540px; margin: 0 auto; padding: 1.5rem 1rem 3rem; }}
.ty-logo {{ text-align: center; padding: 1rem 0 0.5rem; font-size: 22px; font-weight: 800; }}
.ty-check {{ width: 64px; height: 64px; border-radius: 9999px; background: #fff; border: 2px solid #1f9d55; display: flex; align-items: center; justify-content: center; margin: 1rem auto 1.5rem; font-size: 2rem; color: #1f9d55; font-weight: 800; box-shadow: 0 4px 12px -4px rgba(31,157,85,.25); }}
.ty-headline {{ font-size: 1.625rem; font-weight: 800; line-height: 1.2; text-align: center; margin-bottom: 0.875rem; }}
.ty-subhead {{ text-align: center; color: #5b6472; font-size: 1rem; line-height: 1.5; margin-bottom: 1.5rem; max-width: 440px; margin-left: auto; margin-right: auto; }}
.ty-hero {{ border-radius: 12px; overflow: hidden; aspect-ratio: 2848/1331; background: #f7f9fb; margin-bottom: 1.5rem; box-shadow: 0 4px 16px -8px rgba(0,0,0,.15); }}
.ty-hero img {{ width: 100%; height: 100%; object-fit: cover; display: block; }}
.ty-action {{ background: #f0fdf4; border: 1.5px solid #86efac; border-radius: 12px; padding: 1.25rem 1.25rem 1.5rem; margin-bottom: 1rem; }}
.ty-action__eyebrow {{ font-size: 0.7rem; font-weight: 800; letter-spacing: 0.15em; text-transform: uppercase; color: #15803d; margin-bottom: 0.625rem; text-align: center; }}
.ty-action__title {{ font-size: 1.25rem; font-weight: 800; text-align: center; margin-bottom: 0.625rem; }}
.ty-action__body {{ text-align: center; color: #5b6472; font-size: 0.95rem; line-height: 1.5; margin-bottom: 0.75rem; }}
.ty-action__warning {{ text-align: center; color: #15803d; font-weight: 700; font-size: 0.9rem; line-height: 1.45; }}
.ty-box {{ background: #fff; border: 1px solid #e7eaee; border-radius: 8px; margin-bottom: 0.75rem; overflow: hidden; }}
.ty-box__header {{ padding: 0.625rem 1rem; background: #f7f9fb; border-bottom: 1px solid #e7eaee; font-size: 0.7rem; font-weight: 800; letter-spacing: 0.12em; text-transform: uppercase; color: #5b6472; }}
.ty-box__body {{ padding: 0.75rem 1rem; font-size: 0.95rem; }}
.ty-steps-list {{ list-style: none; padding: 0; margin: 0; counter-reset: ty-step; }}
.ty-steps-list li {{ display: flex; gap: 0.625rem; padding: 0.625rem 0; border-bottom: 1px solid #e7eaee; font-size: 0.9rem; line-height: 1.45; counter-increment: ty-step; }}
.ty-steps-list li:last-child {{ border-bottom: none; padding-bottom: 0; }}
.ty-steps-list li::before {{ content: counter(ty-step) "."; font-weight: 800; color: #16a34a; flex-shrink: 0; min-width: 1.25rem; }}
.ty-trust {{ display: flex; gap: 0.5rem; flex-wrap: wrap; justify-content: center; margin-top: 1.25rem; }}
.ty-trust__badge {{ background: #fff; border: 1px solid #e7eaee; border-radius: 9999px; padding: 0.4rem 0.875rem; font-size: 0.75rem; font-weight: 600; color: #5b6472; }}
.ty-footer {{ background: #14181f; color: #9ca3af; padding: 2rem 1.25rem; margin-top: 2rem; font-size: 13px; }}
.ty-footer a {{ color: #9ca3af; text-decoration: none; }}
.ty-footer ul {{ list-style: none; margin: 0.5rem 0 0; padding: 0; }}
.ty-footer li {{ margin-bottom: 8px; }}
.ty-footer__copy {{ text-align: center; margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,.1); font-size: 12px; }}
</style>
<script>
window.SITE_CONFIG = {{
  GEO: '{geo}',
  PRODUCT_SLUG: 'onestart',
  OFFER_NAME: 'OneStart 4250A {geo_upper(geo)}',
  LP_ID: '{geo}-onestart-{g["offer"]}',
  CONVERSION_VALUE: {cpa},
  CONVERSION_CURRENCY: 'EUR'
}};
</script>
<script src="/assets/js/tracking.js" defer></script>
</head>
<body>

<div class="ty-logo"><a href="/" style="color:inherit;text-decoration:none;">powercurve<span style="color:#16a34a;">media</span></a></div>

<main class="ty-page">
  <div class="ty-check" aria-hidden="true">✓</div>
  <h1 class="ty-headline">{tr["ty_h1"]}</h1>
  <p class="ty-subhead">{tr["ty_sub"]}</p>

  <figure class="ty-hero">
    <img src="/assets/img/site/thank_you_draftin.png" alt="{tr["ty_hero_alt"]}" width="2848" height="1331" loading="lazy" decoding="async">
  </figure>

  <section class="ty-action">
    <div class="ty-action__eyebrow">{tr["ty_eyebrow"]}</div>
    <h2 class="ty-action__title">{tr["ty_action_t"]}</h2>
    <p class="ty-action__body">{tr["ty_action_b"]}</p>
    <p class="ty-action__warning">{tr["ty_warn"]}</p>
  </section>

  <section class="ty-box">
    <div class="ty-box__header">{tr["ty_hours_h"]}</div>
    <div class="ty-box__body">{tr["ty_hours"]}</div>
  </section>

  <section class="ty-box">
    <div class="ty-box__header">{tr["ty_next_h"]}</div>
    <div class="ty-box__body">
      <ol class="ty-steps-list">
        <li>{tr["ty_s1"]}</li>
        <li>{tr["ty_s2"]}</li>
        <li>{tr["ty_s3"]}</li>
      </ol>
    </div>
  </section>

  <div class="ty-trust">
    <span class="ty-trust__badge">{tr["ty_b1"]}</span>
    <span class="ty-trust__badge">{tr["ty_b2"]}</span>
    <span class="ty-trust__badge">{tr["ty_b3"]}</span>
  </div>
</main>

<footer class="ty-footer">
  <div class="wrap">
    <h3 style="color:#fff;font-size:13px;margin-bottom:8px;">{tr["ty_footer_info"]}</h3>
    <ul>
      <li><a href="/{geo}/about-us.html">{tr["ty_footer_about"]}</a></li>
      <li><a href="/{geo}/contact-us.html">{tr["ty_footer_contact"]}</a></li>
      <li><a href="/{geo}/privacy-policy.html">{tr["ty_footer_privacy"]}</a></li>
      <li><a href="/{geo}/terms-conditions.html">{tr["ty_footer_terms"]}</a></li>
      <li><a href="/{geo}/cookie-policy.html">{tr["ty_footer_cookie"]}</a></li>
      <li><a href="/{geo}/shipping-policy.html">{tr["ty_footer_ship"]}</a></li>
      <li><a href="/{geo}/refund-policy.html">{tr["ty_footer_refund"]}</a></li>
    </ul>
    <p class="ty-footer__copy">© 2026 <strong>Global Health Distribution S.r.l.</strong> — {tr["footer_rights"]}</p>
  </div>
</footer>

<script>
  (function () {{
    if (!window.gtag) return;
    var p = new URLSearchParams(window.location.search);
    function stored(name) {{
      try {{ return window.localStorage.getItem('df_' + name) || ''; }} catch (e) {{ return ''; }}
    }}
    var campaignId = p.get('campaign_id') || p.get('utm_campaign') || p.get('campaignid') || stored('campaign_id') || '';
    var subid = p.get('subid') || campaignId || stored('subid') || '';
    var transactionId = p.get('order_id') || p.get('transaction_id') || p.get('tid') || subid || ('df_' + Date.now());
    gtag('event', 'conversion', {{
      'send_to': '{CONVERSION_SEND_TO}',
      'value': {cpa_js},
      'currency': 'EUR',
      'transaction_id': transactionId,
      'campaign_id': campaignId,
      'subid': subid,
      'utm_campaign': p.get('utm_campaign') || campaignId,
      'utm_source': p.get('utm_source') || stored('utm_source') || '',
      'utm_medium': p.get('utm_medium') || stored('utm_medium') || '',
      'utm_term': p.get('utm_term') || stored('utm_term') || '',
      'utm_content': p.get('utm_content') || stored('utm_content') || ''
    }});
  }})();
</script>
</body>
</html>
"""


def main() -> list[Path]:
    landing_tpl = IT_LANDING.read_text(encoding="utf-8")
    created: list[Path] = []

    for g in GEOS:
        geo = g["geo"]
        offer = g["offer"]
        tr = T[geo]
        out_dir = ROOT / geo / "onestart" / offer
        out_dir.mkdir(parents=True, exist_ok=True)

        index_path = out_dir / "index.html"
        index_path.write_text(apply_landing(landing_tpl, g, tr), encoding="utf-8")
        created.append(index_path)

        ty_path = out_dir / "thank-you.html"
        ty_path.write_text(build_thankyou(g, tr), encoding="utf-8")
        created.append(ty_path)

        print(f"  {geo}/onestart/{offer}/index.html")
        print(f"  {geo}/onestart/{offer}/thank-you.html")

    return created


if __name__ == "__main__":
    print("Generating OneStart pages...")
    files = main()
    print(f"Done — {len(files)} files written.")

