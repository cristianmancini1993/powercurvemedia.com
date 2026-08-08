#!/usr/bin/env python3
"""Generate Aircelo landing + thank-you pages for LT, PT, ES, PL, SK."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

GEOS = [
    {
        "geo": "lt", "lang": "lt", "offer": "311",
        "price": 69, "currency": "EUR",
        "was": "230 €", "now": "69 €", "cpa": 17.5,
        "filter_value": "19 €", "hour_cost": "0,10 €",
    },
    {
        "geo": "pt", "lang": "pt", "offer": "318",
        "price": 84, "currency": "EUR",
        "was": "280 €", "now": "84 €", "cpa": 17,
        "filter_value": "19 €", "hour_cost": "0,10 €",
    },
    {
        "geo": "es", "lang": "es", "offer": "319",
        "price": 84, "currency": "EUR",
        "was": "280 €", "now": "84 €", "cpa": 17,
        "filter_value": "19 €", "hour_cost": "0,10 €",
    },
    {
        "geo": "pl", "lang": "pl", "offer": "320",
        "price": 349, "currency": "PLN",
        "was": "1.163 zł", "now": "349 zł", "cpa": 18,
        "filter_value": "79 zł", "hour_cost": "0,40 zł",
    },
    {
        "geo": "sk", "lang": "sk", "offer": "321",
        "price": 79, "currency": "EUR",
        "was": "263 €", "now": "79 €", "cpa": 17.5,
        "filter_value": "19 €", "hour_cost": "0,10 €",
    },
]

T = {
    "lt": {
        "title": "Aircelo™ — 4-in-1 koloninis kondicionierius iki 90 m² | -70%",
        "description": "Aircelo™: 4-in-1 koloninis kondicionierius. Vėsina, šildo, sausina ir ventiliuoja iki 90 m². Skaitmeninis ekranas, RGB šviesos ir itin tylus naktinis režimas. Nemokamas pristatymas ir mokėjimas pristatymo metu.",
        "og_title": "Aircelo™ — 4-in-1 kondicionierius | -70%",
        "og_desc": "Vėsina, šildo, sausina ir ventiliuoja iki 90 m². Be žarnų, be meistro. Mokėjimas pristatymo metu.",
        "topbar": "🔥 70 % NUOLAIDA + NEMOKAMAS PRISTATYMAS — MOKĖJIMAS PRISTATYMO METU 🔥",
        "rating": "<strong>4,8/5</strong> — remiantis <strong>2.729+ patvirtintomis apžvalgomis</strong>",
        "gift": "2 METŲ GARANTIJA ĮSKAIČIUOTA + PAPILDOMAS KVAPų FILTRAS DOVANŲ",
        "h1": "Nešiojamas kondicionierius — atvėsinkite arba sušildykite visus namus per 5 minutes <span class=\"hl\">naudodami tik {hour_cost} per valandą (energetinė klasė A+++)</span>",
        "lead": "<strong>Aircelo™</strong> sausina ir ventiliuoja, taip pat vėsina ir šildo — viskas viename kompaktiškame įrenginyje. Skaitmeninis ekranas, RGB šviesos ir itin tylus naktinis režimas, kad galėtumėte naudoti miegodami. Perkelkite kur norite namuose: be žarnų, be skylių, be meistro.",
        "hero_alt": "Aircelo™ 4-in-1 koloninis kondicionierius",
        "cta": "TAIP, NORIU Aircelo™ →",
        "form_note": "🔒 Be užstato · Be kortelės · Mokate tik gavę",
        "f1h": "Nemokamas pristatymas", "f1p": "Pristatymas visoje Lietuvoje",
        "f2h": "Mokėjimas pristatymo metu", "f2p": "Kortelė nereikalinga",
        "f3h": "2 metų garantija", "f3p": "Visiška apsauga įskaičiuota",
        "f4h": "Grąžinimas per 14 dienų", "f4p": "Visas pinigų grąžinimas",
        "urgency": "⏰ 70 % nuolaida baigiasi po",
        "cd_h": "Val.", "cd_m": "Min.", "cd_s": "Sek.",
        "stock_l": "Likučiai sandėlyje", "stock_r": "Liko tik 3 vienetai",
        "live": "<strong>%n žmonių</strong> dabar žiūri šį kondicionierių",
        "form_h": "Užbaikite užsakymą",
        "form_p": "Užpildykite formą — mūsų komanda susisieks, kad patvirtintų visus duomenis.",
        "name_l": "Vardas ir pavardė*", "name_ph": "Jonas Petraitis",
        "phone_l": "Telefono numeris*", "phone_ph": "+370 600 00000",
        "addr_l": "Pristatymo adresas*", "addr_ph": "Gedimino pr. 1, 01103 Vilnius",
        "submit": "TAIP, NORIU Aircelo™ →",
        "w1e": "01 — 4 funkcijos viename",
        "w1h": "Vėsinkite, šildykite, sausinkite ir ventiliuokite vienu prietaisu",
        "w1t": ["Vėsina", "Šildo", "Sausina", "Ventiliuoja"],
        "w1p": "Vienas kompaktiškas prietaisas <strong>pakeičia keturis įrenginius</strong>: vėsina vasarą, šildo žiemą, sausina lietingomis dienomis ir ventiliuoja ištisus metus.",
        "w1i": "Idealu patalpoms iki 90 m² — svetainei, miegamajam ir biurui.",
        "w1alt": "Aircelo vėsina ir šildo per kelias minutes",
        "w2e": "02 — Tikslus valdymas",
        "w2h": "Skaitmeninis ekranas ir automatinis išjungimas pasiekus temperatūrą",
        "w2t": ["LED ekranas", "Auto-off", "RGB šviesos"],
        "w2p": "<strong>Skaitmeninis ekranas</strong> realiu laiku rodo tikslią temperatūrą. Nustatote pageidaujamą reikšmę ir prietaisas automatiškai išsijungia ją pasiekęs.",
        "w2i": "Reguliuojamos RGB šviesos kuria atmosferą ir rodo aktyvų režimą.",
        "w2alt": "Aircelo nešiojamas — perkelkite iš kambario į kambarį",
        "w3e": "03 — Tyliai ir efektyviai",
        "w3h": "Itin tylus naktinis režimas ir mažos energijos sąnaudos",
        "w3t": ["Eco režimas", "Naktinis režimas", "Mažos sąnaudos"],
        "w3p": "Veikia taip tyliai, kad <strong>netrukdo miegui</strong>. Eco ir naktiniai režimai leidžia laikyti įjungtą valandų valandas nesijaudinant dėl sąskaitos.",
        "w3i": "Paruošimas per 2 minutes: be žarnų, be skylių, be meistro.",
        "w3alt": "Aircelo tylus naktinis režimas miegamajame",
        "cmp_label": "Tiesioginis palyginimas",
        "cmp_h": "Pigus ventiliatorius vs Aircelo™",
        "cmp_th1": "Pigus",
        "cmp_rows": [
            ("Funkcijos", "Tik ventiliacija", "4 viename: vėsina, šildo, sausina, ventiliuoja"),
            ("Montavimas", "Dažnai sudėtingas", "2 minutės, be žarnų"),
            ("Padengimas", "Mažas kambarys", "Iki 90 m²"),
            ("Sąnaudos", "Didelės ilgai naudojant", "Mažos, Eco ir naktiniai režimai"),
            ("Ekranas", "Nėra", "Skaitmeninis su auto-off"),
            ("Filtrai", "Bazinis rinkinys", "EPA + nemokamas kvapų filtras"),
        ],
        "rev_h": "Daugiau nei 3.000 patenkintų klientų — štai ką jie sako!",
        "verified": "Patvirtintas pirkimas",
        "reviews": [
            ("Atvyko per dvi dienas!", "«Atvyko per dvi darbo dienas. Mandagus pardavėjas, patikima įmonė ir tikrai puikus produktas. Greitai vėsina!»", "Rūta G. — Vilnius"),
            ("Lengva naudoti ir galinga", "«Labai patinka: greitai vėsina ir labai paprasta naudoti. Skaitmeninis ekranas rodo tikslią temperatūrą.»", "Jonas R. — Kaunas"),
            ("Puiku miegamajam", "«Pirkau miegamajam ir tinka puikiai: naktį beveik negirdėti. Mokėjimas pristatymo metu suteikė pasitikėjimo.»", "Tomas M. — Klaipėda"),
        ],
        "kit_eye": "Viskas įskaičiuota dėžėje",
        "kit_h": "📦 Jūsų Aircelo™ 4-in-1 rinkinyje yra:",
        "kit_alt": "Aircelo dėžės turinys",
        "kit_items": [
            "1× Aircelo™ 4-in-1 koloninis kondicionierius",
            "1× Nuotolinio valdymo pultas",
            "1× Maitinimo kabelis",
            "1× Plaunamas daugkartinis filtras (jau įmontuotas)",
            "1× PAPILDOMAS kvapų filtras DOVANŲ (vertė {filter_value})",
            "1× Lietuviškas vadovas + greito paleidimo instrukcija",
            "Oficiali 24 mėn. garantija + aptarnavimas lietuvių kalba",
            "Nemokamas pristatymas per 24/48 val. visoje Lietuvoje",
        ],
        "faq_h": "Dažnai užduodami klausimai",
        "faqs": [
            ("Ar galiu mokėti pristatymo metu?", "Taip. Mokate grynaisiais kurjeriui gavę siuntinį — be kortelės. Pristatymas per 24–48 val. su sekimo kodu SMS ir el. paštu."),
            ("Kiek turėsiu sumokėti?", "Mokate tik <strong>{now}</strong> pristatymo metu — be užstato ir be kortelės."),
            ("Kaip vyksta montavimas?", "Labai paprasta: išimkite iš dėžės, įjunkite į rozetę ir per kelias minutes paruošta. Be žarnų, be skylių, be meistro."),
            ("Koks energijos suvartojimas?", "Labai mažas. Dėl eco ir naktinių režimų galite laikyti įjungtą valandų valandas nesijaudindami dėl sąskaitos."),
            ("Ar tyliai veikia naktį?", "Turi itin tylų naktinį režimą: galite miegoti ir dirbti su įjungtu prietaisu."),
            ("O jei nepatiks? Ar yra garantija?", "Turite 14 dienų grąžinti su visu pinigų grąžinimu. Kiekvienas prietaisas turi oficialią 24 mėn. garantiją."),
        ],
        "footer_tag": "Naudingi kasdieniai produktai, pristatymas per 24–48 val. su mokėjimu pristatymo metu.",
        "footer_info": "Informacija", "footer_about": "Apie mus", "footer_del": "Pristatymas",
        "footer_ship": "Pristatymo politika", "footer_refund": "Grąžinimo politika",
        "footer_home": "Pradžia", "footer_contact": "Susisiekite",
        "footer_geo": "Lietuva", "footer_copy": "Visos teisės saugomos.",
        "submitting": "Siunčiama...",
        "ty_title": "Užsakymas gautas — Palaukite patvirtinimo skambučio | Aircelo™",
        "ty_desc": "Jūsų Aircelo™ užsakymas užregistruotas. Paskutinis žingsnis: atsiliepkite į patvirtinimo skambutį.",
        "ty_h": "Jūsų užsakymas užregistruotas!",
        "ty_sub": "Puiku — jūsų Aircelo™ užsakymas apdorojamas. Liko tik <strong>paskutinis žingsnis</strong> prieš išsiuntimą.",
        "ty_eye": "👇 Ką dabar reikia padaryti",
        "ty_act_h": "📞 Atsiliepkite į patvirtinimo skambutį",
        "ty_act_p": "Mūsų operatorius susisieks su jumis <strong>per kelias valandas</strong>, kad patvirtintų užsakymą.",
        "ty_warn": "Jei neatsiliepsite, užsakymas bus automatiškai atšauktas.",
        "ty_hours_h": "🕒 Kontaktų valandos",
        "ty_hours": "<strong>Pirmadienis – Šeštadienis</strong> · 9:00 – 18:00",
        "ty_next_h": "📋 Kas toliau",
        "ty_steps": [
            "Skambučio metu <strong>patvirtinkite savo duomenis</strong>",
            "Užsakymas išsiunčiamas per <strong>24–48 valandas</strong>",
            "Pristatymas į namus ir <strong>mokėjimas pristatymo metu</strong>",
        ],
        "ty_b1": "🔒 Mokėjimas pristatymo metu",
        "ty_b2": "🛡️ 2 metų garantija",
        "ty_b3": "🔐 SSL apsauga",
        "ty_footer": "Informacija",
        "ty_about": "Apie mus", "ty_contact": "Kontaktai",
        "ty_copy": "Visos teisės saugomos.",
    },
    "pt": {
        "title": "Aircelo™ — Ar condicionado de coluna 4 em 1 até 90 m² | -70%",
        "description": "Aircelo™: ar condicionado de coluna 4 em 1. Arrefce, aquece, desumidifica e ventila até 90 m². Ecrã digital, luzes RGB e modo noturno ultrassilencioso. Envio grátis e pagamento à cobrança.",
        "og_title": "Aircelo™ — Ar condicionado 4 em 1 | -70%",
        "og_desc": "Arrefce, aquece, desumidifica e ventila até 90 m². Sem tubos, sem técnico. Pagamento à cobrança.",
        "topbar": "🔥 DESCONTO 70% + ENVIO GRÁTIS — PAGAMENTO À COBRANÇA 🔥",
        "rating": "<strong>4,8/5</strong> — com base em <strong>2.729+ avaliações</strong> verificadas",
        "gift": "GARANTIA DE 2 ANOS INCLUÍDA + FILTRO EXTRA ANTI-ODORES DE PRESENTE",
        "h1": "Ar condicionado portátil — Arrefeça ou aqueça toda a casa em 5 minutos <span class=\"hl\">consumindo apenas {hour_cost} por hora (Classe energética A+++)</span>",
        "lead": "<strong>Aircelo™</strong> desumidifica e ventila além de arrefecer e aquecer — tudo num único aparelho compacto. Ecrã digital, luzes RGB e modo noturno ultrassilencioso para usar enquanto dorme. Mova-o onde quiser em casa: sem tubos, sem furos e sem técnico.",
        "hero_alt": "Aircelo™ ar condicionado de coluna 4 em 1",
        "cta": "SIM, QUERO Aircelo™ →",
        "form_note": "🔒 Sem adiantamento · Sem cartão · Paga só quando receber",
        "f1h": "Envio grátis", "f1p": "Entrega em todo o Portugal",
        "f2h": "Pagamento à cobrança", "f2p": "Não é necessário cartão",
        "f3h": "Garantia de 2 anos", "f3p": "Cobertura completa incluída",
        "f4h": "Devolução em 14 dias", "f4p": "Reembolso total",
        "urgency": "⏰ O desconto de 70% termina em",
        "cd_h": "Horas", "cd_m": "Min.", "cd_s": "Seg.",
        "stock_l": "Disponibilidade em stock", "stock_r": "Só restam 3 unidades",
        "live": "<strong>%n pessoas</strong> estão a ver este ar condicionado agora",
        "form_h": "Conclua a sua encomenda",
        "form_p": "Preencha o formulário abaixo — a nossa equipa contactá-lo-á para confirmar todos os detalhes.",
        "name_l": "Nome e apelido*", "name_ph": "Maria Silva",
        "phone_l": "Número de telefone*", "phone_ph": "+351 912 345 678",
        "addr_l": "Morada de entrega*", "addr_ph": "Av. da Liberdade 100, 1250-096 Lisboa",
        "submit": "SIM, QUERO Aircelo™ →",
        "w1e": "01 — 4 funções em 1",
        "w1h": "Arrefeça, aqueça, desumidifique e ventile com um só aparelho",
        "w1t": ["Arrefce", "Aquece", "Desumidifica", "Ventila"],
        "w1p": "Um único aparelho compacto <strong>substitui quatro dispositivos</strong>: arrefece no verão, aquece no inverno, desumidifica em dias de chuva e ventila o ano todo.",
        "w1i": "Ideal para espaços até 90 m² — sala, quarto e escritório.",
        "w1alt": "Aircelo arrefece e aquece em poucos minutos",
        "w2e": "02 — Controlo preciso",
        "w2h": "Ecrã digital e desligamento automático à temperatura desejada",
        "w2t": ["Ecrã LED", "Auto-off", "Luzes RGB"],
        "w2p": "O <strong>ecrã digital</strong> mostra a temperatura exata em tempo real. Define o valor desejado e o aparelho desliga-se automaticamente ao atingi-lo.",
        "w2i": "As luzes RGB reguláveis criam ambiente e indicam o modo ativo.",
        "w2alt": "Aircelo portátil — mova de quarto em quarto",
        "w3e": "03 — Silencioso e eficiente",
        "w3h": "Modo noturno ultrassilencioso e baixo consumo energético",
        "w3t": ["Modo Eco", "Modo Noite", "Baixo consumo"],
        "w3p": "Funciona de forma tão discreta que <strong>não interrompe o sono</strong>. Os modos eco e noite permitem mantê-lo ligado horas sem se preocupar com a fatura.",
        "w3i": "Instalação em 2 minutos: sem tubos, sem furos e sem técnico.",
        "w3alt": "Aircelo modo noturno silencioso no quarto",
        "cmp_label": "Comparação direta",
        "cmp_h": "Ventoinha barata vs Aircelo™",
        "cmp_th1": "Barata",
        "cmp_rows": [
            ("Funções", "Só ventilação", "4 em 1: arrefece, aquece, desumidifica, ventila"),
            ("Instalação", "Muitas vezes complexa", "2 minutos, sem tubos"),
            ("Cobertura", "Quarto pequeno", "Até 90 m²"),
            ("Consumo", "Alto em uso prolongado", "Baixo consumo, modos Eco e Noite"),
            ("Ecrã", "Inexistente", "Digital com desligamento automático"),
            ("Filtros", "Kit básico", "EPA + filtro anti-odores grátis"),
        ],
        "rev_h": "Mais de 3.000 clientes satisfeitos — eis o que dizem!",
        "verified": "Compra verificada",
        "reviews": [
            ("Chegou em dois dias!", "«Chegou em dois dias úteis. Vendedor simpático, empresa fiável e produto realmente excelente. Arrefece rápido!»", "Maria G. — Lisboa"),
            ("Fácil de usar e potente", "«Adoro: arrefece rápido e é muito fácil de usar. O ecrã digital mostra a temperatura exata.»", "Lucas R. — Porto"),
            ("Perfeito para o quarto", "«Comprei para o quarto e é perfeito: à noite quase não se ouve. O pagamento à cobrança deu-me confiança.»", "Carlos M. — Coimbra"),
        ],
        "kit_eye": "Tudo incluído na caixa",
        "kit_h": "📦 O seu kit Aircelo™ 4 em 1 inclui:",
        "kit_alt": "Conteúdo da caixa Aircelo",
        "kit_items": [
            "1× Ar condicionado de coluna Aircelo™ 4 em 1",
            "1× Comando à distância",
            "1× Cabo de alimentação",
            "1× Filtro lavável reutilizável (já instalado)",
            "1× Filtro anti-odores EXTRA DE PRESENTE (valor {filter_value})",
            "1× Manual em português + guia de início rápido",
            "Garantia oficial 24 meses + apoio em português",
            "Envio grátis em 24/48 h em todo o Portugal",
        ],
        "faq_h": "Perguntas frequentes",
        "faqs": [
            ("Posso pagar à cobrança?", "Sim. Paga em dinheiro ao estafeta quando recebe o pacote — sem cartão. Envio em 24–48 h com código de seguimento por SMS e e-mail."),
            ("Quanto terei de pagar?", "Paga apenas <strong>{now}</strong> à cobrança — sem adiantamento e sem cartão."),
            ("Como é a instalação?", "Muito simples: tire da caixa, ligue à tomada e em poucos minutos está pronto. Sem tubos, sem furos e sem técnico."),
            ("Qual é o consumo energético?", "Muito baixo. Graças aos modos eco e noite, pode mantê-lo ligado horas sem se preocupar com a fatura."),
            ("É silencioso à noite?", "Tem um modo noturno ultrassilencioso: pode dormir e trabalhar com o aparelho ligado."),
            ("E se não gostar? Há garantia?", "Tem 14 dias para devolver com reembolso total. Cada aparelho tem 24 meses de garantia oficial."),
        ],
        "footer_tag": "Produtos úteis para o dia a dia, entrega em 24–48 horas com pagamento à cobrança.",
        "footer_info": "Informações", "footer_about": "Sobre nós", "footer_del": "Entrega",
        "footer_ship": "Política de envio", "footer_refund": "Política de devolução",
        "footer_home": "Início", "footer_contact": "Contacte-nos",
        "footer_geo": "Portugal", "footer_copy": "Todos os direitos reservados.",
        "submitting": "A enviar...",
        "ty_title": "Encomenda recebida — Aguarde a chamada de confirmação | Aircelo™",
        "ty_desc": "A sua encomenda Aircelo™ foi registada. Último passo: atenda a chamada de confirmação.",
        "ty_h": "A sua encomenda foi registada!",
        "ty_sub": "Ótimo — a sua encomenda Aircelo™ está a ser processada. Falta apenas <strong>um último passo</strong> antes do envio.",
        "ty_eye": "👇 O que precisa de fazer agora",
        "ty_act_h": "📞 Atenda a chamada de confirmação",
        "ty_act_p": "O nosso operador contactá-lo-á <strong>dentro de algumas horas</strong> para confirmar a encomenda.",
        "ty_warn": "Se não atender a chamada, a encomenda será automaticamente cancelada.",
        "ty_hours_h": "🕒 Horário de contacto",
        "ty_hours": "<strong>Segunda – Sábado</strong> · 9:00 – 18:00",
        "ty_next_h": "📋 O que acontece a seguir",
        "ty_steps": [
            "Na chamada, <strong>confirme os seus dados</strong>",
            "A encomenda é enviada em <strong>24–48 horas</strong>",
            "Entrega ao domicílio e pagamento <strong>à cobrança</strong>",
        ],
        "ty_b1": "🔒 Pagamento à cobrança",
        "ty_b2": "🛡️ Garantia de 2 anos",
        "ty_b3": "🔐 Protegido por SSL",
        "ty_footer": "Informações",
        "ty_about": "Sobre nós", "ty_contact": "Contacto",
        "ty_copy": "Todos os direitos reservados.",
    },
    "es": {
        "title": "Aircelo™ — Climatizador de columna 4 en 1 hasta 90 m² | -70%",
        "description": "Aircelo™: climatizador de columna 4 en 1. Enfría, calienta, deshumidifica y ventila hasta 90 m². Pantalla digital, luces RGB y modo nocturno ultrasilencioso. Envío gratis y pago contra reembolso.",
        "og_title": "Aircelo™ — Climatizador 4 en 1 | -70%",
        "og_desc": "Enfría, calienta, deshumidifica y ventila hasta 90 m². Sin tubos, sin técnico. Pago contra reembolso.",
        "topbar": "🔥 DESCUENTO 70% + ENVÍO GRATIS — PAGO CONTRA REEMBOLSO 🔥",
        "rating": "<strong>4,8/5</strong> — basado en <strong>2.729+ reseñas</strong> verificadas",
        "gift": "GARANTÍA DE 2 AÑOS INCLUIDA + FILTRO EXTRA ANTIOLORES DE REGALO",
        "h1": "Aire acondicionado portátil — Enfría o calienta toda la casa en 5 minutos <span class=\"hl\">consumiendo solo {hour_cost} la hora (Clase energética A+++)</span>",
        "lead": "<strong>Aircelo™</strong> deshumidifica y ventila además de enfriar y calentar — todo en un único dispositivo compacto. Pantalla digital, luces RGB y modo nocturno ultrasilencioso para usarlo mientras duermes. Lo mueves donde quieras en casa: sin tubos, sin agujeros y sin técnico.",
        "hero_alt": "Aircelo™ climatizador de columna 4 en 1",
        "cta": "SÍ, QUIERO Aircelo™ →",
        "form_note": "🔒 Sin anticipo · Sin tarjeta · Pagas solo cuando lo recibes",
        "f1h": "Envío gratis", "f1p": "Entrega en toda España",
        "f2h": "Pago contra reembolso", "f2p": "No se requiere tarjeta",
        "f3h": "Garantía de 2 años", "f3p": "Cobertura completa incluida",
        "f4h": "Devolución en 14 días", "f4p": "Reembolso completo",
        "urgency": "⏰ El descuento del 70% termina en",
        "cd_h": "Horas", "cd_m": "Min.", "cd_s": "Seg.",
        "stock_l": "Disponibilidad en stock", "stock_r": "Solo quedan 3 unidades",
        "live": "<strong>%n personas</strong> están viendo este climatizador ahora",
        "form_h": "Completa tu pedido",
        "form_p": "Rellena el formulario de abajo: nuestro equipo te contactará para confirmar todos los detalles.",
        "name_l": "Nombre y apellidos*", "name_ph": "María García",
        "phone_l": "Número de teléfono*", "phone_ph": "+34 612 345 678",
        "addr_l": "Dirección de envío*", "addr_ph": "Calle Gran Vía 28, 28013 Madrid",
        "submit": "SÍ, QUIERO Aircelo™ →",
        "w1e": "01 — 4 funciones en 1",
        "w1h": "Enfría, calienta, deshumidifica y ventila con un solo aparato",
        "w1t": ["Enfría", "Calienta", "Deshumidifica", "Ventila"],
        "w1p": "Un solo aparato compacto <strong>sustituye cuatro dispositivos</strong>: enfría en verano, calienta en invierno, deshumidifica en días de lluvia y ventila todo el año.",
        "w1i": "Ideal para estancias de hasta 90 m² — salón, dormitorio y oficina.",
        "w1alt": "Aircelo enfría y calienta en pocos minutos",
        "w2e": "02 — Control preciso",
        "w2h": "Pantalla digital y apagado automático a la temperatura deseada",
        "w2t": ["Pantalla LED", "Auto-off", "Luces RGB"],
        "w2p": "La <strong>pantalla digital</strong> muestra la temperatura exacta en tiempo real. Ajustas el valor deseado y el aparato se apaga automáticamente al alcanzarlo.",
        "w2i": "Las luces RGB regulables crean ambiente e indican el modo activo.",
        "w2alt": "Aircelo portátil — muévelo de habitación en habitación",
        "w3e": "03 — Silencioso y eficiente",
        "w3h": "Modo nocturno ultrasilencioso y bajo consumo energético",
        "w3t": ["Modo Eco", "Modo Noche", "Bajo consumo"],
        "w3p": "Funciona de forma tan discreta que <strong>no interrumpe el sueño</strong>. Los modos eco y noche permiten mantenerlo encendido horas sin preocuparse por la factura.",
        "w3i": "Instalación en 2 minutos: sin tubos, sin agujeros y sin técnico.",
        "w3alt": "Aircelo modo nocturno silencioso en el dormitorio",
        "cmp_label": "Comparación directa",
        "cmp_h": "Ventilador barato vs Aircelo™",
        "cmp_th1": "Barato",
        "cmp_rows": [
            ("Funciones", "Solo ventilación", "4 en 1: enfría, calienta, deshumidifica, ventila"),
            ("Instalación", "A menudo compleja", "2 minutos, sin tubos"),
            ("Cobertura", "Habitación pequeña", "Hasta 90 m²"),
            ("Consumo", "Alto en uso prolongado", "Bajo consumo, modos Eco y Noche"),
            ("Pantalla", "Inexistente", "Digital con autoapagado"),
            ("Filtros", "Kit básico", "EPA + filtro antiolores gratis"),
        ],
        "rev_h": "Más de 3.000 clientes satisfechos — ¡esto es lo que dicen!",
        "verified": "Compra verificada",
        "reviews": [
            ("¡Llegó en dos días!", "«Llegó en dos días laborables. Vendedor amable, empresa fiable y producto realmente excelente. ¡Enfría rápido!»", "María G. — Madrid"),
            ("Fácil de usar y potente", "«Me encanta: enfría rápido y es muy fácil de usar. La pantalla digital muestra la temperatura exacta.»", "Lucas R. — Barcelona"),
            ("Perfecto para el dormitorio", "«Lo compré para el dormitorio y es perfecto: por la noche casi no se oye. El pago contra reembolso me dio confianza.»", "Carlos M. — Valencia"),
        ],
        "kit_eye": "Todo incluido en la caja",
        "kit_h": "📦 Tu kit Aircelo™ 4 en 1 incluye:",
        "kit_alt": "Contenido de la caja Aircelo",
        "kit_items": [
            "1× Climatizador de columna Aircelo™ 4 en 1",
            "1× Mando a distancia",
            "1× Cable de alimentación",
            "1× Filtro lavable reutilizable (ya instalado)",
            "1× Filtro antiolores EXTRA DE REGALO (valor {filter_value})",
            "1× Manual en español + guía de inicio rápido",
            "Garantía oficial 24 meses + atención en español",
            "Envío gratis en 24/48 h en toda España",
        ],
        "faq_h": "Preguntas frecuentes",
        "faqs": [
            ("¿Puedo pagar contra reembolso?", "Sí. Pagas en efectivo al mensajero cuando recibes el paquete — sin tarjeta. Envío en 24–48 h con código de seguimiento por SMS y email."),
            ("¿Cuánto tendré que pagar?", "Pagas solo <strong>{now}</strong> contra reembolso — sin anticipo y sin tarjeta."),
            ("¿Cómo es la instalación?", "Muy sencilla: sácalo de la caja, enchúfalo y en pocos minutos está listo. Sin tubos, sin agujeros y sin técnico."),
            ("¿Cuál es el consumo energético?", "Muy bajo. Gracias a los modos eco y noche, puedes mantenerlo encendido horas sin preocuparte por la factura."),
            ("¿Es silencioso por la noche?", "Tiene un modo nocturno ultrasilencioso: puedes dormir y trabajar con el aparato encendido."),
            ("¿Y si no me gusta? ¿Hay garantía?", "Tienes 14 días para devolverlo con reembolso completo. Cada aparato tiene 24 meses de garantía oficial."),
        ],
        "footer_tag": "Productos útiles para el día a día, entrega en 24–48 horas con pago contra reembolso.",
        "footer_info": "Información", "footer_about": "Sobre nosotros", "footer_del": "Entrega",
        "footer_ship": "Política de envío", "footer_refund": "Política de devolución",
        "footer_home": "Inicio", "footer_contact": "Contáctanos",
        "footer_geo": "España", "footer_copy": "Todos los derechos reservados.",
        "submitting": "Enviando...",
        "ty_title": "Pedido recibido — Espera la llamada de confirmación | Aircelo™",
        "ty_desc": "Tu pedido Aircelo™ ha sido registrado. Último paso: responde a la llamada de confirmación.",
        "ty_h": "¡Tu pedido ha sido registrado!",
        "ty_sub": "Genial — tu pedido Aircelo™ se está procesando. Solo queda <strong>un último paso</strong> antes del envío.",
        "ty_eye": "👇 Lo que debes hacer ahora",
        "ty_act_h": "📞 Responde a la llamada de confirmación",
        "ty_act_p": "Nuestro operador te contactará <strong>en unas horas</strong> para confirmar el pedido.",
        "ty_warn": "Si no respondes a la llamada, el pedido se cancelará automáticamente.",
        "ty_hours_h": "🕒 Horario de contacto",
        "ty_hours": "<strong>Lunes – Sábado</strong> · 9:00 – 18:00",
        "ty_next_h": "📋 Qué ocurre después",
        "ty_steps": [
            "En la llamada, <strong>confirma tus datos</strong>",
            "Tu pedido se envía en <strong>24–48 horas</strong>",
            "Entrega a domicilio y pago <strong>contra reembolso</strong>",
        ],
        "ty_b1": "🔒 Pago contra reembolso",
        "ty_b2": "🛡️ Garantía de 2 años",
        "ty_b3": "🔐 Protegido SSL",
        "ty_footer": "Información",
        "ty_about": "Sobre nosotros", "ty_contact": "Contacto",
        "ty_copy": "Todos los derechos reservados.",
    },
    "pl": {
        "title": "Aircelo™ — Klimatyzator kolumnowy 4 w 1 do 90 m² | -70%",
        "description": "Aircelo™: klimatyzator kolumnowy 4 w 1. Chłodzi, ogrzewa, osusza i wentyluje do 90 m². Wyświetlacz cyfrowy, światła RGB i ultrasrebrny tryb nocny. Darmowa dostawa i płatność przy odbiorze.",
        "og_title": "Aircelo™ — Klimatyzator 4 w 1 | -70%",
        "og_desc": "Chłodzi, ogrzewa, osusza i wentyluje do 90 m². Bez rur, bez technika. Płatność przy odbiorze.",
        "topbar": "🔥 RABAT 70% + DARMOWA DOSTAWA — PŁATNOŚĆ PRZY ODBIORZE 🔥",
        "rating": "<strong>4,8/5</strong> — na podstawie <strong>2 729+ zweryfikowanych opinii</strong>",
        "gift": "2 LATA GWARANCJI W CENIE + DODATKOWY FILTR ANTYZAPACHOWY W PREZENCIE",
        "h1": "Przenośny klimatyzator — Schłodź lub ogrzej cały dom w 5 minut <span class=\"hl\">zużywając tylko {hour_cost} na godzinę (Klasa energetyczna A+++)</span>",
        "lead": "<strong>Aircelo™</strong> osusza i wentyluje oprócz chłodzenia i ogrzewania — wszystko w jednym kompaktowym urządzeniu. Wyświetlacz cyfrowy, światła RGB i ultrasrebrny tryb nocny, aby używać go podczas snu. Przenosisz go gdzie chcesz w domu: bez rur, bez wiercenia i bez technika.",
        "hero_alt": "Aircelo™ klimatyzator kolumnowy 4 w 1",
        "cta": "TAK, CHCĘ Aircelo™ →",
        "form_note": "🔒 Bez zaliczki · Bez karty · Płacisz dopiero po otrzymaniu",
        "f1h": "Darmowa dostawa", "f1p": "Dostawa w całej Polsce",
        "f2h": "Płatność przy odbiorze", "f2p": "Karta nie jest wymagana",
        "f3h": "2 lata gwarancji", "f3p": "Pełna ochrona w cenie",
        "f4h": "Zwrot w 14 dni", "f4p": "Pełny zwrot pieniędzy",
        "urgency": "⏰ Rabat 70% kończy się za",
        "cd_h": "Godz.", "cd_m": "Min.", "cd_s": "Sek.",
        "stock_l": "Dostępność w magazynie", "stock_r": "Zostały tylko 3 sztuki",
        "live": "<strong>%n osób</strong> ogląda teraz ten klimatyzator",
        "form_h": "Dokończ zamówienie",
        "form_p": "Wypełnij formularz poniżej — nasz zespół skontaktuje się, aby potwierdzić wszystkie szczegóły.",
        "name_l": "Imię i nazwisko*", "name_ph": "Jan Kowalski",
        "phone_l": "Numer telefonu*", "phone_ph": "+48 500 000 000",
        "addr_l": "Adres dostawy*", "addr_ph": "ul. Marszałkowska 1, 00-001 Warszawa",
        "submit": "TAK, CHCĘ Aircelo™ →",
        "w1e": "01 — 4 funkcje w 1",
        "w1h": "Chłodź, ogrzewaj, osuszaj i wentyluj jednym urządzeniem",
        "w1t": ["Chłodzi", "Ogrzewa", "Osusza", "Wentyluje"],
        "w1p": "Jedno kompaktowe urządzenie <strong>zastępuje cztery aparaty</strong>: chłodzi latem, ogrzewa zimą, osusza w deszczowe dni i wentyluje przez cały rok.",
        "w1i": "Idealne do pomieszczeń do 90 m² — salonu, sypialni i biura.",
        "w1alt": "Aircelo chłodzi i ogrzewa w kilka minut",
        "w2e": "02 — Precyzyjna kontrola",
        "w2h": "Wyświetlacz cyfrowy i automatyczne wyłączenie przy żądanej temperaturze",
        "w2t": ["Wyświetlacz LED", "Auto-off", "Światła RGB"],
        "w2p": "<strong>Wyświetlacz cyfrowy</strong> pokazuje dokładną temperaturę w czasie rzeczywistym. Ustawiasz żądaną wartość, a urządzenie wyłącza się automatycznie po jej osiągnięciu.",
        "w2i": "Regulowane światła RGB tworzą atmosferę i wskazują aktywny tryb.",
        "w2alt": "Aircelo przenośny — przenieś z pokoju do pokoju",
        "w3e": "03 — Cichy i wydajny",
        "w3h": "Ultrasrebrny tryb nocny i niskie zużycie energii",
        "w3t": ["Tryb Eco", "Tryb Nocny", "Niskie zużycie"],
        "w3p": "Działa tak dyskretnie, że <strong>nie przerywa snu</strong>. Tryby eco i nocny pozwalają trzymać go włączonego godzinami bez obaw o rachunek.",
        "w3i": "Instalacja w 2 minuty: bez rur, bez wiercenia i bez technika.",
        "w3alt": "Aircelo cichy tryb nocny w sypialni",
        "cmp_label": "Bezpośrednie porównanie",
        "cmp_h": "Tani wentylator vs Aircelo™",
        "cmp_th1": "Tani",
        "cmp_rows": [
            ("Funkcje", "Tylko wentylacja", "4 w 1: chłodzi, ogrzewa, osusza, wentyluje"),
            ("Instalacja", "Często skomplikowana", "2 minuty, bez rur"),
            ("Zasięg", "Mały pokój", "Do 90 m²"),
            ("Zużycie", "Wysokie przy długim użyciu", "Niskie, tryby Eco i Nocny"),
            ("Wyświetlacz", "Brak", "Cyfrowy z auto-off"),
            ("Filtry", "Zestaw podstawowy", "EPA + darmowy filtr antyzapachowy"),
        ],
        "rev_h": "Ponad 3000 zadowolonych klientów — oto co mówią!",
        "verified": "Zakup zweryfikowany",
        "reviews": [
            ("Dotarło w dwa dni!", "«Dotarło w dwa dni robocze. Miły sprzedawca, solidna firma i naprawdę świetny produkt. Szybko chłodzi!»", "Maria G. — Warszawa"),
            ("Łatwy w użyciu i mocny", "«Uwielbiam: szybko chłodzi i jest bardzo łatwy w obsłudze. Wyświetlacz cyfrowy pokazuje dokładną temperaturę.»", "Łukasz R. — Kraków"),
            ("Idealny do sypialni", "«Kupiłem do sypialni i jest idealny: w nocy prawie go nie słychać. Płatność przy odbiorze dała mi pewność.»", "Karol M. — Gdańsk"),
        ],
        "kit_eye": "Wszystko w zestawie",
        "kit_h": "📦 Twój zestaw Aircelo™ 4 w 1 zawiera:",
        "kit_alt": "Zawartość pudełka Aircelo",
        "kit_items": [
            "1× Klimatyzator kolumnowy Aircelo™ 4 w 1",
            "1× Pilot zdalnego sterowania",
            "1× Kabel zasilający",
            "1× Filtr wielokrotnego użytku (już zamontowany)",
            "1× DODATKOWY filtr antyzapachowy W PREZENCIE (wartość {filter_value})",
            "1× Instrukcja po polsku + szybki start",
            "Oficjalna gwarancja 24 miesiące + wsparcie po polsku",
            "Darmowa dostawa w 24/48 h w całej Polsce",
        ],
        "faq_h": "Często zadawane pytania",
        "faqs": [
            ("Czy mogę zapłacić przy odbiorze?", "Tak. Płacisz gotówką kurierowi przy odbiorze paczki — bez karty. Wysyłka w 24–48 h z kodem śledzenia SMS i e-mail."),
            ("Ile będę musiał zapłacić?", "Płacisz tylko <strong>{now}</strong> przy odbiorze — bez zaliczki i bez karty."),
            ("Jak wygląda instalacja?", "Bardzo prosto: wyjmij z pudełka, podłącz do gniazdka i w kilka minut jest gotowy. Bez rur, bez wiercenia i bez technika."),
            ("Jakie jest zużycie energii?", "Bardzo niskie. Dzięki trybom eco i nocnemu możesz trzymać go włączonego godzinami bez obaw o rachunek."),
            ("Czy jest cichy w nocy?", "Ma ultrasrebrny tryb nocny: możesz spać i pracować przy włączonym urządzeniu."),
            ("A jeśli mi się nie spodoba? Czy jest gwarancja?", "Masz 14 dni na zwrot z pełnym zwrotem pieniędzy. Każde urządzenie ma oficjalną 24-miesięczną gwarancję."),
        ],
        "footer_tag": "Przydatne produkty codziennego użytku, dostawa w 24–48 godzin z płatnością przy odbiorze.",
        "footer_info": "Informacje", "footer_about": "O nas", "footer_del": "Dostawa",
        "footer_ship": "Polityka wysyłki", "footer_refund": "Polityka zwrotów",
        "footer_home": "Strona główna", "footer_contact": "Kontakt",
        "footer_geo": "Polska", "footer_copy": "Wszelkie prawa zastrzeżone.",
        "submitting": "Wysyłanie...",
        "ty_title": "Zamówienie otrzymane — Poczekaj na telefon potwierdzający | Aircelo™",
        "ty_desc": "Twoje zamówienie Aircelo™ zostało zarejestrowane. Ostatni krok: odbierz telefon potwierdzający.",
        "ty_h": "Twoje zamówienie zostało zarejestrowane!",
        "ty_sub": "Świetnie — Twoje zamówienie Aircelo™ jest przetwarzane. Został tylko <strong>ostatni krok</strong> przed wysyłką.",
        "ty_eye": "👇 Co musisz zrobić teraz",
        "ty_act_h": "📞 Odbierz telefon potwierdzający",
        "ty_act_p": "Nasz operator skontaktuje się z Tobą <strong>w ciągu kilku godzin</strong>, aby potwierdzić zamówienie.",
        "ty_warn": "Jeśli nie odbierzesz telefonu, zamówienie zostanie automatycznie anulowane.",
        "ty_hours_h": "🕒 Godziny kontaktu",
        "ty_hours": "<strong>Poniedziałek – Sobota</strong> · 9:00 – 18:00",
        "ty_next_h": "📋 Co dalej",
        "ty_steps": [
            "Podczas rozmowy <strong>potwierdź swoje dane</strong>",
            "Zamówienie wysyłamy w ciągu <strong>24–48 godzin</strong>",
            "Dostawa do domu i płatność <strong>przy odbiorze</strong>",
        ],
        "ty_b1": "🔒 Płatność przy odbiorze",
        "ty_b2": "🛡️ 2 lata gwarancji",
        "ty_b3": "🔐 Chronione SSL",
        "ty_footer": "Informacje",
        "ty_about": "O nas", "ty_contact": "Kontakt",
        "ty_copy": "Wszelkie prawa zastrzeżone.",
    },
    "sk": {
        "title": "Aircelo™ — Stĺpcová klimatizácia 4 v 1 do 90 m² | -70%",
        "description": "Aircelo™: stĺpcová klimatizácia 4 v 1. Chladí, kúri, odvlhčuje a vetrá do 90 m². Digitálny displej, RGB svetlá a ultrasilentný nočný režim. Doprava zdarma a platba na dobierku.",
        "og_title": "Aircelo™ — Klimatizácia 4 v 1 | -70%",
        "og_desc": "Chladí, kúri, odvlhčuje a vetrá do 90 m². Bez hadíc, bez technika. Platba na dobierku.",
        "topbar": "🔥 ZĽAVA 70 % + DOPRAVA ZDARMA — PLATBA NA DOBIERKU 🔥",
        "rating": "<strong>4,8/5</strong> — na základe <strong>2 729+ overených recenzií</strong>",
        "gift": "2-ROČNÁ ZÁRUKA V CENE + EXTRA FILTER PROTI ZÁPACHU AKO DARČEK",
        "h1": "Prenosná klimatizácia — Ochlaďte alebo vykúrte celý dom za 5 minút <span class=\"hl\">so spotrebou len {hour_cost} za hodinu (Energetická trieda A+++)</span>",
        "lead": "<strong>Aircelo™</strong> odvlhčuje a vetrá okrem chladenia a kúrenia — všetko v jednom kompaktnom zariadení. Digitálny displej, RGB svetlá a ultrasilentný nočný režim na používanie počas spánku. Presuniete ho kamkoľvek v dome: bez hadíc, bez dier a bez technika.",
        "hero_alt": "Aircelo™ stĺpcová klimatizácia 4 v 1",
        "cta": "ÁNO, CHCEM Aircelo™ →",
        "form_note": "🔒 Bez zálohy · Bez karty · Platíte až po prevzatí",
        "f1h": "Doprava zdarma", "f1p": "Doručenie po celom Slovensku",
        "f2h": "Platba na dobierku", "f2p": "Karta nie je potrebná",
        "f3h": "2-ročná záruka", "f3p": "Kompletné krytie v cene",
        "f4h": "Vrátenie do 14 dní", "f4p": "Plná refundácia",
        "urgency": "⏰ Zľava 70 % končí o",
        "cd_h": "Hod.", "cd_m": "Min.", "cd_s": "Sek.",
        "stock_l": "Dostupnosť na sklade", "stock_r": "Zostávajú len 3 kusy",
        "live": "<strong>%n ľudí</strong> si práve prezerá túto klimatizáciu",
        "form_h": "Dokončite objednávku",
        "form_p": "Vyplňte formulár nižšie — náš tím vás kontaktuje na potvrdenie všetkých údajov.",
        "name_l": "Meno a priezvisko*", "name_ph": "Ján Novák",
        "phone_l": "Telefónne číslo*", "phone_ph": "+421 900 000 000",
        "addr_l": "Dodacia adresa*", "addr_ph": "Hlavná 1, 811 01 Bratislava",
        "submit": "ÁNO, CHCEM Aircelo™ →",
        "w1e": "01 — 4 funkcie v 1",
        "w1h": "Chlaďte, kúrte, odvlhčujte a vetrujte jedným prístrojom",
        "w1t": ["Chladí", "Kúri", "Odvlhčuje", "Vetrá"],
        "w1p": "Jeden kompaktný prístroj <strong>nahrádza štyri zariadenia</strong>: chladí v lete, kúri v zime, odvlhčuje v daždivé dni a vetrá celý rok.",
        "w1i": "Ideálne pre priestory do 90 m² — obývačku, spálňu a kanceláriu.",
        "w1alt": "Aircelo chladí a kúri za pár minút",
        "w2e": "02 — Presné ovládanie",
        "w2h": "Digitálny displej a automatické vypnutie pri nastavenej teplote",
        "w2t": ["LED displej", "Auto-off", "RGB svetlá"],
        "w2p": "<strong>Digitálny displej</strong> ukazuje presnú teplotu v reálnom čase. Nastavíte požadovanú hodnotu a prístroj sa automaticky vypne po jej dosiahnutí.",
        "w2i": "Nastaviteľné RGB svetlá vytvárajú atmosféru a ukazujú aktívny režim.",
        "w2alt": "Aircelo prenosný — preneste z izby do izby",
        "w3e": "03 — Tichý a úsporný",
        "w3h": "Ultrasilentný nočný režim a nízka spotreba energie",
        "w3t": ["Eco režim", "Nočný režim", "Nízka spotreba"],
        "w3p": "Funguje tak diskrétne, že <strong>neruší spánok</strong>. Režimy eco a noc umožňujú nechať ho zapnutý hodiny bez obáv o účet.",
        "w3i": "Inštalácia za 2 minúty: bez hadíc, bez dier a bez technika.",
        "w3alt": "Aircelo tichý nočný režim v spálni",
        "cmp_label": "Priame porovnanie",
        "cmp_h": "Lacný ventilátor vs Aircelo™",
        "cmp_th1": "Lacný",
        "cmp_rows": [
            ("Funkcie", "Len ventilácia", "4 v 1: chladí, kúri, odvlhčuje, vetrá"),
            ("Inštalácia", "Často zložitá", "2 minúty, bez hadíc"),
            ("Pokrytie", "Malá miestnosť", "Do 90 m²"),
            ("Spotreba", "Vysoká pri dlhom používaní", "Nízka, režimy Eco a Noc"),
            ("Displej", "Žiadny", "Digitálny s auto-off"),
            ("Filtre", "Základná sada", "EPA + filter proti zápachu zdarma"),
        ],
        "rev_h": "Viac ako 3 000 spokojných zákazníkov — toto hovoria!",
        "verified": "Overený nákup",
        "reviews": [
            ("Prišlo za dva dni!", "«Prišlo za dva pracovné dni. Príjemný predajca, spoľahlivá firma a naozaj výborný produkt. Rýchlo chladí!»", "Mária G. — Bratislava"),
            ("Jednoduché a výkonné", "«Milujem to: rýchlo chladí a je veľmi jednoduché na používanie. Digitálny displej ukazuje presnú teplotu.»", "Lukáš R. — Košice"),
            ("Perfektné do spálne", "«Kúpil som to do spálne a je perfektné: v noci ho takmer nepočuť. Platba na dobierku mi dala istotu.»", "Karol M. — Žilina"),
        ],
        "kit_eye": "Všetko v balení",
        "kit_h": "📦 Vaša sada Aircelo™ 4 v 1 obsahuje:",
        "kit_alt": "Obsah balenia Aircelo",
        "kit_items": [
            "1× Stĺpcová klimatizácia Aircelo™ 4 v 1",
            "1× Diaľkové ovládanie",
            "1× Napájací kábel",
            "1× Umývateľný opakovane použiteľný filter (už nainštalovaný)",
            "1× EXTRA filter proti zápachu AKO DARČEK (hodnota {filter_value})",
            "1× Manuál v slovenčine + rýchly návod",
            "Oficiálna 24-mesačná záruka + podpora v slovenčine",
            "Doprava zdarma do 24/48 h po celom Slovensku",
        ],
        "faq_h": "Často kladené otázky",
        "faqs": [
            ("Môžem platiť na dobierku?", "Áno. Platíte hotovosťou kuriérovi pri prevzatí balíka — bez karty. Odoslanie do 24–48 h s kódom sledovania SMS a e-mailom."),
            ("Koľko budem platiť?", "Platíte iba <strong>{now}</strong> na dobierku — bez zálohy a bez karty."),
            ("Ako prebieha inštalácia?", "Veľmi jednoducho: vyberte z krabice, zapojte do zásuvky a o pár minút je pripravené. Bez hadíc, bez dier a bez technika."),
            ("Aká je spotreba energie?", "Veľmi nízka. Vďaka režimom eco a noc ho môžete nechať zapnutý hodiny bez obáv o účet."),
            ("Je tiché v noci?", "Má ultrasilentný nočný režim: môžete spať a pracovať so zapnutým prístrojom."),
            ("A čo ak sa mi nebude páčiť? Je záruka?", "Máte 14 dní na vrátenie s plnou refundáciou. Každý prístroj má oficiálnu 24-mesačnú záruku."),
        ],
        "footer_tag": "Užitočné produkty na každý deň, doručenie do 24–48 hodín s platbou na dobierku.",
        "footer_info": "Informácie", "footer_about": "O nás", "footer_del": "Doručenie",
        "footer_ship": "Zásady dopravy", "footer_refund": "Zásady vrátenia",
        "footer_home": "Domov", "footer_contact": "Kontaktujte nás",
        "footer_geo": "Slovensko", "footer_copy": "Všetky práva vyhradené.",
        "submitting": "Odosiela sa...",
        "ty_title": "Objednávka prijatá — Počkajte na potvrdzovací hovor | Aircelo™",
        "ty_desc": "Vaša objednávka Aircelo™ bola zaregistrovaná. Posledný krok: prijmite potvrdzovací hovor.",
        "ty_h": "Vaša objednávka bola zaregistrovaná!",
        "ty_sub": "Skvelé — vaša objednávka Aircelo™ sa spracováva. Zostáva len <strong>posledný krok</strong> pred odoslaním.",
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
            "Doručenie domov a <strong>platba na dobierku</strong>",
        ],
        "ty_b1": "🔒 Platba na dobierku",
        "ty_b2": "🛡️ 2-ročná záruka",
        "ty_b3": "🔐 SSL ochrana",
        "ty_footer": "Informácie",
        "ty_about": "O nás", "ty_contact": "Kontakt",
        "ty_copy": "Všetky práva vyhradené.",
    },
}


def fmt(text: str, g: dict) -> str:
    return text.format(
        hour_cost=g["hour_cost"],
        filter_value=g["filter_value"],
        now=g["now"],
        was=g["was"],
    )


def tags_html(tags: list[str]) -> str:
    return "".join(f'<span class="tag">{t}</span>' for t in tags)


def cmp_rows_html(rows: list[tuple[str, str, str]]) -> str:
    out = []
    for label, cheap, win in rows:
        out.append(
            f"    <tr><td>{label}</td><td>{cheap}</td><td class=\"win\">{win}</td></tr>"
        )
    return "\n".join(out)


def reviews_html(tr: dict) -> str:
    parts = []
    for i, (title, quote, author) in enumerate(tr["reviews"], 1):
        parts.append(
            f"""      <div class="testimonial">
        <img decoding="async" class="t-photo" src="/assets/img/reviews/aircelo/review-{i}.png?v=3" alt="{author}" loading="lazy" onerror="this.src='/assets/img/placeholder.svg'">
        <div class="t-body">
          <div class="stars">★★★★★</div>
          <h4>{title}</h4>
          <p>{quote}</p>
          <div class="author-row"><div class="author">{author}, {tr['verified']}</div></div>
        </div>
      </div>"""
        )
    return "\n".join(parts)


def kit_items_html(items: list[str], g: dict) -> str:
    return "\n".join(f"        <li>{fmt(item, g)}</li>" for item in items)


def faq_html(tr: dict, g: dict) -> str:
    parts = []
    for q, a in tr["faqs"]:
        parts.append(
            f"""  <div class="faq-item"><button class="faq-q" type="button"><span>{q}</span><span class="arrow">▾</span></button>
    <div class="faq-a"><p>{fmt(a, g)}</p></div></div>"""
        )
    return "\n".join(parts)


def landing_html(g: dict, tr: dict) -> str:
    geo, lang, offer = g["geo"], g["lang"], g["offer"]
    price = g["price"]
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
<link rel="canonical" href="https://powercurvemedia.com/{geo}/aircelo/{offer}/">
<meta property="og:type" content="product">
<meta property="og:title" content="{tr['og_title']}">
<meta property="og:description" content="{tr['og_desc']}">
<meta property="og:image" content="https://powercurvemedia.com/assets/img/products/aircelo/hero.png?v=2">
<meta property="og:url" content="https://powercurvemedia.com/{geo}/aircelo/{offer}/">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/climaone-landing.css">
<style>
.compare{{background:linear-gradient(180deg,#f0f4f8 0%,#e8eef4 100%);padding:36px 0}}
.compare .compare__inner{{max-width:var(--max-width);margin:0 auto;padding:0 var(--gutter);text-align:center}}
.compare table{{margin:0 auto;max-width:680px;width:100%;background:#fff;box-shadow:0 10px 32px rgba(20,24,31,.08)}}
.compare th,.compare td{{padding:14px 12px;vertical-align:middle;text-align:center}}
.compare th:first-child,.compare td:first-child{{text-align:left}}
.compare th.highlight,.compare td.win{{background:#ecfdf5}}
.compare th.highlight{{color:#047857}}
.compare tr:nth-child(even) td:not(.win){{background:#fafbfc}}
.compare tr:nth-child(even) td.win{{background:#d1fae5}}
@media (max-width:959px){{
  .hero-image{{aspect-ratio:1/1}}
  .hero-image img,.hero-image video{{width:100%;height:100%;object-fit:cover;object-position:center}}
  .why-img{{aspect-ratio:1/1;border-radius:var(--radius-lg);overflow:hidden}}
  .why-img img,.why-img video{{width:100%;height:100%;object-fit:cover;object-position:center;border-radius:0;display:block}}
  .kit-box>img{{aspect-ratio:1/1;width:100%;object-fit:cover;object-position:center}}
  .testimonial .t-photo{{aspect-ratio:1/1;object-fit:cover;object-position:center}}
}}
</style>
<script>
window.SITE_CONFIG = {{
  GEO: '{geo}',
  PRODUCT_SLUG: 'aircelo/{offer}',
  CURRENCY: '{g['currency']}',
  PRICE: {price},
  OFFER_NAME: 'Aircelo {offer} {geo.upper()}',
  LP_ID: '{geo}-aircelo-{offer}',
  FORM_ENDPOINT: 'https://TODO-network-endpoint.com/api/lead',
  SUBMITTING_LABEL: '{tr['submitting']}',
  LIVE_WATCHING_TEMPLATE: '{tr['live']}'
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
    <h1>{fmt(tr['h1'], g)}</h1>
    <p class="lead">{tr['lead']}</p>
    <div class="hero-image hero-image-mobile-only">
      <img decoding="async" src="/assets/img/products/aircelo/hero.png?v=2" alt="{tr['hero_alt']}" width="560" height="560" loading="eager" fetchpriority="high" onerror="this.src='/assets/img/placeholder.svg'">
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
    <img decoding="async" src="/assets/img/products/aircelo/hero.png?v=2" alt="{tr['hero_alt']}" width="560" height="560" loading="eager" fetchpriority="high" onerror="this.src='/assets/img/placeholder.svg'">
  </div>
</section>

<div class="wrap">
  <div class="feature-row">
    <div class="feature-item"><div class="ico">🚚</div><h4>{tr['f1h']}</h4><p>{tr['f1p']}</p></div>
    <div class="feature-item"><div class="ico">💳</div><h4>{tr['f2h']}</h4><p>{tr['f2p']}</p></div>
    <div class="feature-item"><div class="ico">🛡️</div><h4>{tr['f3h']}</h4><p>{tr['f3p']}</p></div>
    <div class="feature-item"><div class="ico">↩️</div><h4>{tr['f4h']}</h4><p>{tr['f4p']}</p></div>
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
        <div class="stock-bar"><div class="stock-bar-fill" style="width:92%"></div></div>
      </div>
      <div class="live-row">
        <span class="dot"></span>
        <span id="liveCount">{tr['live'].replace('%n', '16')}</span>
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
    <div class="why-img"><img decoding="async" src="/assets/img/products/aircelo/desc-1.png?v=2" alt="{tr['w1alt']}" loading="lazy" onerror="this.src='/assets/img/placeholder.svg'"></div>
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
    <div class="why-img"><img decoding="async" src="/assets/img/products/aircelo/desc-2.png?v=2" alt="{tr['w2alt']}" loading="lazy" onerror="this.src='/assets/img/placeholder.svg'"></div>
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
    <div class="why-img"><img decoding="async" src="/assets/img/products/aircelo/desc-3.png?v=2" alt="{tr['w3alt']}" loading="lazy" onerror="this.src='/assets/img/placeholder.svg'"></div>
    <div>
      <div class="num-eyebrow">{tr['w3e']}</div>
      <h3>{tr['w3h']}</h3>
      <div class="tag-row">{tags_html(tr['w3t'])}</div>
      <p>{tr['w3p']}</p>
      <p class="italic">{tr['w3i']}</p>
    </div>
  </div>
</section>

<section class="compare">
  <div class="compare__inner">
  <div class="section-label">{tr['cmp_label']}</div>
  <h2>{tr['cmp_h']}</h2>
  <table>
    <tr><th></th><th>{tr['cmp_th1']}</th><th class="highlight">Aircelo™</th></tr>
{cmp_rows_html(tr['cmp_rows'])}
  </table>
  </div>
</section>

<section class="testimonials">
  <div class="wrap">
    <div class="section-heading">
      <h2>{tr['rev_h']}</h2>
    </div>
    <div class="t-grid">
{reviews_html(tr)}
    </div>
  </div>
</section>

<section class="kit-section wrap">
  <div class="section-heading">
    <span class="eyebrow">{tr['kit_eye']}</span>
    <h2>{tr['kit_h']}</h2>
  </div>
  <div class="kit-box">
    <img decoding="async" src="/assets/img/products/aircelo/kit.png?v=2" alt="{tr['kit_alt']}" loading="lazy" onerror="this.src='/assets/img/placeholder.svg'">
    <div class="kit-content">
      <div class="price-block" style="margin-bottom:16px;">
        <span class="was">{g['was']}</span>
        <span class="now">{g['now']}</span>
        <span class="pct">-70%</span>
      </div>
      <ul>
{kit_items_html(tr['kit_items'], g)}
      </ul>
      <a href="#order-form" class="cta-btn">{tr['cta']}</a>
    </div>
  </div>
</section>

<section class="faq wrap">
  <div class="section-heading"><h2>{tr['faq_h']}</h2></div>
{faq_html(tr, g)}
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
        <li><a href="/{geo}/">{tr['footer_geo']}</a></li>
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

<script src="/assets/js/aircelo-landing.js" defer></script>
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
    cpa = g["cpa"]
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
  PRODUCT_SLUG: 'aircelo/{offer}',
  OFFER_NAME: 'Aircelo {offer} {geo.upper()}',
  LP_ID: '{geo}-aircelo-{offer}',
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
  <h1 class="ty-headline">{tr['ty_h']}</h1>
  <p class="ty-subhead">{tr['ty_sub']}</p>

  <figure class="ty-hero">
    <img src="/assets/img/site/thank_you_draftin.png" alt="powercurvemedia" width="2848" height="1331" loading="lazy" decoding="async" onerror="this.src='/assets/img/placeholder.svg'">
  </figure>

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
    <div class="ty-box__body">
      <ol class="ty-steps-list">
{steps}
      </ol>
    </div>
  </section>

  <div class="ty-trust">
    <span class="ty-trust__badge">{tr['ty_b1']}</span>
    <span class="ty-trust__badge">{tr['ty_b2']}</span>
    <span class="ty-trust__badge">{tr['ty_b3']}</span>
  </div>
</main>

<footer class="ty-footer">
  <div class="wrap">
    <h3 style="color:#fff;font-size:13px;margin-bottom:8px;">{tr['ty_footer']}</h3>
    <ul>
      <li><a href="/{geo}/about-us.html">{tr['ty_about']}</a></li>
      <li><a href="/{geo}/contact-us.html">{tr['ty_contact']}</a></li>
      <li><a href="/{geo}/privacy-policy.html">Privacy Policy</a></li>
      <li><a href="/{geo}/terms-conditions.html">Terms</a></li>
      <li><a href="/{geo}/cookie-policy.html">Cookie Policy</a></li>
      <li><a href="/{geo}/shipping-policy.html">{tr['footer_ship']}</a></li>
      <li><a href="/{geo}/refund-policy.html">{tr['footer_refund']}</a></li>
    </ul>
    <p class="ty-footer__copy">© 2026 <strong>Global Health Distribution S.r.l.</strong> — {tr['ty_copy']}</p>
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
      'send_to': 'AW-18294109732/3Pa8COOx7dUcEOv3tatE',
      'value': {cpa},
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


def redirect_html(geo: str, offer: str, lang: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<title>Redirect…</title>
<link rel="canonical" href="https://powercurvemedia.com/{geo}/aircelo/{offer}/">
<script>window.location.replace('/{geo}/aircelo/{offer}/' + window.location.search + window.location.hash);</script>
<meta http-equiv="refresh" content="0;url=/{geo}/aircelo/{offer}/">
</head>
<body><p><a href="/{geo}/aircelo/{offer}/">Aircelo™</a></p></body>
</html>
"""


def main() -> None:
    for g in GEOS:
        geo = g["geo"]
        offer = g["offer"]
        tr = T[geo]
        out_dir = ROOT / geo / "aircelo" / offer
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "index.html").write_text(landing_html(g, tr), encoding="utf-8")
        (out_dir / "thank-you.html").write_text(thankyou_html(g, tr), encoding="utf-8")

        parent = ROOT / geo / "aircelo"
        parent.mkdir(parents=True, exist_ok=True)
        (parent / "index.html").write_text(redirect_html(geo, offer, g["lang"]), encoding="utf-8")
        (parent / "landing.html").write_text(redirect_html(geo, offer, g["lang"]), encoding="utf-8")
        print(f"Generated {out_dir}")

    # Sitemap entries
    sitemap = ROOT / "sitemap.xml"
    text = sitemap.read_text(encoding="utf-8")
    marker = "  <url><loc>https://powercurvemedia.com/it/aircelo/</loc>"
    if "aircelo/311" not in text and marker in text:
        entries = []
        for g in GEOS:
            entries.append(
                f"  <url><loc>https://powercurvemedia.com/{g['geo']}/aircelo/{g['offer']}/</loc>"
                f"<lastmod>2026-08-08</lastmod><changefreq>weekly</changefreq><priority>0.95</priority></url>"
            )
        insert = "\n".join(entries) + "\n"
        # Insert after IT aircelo line
        idx = text.find(marker)
        end = text.find("\n", idx)
        text = text[: end + 1] + insert + text[end + 1 :]
        sitemap.write_text(text, encoding="utf-8")
        print("Updated sitemap.xml")


if __name__ == "__main__":
    main()
