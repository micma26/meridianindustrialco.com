"""Builds fr/products.html from the product data in build_products.py.
Run from the repo root: python3 _build/build_products_fr.py"""
import importlib.util, re, sys
from html import escape

import os
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_products.py")
spec = importlib.util.spec_from_file_location("bp", SRC)
bp = importlib.util.module_from_spec(spec); spec.loader.exec_module(bp)
NB = " "

APPS_FR = {"blasting": "Minage", "power": "Énergie", "ic": "Instrumentation et contrôle",
           "data": "Données et réseaux", "fibre": "Dorsale fibre", "control": "Salle de contrôle",
           "transport": "Trafic et ferroviaire", "security": "Alarme incendie et sécurité"}

PROPS_FR = {"Steel-wire armour": "Armure en fils d'acier", "Steel-tape armour": "Armure en feuillard d'acier",
            "Fire rating": "Résistance au feu", "Low smoke, zero halogen": "Faible fumée, sans halogène",
            "Water blocking": "Étanchéité à l'eau", "Rodent and termite protection": "Protection rongeurs et termites"}

# id: (sidebar, title, description)
FAM_FR = {
 "blasting": ("Fil de tir", "Fil de tir",
   "Fil à paire torsadée pour relier les détonateurs et le matériel de tir, en mine à ciel ouvert et souterraine. "
   "Chaque tir en consomme, vous en recommandez donc régulièrement. Envoyez-nous vos prévisions de tir et nous planifions l'approvisionnement."),
 "power": ("Câbles armés", "Câbles d'énergie armés",
   "Câbles d'énergie armés pour les mines, les usines et les réseaux électriques, unipolaires et multipolaires, cuivre ou aluminium, "
   "de Elegar-Kerpen, partenaire de Garland. Fabriqués selon votre tension, section et armure. Envoyez-nous votre cahier des charges."),
 "ic-swa": ("Armé (SWA)", "Instrumentation et contrôle : armé (SWA)",
   "Câble multipaire armé en fils d'acier pour les parcours extérieurs, l'enfouissement et les zones exposées de la mine. "
   "Écran aluminium individuel et général avec protection SWA."),
 "ic-screened": ("Blindé (IND+OAS)", "Instrumentation et contrôle : blindé (IND+OAS)",
   "Câble multipaire à écran individuel et général pour le contrôle de procédé et la mesure dans les bâtiments et salles de contrôle. "
   "Garde des signaux propres dans les environnements à fort bruit électrique."),
 "ic-triad": ("Multitriade", "Instrumentation et contrôle : multitriade",
   "Câble à triades torsadées pour thermocouples, sondes RTD et boucles 4-20 mA. "
   "Les écrans individuels et général évitent les interférences sur les longs parcours en usine de procédé."),
 "ic-aw": ("Industrie lourde (AW)", "Instrumentation et contrôle : industrie lourde (série AW)",
   "Câble d'instrumentation armé avec écran individuel, écran aluminium général et SWA. "
   "Conçu pour les mines souterraines et les usines chimiques."),
 "ic-icon": ("Gamme ICON", "Instrumentation et contrôle : gamme ICON",
   "Câbles d'instrumentation et de contrôle standard et sur mesure de la gamme ICON d'Elegar-Kerpen. Envoyez-nous votre cahier des charges."),
 "data-multicore": ("Multiconducteur blindé", "Données et réseaux : multiconducteur blindé",
   "Câble multiconducteur blindé pour le SCADA, les communications du site et le câblage des systèmes de contrôle. De 4 à 36 conducteurs."),
 "data-multipair": ("Multipaire blindé", "Données et réseaux : multipaire blindé",
   "Câble multipaire blindé pour les réseaux et communications du site. Versions à écran individuel et général pour les zones perturbées."),
 "data-cat6a": ("Cat6A résistant au feu", "Données et réseaux : Cat6A résistant au feu",
   "Câble de données Cat6A qui continue de fonctionner dans un incendie. Testé pour l'intégrité du circuit selon IEC 60331-23 pendant 120 minutes."),
 "data-lan": ("Cat6 et Cat6A LSZH", "Données et réseaux : Cat6 et Cat6A, faible fumée",
   "Câble réseau pour salles de contrôle, bâtiments d'usine et bureaux, avec gaine à faible dégagement de fumée et sans halogène."),
 "data-external": ("Extérieur, rempli de gel", "Données et réseaux : extérieur, rempli de gel",
   "Câble de données et de communication extérieur rempli de gel pour bloquer l'eau, pour fourreaux enterrés et longs parcours extérieurs."),
 "fibre": ("Fibre armée", "Dorsale fibre : fibre armée",
   "Fibre armée pour les dorsales de site, en fourreau ou en pose directe enterrée. Versions monomodes présentées. "
   "Multimode OM3 et OM4, et jusqu'à 144 fibres en versions non métalliques, sur demande."),
 "fibre-fire": ("Fibre résistante au feu", "Dorsale fibre : fibre résistante au feu",
   "Fibre qui maintient une liaison de communication en cas d'incendie. Résistance au feu selon IEC 60331-25 pendant 120 minutes."),
 "control-room": ("Baies et boîtiers", "Salle de contrôle : baies, coffrets et boîtiers d'épissure",
   "Matériel pour raccorder et protéger le réseau, du tiroir optique au coffret de terrain."),
 "traffic": ("Boucles de détection", "Trafic et ferroviaire : câbles de boucle de détection",
   "Câbles pour les boucles de détection de véhicules et les feux de signalisation sur routes, pistes de roulage, barrières et accès de tunnels."),
 "rail": ("Signalisation ferroviaire", "Trafic et ferroviaire : câbles de signalisation ferroviaire",
   "Câbles de signalisation et de communication ferroviaires. Garland conçoit aussi des câbles ferroviaires selon les spécifications de votre projet."),
 "fire-alarm": ("Alarme incendie", "Alarme incendie et sécurité : câbles d'alarme incendie",
   "Câble d'alarme incendie rouge, résistant au feu pendant 120 minutes, pour les circuits d'alarme, de détection et de sonorisation."),
 "cctv": ("Vidéosurveillance et coaxial", "Alarme incendie et sécurité : vidéosurveillance et coaxial",
   "Câbles coaxiaux et composites pour caméras de vidéosurveillance, transportant vidéo et alimentation dans un seul câble."),
 "security-multicore": ("Contrôle d'accès", "Alarme incendie et sécurité : contrôle d'accès et alarme",
   "Câble multiconducteur blindé pour le contrôle d'accès, les équipements de porte, les centrales d'alarme et les interphones."),
}

# Whole-row overrides where the phrase rules would read badly
ROW_FR = {
 "LV armoured power cable, single and multicore": "Câble d'énergie armé BT, unipolaire et multipolaire",
 "MV armoured power cable": "Câble d'énergie armé MT",
 "Power cable for grid and distribution networks, copper or aluminium, built to your voltage": "Câble d'énergie pour réseaux électriques et de distribution, cuivre ou aluminium, selon votre tension",
 "Fibre splice closures, 24 to 1,152 fibres": "Boîtiers d'épissure fibre, de 24 à 1 152 fibres",
 "IP65 enclosures, rack mount or DIN rail, sized to order": "Coffrets IP65, montage en baie ou sur rail DIN, dimensionnés sur mesure",
 "1RU sliding fibre panel (FOBOT), 24/48 fibres, black": "Tiroir optique coulissant 1U (FOBOT), 24/48 fibres, noir",
 "Rodent-proof rear plates for MT30903B, set of 2": "Plaques arrière anti-rongeurs pour MT30903B, lot de 2",
 "Rack mount sliding drawer fibre panel (FOBOT), 48 ports": "Tiroir optique coulissant en baie (FOBOT), 48 ports",
 "Wall cabinet, 6RU, 600mm deep, glass door": "Coffret mural 6U, profondeur 600 mm, porte vitrée",
 "Floor rack, 27U, 600 x 600mm, glass front, metal rear, complete": "Baie au sol 27U, 600 x 600 mm, façade vitrée, arrière métal, complète",
 "Floor rack, 45U, 600 x 800mm, glass front, metal rear, complete": "Baie au sol 45U, 600 x 800 mm, façade vitrée, arrière métal, complète",
 "Server rack, 45U, 800 x 1000mm, mesh front and rear, complete": "Baie serveur 45U, 800 x 1000 mm, portes perforées avant et arrière, complète",
 "Composite CCTV cable, RG59 coax + 2 core 24/0.20mm power, 250m": "Câble composite vidéosurveillance, coaxial RG59 + alimentation 2 conducteurs 24/0,20 mm, 250 m",
 "Composite CCTV cable, RG59 coax + 2 core 24/0.20mm power, black, 250m": "Câble composite vidéosurveillance, coaxial RG59 + alimentation 2 conducteurs 24/0,20 mm, noir, 250 m",
}

PHRASES = [
 (r"Shot Fire Cable", "Câble de tir"),
 (r"Individual \+ Collective Screen", "écran individuel + général"),
 (r"Individual Screen", "écran individuel"),
 (r"Braided Screen", "écran tressé"),
 (r"overall screened", "écran général"), (r"overall screen", "écran général"),
 (r"foil screened", "écran feuillard"),
 (r"Multi-Pair", "Multipaire"), (r"Multi-Triad", "Multitriade"), (r"Multi-Conductor", "Multiconducteur"),
 (r"Figure-8", "en 8"),
 (r"Jelly Filled|jelly filled", "rempli de gel"),
 (r"Underground telephone cable", "Câble téléphonique enterré"),
 (r"Loop detector cable", "Câble de boucle de détection"),
 (r"Loop feeder cable", "Câble d'alimentation de boucle"),
 (r"Traffic signal cable", "Câble de signalisation routière"),
 (r"Rail cable", "Câble ferroviaire"),
 (r"Fire alarm cable", "Câble d'alarme incendie"),
 (r"Composite CCTV cable", "Câble composite vidéosurveillance"),
 (r"Coaxial cable", "Câble coaxial"),
 (r"(\d+) core ([\d.]+mm) power", r"\2, alimentation \1 conducteurs"),
 (r"Armoured fibre", "Fibre armée"), (r"Fire-rated fibre", "Fibre résistante au feu"),
 (r"OS2 single mode", "monomode OS2"), (r"(OM\d) multimode", r"multimode \1"),
 (r"120-minute fire rating", "résistance au feu 120 minutes"),
 (r"\(120 min\)", "(120 minutes)"),
 (r"quad screen", "quadruple écran"), (r"84% braid", "tresse 84 %"),
 (r"^Cable (\d)", r"Câble \1"),
 (r"\b1 Pair\b|\b1 pair\b", "1 paire"), (r"\b(\d+) Pair\b|\b(\d+) pair\b", lambda m: f"{m.group(1) or m.group(2)} paires"),
 (r"\b1 Triad\b", "1 triade"), (r"\b(\d+) Triad\b", r"\1 triades"),
 (r"\b1 Core\b|\b1 core\b", "1 conducteur"), (r"\b(\d+) Core\b|\b(\d+) core\b", lambda m: f"{m.group(1) or m.group(2)} conducteurs"),
 (r"\bScreened\b", "blindé"), (r"\bblack\b", "noir"), (r"\bgrey\b", "gris"), (r"\bblue\b", "bleu"), (r"\bred\b", "rouge"),
 (r"(\d)\.(\d)", r"\1,\2"),
 (r"(\d)(mm²|mm|m)(?![A-Za-z])", r"\1 \2"),
]


def row_fr(en):
    if en in ROW_FR:
        return ROW_FR[en]
    s = en
    for pat, rep in PHRASES:
        s = re.sub(pat, rep, s)
    return s


def build():
    bp.APPS[:] = [(a, n, APPS_FR[a]) for a, n, _ in bp.APPS]
    for f in bp.FAMILIES:
        f["side"], f["title"], f["desc"] = FAM_FR[f["id"]]
        f["props"] = [PROPS_FR[p] for p in f["props"]]
        f["rows"] = [(p, row_fr(d)) for p, d in f["rows"]]
    fams = "".join(bp.family_html(f) for f in bp.FAMILIES)
    page = bp.PAGE
    # swap the generated blocks
    page = re.sub(r'(<div class="filter-bar">\n).*?(\n  </div>)', lambda m: m.group(1) + bp.filters_html() + m.group(2), page, count=1, flags=re.S)
    page = re.sub(r'(<aside class="sidebar">\n).*?(\n      <div class="sidebar-enquiry">)', lambda m: m.group(1) + bp.sidebar_html() + m.group(2), page, count=1, flags=re.S)
    page = re.sub(r'(<div class="families">).*?(\n\n    </div>\n  </div>)', lambda m: m.group(1) + fams + m.group(2), page, count=1, flags=re.S)
    swaps = [
     ('<html lang="en">', '<html lang="fr">'),
     ('<title>Product Range | Meridian Industrial Co.</title>', '<title>Gamme de produits | Meridian Industrial Co.</title>'),
     ('<a href="/" class="nav-logo">', '<a href="/fr/" class="nav-logo">'),
     ('<a href="/" class="nav-link">Home</a>', '<a href="/fr/" class="nav-link">Accueil</a>'),
     ('<a href="/products.html" class="lang-opt active">EN</a><span class="lang-sep">|</span><a href="/fr/products.html" class="lang-opt">FR</a>',
      '<a href="/products.html" class="lang-opt">EN</a><span class="lang-sep">|</span><a href="/fr/products.html" class="lang-opt active">FR</a>'),
     ('class="nav-cta">Make an Enquiry</a>', 'class="nav-cta">Faire une demande</a>'),
     ('<p class="page-eyebrow">Product Range</p>', '<p class="page-eyebrow">Gamme de produits</p>'),
     ('<h1 class="page-title">Every cable your operation depends on, <em>from one supplier.</em></h1>',
      '<h1 class="page-title">Tous les câbles dont dépend votre exploitation, <em>chez un seul fournisseur.</em></h1>'),
     ('<button class="filter-btn active" data-filter="all">All products</button>', '<button class="filter-btn active" data-filter="all">Tous les produits</button>'),
     ("Don't see what you need?", f"Vous ne trouvez pas ce qu'il vous faut{NB}?"),
     ('Contact us.</a> Garland builds to order.', 'Contactez-nous.</a> Garland fabrique sur mesure.'),
     ('<th>Part No.</th><th>Description</th><th>Enquire</th>', '<th>Référence</th><th>Description</th><th>Demande</th>'),
     ('class="enquire-link">Enquire</a>', 'class="enquire-link">Demander</a>'),
     ('<td class="td-part td-req">On request</td>', '<td class="td-part td-req">Sur demande</td>'),
     ('?subject=Enquiry: ', '?subject=Demande : '),
     ('<h2>Need a specification outside this range?<br><em>Garland builds to order.</em></h2>',
      f'<h2>Besoin d\'une spécification hors de cette gamme{NB}?<br><em>Garland fabrique sur mesure.</em></h2>'),
     ('class="cta-button">Make an Enquiry</a>', 'class="cta-button">Faire une demande</a>'),
     ('<a href="/">Meridian Industrial Co.</a>', '<a href="/fr/">Meridian Industrial Co.</a>'),
     ('All rights reserved.', 'Tous droits réservés.'),
    ]
    for old, new in swaps:
        assert old in page, old[:70]
        page = page.replace(old, new)
    # intro, CTA text and meta: match on the start so small EN edits don't break the build
    page = re.sub(r'<p class="page-intro">.*?</p>',
                  '<p class="page-intro">Une sélection de la gamme Garland, classée par application. Demandez-nous d\'autres sections, longueurs et couleurs. '
                  'Pour les fiches techniques ou les prix, utilisez le lien de demande sur chaque ligne.</p>', page, count=1)
    page = re.sub(r'(<div class="cta-band">.*?</h2>\n    )<p>.*?</p>',
                  lambda m: m.group(1) + "<p>Cette page présente une sélection. Dites-nous ce dont votre site a besoin et nous le trouverons dans la gamme complète, ou le fabriquerons. Nous répondons sous 24 heures.</p>",
                  page, count=1, flags=re.S)
    page = re.sub(r'<meta name="description" content="[^"]*" />',
                  '<meta name="description" content="Câbles industriels Garland pour les mines, le transport, les communications et la sécurité : câbles de tir, énergie, instrumentation, données, fibre, trafic, ferroviaire, alarme incendie et vidéosurveillance." />', page, count=1)
    open("fr/products.html", "w", encoding="utf-8").write(page)
    print("wrote fr/products.html")


if __name__ == "__main__":
    build()
