"""Builds fr/index.html from index.html by translating every visible string.
Run from the repo root: python3 _build/build_fr_index.py
Fails loudly if any English string it expects is missing, so EN edits don't silently drift."""
import re
from babel import Locale

NB = " "  # non-breaking space before : ? ! in French

T = {
    # nav / hero
    "Product Range": "Gamme de produits",
    "Make an Enquiry": "Faire une demande",
    "Garland industrial cable, supplied by Meridian Industrial Co.": "Câbles industriels Garland, fournis par Meridian Industrial Co.",
    "Cable for the systems": "Des câbles pour vos",
    "that can't stop.": "systèmes critiques.",
    "Garland cable for mining, transport, communications and security projects. Built to your specification and supplied wherever you operate.":
        "Câbles Garland pour les projets miniers, de transport, de communication et de sécurité. Fabriqués selon votre cahier des charges et livrés là où vous opérez.",
    "Mining and industrial": "Mines et industrie",
    "Transport": "Transport",
    "Communications": "Communications",
    "Security and integration": "Sécurité et intégration",
    # about
    "About": "À propos",
    "One supplier for every cable your operation depends on.": "Un seul fournisseur pour tous les câbles dont dépend votre exploitation.",
    "Meridian Industrial Co. supplies": "Meridian Industrial Co. fournit les",
    "Garland cable": "câbles Garland",
    ", a Madison Group brand. Garland has engineered industrial cable since 1972.":
        ", une marque du groupe Madison. Garland conçoit des câbles industriels depuis 1972.",
    "Every site is different. You deal with one team for blast wire, power, instrumentation, data and fibre. We take care of the cable, so you can focus on running the operation.":
        "Chaque site est différent. Vous traitez avec une seule équipe pour les câbles de tir, d'énergie, d'instrumentation, de données et la fibre. Nous nous occupons du câble, pour que vous puissiez vous concentrer sur l'exploitation.",
    "Where your site needs something non-standard, Garland builds it to order.":
        "Lorsque votre site a besoin d'un câble hors standard, Garland le fabrique sur mesure.",
    "Industries served": "Secteurs desservis",
    "Garland engineering industrial cable since": "Garland conçoit des câbles industriels depuis",
    "24h": "24 h",
    "Enquiry response": "Réponse à votre demande",
    # industries
    "Industries": "Secteurs",
    "Garland cable is at the heart of four industries.": "Les câbles Garland sont au cœur de quatre secteurs.",
    "Blasting and shot firing": "Minage et tir",
    "Power to crushers, conveyors and pumps": "Alimentation des concasseurs, convoyeurs et pompes",
    "Process control and instrumentation": "Contrôle de procédé et instrumentation",
    "Site-wide fibre and data": "Fibre et données sur tout le site",
    "View products →": "Voir les produits →",
    "Tunnel ventilation and fire detection": "Ventilation et détection incendie en tunnel",
    "Rail signalling and communications": "Signalisation et communications ferroviaires",
    "Traffic control and road monitoring": "Gestion du trafic et surveillance routière",
    "Backbone and long-haul fibre": "Fibre de dorsale et longue distance",
    "Data centres and local networks": "Centres de données et réseaux locaux",
    "Pre-terminated fibre assemblies": "Assemblages fibre préconnectorisés",
    "Fire alarm and public address circuits": "Circuits d'alarme incendie et de sonorisation",
    "CCTV cameras": "Caméras de vidéosurveillance",
    "Access control and alarm panels": "Contrôle d'accès et centrales d'alarme",
    "Across all four, the brief is the same:": f"Dans les quatre secteurs, l'exigence est la même{NB}:",
    "cable that keeps working where a failure stops the operation or puts people at risk.":
        "un câble qui continue de fonctionner là où une panne arrête l'exploitation ou met des personnes en danger.",
    # mining applications
    "Mining in focus": "Focus mines",
    "In mining, six applications cover the site, from the blast hole to the control room.":
        "Dans une mine, six applications couvrent le site, du trou de mine à la salle de contrôle.",
    "Blasting": "Minage",
    "Twisted-pair wire that connects detonators and firing equipment. Every shot uses it, so we plan supply around your blast programme.":
        "Fil à paire torsadée qui relie les détonateurs et le matériel de tir. Chaque tir en consomme, nous planifions donc l'approvisionnement selon votre programme de tir.",
    "View range →": "Voir la gamme →",
    "Power": "Énergie",
    "LV and MV armoured power cable for mine and plant distribution, from Garland's partner Elegar-Kerpen.":
        "Câbles d'énergie armés BT et MT pour la distribution sur la mine et l'usine, de Elegar-Kerpen, partenaire de Garland.",
    "Instrumentation and control": "Instrumentation et contrôle",
    "Screened and armoured pair and triad cable for process control and sensor loops. Includes ICON Flex, Chem and Arctic for harsh conditions.":
        "Câbles à paires et triades blindés et armés pour le contrôle de procédé et les boucles de capteurs. Comprend ICON Flex, Chem et Arctic pour les conditions difficiles.",
    "Data and networks": "Données et réseaux",
    "Screened multicore, multipair and Cat6A cable for SCADA and site communications.":
        "Câbles multiconducteurs, multipaires et Cat6A blindés pour le SCADA et les communications du site.",
    "Fibre backbone": "Dorsale fibre",
    "Armoured industrial fibre, 6 to 144 fibres, single and multimode, for site-wide backbones.":
        "Fibre industrielle armée, de 6 à 144 fibres, monomode et multimode, pour les dorsales de site.",
    "Control room": "Salle de contrôle",
    "Racks, enclosures and splice closures to terminate and protect the network.":
        "Baies, coffrets et boîtiers d'épissure pour raccorder et protéger le réseau.",
    "Available with": "Disponible avec",
    "Steel-wire armour": "Armure en fils d'acier",
    "Fire rating": "Résistance au feu",
    "Low smoke, zero halogen": "Faible dégagement de fumée, sans halogène",
    "Water blocking": "Étanchéité à l'eau",
    "Rodent and termite protection": "Protection contre rongeurs et termites",
    # why
    "Why Meridian": "Pourquoi Meridian",
    "Buying through us gives you one accountable contact, from specification to after-sales.":
        "En achetant chez nous, vous avez un seul interlocuteur responsable, de la spécification à l'après-vente.",
    "Your specification": "Votre cahier des charges",
    "Built to IEC, national or project specification. Custom builds when no standard product fits.":
        "Fabriqué selon les normes IEC, nationales ou les spécifications du projet. Fabrication sur mesure quand aucun produit standard ne convient.",
    "One contact": "Un seul interlocuteur",
    "One contact from quote to after-sales, in English and French. We take any issue back to the factory for you.":
        "Un seul interlocuteur du devis à l'après-vente, en français et en anglais. Nous remontons tout problème à l'usine pour vous.",
    "Planned supply": "Approvisionnement planifié",
    "Send us your forecast. We plan production and consolidate shipments around it.":
        "Envoyez-nous vos prévisions. Nous planifions la production et regroupons les expéditions en conséquence.",
    "Like-for-like price": "Prix comparable",
    "Quoted against the same certified specification, with one quote for your full cable schedule.":
        "Chiffré sur la même spécification certifiée, avec un seul devis pour toute votre liste de câbles.",
    # contact + footer
    "Ready to discuss your requirements?": f"Prêt à discuter de vos besoins{NB}?",
    "Tell us about your site and what you need. We respond within 24 hours.":
        "Parlez-nous de votre site et de vos besoins. Nous répondons sous 24 heures.",
    "© 2026 Meridian Industrial Co. All rights reserved.": "© 2026 Meridian Industrial Co. Tous droits réservés.",
    # form
    "We respond within 24 hours.": "Nous répondons sous 24 heures.",
    "Name": "Nom",
    "Company": "Société",
    "Email": "E-mail",
    "Country": "Pays",
    "Sector": "Secteur",
    "Select sector": "Choisir un secteur",
    "EPC or installer": "EPC ou installateur",
    "Other": "Autre",
    "Requirement": "Besoin",
    "Send Enquiry →": "Envoyer la demande →",
    "Thank you. We have your enquiry and will respond within 24 hours.":
        "Merci. Nous avons bien reçu votre demande et vous répondrons sous 24 heures.",
}

# Attributes and other exact-string swaps (old, new, expected count)
SWAPS = [
    ('<html lang="en">', '<html lang="fr">', 1),
    ('<title>Meridian Industrial Co. | Garland industrial cable</title>',
     '<title>Meridian Industrial Co. | Câbles industriels Garland</title>', 1),
    ('content="Garland industrial cable for mining, transport, communications and security projects, supplied by Meridian Industrial Co."',
     'content="Câbles industriels Garland pour les projets miniers, de transport, de communication et de sécurité, fournis par Meridian Industrial Co."', 1),
    ('alt="Mining equipment working on an open-pit haul road"', 'alt="Engins miniers sur une piste de mine à ciel ouvert"', 1),
    ('placeholder="Your name"', 'placeholder="Votre nom"', 1),
    ('placeholder="Company or organisation"', 'placeholder="Société ou organisation"', 1),
    ('placeholder="your@email.com"', 'placeholder="vous@exemple.com"', 1),
    ('placeholder="What cable do you need, and for which site?"', f'placeholder="Quel câble vous faut-il, et pour quel site{NB}?"', 1),
    ('<a href="/" class="lang-opt active">EN</a><span class="lang-sep">|</span><a href="/fr/" class="lang-opt">FR</a>',
     '<a href="/" class="lang-opt">EN</a><span class="lang-sep">|</span><a href="/fr/" class="lang-opt active">FR</a>', 1),
    ('href="/products.html', 'href="/fr/products.html', None),
    ('<a class="nav-logo" href="/">', '<a class="nav-logo" href="/fr/">', 1),
    ('`New enquiry: ${document.getElementById(\'f-name\').value} (${country})`',
     '`New enquiry (FR site): ${document.getElementById(\'f-name\').value} (${country})`', 1),
]

EN_MAIN = ["Morocco", "Mauritania", "South Africa", "Saudi Arabia", "United Arab Emirates"]
# English names used on the EN form that Babel spells differently
EN_ALIASES = {
    "Bahamas": "BS", "Brunei": "BN", "Cabo Verde": "CV", "Congo": "CG", "Côte d'Ivoire": "CI",
    "Czechia": "CZ", "Democratic Republic of the Congo": "CD", "Eswatini": "SZ", "Gambia": "GM",
    "Laos": "LA", "Micronesia": "FM", "Myanmar": "MM", "North Korea": "KP", "North Macedonia": "MK",
    "Russia": "RU", "São Tomé and Príncipe": "ST", "South Korea": "KR", "Syria": "SY",
    "Timor-Leste": "TL", "Türkiye": "TR", "United Kingdom": "GB", "United States": "US",
    "Vietnam": "VN", "Iran": "IR", "Bolivia": "BO", "Venezuela": "VE", "Moldova": "MD", "Tanzania": "TZ",
    "Saint Kitts and Nevis": "KN", "Saint Lucia": "LC", "Saint Vincent and the Grenadines": "VC",
    "Antigua and Barbuda": "AG", "Trinidad and Tobago": "TT", "Bosnia and Herzegovina": "BA",
    "Guinea-Bissau": "GW",
}
FR_OVERRIDES = {"CD": "République démocratique du Congo", "CG": "Congo", "MM": "Myanmar",
                "US": "États-Unis", "GB": "Royaume-Uni", "TR": "Türkiye"}


def country_select(en_select_html):
    en_names = [n.replace("&#39;", "'") for n in re.findall(r"<option>([^<]+)</option>", en_select_html)]
    en_names = [n for n in en_names if n != "Other"]
    en_loc, fr_loc = Locale("en"), Locale("fr")
    by_name = {v: k for k, v in en_loc.territories.items() if len(k) == 2}
    pairs = {}
    for n in en_names:
        code = EN_ALIASES.get(n) or by_name.get(n)
        assert code, f"no ISO code for {n}"
        pairs[n] = FR_OVERRIDES.get(code, fr_loc.territories[code])
    esc = lambda x: x.replace("'", "&#39;")
    ind = "                    "
    out = [ind + '<option value="">Choisir un pays</option>', ind + '<optgroup label="Marchés principaux">']
    out += [f'{ind}    <option value="{esc(n)}">{esc(pairs[n])}</option>' for n in EN_MAIN]
    out += [ind + "</optgroup>", ind + '<optgroup label="Tous les pays">']
    import locale
    for n in sorted(set(pairs), key=lambda n: pairs[n].replace("É", "E").replace("Î", "I").lower()):
        out.append(f'{ind}    <option value="{esc(n)}">{esc(pairs[n])}</option>')
    out += [ind + '    <option value="Other">Autre</option>', ind + "</optgroup>"]
    return "\n".join(out)


def build():
    s = open("index.html", encoding="utf-8").read()
    for old, new, n in SWAPS:
        c = s.count(old)
        assert c >= 1 and (n is None or c == n), (c, old[:60])
        s = s.replace(old, new)
    # sector options: French label, English value (so emails match the EN site)
    for en in ["Mining and industrial", "Transport", "Communications", "Security and integration", "EPC or installer", "Other"]:
        old = f"<option>{en}</option>"
        if old in s:
            s = s.replace(old, f'<option value="{en}">{T[en]}</option>')
    # country dropdown
    m = re.search(r'(<select id="f-country"[^>]*>\n)(.*?)(\n\s*</select>)', s, flags=re.S)
    s = s[:m.start(2)] + country_select(m.group(2)) + s[m.end(2):]
    # visible text nodes
    missing = []
    for en, fr in sorted(T.items(), key=lambda kv: -len(kv[0])):
        pat = ">" + en.replace("'", "'") + "<"
        esc_en = en.replace("&", "&amp;")
        hits = s.count(">" + esc_en + "<") + s.count(">" + en + "<")
        if not hits and f">{esc_en}\n" not in s:
            # text nodes can carry surrounding whitespace
            rx = re.compile(r">(\s*)" + re.escape(esc_en) + r"(\s*)<")
            if not rx.search(s):
                if en not in ("EPC or installer", "Other"): missing.append(en)
                continue
        rx = re.compile(r">(\s*)" + re.escape(esc_en) + r"(\s*)<")
        s = rx.sub(lambda mm: ">" + mm.group(1) + fr.replace("&", "&amp;") + mm.group(2) + "<", s)
    assert not missing, missing
    open("fr/index.html", "w", encoding="utf-8").write(s)
    print("wrote fr/index.html")


if __name__ == "__main__":
    build()
