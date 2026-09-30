"""Builds products.html for meridianindustrialco.com from the product data below."""
from html import escape

MAIL = "sales@meridianindustrialco.com"

# (application id, number, name)
APPS = [
    ("blasting", 1, "Blasting"),
    ("power", 2, "Power"),
    ("ic", 3, "Instrumentation and control"),
    ("data", 4, "Data and networks"),
    ("fibre", 5, "Fibre backbone"),
    ("control", 6, "Control room"),
    ("transport", 7, "Traffic and rail"),
    ("security", 8, "Fire alarm and security"),
]

# Each family: anchor id, app id, short sidebar name, title, properties, description, rows
# Row: (part number or None for "on request", description)
FAMILIES = [
    dict(id="blasting", app="blasting", side="Blast wire", title="Blast wire",
         props=[],
         desc="Twisted-pair connecting wire for detonators and firing equipment, for open-pit and underground blasting. "
              "Every shot uses it, so you reorder it regularly. Send us your blast forecast and we plan supply around it.",
         rows=[("SF16RW100", "Shot Fire Cable, 0.6mm, 1 Pair, PVC, 100m"),
               ("SF16RW200", "Shot Fire Cable, 0.6mm, 1 Pair, PVC, 200m"),
               ("SF16RW250", "Shot Fire Cable, 0.6mm, 1 Pair, PVC, 250m"),
               ("SF16RW500", "Shot Fire Cable, 0.6mm, 1 Pair, PVC, 500m"),
               ("SF17WHRD100", "Shot Fire Cable, 0.7mm, 1 Pair, Figure-8, PVC, 100m")]),
    dict(id="power", app="power", side="Armoured power", title="Armoured power cable",
         props=["Steel-wire armour"],
         desc="LV and MV armoured power cable for mine and plant distribution, single and multicore, "
              "from Garland's partner Elegar-Kerpen. Built to your voltage, size and armour. Send us your specification.",
         rows=[(None, "LV armoured power cable, single and multicore"),
               (None, "MV armoured power cable")]),
    dict(id="ic-swa", app="ic", side="Armoured (SWA)", title="Instrumentation and control: armoured (SWA)",
         props=["Steel-wire armour"],
         desc="Steel-wire armoured multipair cable for outdoor runs, burial and exposed mine areas. "
              "Individual and overall aluminium screen with SWA protection.",
         rows=[("MCP7052SSWA1000", "Multi-Pair, 7/0.50mm, 2 Pair, Screened, PVC/SWA/PVC, 1000m"),
               ("MCP7054SSWA1000", "Multi-Pair, 7/0.50mm, 4 Pair, Screened, PVC/SWA/PVC, 1000m"),
               ("MCP7056SSWA1000", "Multi-Pair, 7/0.50mm, 6 Pair, Screened, PVC/SWA/PVC, 1000m"),
               ("MCP70512SSWA500", "Multi-Pair, 7/0.50mm, 12 Pair, Screened, PVC/SWA/PVC, 500m"),
               ("MCP7036SSWA500", "Multi-Pair, 7/0.30mm, 6 Pair, Screened, PVC/SWA/PVC, 500m"),
               ("MCP7034SSWA1000", "Multi-Pair, 7/0.30mm, 4 Pair, Screened, PVC/SWA/PVC, 1000m")]),
    dict(id="ic-screened", app="ic", side="Screened (IND+OAS)", title="Instrumentation and control: screened (IND+OAS)",
         props=[],
         desc="Individually and overall screened multipair cable for process control and measurement "
              "in plant buildings and control rooms. Keeps signals clean where there is a lot of electrical noise.",
         rows=[("MCP7052ISCS1000", "Multi-Pair, 7/0.50mm, 2 Pair, Individual + Collective Screen, PVC, 1000m"),
               ("MCP70512ISCS1000", "Multi-Pair, 7/0.50mm, 12 Pair, Individual + Collective Screen, PVC, 1000m"),
               ("MCP7034ISCS1000", "Multi-Pair, 7/0.30mm, 4 Pair, Individual + Collective Screen, PVC, 1000m"),
               ("MCP70312ISCS1000", "Multi-Pair, 7/0.30mm, 12 Pair, Individual + Collective Screen, PVC, 1000m")]),
    dict(id="ic-triad", app="ic", side="Multi-triad", title="Instrumentation and control: multi-triad",
         props=[],
         desc="Twisted triad cable for thermocouple, RTD and 4-20 mA signal loops. "
              "Individual and collective screens stop circuits interfering on long runs in process plants.",
         rows=[("MCT7031S500", "Multi-Triad, 7/0.3mm, 1 Triad, Screened, PVC, 500m"),
               ("MCT7036ISCS1000", "Multi-Triad, 7/0.3mm, 6 Triad, Individual + Collective Screen, PVC, 1000m"),
               ("MCT70312ISCS1000", "Multi-Triad, 7/0.3mm, 12 Triad, Individual + Collective Screen, PVC, 1000m")]),
    dict(id="ic-aw", app="ic", side="Heavy industrial (AW)", title="Instrumentation and control: heavy industrial (AW series)",
         props=["Steel-wire armour"],
         desc="Armoured instrumentation cable with individual screen, overall aluminium screen and SWA. "
              "Built for underground mines and chemical plants.",
         rows=[("MCT7052S1000-AW", "Cable 2P 0.5mm² IND+OAS+SWA, PVC/SWA/PVC, 1000m"),
               ("MCT7056S1000-AW", "Cable 12P 0.5mm² IND+OAS+SWA, PVC/SWA/PVC, 1000m"),
               ("MCT7053S1000-AW", "Cable 20P 0.5mm² IND+OAS+SWA, PVC/SWA/PVC, 1000m"),
               ("MCP7031S1000-AW", "Cable 4T 1.5mm² IND+OAS+SWA, PVC/SWA/PVC, 1000m"),
               ("MCP7033S1000-AW", "Cable 20T 1.5mm² IND+OAS+SWA, PVC/SWA/PVC, 1000m")]),
    dict(id="ic-icon", app="ic", side="ICON range", title="Instrumentation and control: ICON range",
         props=[],
         desc="Standard and custom instrumentation and control cable from Elegar-Kerpen's ICON range. Send us your specification.",
         rows=[(None, "ICON Base"), (None, "ICON Flex"), (None, "ICON Chem"),
               (None, "ICON Arctic"), (None, "ICON Safe"), (None, "ICON Bus")]),
    dict(id="data-multicore", app="data", side="Multicore screened", title="Data and networks: multicore screened",
         props=[],
         desc="Screened multicore cable for SCADA, site communications and control system wiring. 4 to 36 cores.",
         rows=[("MC74S500", "Multi-Conductor, 7/0.20mm, 4 Core, Screened, PVC, 500m"),
               ("MC76S500", "Multi-Conductor, 7/0.20mm, 6 Core, Screened, PVC, 500m"),
               ("MC78S500", "Multi-Conductor, 7/0.20mm, 8 Core, Screened, PVC, 500m"),
               ("MC725S500", "Multi-Conductor, 7/0.20mm, 25 Core, Screened, PVC, 500m"),
               ("MC736S500", "Multi-Conductor, 7/0.20mm, 36 Core, Screened, PVC, 500m")]),
    dict(id="data-multipair", app="data", side="Multipair screened", title="Data and networks: multipair screened",
         props=[],
         desc="Screened multipair cable for site networks and communications. Individual and collective screen versions for noisy areas.",
         rows=[("MCP2S500", "Multi-Pair, 7/0.20mm, 2 Pair, Screened, PVC, 500m"),
               ("MCP4S500", "Multi-Pair, 7/0.20mm, 4 Pair, Screened, PVC, 500m"),
               ("MCP6S500", "Multi-Pair, 7/0.20mm, 6 Pair, Screened, PVC, 500m"),
               ("MCP8S500", "Multi-Pair, 7/0.20mm, 8 Pair, Screened, PVC, 500m"),
               ("MCP4ISCS500", "Multi-Pair, 7/0.20mm, 4 Pair, Individual + Collective Screen, PVC, 500m")]),
    dict(id="data-cat6a", app="data", side="Fire-rated Cat6A", title="Data and networks: fire-rated Cat6A",
         props=["Fire rating", "Low smoke, zero halogen"],
         desc="Cat6A data cable that keeps working in a fire. Tested for circuit integrity to IEC 60331-23 for 120 minutes.",
         rows=[("SFTPL6AFIRERD100", "Cat6A S/FTP, 23 AWG, LSZH, red, IEC 60331-23 (120 min), 100m"),
               ("SFTPL6AFIRERD305", "Cat6A S/FTP, 23 AWG, LSZH, red, IEC 60331-23 (120 min), 305m")]),
    dict(id="data-lan", app="data", side="Cat6 and Cat6A LSZH", title="Data and networks: Cat6 and Cat6A, low smoke",
         props=["Low smoke, zero halogen"],
         desc="Network cable for control rooms, plant buildings and offices, with low smoke, zero halogen sheaths.",
         rows=[("FTPL6AHFBK305", "Cat6A, 4 pair, foil screened, LSZH, black, 305m"),
               ("FTPL6AHFGY500", "Cat6A, 4 pair, foil screened, LSZH, grey, 500m"),
               ("FTPL6AHFBL305", "Cat6A, 4 pair, foil screened, LSZH, blue, 305m"),
               ("UTPL6HFGY305RBA", "Cat6, 4 pair, UTP, LSZH, grey, 305m")]),
    dict(id="data-external", app="data", side="External, jelly-filled", title="Data and networks: external, jelly-filled",
         props=["Water blocking"],
         desc="Outdoor data and communications cable with jelly filling to keep water out, for underground ducts and long outdoor runs.",
         rows=[("UTPL6JFBK305", "Cat6, 4 pair, UTP, jelly filled, PE, 305m"),
               ("UTPL6PP500", "Cat6, 4 pair, UTP, Poly/Poly, 500m"),
               ("MCP2SJFP500", "Multi-Pair, 7/0.20mm, 2 Pair, Screened, Jelly Filled, Poly, 500m"),
               ("MCP2ISJFP500", "Multi-Pair, 7/0.20mm, 2 Pair, Individual Screen, Jelly Filled, Poly, 500m"),
               ("MCP3SJFP500", "Multi-Pair, 7/0.20mm, 3 Pair, Screened, Jelly Filled, Poly, 500m"),
               ("MC146JFPP500", "Multi-Conductor, 14/0.20mm, 6 Core, Jelly Filled, Poly/Poly, 500m"),
               ("ETC2064JF1000", "Underground telephone cable, 10 Pair 0.64mm, Jelly Filled, Poly, 1000m"),
               ("ETC10064JF1000", "Underground telephone cable, 50 Pair 0.64mm, Jelly Filled, Poly, 1000m"),
               ("ETC20064JF500", "Underground telephone cable, 100 Pair 0.64mm, Jelly Filled, Poly, 500m")]),
    dict(id="fibre", app="fibre", side="Armoured fibre", title="Fibre backbone: armoured fibre",
         props=["Steel-tape armour", "Rodent and termite protection"],
         desc="Armoured fibre for site-wide backbones, in duct or direct burial. Single mode shown. "
              "OM3 and OM4 multimode, and up to 144 fibres in non-metallic versions, on request.",
         rows=[("GLTSM1AH006BK", "Armoured fibre, OS2 single mode, 6 fibres, PE/NY/CSTA/PE"),
               ("GLTSM1AH012BK", "Armoured fibre, OS2 single mode, 12 fibres, PE/NY/CSTA/PE"),
               ("GLTSM1AH024BK", "Armoured fibre, OS2 single mode, 24 fibres, PE/NY/CSTA/PE"),
               ("GLTSM1AH048BK", "Armoured fibre, OS2 single mode, 48 fibres, PE/NY/CSTA/PE"),
               ("GLTSM1AH072BK", "Armoured fibre, OS2 single mode, 72 fibres, PE/NY/CSTA/PE")]),
    dict(id="fibre-fire", app="fibre", side="Fire-rated fibre", title="Fibre backbone: fire-rated fibre",
         props=["Fire rating", "Low smoke, zero halogen"],
         desc="Fibre that keeps a communication path open in a fire. Fire rated to IEC 60331-25 for 120 minutes.",
         rows=[("GLTSM1RC006RD", "Fire-rated fibre, OS2 single mode, 6 fibres, LSZH, IEC 60331-25 (120 min)"),
               ("GLTSM1RC012RD", "Fire-rated fibre, OS2 single mode, 12 fibres, LSZH, IEC 60331-25 (120 min)"),
               ("GLTOM3RC012RD", "Fire-rated fibre, OM3 multimode, 12 fibres, LSZH, IEC 60331-25 (120 min)"),
               ("GLTOM4RC012RD", "Fire-rated fibre, OM4 multimode, 12 fibres, LSZH, IEC 60331-25 (120 min)")]),
    dict(id="control-room", app="control", side="Racks and closures", title="Control room: racks, enclosures and splice closures",
         props=[],
         desc="Hardware to terminate and protect the network, from the fibre panel to the field enclosure.",
         rows=[("MT30903B", "1RU sliding fibre panel (FOBOT), 24/48 fibres, black"),
               ("MT309AK", "Rodent-proof rear plates for MT30903B, set of 2"),
               ("MT30905", "Rack mount sliding drawer fibre panel (FOBOT), 48 ports"),
               (None, "Fibre splice closures, 24 to 1,152 fibres"),
               ("GDR6U600X600WGD", "Wall cabinet, 6RU, 600mm deep, glass door"),
               ("GDR27U600X600FGD", "Floor rack, 27U, 600 x 600mm, glass front, metal rear, complete"),
               ("GDR45U600X800FGD", "Floor rack, 45U, 600 x 800mm, glass front, metal rear, complete"),
               ("GDR45U800X1000FMD", "Server rack, 45U, 800 x 1000mm, mesh front and rear, complete"),
               (None, "IP65 enclosures, rack mount or DIN rail, sized to order")]),
    dict(id="traffic", app="transport", side="Loop detector and feeder", title="Traffic and rail: loop detector and feeder cable",
         props=["Water blocking"],
         desc="Cable for vehicle detection loops and traffic signals on roads, haul roads, gates and tunnel approaches.",
         rows=[("MC7051XLPE500", "Loop detector cable, 1.5mm², 1 core, XLPE, 500m"),
               ("MC7051XLPE1000", "Loop detector cable, 1.5mm², 1 core, XLPE, 1000m"),
               ("MC7052JFSTD500", "Loop feeder cable, 1.5mm², 1 pair, jelly filled, 500m"),
               ("MC7056JFSTD500", "Loop feeder cable, 1.5mm², 3 pair, jelly filled, 500m"),
               ("MC7058JFSTD500", "Loop feeder cable, 1.5mm², 4 pair, jelly filled, 500m"),
               ("MCC6QTRAFFICUV500", "Traffic signal cable, 6 core, PVC/PVC, 500m")]),
    dict(id="rail", app="transport", side="Rail signalling", title="Traffic and rail: rail signalling cable",
         props=[],
         desc="Signalling and communications cable for rail. Garland also designs rail cable to your project specification.",
         rows=[("MC70510RAIL400", "Rail cable, 1.5mm², 10 core, PVC/PVC, 400m"),
               ("MC70520RAIL400", "Rail cable, 1.5mm², 20 core, PVC/PVC, 400m"),
               ("MC70550RAIL400", "Rail cable, 1.5mm², 50 core, PVC/PVC, 400m"),
               ("PTC09010SRAILGY500", "Rail cable, 0.9mm, 10 pair, overall screened, PE/PVC, 500m"),
               ("ETC409JFSPEN500", "Rail cable, 0.9mm, 4 core, overall screened, PE/PVC, 500m")]),
    dict(id="fire-alarm", app="security", side="Fire alarm", title="Fire alarm and security: fire alarm cable",
         props=["Fire rating", "Low smoke, zero halogen"],
         desc="Red fire alarm cable, fire rated for 120 minutes, for alarm, detection and public address circuits.",
         rows=[("MC7032FRHFRD500", "Fire alarm cable, 2 core 0.5mm², LSZH, red, 120-minute fire rating, 500m"),
               ("MC7042FRHFRD500", "Fire alarm cable, 2 core 1.0mm², LSZH, red, 120-minute fire rating, 500m"),
               ("MC7032FRSHFRD500", "Fire alarm cable, 2 core 0.5mm², overall screen, LSZH, red, 120-minute fire rating, 500m"),
               ("MC7042FRSHFRD500", "Fire alarm cable, 2 core 1.0mm², overall screen, LSZH, red, 120-minute fire rating, 500m")]),
    dict(id="cctv", app="security", side="CCTV and coax", title="Fire alarm and security: CCTV and coax",
         props=[],
         desc="Coax and composite cable for CCTV cameras, carrying video and power in one run.",
         rows=[("CCTVCOM24250", "Composite CCTV cable, RG59 coax + 2 core 24/0.20mm power, 250m"),
               ("CCTVCOM24BK250", "Composite CCTV cable, RG59 coax + 2 core 24/0.20mm power, black, 250m"),
               ("CC59300B", "Coaxial cable, RG59B/U, 75 ohm, 84% braid, 300m"),
               ("CC6QS305RBW", "Coaxial cable, RG6, 75 ohm, quad screen, 305m")]),
    dict(id="security-multicore", app="security", side="Access control", title="Fire alarm and security: access control and alarm cable",
         props=[],
         desc="Screened multicore cable for access control, door hardware, alarm panels and intercoms.",
         rows=[("MC76S500", "Multi-Conductor, 7/0.20mm, 6 Core, Screened, PVC, 500m"),
               ("MC78S500", "Multi-Conductor, 7/0.20mm, 8 Core, Screened, PVC, 500m"),
               ("MC78BS500", "Multi-Conductor, 7/0.20mm, 8 Core, Braided Screen, PVC, 500m")]),
]


def enquire(part, desc):
    subj = part if part else desc
    return f'<a href="mailto:{MAIL}?subject=Enquiry: {escape(subj, quote=True)}" class="enquire-link">Enquire</a>'


def family_html(f):
    app = next(a for a in APPS if a[0] == f["app"])
    props = "".join(f'<span class="prop-tag">{escape(p)}</span>' for p in f["props"])
    rows = []
    for part, desc in f["rows"]:
        p = f'<td class="td-part">{escape(part)}</td>' if part else '<td class="td-part td-req">On request</td>'
        rows.append(f'            <tr>{p}<td class="td-name">{escape(desc)}</td><td class="td-action">{enquire(part, desc)}</td></tr>')
    return f'''
      <div class="family-block" id="{f["id"]}" data-app="{f["app"]}">
        <div class="family-header">
          <div class="family-tags"><span class="app-tag"><b>{app[1]}</b>{escape(app[2])}</span>{props}</div>
          <h2 class="family-name">{escape(f["title"])}</h2>
          <p class="family-desc">{escape(f["desc"])}</p>
        </div>
        <table class="product-table">
          <thead><tr><th>Part No.</th><th>Description</th><th>Enquire</th></tr></thead>
          <tbody>
{chr(10).join(rows)}
          </tbody>
        </table>
      </div>'''


def sidebar_html():
    out = []
    for app_id, num, name in APPS:
        out.append(f'      <p class="sidebar-group"><b>{num}</b>{escape(name)}</p>')
        for f in FAMILIES:
            if f["app"] == app_id:
                out.append(f'      <a href="#{f["id"]}" class="sidebar-link">{escape(f["side"])}</a>')
    return "\n".join(out)


def filters_html():
    btns = ['    <button class="filter-btn active" data-filter="all">All products</button>']
    for app_id, num, name in APPS:
        btns.append(f'    <button class="filter-btn" data-filter="{app_id}">{num}. {escape(name)}</button>')
    return "\n".join(btns)


CSS = r"""
    :root {
      --ink:     #0B1D33;
      --navy:    #1F497D;
      --indigo:  #2C318E;
      --steel:   #5B7FA8;
      --sky:     #9DB9DC;
      --ice:     #DCE6F2;
      --mist:    #F1F5FA;
      --slate:   #5A6573;
      --white:   #FFFFFF;
      --display: 'Cormorant Garamond', Georgia, serif;
      --body:    'DM Sans', system-ui, sans-serif;
    }
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }
    body {
      background: var(--white);
      color: var(--ink);
      font-family: var(--body);
      font-size: 15px;
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
    }

    /* Nav */
    nav {
      position: fixed; top: 0; left: 0; right: 0; z-index: 100;
      display: flex; align-items: center; justify-content: space-between;
      padding: 0 5vw; height: 64px;
      background: rgba(11,29,51,0.96);
      backdrop-filter: blur(10px);
      border-bottom: 1px solid rgba(157,185,220,0.18);
    }
    .nav-logo {
      font-size: 0.75rem; font-weight: 600; letter-spacing: 0.22em; text-transform: uppercase;
      color: var(--white); text-decoration: none;
    }
    .nav-right { display: flex; align-items: center; gap: 2rem; }
    .nav-link {
      font-size: 0.68rem; font-weight: 500; letter-spacing: 0.18em; text-transform: uppercase;
      color: var(--sky); text-decoration: none;
    }
    .nav-link:hover { color: var(--white); }
    .nav-cta {
      font-size: 0.7rem; font-weight: 600; letter-spacing: 0.16em; text-transform: uppercase;
      color: var(--white); background: var(--indigo); text-decoration: none;
      padding: 0.6rem 1.4rem; transition: background 0.2s;
    }
    .nav-cta:hover { background: var(--navy); }

    /* Header */
    .page-header { background: var(--ink); color: var(--white); padding: 128px 5vw 64px; }
    .page-header-inner { max-width: 1200px; margin: 0 auto; }
    .page-eyebrow {
      display: flex; align-items: center; gap: 1rem;
      font-size: 0.7rem; font-weight: 500; letter-spacing: 0.26em; text-transform: uppercase;
      color: var(--sky); margin-bottom: 1.4rem;
    }
    .page-eyebrow::before { content: ''; width: 36px; height: 1px; background: var(--sky); }
    .page-title {
      font-family: var(--display); font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 500; line-height: 1.08;
      margin-bottom: 1.4rem; max-width: 820px;
    }
    .page-title em { font-style: italic; color: var(--sky); }
    .page-intro { font-size: 1rem; font-weight: 300; color: var(--ice); max-width: 620px; line-height: 1.75; }

    /* Filters */
    .filter-bar {
      background: var(--mist); border-bottom: 1px solid var(--ice);
      padding: 1.4rem 5vw; display: flex; gap: 0.5rem; flex-wrap: wrap;
    }
    .filter-btn {
      font-family: var(--body); font-size: 0.72rem; font-weight: 500; letter-spacing: 0.06em;
      color: var(--navy); background: var(--white); border: 1px solid var(--ice);
      padding: 0.45rem 0.95rem; cursor: pointer; transition: all 0.18s;
    }
    .filter-btn:hover { border-color: var(--indigo); color: var(--indigo); }
    .filter-btn.active { background: var(--indigo); border-color: var(--indigo); color: var(--white); }

    /* Layout */
    .products-layout {
      display: grid; grid-template-columns: 230px 1fr;
      max-width: 1200px; margin: 0 auto; padding: 3.5rem 5vw 6rem;
    }
    .sidebar {
      position: sticky; top: 88px; height: fit-content;
      padding-right: 2rem; border-right: 1px solid var(--ice);
    }
    .sidebar-group {
      display: flex; align-items: center; gap: 0.55rem;
      font-size: 0.66rem; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase;
      color: var(--ink); margin: 1.2rem 0 0.35rem;
    }
    .sidebar-group:first-child { margin-top: 0; }
    .sidebar-group b, .app-tag b {
      display: inline-flex; align-items: center; justify-content: center;
      width: 1.35rem; height: 1.35rem; border-radius: 50%;
      background: var(--indigo); color: var(--white); font-size: 0.66rem; letter-spacing: 0;
    }
    .sidebar-link {
      display: block; font-size: 0.82rem; color: var(--slate); text-decoration: none;
      padding: 0.28rem 0 0.28rem 0.75rem; margin-left: 0.6rem;
      border-left: 2px solid var(--ice); transition: color 0.18s, border-color 0.18s;
    }
    .sidebar-link:hover { color: var(--ink); border-left-color: var(--steel); }
    .sidebar-link.active { color: var(--indigo); border-left-color: var(--indigo); font-weight: 500; }
    .sidebar-enquiry { font-size: 0.8rem; color: var(--slate); line-height: 1.6; margin-top: 2rem; }
    .sidebar-enquiry a { color: var(--indigo); font-weight: 500; text-decoration: none; }

    /* Families */
    .families { padding-left: 3rem; min-width: 0; }
    .family-block { margin-bottom: 3.8rem; scroll-margin-top: 88px; }
    .family-header { margin-bottom: 1.2rem; padding-bottom: 1rem; border-bottom: 2px solid var(--ink); }
    .family-tags { display: flex; gap: 0.4rem; flex-wrap: wrap; margin-bottom: 0.8rem; align-items: center; }
    .app-tag {
      display: inline-flex; align-items: center; gap: 0.45rem;
      font-size: 0.66rem; font-weight: 600; letter-spacing: 0.12em; text-transform: uppercase;
      color: var(--indigo); margin-right: 0.4rem;
    }
    .prop-tag { font-size: 0.78rem; color: var(--slate); }
    .prop-tag::before { content: '\00B7'; color: var(--steel); margin: 0 0.5rem 0 0.1rem; }
    .family-name { font-family: var(--display); font-size: 1.75rem; font-weight: 600; line-height: 1.15; margin-bottom: 0.5rem; }
    .family-desc { font-size: 0.9rem; color: var(--slate); line-height: 1.7; max-width: 680px; }

    /* Tables */
    .product-table { width: 100%; border-collapse: collapse; }
    .product-table th {
      font-size: 0.64rem; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase;
      color: var(--steel); text-align: left; padding: 0.5rem 0.75rem 0.5rem 0;
      border-bottom: 1px solid var(--ice);
    }
    .product-table th:last-child { text-align: right; }
    .product-table tbody tr { border-bottom: 1px solid var(--ice); transition: background 0.15s; }
    .product-table tbody tr:hover { background: var(--mist); }
    .product-table td { padding: 0.7rem 0.75rem 0.7rem 0; vertical-align: middle; }
    .td-part {
      font-family: 'DM Mono', 'Courier New', monospace; font-size: 0.8rem;
      color: var(--indigo); white-space: nowrap; width: 190px;
    }
    .td-req { font-family: var(--body); font-style: italic; color: var(--steel); }
    .td-name { font-size: 0.88rem; color: var(--ink); }
    .td-action { text-align: right; white-space: nowrap; }
    .enquire-link {
      font-size: 0.68rem; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase;
      color: var(--indigo); text-decoration: none; border: 1px solid var(--ice);
      padding: 0.3rem 0.7rem; display: inline-block; transition: all 0.18s;
    }
    .enquire-link:hover { background: var(--indigo); border-color: var(--indigo); color: var(--white); }

    /* CTA */
    .cta-band { background: var(--ink); color: var(--white); padding: 5rem 5vw; text-align: center; }
    .cta-band h2 { font-family: var(--display); font-size: clamp(1.9rem, 3.6vw, 2.8rem); font-weight: 500; line-height: 1.15; margin-bottom: 0.9rem; }
    .cta-band h2 em { font-style: italic; color: var(--sky); }
    .cta-band p { font-size: 1rem; font-weight: 300; color: var(--ice); margin-bottom: 2.2rem; }
    .cta-button {
      display: inline-block; font-size: 0.72rem; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase;
      color: var(--ink); background: var(--white); padding: 1rem 2.4rem; text-decoration: none; transition: background 0.2s;
    }
    .cta-button:hover { background: var(--ice); }

    footer {
      background: var(--ink); padding: 2rem 5vw; border-top: 1px solid rgba(157,185,220,0.18);
      display: flex; justify-content: space-between; align-items: center; gap: 1rem; flex-wrap: wrap;
      font-size: 0.72rem; color: var(--steel);
    }
    footer a { color: var(--ice); text-decoration: none; font-weight: 600; letter-spacing: 0.2em; text-transform: uppercase; font-size: 0.68rem; }

    .lang-switch { display: flex; align-items: center; gap: 0.5rem; font-size: 0.66rem; font-weight: 500; letter-spacing: 0.14em; }
    .lang-opt { color: var(--sky); text-decoration: none; }
    .lang-opt:hover { color: var(--white); }
    .lang-opt.active { color: var(--white); font-weight: 600; }
    .lang-sep { color: var(--steel); }

    @media (max-width: 860px) {
      .products-layout { grid-template-columns: 1fr; padding: 2.5rem 16px 4rem; }
      .sidebar { display: none; }
      .families { padding-left: 0; }
      .product-table th:first-child, .product-table td:first-child { display: none; }
      .page-header { padding: 104px 16px 48px; }
      .filter-bar { padding: 1.2rem 16px; }
      nav { padding: 0 16px; }
      .nav-link { display: none; }
      .nav-logo { font-size: 0.66rem; letter-spacing: 0.14em; white-space: nowrap; }
      .nav-cta { display: none; }
      .nav-right { gap: 1rem; }
      .cta-band { padding: 4rem 16px; }
      footer { flex-direction: column; align-items: flex-start; padding: 1.8rem 16px; }
    }
"""

JS = r"""
    const filterBtns = document.querySelectorAll('.filter-btn');
    const blocks = document.querySelectorAll('.family-block');
    filterBtns.forEach(btn => btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const f = btn.dataset.filter;
      blocks.forEach(b => { b.style.display = (f === 'all' || b.dataset.app === f) ? '' : 'none'; });
    }));

    const links = document.querySelectorAll('.sidebar-link');
    const obs = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          links.forEach(l => l.classList.remove('active'));
          const a = document.querySelector(`.sidebar-link[href="#${e.target.id}"]`);
          if (a) a.classList.add('active');
        }
      });
    }, { rootMargin: '-30% 0px -60% 0px' });
    blocks.forEach(b => obs.observe(b));
"""

PAGE = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Product Range | Meridian Industrial Co.</title>
  <meta name="description" content="Garland industrial cable for mining, transport, communications and security: blast wire, power, instrumentation, data, fibre, traffic, rail, fire alarm and CCTV cable." />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet" />
  <style>{CSS}  </style>
  <!-- Umami analytics: no cookies -->
  <script defer src="https://cloud.umami.is/script.js" data-website-id="94bee893-eeed-4368-afdb-194bfc29fc61"></script>
</head>
<body>

  <nav>
    <a href="/" class="nav-logo">Meridian Industrial Co.</a>
    <div class="nav-right">
      <a href="/" class="nav-link">Home</a>
      <div class="lang-switch"><a href="/products.html" class="lang-opt active">EN</a><span class="lang-sep">|</span><a href="/fr/products.html" class="lang-opt">FR</a></div>
      <a href="mailto:{MAIL}" class="nav-cta">Make an Enquiry</a>
    </div>
  </nav>

  <header class="page-header">
    <div class="page-header-inner">
      <p class="page-eyebrow">Product Range</p>
      <h1 class="page-title">Every cable your operation depends on, <em>from one supplier.</em></h1>
      <p class="page-intro">A selection from the Garland range, grouped by application. Ask us for other sizes, lengths and colours. For datasheets or pricing, use the enquiry link on any line.</p>
    </div>
  </header>

  <div class="filter-bar">
{filters_html()}
  </div>

  <div class="products-layout">
    <aside class="sidebar">
{sidebar_html()}
      <div class="sidebar-enquiry">
        <p>Don't see what you need?<br><a href="mailto:{MAIL}">Contact us.</a> Garland builds to order.</p>
      </div>
    </aside>

    <div class="families">{''.join(family_html(f) for f in FAMILIES)}

    </div>
  </div>

  <div class="cta-band">
    <h2>Need a specification outside this range?<br><em>Garland builds to order.</em></h2>
    <p>This page shows a selection. Tell us what your site needs and we'll find it in the full range, or build it. We respond within 24 hours.</p>
    <a href="mailto:{MAIL}" class="cta-button">Make an Enquiry</a>
  </div>

  <footer>
    <a href="/">Meridian Industrial Co.</a>
    <span>© 2026 Meridian Industrial Co. All rights reserved.</span>
  </footer>

  <script>{JS}  </script>

</body>
</html>
"""

if __name__ == "__main__":
    import sys
    out = sys.argv[1] if len(sys.argv) > 1 else "products.html"
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(PAGE)
    print("wrote", out)
