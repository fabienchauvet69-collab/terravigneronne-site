"""Génère les pages statiques du site Terra Vigneronne (en-tête et pied communs)."""
import json
import pathlib
import sys

OUT = pathlib.Path(sys.argv[1])
BASE = "https://terravigneronne.com"
LOGO = "https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=240,fit=crop/zTo0Ltb35tv1lQDR/chatgpt-image-29-mai-2026-10_59_16-1-GHMG8awh0hkYMXge.png"
HERO = "https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=1920,fit=crop/zTo0Ltb35tv1lQDR/xp7qb0-ebW5w7hSgJzZCR1R.png"
PHONE = "07 49 10 83 09"
PHONE_INTL = "+33749108309"
EMAIL = "contact@terravigneronne.com"
WHATSAPP = "https://wa.me/message/CX5Z723TUZDWL1"

NAV = [
    ("/", "Accueil"),
    ("/tarifs-offres", "Services & tarifs"),
    ("/qui-sommes-nous", "Qui sommes-nous"),
]

ICONS = {
    "key": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="7.5" cy="15.5" r="4.5"/><path d="m10.7 12.3 9.3-9.3M16 7l3 3M19 4l2 2"/></svg>',
    "clean": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 21h18M6 21V10l6-6 6 6v11"/><path d="M10 21v-5h4v5"/></svg>',
    "linen": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="12" cy="13" r="4"/><path d="M7 7h.01M10 7h.01"/></svg>',
    "eye": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></svg>',
    "tool": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z"/></svg>',
    "camera": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 7h3l2-3h6l2 3h3a1 1 0 0 1 1 1v11a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V8a1 1 0 0 1 1-1z"/><circle cx="12" cy="13" r="4"/></svg>',
}

LOCAL_BUSINESS = {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "@id": BASE + "/#entreprise",
    "name": "Terra Vigneronne – Conciergerie à Pézenas",
    "description": "Conciergerie et intendance de logements à Pézenas : accueil des voyageurs, ménage, linge, suivi et entretien de résidences secondaires et de locations saisonnières.",
    "url": BASE + "/",
    "logo": LOGO,
    "image": HERO,
    "telephone": PHONE_INTL,
    "email": EMAIL,
    "priceRange": "€€",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "7 rue Henri Reboul",
        "postalCode": "34120",
        "addressLocality": "Pézenas",
        "addressRegion": "Occitanie",
        "addressCountry": "FR",
    },
    "areaServed": {"@type": "City", "name": "Pézenas"},
    "sameAs": [
        "https://www.instagram.com/terravigneronne",
        "https://www.facebook.com/profile.php?id=61590410080492",
    ],
    "legalName": "SOGEQ",
    "vatID": "FR31993443225",
}


def head(title, description, path, extra_ld=None, noindex=False):
    lds = [LOCAL_BUSINESS] + (extra_ld or [])
    ld = "\n".join(
        '<script type="application/ld+json">' + json.dumps(x, ensure_ascii=False) + "</script>" for x in lds
    )
    robots = '<meta name="robots" content="noindex">' if noindex else ""
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
{robots}
<link rel="canonical" href="{BASE}{path}">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/assets/fonts/montserrat-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/style.css">
<meta name="theme-color" content="#33424e">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="Terra Vigneronne">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{BASE}{path}">
<meta property="og:image" content="{HERO}">
<meta name="twitter:card" content="summary_large_image">
{ld}
</head>
<body>
<a class="skip" href="#contenu">Aller au contenu</a>
"""


def header(current):
    items = "".join(
        f'<li><a href="{href}"{" aria-current=\"page\"" if href == current else ""}>{label}</a></li>' for href, label in NAV
    )
    return f"""<header class="site-header">
  <div class="wrap">
    <a class="brand" href="/" aria-label="Terra Vigneronne, retour à l'accueil">
      <img src="{LOGO}" alt="Logo Terra Vigneronne" width="56" height="56">
      <span class="brand-text"><strong>Terra Vigneronne</strong><span>Conciergerie · Pézenas</span></span>
    </a>
    <nav class="nav" aria-label="Menu principal">
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="menu">Menu</button>
      <ul id="menu">
        {items}
        <li><a class="btn" href="/contact"{" aria-current=\"page\"" if current == "/contact" else ""}>Demander un devis</a></li>
      </ul>
    </nav>
  </div>
</header>
<main id="contenu">
"""


FOOTER = f"""</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <h4>Terra Vigneronne</h4>
        <p>Conciergerie et intendance de logements à Pézenas et alentours.</p>
        <p>7 rue Henri Reboul<br>34120 Pézenas</p>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><a href="tel:{PHONE_INTL}">{PHONE}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="{WHATSAPP}" rel="noopener">WhatsApp</a></li>
        </ul>
      </div>
      <div>
        <h4>Le site</h4>
        <ul>
          <li><a href="/tarifs-offres">Services & tarifs</a></li>
          <li><a href="/qui-sommes-nous">Qui sommes-nous</a></li>
          <li><a href="/contact">Contact & devis</a></li>
        </ul>
      </div>
      <div>
        <h4>Suivez-nous</h4>
        <ul>
          <li><a href="https://www.instagram.com/terravigneronne" rel="noopener">Instagram</a></li>
          <li><a href="https://www.facebook.com/profile.php?id=61590410080492" rel="noopener">Facebook</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Terra Vigneronne · SOGEQ SASU · RCS Béziers 993 443 225</span>
      <span><a href="/mentions-legales">Mentions légales</a> · <a href="/cgv">CGV</a> · <a href="/politique-de-confidentialite">Confidentialité</a></span>
    </div>
  </div>
</footer>
<script src="/assets/site.js" defer></script>
</body>
</html>
"""

CTA = """<section class="cta">
  <div class="wrap">
    <div>
      <h2>Parlons de votre logement</h2>
      <p>Visite du bien et devis gratuits, à Pézenas et alentours.</p>
    </div>
    <a class="btn" href="/contact">Demander un devis</a>
  </div>
</section>
"""


def page(name, path, title, description, body, extra_ld=None, noindex=False):
    html = head(title, description, path, extra_ld, noindex) + header(path) + body + FOOTER
    (OUT / name).write_text(html, encoding="utf-8")


def card(icon, title, price, text):
    price_html = f'<p class="price">{price}</p>' if price else ""
    return f'<div class="card"><div class="icon">{ICONS[icon]}</div><h3>{title}</h3>{price_html}<p>{text}</p></div>'


# ---------------------------------------------------------------- Accueil
FAQ = [
    ("Que comprend l'abonnement à 39 € par mois ?",
     "Le suivi de votre logement, l'assistance au propriétaire, la gestion des demandes de vos voyageurs, notre disponibilité et nos conseils personnalisés. Les interventions sur place (accueil, ménage, linge…) sont facturées à l'acte, selon la grille de tarifs."),
    ("Gérez-vous mes annonces Airbnb ou Booking ?",
     "Non. Vous gardez la main sur vos annonces, vos prix et vos réservations. Nous prenons en charge tout ce qui se passe sur place : arrivées, départs, ménage, linge, contrôle du logement et coordination des artisans."),
    ("Je n'ai pas de location saisonnière, juste une résidence secondaire. Est-ce pour moi ?",
     "Oui. Notre formule d'intendance de résidence secondaire couvre les visites régulières, l'aération, la gestion du courrier, la vérification après intempéries et la préparation du logement avant votre arrivée. Elle est établie sur devis."),
    ("Dans quelles communes intervenez-vous ?",
     "Nous sommes installés à Pézenas et intervenons à Pézenas et dans les communes alentour. Indiquez-nous l'adresse de votre logement : nous vous confirmons tout de suite si nous pouvons nous en occuper."),
    ("Comment se passe le démarrage ?",
     "Nous visitons le logement avec vous, nous convenons des prestations dont vous avez besoin et nous vous remettons un devis écrit. Vous ne payez ensuite que les interventions réellement réalisées, en plus de l'abonnement."),
]

faq_ld = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ
    ],
}
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ)

home = f"""
<section class="hero" style="background-image:url('{HERO}')">
  <div class="wrap">
    <span class="eyebrow">Conciergerie de logements · Pézenas</span>
    <h1>Votre logement à Pézenas, entretenu et prêt à accueillir, sans vous déplacer</h1>
    <p class="lead">Location saisonnière ou résidence secondaire : nous accueillons vos voyageurs, faisons le ménage, gérons le linge et veillons sur votre bien. Abonnement à partir de 39 € TTC par mois, puis vous ne payez que ce qui est fait.</p>
    <div class="actions">
      <a class="btn" href="/contact">Demander un devis gratuit</a>
      <a class="btn btn-ghost" href="/tarifs-offres">Voir les tarifs</a>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow" style="color:var(--orange-dark)">Ce que nous faisons</span>
      <h2>Tout ce qui se passe sur place, on s'en charge</h2>
      <p>Vous gardez vos annonces, vos prix et vos réservations. Nous assurons le terrain, avec le niveau d'exigence de l'hôtellerie haut de gamme.</p>
    </div>
    <div class="grid g3">
      {card("key", "Accueil et départ des voyageurs", "À partir de 35 €", "Remise des clés, présentation du logement, puis état des lieux au départ avec compte rendu en cas d'anomalie.")}
      {card("clean", "Ménage professionnel", "À partir de 60 €", "Nettoyage complet entre deux séjours : sols, cuisine, sanitaires, chambres et remise en ambiance du logement.")}
      {card("linen", "Gestion du linge", "À partir de 25 €", "Récupération, blanchisserie, remplacement et préparation des lits avec un contrôle qualité du linge.")}
      {card("eye", "Intendance de résidence secondaire", "Sur devis", "Visites régulières, aération, courrier, vérification après intempéries et préparation avant votre arrivée.")}
      {card("tool", "Coordination des artisans", "À partir de 45 €", "Prise de rendez-vous, accueil et suivi des interventions : plomberie, électricité, climatisation, jardin, piscine.")}
      {card("camera", "Photos de votre logement", "À partir de 120 €", "Des photos intérieures et extérieures soignées pour présenter votre bien sous son meilleur jour.")}
    </div>
    <p style="margin-top:32px"><a class="btn btn-line" href="/tarifs-offres">Le détail de chaque prestation</a></p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow" style="color:var(--orange-dark)">Comment ça marche</span>
      <h2>Trois étapes, sans engagement de volume</h2>
    </div>
    <div class="grid g3 steps">
      <div class="step"><h3>On visite votre bien</h3><p>Nous venons voir le logement avec vous, à Pézenas ou alentour, et notons vos attentes : accès, équipements, linge, fréquence des séjours.</p></div>
      <div class="step"><h3>Vous choisissez vos prestations</h3><p>Un abonnement à partir de 39 € par mois, puis les interventions dont vous avez besoin, au tarif affiché. Devis écrit avant de commencer.</p></div>
      <div class="step"><h3>On s'occupe du reste</h3><p>Nous intervenons à chaque séjour ou à chaque visite et vous tenons informé, avec un compte rendu en cas d'anomalie.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap split">
    <div>
      <span class="eyebrow" style="color:var(--orange-dark)">Pourquoi nous</span>
      <h2>Une conciergerie installée à Pézenas</h2>
      <ul class="checks">
        <li><strong>Sur place.</strong> Nos bureaux sont au 7 rue Henri Reboul, en plein Pézenas : nous connaissons les rues, les accès et les artisans du secteur.</li>
        <li><strong>Des standards hôteliers.</strong> La conciergerie a été fondée par un professionnel de l'hôtellerie de luxe, formé en Suisse.</li>
        <li><strong>Des prix lisibles.</strong> Un abonnement bas, une grille de tarifs publique, et vous ne payez que ce qui est réellement fait.</li>
        <li><strong>Vous restez maître de votre bien.</strong> Pas de mandat de gestion locative : vos annonces, vos prix et vos revenus restent les vôtres.</li>
      </ul>
      <p><a href="/qui-sommes-nous">En savoir plus sur Terra Vigneronne</a></p>
    </div>
    <div class="offer" style="grid-template-columns:1fr">
      <div>
        <h3>Abonnement propriétaire</h3>
        <p class="amount">39 € <small>TTC / mois, à partir de</small></p>
      </div>
      <ul class="checks">
        <li>Suivi de votre logement</li>
        <li>Assistance propriétaire</li>
        <li>Gestion des demandes de vos voyageurs</li>
        <li>Support et disponibilité</li>
        <li>Conseils personnalisés</li>
      </ul>
      <a class="btn" href="/contact">Demander un devis</a>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow" style="color:var(--orange-dark)">Questions fréquentes</span>
      <h2>Ce qu'on nous demande le plus</h2>
    </div>
    <div class="prose" style="max-width:860px">{faq_html}</div>
  </div>
</section>
{CTA}"""

page(
    "index.html", "/",
    "Conciergerie à Pézenas : ménage, accueil voyageurs, intendance | Terra Vigneronne",
    "Conciergerie à Pézenas (Hérault) pour locations saisonnières et résidences secondaires : accueil des voyageurs, ménage, linge, suivi du logement. Dès 39 € TTC/mois.",
    home, [faq_ld],
)

# ---------------------------------------------------------------- Tarifs
RATES = [
    ("Accueil des voyageurs (check-in)", "Remise des clés, présentation du logement et des équipements, aide à l'installation, recommandations locales. Accueil en personne ou arrivée autonome sécurisée, selon vos besoins.", "dès 35 €"),
    ("Départ et contrôle du logement (check-out)", "Récupération des clés, vérification de la propreté, des équipements et des installations, aération, fermeture sécurisée, signalement des dommages, oublis ou anomalies, compte rendu si nécessaire.", "dès 35 €"),
    ("Ménage professionnel", "Sols et surfaces, désinfection de la cuisine et de la salle de bain, sanitaires, préparation des chambres, contrôle général et remise en ambiance. Ménage renforcé ou de fin de saison possible. Tarif selon la taille du logement.", "dès 60 €"),
    ("Gestion du linge", "Récupération du linge utilisé, lavage et blanchisserie, remplacement, préparation des lits, contrôle qualité. Draps, serviettes, tapis de bain, linge de piscine ou de plage.", "dès 25 €"),
    ("Courses avant arrivée", "Installation dans le logement des courses commandées : produits alimentaires, boissons, produits locaux, petit-déjeuner, produits pour bébé. Pratique pour les arrivées tardives.", "dès 25 € + achats"),
    ("Coordination maintenance et artisans", "Prise de rendez-vous, accueil des artisans, suivi et contrôle après intervention, compte rendu. Plomberie, électricité, climatisation, jardin, piscine, serrurerie, petites réparations.", "dès 45 €"),
    ("Photos du logement", "Photos intérieures et extérieures, mise en valeur des espaces, travail de la lumière, conseils de présentation et de décoration.", "dès 120 €"),
    ("Intendance de résidence secondaire", "Visites régulières, aération, contrôle intérieur et extérieur, courrier, coordination des prestataires, préparation avant votre arrivée, vérification après intempéries ou longue absence.", "sur devis"),
]
rows = "".join(
    f"<tr><td><strong>{n}</strong><span>{d}</span></td><td>{p}</td></tr>" for n, d, p in RATES
)
offer_ld = {
    "@context": "https://schema.org",
    "@type": "OfferCatalog",
    "name": "Prestations de conciergerie Terra Vigneronne",
    "itemListElement": [
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Abonnement propriétaire"},
         "priceSpecification": {"@type": "UnitPriceSpecification", "price": 39, "priceCurrency": "EUR", "unitText": "mois"}}
    ] + [
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n, "description": d}} for n, d, _ in RATES
    ],
}

tarifs = f"""
<section class="page-hero">
  <div class="wrap">
    <span class="eyebrow">Services & tarifs</span>
    <h1>Tarifs de conciergerie à Pézenas</h1>
    <p>Un abonnement mensuel pour le suivi de votre logement, puis chaque intervention au prix affiché. Pas de commission sur vos loyers.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="offer">
      <div>
        <span class="eyebrow">Formule propriétaire</span>
        <h2>Abonnement</h2>
        <p class="amount">39 € <small>TTC / mois, à partir de</small></p>
        <p style="color:#dfe5ea;margin-top:14px">Un accompagnement permanent, et vous ne payez que les prestations réellement réalisées.</p>
      </div>
      <div>
        <h3>L'abonnement comprend</h3>
        <ul class="checks">
          <li>Suivi de votre logement</li>
          <li>Assistance propriétaire</li>
          <li>Gestion des demandes de vos voyageurs</li>
          <li>Support et disponibilité</li>
          <li>Conseils personnalisés</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="alt" style="padding-top:0;background:linear-gradient(var(--white) 0,var(--white) 40px,var(--sand) 40px)">
  <div class="wrap">
    <div class="section-head" style="padding-top:72px">
      <h2>Prestations à la carte</h2>
      <p>Prix TTC, en euros. Ce sont des prix de départ, ajustés selon la taille et la configuration du logement. Vous recevez un devis écrit avant toute intervention.</p>
    </div>
    <table class="rates">
      <thead><tr><th>Prestation</th><th>Tarif</th></tr></thead>
      <tbody>{rows}</tbody>
    </table>
    <p class="note" style="margin-top:18px">Besoin d'une prestation qui n'apparaît pas ici ? Décrivez-la nous : nous vous faisons une proposition sur mesure.</p>
  </div>
</section>
{CTA}"""

page(
    "tarifs-offres.html", "/tarifs-offres",
    "Tarifs conciergerie Pézenas : abonnement dès 39 €/mois | Terra Vigneronne",
    "Tarifs de conciergerie à Pézenas : abonnement propriétaire dès 39 € TTC/mois, accueil voyageurs dès 35 €, ménage dès 60 €, linge dès 25 €. Devis gratuit.",
    tarifs, [offer_ld],
)

# ---------------------------------------------------------------- Qui sommes-nous
about = f"""
<section class="page-hero">
  <div class="wrap">
    <span class="eyebrow">Qui sommes-nous</span>
    <h1>Une conciergerie de Pézenas, aux standards de l'hôtellerie</h1>
    <p>Terra Vigneronne prend soin des logements de propriétaires qui ne peuvent pas être sur place, à Pézenas et alentour.</p>
  </div>
</section>

<section>
  <div class="wrap split">
    <div class="prose">
      <h2 style="margin-top:0">Notre histoire</h2>
      <p>Terra Vigneronne est une conciergerie installée à Pézenas, au 7 rue Henri Reboul. Elle a été fondée par un professionnel issu de l'hôtellerie de luxe, formé en Suisse, qui a voulu appliquer aux maisons et appartements de la région le niveau d'exigence d'un grand hôtel.</p>
      <p>Notre métier est simple : être sur place quand vous ne pouvez pas l'être. Accueillir vos voyageurs, préparer et contrôler le logement, gérer le linge, coordonner les artisans et veiller sur les résidences secondaires, toute l'année.</p>
      <h2>Notre façon de travailler</h2>
      <ul class="checks">
        <li>Un interlocuteur unique, joignable par téléphone, e-mail ou WhatsApp.</li>
        <li>Des tarifs publics, et un devis écrit avant toute intervention.</li>
        <li>Un compte rendu dès qu'une anomalie est constatée dans le logement.</li>
        <li>Le soin du détail : chaque logement est préparé comme une chambre d'hôtel.</li>
      </ul>
    </div>
    <div class="card" style="background:var(--sand)">
      <h3>Nous rencontrer</h3>
      <ul class="contact-list">
        <li><strong>Adresse</strong>7 rue Henri Reboul, 34120 Pézenas</li>
        <li><strong>Téléphone</strong><a href="tel:{PHONE_INTL}">{PHONE}</a></li>
        <li><strong>E-mail</strong><a href="mailto:{EMAIL}">{EMAIL}</a></li>
      </ul>
      <a class="btn" href="/contact">Prendre rendez-vous</a>
    </div>
  </div>
</section>
{CTA}"""

page(
    "qui-sommes-nous.html", "/qui-sommes-nous",
    "Qui sommes-nous ? Conciergerie installée à Pézenas | Terra Vigneronne",
    "Terra Vigneronne, conciergerie installée 7 rue Henri Reboul à Pézenas, fondée par un professionnel de l'hôtellerie de luxe formé en Suisse.",
    about,
)

# ---------------------------------------------------------------- Contact
contact = f"""
<section class="page-hero">
  <div class="wrap">
    <span class="eyebrow">Contact & devis</span>
    <h1>Demandez votre devis de conciergerie</h1>
    <p>Décrivez votre logement et vos besoins : nous revenons vers vous pour organiser une visite, gratuite et sans engagement.</p>
  </div>
</section>

<section>
  <div class="wrap split" style="align-items:start">
    <div>
      <div id="form-status" role="status" hidden></div>
      <form action="/envoi.php" method="post">
        <div class="row">
          <div class="field"><label for="nom">Nom et prénom *</label><input id="nom" name="nom" autocomplete="name" required maxlength="120"></div>
          <div class="field"><label for="tel">Téléphone</label><input id="tel" name="tel" type="tel" autocomplete="tel" maxlength="30"></div>
        </div>
        <div class="field"><label for="email">E-mail *</label><input id="email" name="email" type="email" autocomplete="email" required maxlength="160"></div>
        <div class="row">
          <div class="field"><label for="type">Type de logement</label>
            <select id="type" name="type">
              <option>Location saisonnière</option>
              <option>Résidence secondaire</option>
              <option>Autre</option>
            </select></div>
          <div class="field"><label for="commune">Commune du logement</label><input id="commune" name="commune" maxlength="80" placeholder="Pézenas"></div>
        </div>
        <div class="field"><label for="message">Votre besoin *</label><textarea id="message" name="message" rows="6" required maxlength="4000" placeholder="Taille du logement, prestations souhaitées, fréquence des séjours…"></textarea></div>
        <div class="hp" aria-hidden="true"><label for="site">Ne pas remplir</label><input id="site" name="site" tabindex="-1" autocomplete="off"></div>
        <div class="field"><label class="consent"><input type="checkbox" name="rgpd" value="1" required> <span>J'accepte que mes informations soient utilisées pour répondre à ma demande. Voir notre <a href="/politique-de-confidentialite">politique de confidentialité</a>.</span></label></div>
        <button class="btn" type="submit">Envoyer ma demande</button>
      </form>
    </div>
    <div class="card" style="background:var(--sand)">
      <h3>Nous joindre directement</h3>
      <ul class="contact-list">
        <li><strong>Téléphone</strong><a href="tel:{PHONE_INTL}">{PHONE}</a></li>
        <li><strong>E-mail</strong><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><strong>WhatsApp</strong><a href="{WHATSAPP}" rel="noopener">Écrire sur WhatsApp</a></li>
        <li><strong>Adresse</strong>7 rue Henri Reboul<br>34120 Pézenas</li>
      </ul>
    </div>
  </div>
</section>
"""

page(
    "contact.html", "/contact",
    "Contact et devis conciergerie à Pézenas | Terra Vigneronne",
    "Contactez Terra Vigneronne, conciergerie à Pézenas : devis et visite gratuits. 07 49 10 83 09 · contact@terravigneronne.com · 7 rue Henri Reboul.",
    contact,
)

# ---------------------------------------------------------------- Pages légales
LEGAL = pathlib.Path(__file__).parent / "legal"
for name, path, title, desc in [
    ("mentions-legales.html", "/mentions-legales", "Mentions légales | Terra Vigneronne", "Mentions légales du site terravigneronne.com, édité par SOGEQ SASU."),
    ("politique-de-confidentialite.html", "/politique-de-confidentialite", "Politique de confidentialité | Terra Vigneronne", "Comment Terra Vigneronne (SOGEQ) traite vos données personnelles."),
    ("cgv.html", "/cgv", "Conditions générales de vente | Terra Vigneronne", "Conditions générales de vente des prestations de conciergerie Terra Vigneronne."),
]:
    content = (LEGAL / name).read_text(encoding="utf-8")
    body = f'<section class="page-hero"><div class="wrap"><h1>{title.split(" | ")[0]}</h1></div></section><section><div class="wrap prose">{content}</div></section>'
    page(name, path, title, desc, body)

page(
    "404.html", "/404",
    "Page introuvable | Terra Vigneronne",
    "Cette page n'existe pas ou a été déplacée.",
    '<section class="page-hero"><div class="wrap"><h1>Page introuvable</h1><p>Cette page n\'existe pas ou a été déplacée.</p></div></section><section><div class="wrap"><a class="btn" href="/">Retour à l\'accueil</a> <a class="btn btn-line" href="/contact">Nous contacter</a></div></section>',
    noindex=True,
)
print("ok")
