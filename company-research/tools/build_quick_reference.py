from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = Workbook()

# ═══════════════════════════════════════════════════════════════════════════════
# THEME  — one set of rules applied uniformly across every sheet
# ═══════════════════════════════════════════════════════════════════════════════
# Backgrounds
NAVY      = "1B3A6B"   # section headers (all sheets)
MID_BG    = "D6E4F0"   # column headers  (all sheets)
LIGHT_BG  = "EEF2F8"   # alternating row tint
WHITE     = "FFFFFF"

# Status colours
GREEN_BG  = "C6EFCE";  GREEN_FG  = "276221"
YELLOW_BG = "FFEB9C";  YELLOW_FG = "9C6500"
RED_BG    = "FFC7CE";  RED_FG    = "9C0006"

# Tab accent colours (used ONLY for the title banner row on each sheet)
TAB = {
    "Origin":               "1B6BA0",
    "Array":                "217346",
    "Vector":               "7B3F9E",
    "External Software":    "1B3A6B",
    "Internal Stack":       "404040",
    "Target Customer Profiles": "B8520A",
    "Competitors":          "6B1A1A",
    "Buyer & User Personas":"4B2D8F",
}

# ── Style helpers ─────────────────────────────────────────────────────────────
def bold(size=10, color="000000"):
    return Font(name="Arial", bold=True, size=size, color=color)
def reg(size=10, color="000000"):
    return Font(name="Arial", bold=False, size=size, color=color)
def fill(hex_color):
    return PatternFill("solid", fgColor=hex_color)
def walign(h="left", v="top"):
    return Alignment(wrap_text=True, horizontal=h, vertical=v)
def border():
    s = Side(style="thin", color="CCCCCC")
    return Border(left=s, right=s, top=s, bottom=s)
def cw(ws, col, w):
    ws.column_dimensions[get_column_letter(col)].width = w

# ── Universal cell writers ────────────────────────────────────────────────────
def title_cell(ws, tab_name, ncols, text):
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=ncols)
    c = ws.cell(row=1, column=1, value=text)
    c.font = bold(12, WHITE)
    c.fill = fill(TAB[tab_name])
    c.alignment = walign("center", "center")
    c.border = border()
    for col in range(2, ncols + 1):
        mc = ws.cell(row=1, column=col)
        mc.fill = fill(TAB[tab_name])
        mc.border = border()
    ws.row_dimensions[1].height = 24

def col_headers(ws, row, headers):
    ws.row_dimensions[row].height = 18
    for c, h in enumerate(headers, 1):
        cell = ws.cell(row=row, column=c, value=h)
        cell.font = bold(10)
        cell.fill = fill(MID_BG)
        cell.alignment = walign("center", "center")
        cell.border = border()

def section_hdr(ws, row, label, ncols):
    ws.row_dimensions[row].height = 18
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=ncols)
    c = ws.cell(row=row, column=1, value=label)
    c.font = bold(10, WHITE)
    c.fill = fill(NAVY)
    c.alignment = walign("left", "center")
    c.border = border()
    for col in range(2, ncols + 1):
        mc = ws.cell(row=row, column=col)
        mc.fill = fill(NAVY)
        mc.border = border()

def data_row(ws, row, values, shade=False, height=42):
    bg = LIGHT_BG if shade else WHITE
    ws.row_dimensions[row].height = height
    for c, v in enumerate(values, 1):
        cell = ws.cell(row=row, column=c, value=v)
        cell.font = reg(10)
        cell.fill = fill(bg)
        cell.alignment = walign()
        cell.border = border()

def spacer_row(ws, row):
    ws.row_dimensions[row].height = 6
    for c in range(1, ws.max_column + 2):
        cell = ws.cell(row=row, column=c)
        cell.fill = fill("E0E0E0")
        cell.border = border()

def setup_ws(ws, tab_name):
    ws.sheet_view.showGridLines = False
    ws.sheet_properties.tabColor = TAB[tab_name]
    ws.freeze_panes = "A3"

# ═══════════════════════════════════════════════════════════════════════════════
# ROBOT SHEET BUILDER
# ═══════════════════════════════════════════════════════════════════════════════
def robot_sheet(ws, tab_name, rows_data):
    setup_ws(ws, tab_name)
    title_cell(ws, tab_name, 3, f"LOCUS ROBOTICS  ·  {tab_name.upper()}  QUICK REFERENCE")
    col_headers(ws, 2, ["METRIC", "VALUE", "DESCRIPTION"])
    cw(ws, 1, 28); cw(ws, 2, 22); cw(ws, 3, 55)
    r = 3
    shade = False
    for item in rows_data:
        if item[0] == "SECTION":
            section_hdr(ws, r, item[1], 3)
            shade = False
        else:
            data_row(ws, r, [item[1], item[2], item[3]], shade)
            shade = not shade
        r += 1

# ── Deployment scale blocks ───────────────────────────────────────────────────
FLEET_SCALE = [
    ("SECTION", "DEPLOYMENT SCALE"),
    ("ROW", "Customer Sites",       "350+ sites / 150+ customers",
     "20+ countries across NA, EMEA, APAC. Source: Locus press release, Oct 2025."),
    ("ROW", "Active Robots",        "Tens of thousands (fleet-wide)",
     "Exact per-model split not published. Majority of deployed units are Origin. Source: Automated Warehouse, Oct 2025."),
    ("ROW", "Total Lifetime Picks", "6B+ picks (fleet-wide)",
     "Hit 6B in Oct 2025; last 1B in 24 weeks — fastest pace in company history. Source: Automated Warehouse, Oct 2025."),
    ("ROW", "Annual Throughput",    "1.8B units in 2024 (+50% YoY)",
     "45M picks/week in 2025; on track for 60M/week in Q4 peak. Source: Locus press release, Oct 2025."),
    ("ROW", "RaaS Pricing",         "~$1,990/mo + ~$35K hardware (illustrative)",
     "One third-party source only — not officially published. Use directionally; do NOT quote to customers."),
    ("ROW", "Avg ROI Timeframe",    "6 months or less (Locus claim)",
     "Locus claim. Industry median ~13 months. Staples Canada: 1M picks in 70 days. 500K sq ft DC: under 18 months."),
]

ARRAY_SCALE = [
    ("SECTION", "DEPLOYMENT SCALE"),
    ("ROW", "Customer Sites",       "Early access only (DHL Supply Chain)",
     "Launched April 2026. DHL is primary early-access customer. Broader commercial deployments pending."),
    ("ROW", "Active Robots",        "Not publicly disclosed",
     "Too early for published deployment counts. Check with product team for latest."),
    ("ROW", "Fleet-Level Picks",    "Included in 6B+ fleet total",
     "Array pick volume not broken out separately. All Locus robots contribute to the 6B+ figure."),
    ("ROW", "RaaS Pricing",         "Premium tier (not published)",
     "Expected significantly higher than Origin. Exact pricing not disclosed."),
    ("ROW", "Avg ROI Timeframe",    "TBD — insufficient data",
     "Too early to publish. Apply general Locus claim (<6 months) with heavy caveat given brand-new product stage."),
    ("ROW", "Industry Awards",      "RBR50 / AI Breakthrough / AI Excellence (2026)",
     "Three major awards within weeks of launch — strong third-party validation for a brand-new product."),
]

# ── Robot data ────────────────────────────────────────────────────────────────
origin_data = [
    ("SECTION","IDENTITY"),
    ("ROW","Robot Name","Locus Origin","Collaborative AMR — the flagship Locus robot since 2016"),
    ("ROW","Robot Type","Person-to-Goods (P2G)","Robot navigates to pick location; human picker places item in tote"),
    ("ROW","Launch Year","2016","Most battle-tested robot in the portfolio; 10 years in production"),
    ("ROW","Best-Fit Workflows","Order picking, putaway","High-volume e-commerce, retail, 3PL fulfillment"),
    ("SECTION","PHYSICAL SPECS"),
    ("ROW","Payload Capacity","36 kg / 79 lbs","Tote capacity for picked items carried by the robot"),
    ("ROW","Dimensions (LxWxH)","558 x 558 x 1,468 mm","Compact footprint fits standard warehouse aisle widths"),
    ("ROW","Robot Weight","45 kg / 99 lbs",""),
    ("ROW","Max Speed","5 m/s (~11 mph)","Faster than walking pace; slows near associates for safety"),
    ("ROW","Mobility Type","Standard wheeled","Forward/reverse/turn; not omnidirectional"),
    ("SECTION","OPERATIONAL PERFORMANCE"),
    ("ROW","UPH (with robots)","120-150 units/hour","Up from 30-40 UPH manual — 2-3x improvement per worker"),
    ("ROW","UPH Improvement","2-3x vs. manual","DHL reported 30-180% increase across 40+ sites"),
    ("ROW","Training Time","80% reduction (DHL)","Intuitive screen interface; minimal training required"),
    ("ROW","Operating Hours","Multi-shift capable","Charges autonomously between missions at docking stations"),
    ("ROW","Accuracy","High (not publicly specified)","Vision-guided interface reduces pick errors vs. paper/RF"),
    ("SECTION","FLEET & INTEGRATION"),
    ("ROW","Picker-to-Robot Ratio","1 robot : 2-3 human pickers","Standard ratio; varies by facility density and order profile"),
    ("ROW","Works Alongside","Locus Vector, Locus Array","Unified LocusONE fleet — coordinates across robot types"),
    ("ROW","WMS Integration","API (any WMS)","Named: Manhattan Associates, Blue Yonder, Logiwa, Made4Net, Tecsys"),
    ("ROW","Track Record","2B+ picks / 300+ deployments","Most proven robot in the Locus portfolio"),
] + FLEET_SCALE + [
    ("SECTION","KEY DIFFERENTIATOR"),
    ("ROW","Why Origin","Proven at scale, lowest barrier to entry",
     "Drops into existing brownfield operations without facility redesign. No new infrastructure needed. Fastest path to ROI in the Locus fleet."),
    ("SECTION","HONEST LIMITATIONS"),
    ("ROW","Labor Dependency","Still requires human picker","If you can't staff the floor, the robot sits idle. Does NOT eliminate labor — it augments it."),
    ("ROW","Throughput Ceiling","Tied to picker count + speed","Can't scale throughput beyond what your labor force can physically support"),
    ("ROW","Heavy Goods","36 kg payload limit","Large or heavy SKUs require Vector or a different solution entirely"),
    ("ROW","Low-Density Risk","Sparse SKU layout reduces gains","Wide-spread facilities with few picks per aisle see diminished travel efficiency benefits"),
    ("ROW","Aisle Constraints","Standard wheels; needs clear path","Very narrow, cluttered, or congested aisles reduce effectiveness and safety margin"),
]

array_data = [
    ("SECTION","IDENTITY"),
    ("ROW","Robot Name","Locus Array","Fully autonomous picking robot — no human required in the picking zone"),
    ("ROW","Robot Type","Robots-to-Goods (R2G) Autonomous","Robot navigates to shelf AND picks the item itself using AI-guided arm"),
    ("ROW","Launch Year","April 2026","Brand new. DHL Supply Chain is primary early-access customer."),
    ("ROW","Best-Fit Workflows","Picking, putaway, induction, replenishment, slotting, deplenishment",
     "End-to-end autonomous fulfillment within a dedicated aisle zone"),
    ("SECTION","PHYSICAL SPECS"),
    ("ROW","Tote Capacity","6 order totes simultaneously","Each tote up to 66 lbs; operates rack-to-tote directly in the aisle"),
    ("ROW","Reach Height","Up to 10 ft (3 m)","Picks from either side of very narrow aisle across 10-ft rack height"),
    ("ROW","Mobility Type","Omnidirectional (Vector-derived)","Tight turns in narrow aisles; slides alongside shelving on either side"),
    ("ROW","Picking Mechanism","Vision-guided robotic arm","Suction cup end effectors + NeuraGrasp AI for irregular shapes and polybags"),
    ("ROW","AI Grasping","NeuraGrasp (Nexera acquisition)","Patented grasping tech; handles items traditional suction systems can't"),
    ("SECTION","OPERATIONAL PERFORMANCE"),
    ("ROW","SKU Coverage (solo)","60-70% of e-comm SKUs","Includes ~30% of polybag SKUs; remaining covered by Origin + Vector"),
    ("ROW","SKU Coverage (fleet)","100% when paired w/ Origin + Vector","Unified LocusONE fleet covers full SKU catalog across all robot types"),
    ("ROW","Labor Reduction","Up to 90% in automated zone","Near-zero-touch fulfillment within the Array-dedicated aisle zone"),
    ("ROW","Accuracy","99.9% (stated)","Vision-guided picking with AI validation at point of grasp"),
    ("ROW","Operating Hours","24/7 capable","No labor dependency for covered workflows; runs overnight shifts autonomously"),
    ("SECTION","FLEET & INTEGRATION"),
    ("ROW","Works Alongside","Locus Origin, Locus Vector","Handles autonomous zone; Origin + Vector cover remaining SKUs and heavy transport"),
    ("ROW","WMS Integration","Via LocusONE API","Same integration layer as Origin and Vector; no separate WMS connection needed"),
    ("ROW","Awards (since launch)","2026 RBR50 / AI Breakthrough / AI Excellence",
     "Three major industry awards within weeks of launch — unusually fast market validation"),
] + ARRAY_SCALE + [
    ("SECTION","KEY DIFFERENTIATOR"),
    ("ROW","Why Array","Only Locus robot with zero labor dependency in its zone",
     "Combines mobile robotics + picking arm + AI grasping in one unit. Gets smarter over time as LocusONE AI models improve with each pick."),
    ("SECTION","HONEST LIMITATIONS"),
    ("ROW","New to Market","Launched April 2026","Very limited deployment track record. DHL is the primary early access site. Buying risk is real."),
    ("ROW","SKU Coverage Gap","30-40% not coverable autonomously","Polybags, very light items, irregular shapes, and oversized items remain challenging"),
    ("ROW","Facility Requirements","Requires dedicated narrow-aisle racking up to 10 ft",
     "Most brownfield sites need layout modifications. Not a drop-in like Origin."),
    ("ROW","Implementation Complexity","Higher than Origin","More infrastructure, longer deployment runway, more complex change management"),
    ("ROW","Cost","Premium tier (unpublished)","Expected significantly higher RaaS rate than Origin. ROI case needs careful modeling."),
]

vector_data = [
    ("SECTION","IDENTITY"),
    ("ROW","Robot Name","Locus Vector","Heavy-payload AMR for material transport and handling"),
    ("ROW","Robot Type","Heavy Transport AMR","Moves heavy goods through facility; not a picking or fulfillment solution"),
    ("ROW","Launch Year","2023 (acquired from Waypoint Robotics)","Newest robot in the Locus portfolio; still building deployment track record"),
    ("ROW","Best-Fit Workflows","Transport, replenishment, putaway, heavy goods movement",
     "Moves product between zones; supports fulfillment operations indirectly"),
    ("SECTION","PHYSICAL SPECS"),
    ("ROW","Payload Capacity","Up to 272 kg / 600 lbs","Industrial strength; purpose-built for heavy goods that Origin cannot carry"),
    ("ROW","Mobility Type","Omnidirectional","Maneuvers in virtually any orientation; handles extremely tight spaces"),
    ("ROW","Navigation","Dual safety-rated LiDAR + 3-stage safety system",
     "Operates safely alongside workers, forklifts, and other equipment"),
    ("ROW","Chassis","Industrial strength","Built for repeated heavy-load cycles in warehouse environments"),
    ("SECTION","OPERATIONAL PERFORMANCE"),
    ("ROW","Productivity Improvement","50% (GEODIS Dallas TX)","12 Vectors across 40,000 sq ft picking area; 50% productivity gain"),
    ("ROW","Operating Hours","Multi-shift capable",""),
    ("ROW","Cycle Time","Significantly reduced (stated)","State-of-the-art sensors and algorithms reduce cycle times vs. manual transport"),
    ("SECTION","FLEET & INTEGRATION"),
    ("ROW","Works Alongside","Locus Origin, Locus Array","Handles heavy/transport tasks Origin and Array cannot; same LocusONE platform"),
    ("ROW","WMS Integration","Via LocusONE API","Unified integration layer shared across the full Locus fleet"),
    ("ROW","Notable Deployment","GEODIS — expanding to 1,000 LocusBots worldwide",
     "GEODIS committed to 1,000-bot global deployment after Dallas TX Vector success"),
] + FLEET_SCALE + [
    ("SECTION","KEY DIFFERENTIATOR"),
    ("ROW","Why Vector","Only robot in the fleet that handles heavy payloads (600 lbs)",
     "Omnidirectional mobility navigates spaces where forklifts can't. Fills the transport gap Origin and Array don't address."),
    ("SECTION","HONEST LIMITATIONS"),
    ("ROW","Not a Picking Solution","Does not fulfill orders","Cannot replace pickers or Array for order fulfillment. Transport only."),
    ("ROW","Niche Use Case","Only relevant when heavy transport is a bottleneck",
     "Most standard e-comm operations won't need it as primary robot. Usually sold as a fleet complement."),
    ("ROW","Less Proven","Launched 2023; fewer public deployments","Origin has years of battle-tested track record. Vector is still building its portfolio."),
    ("ROW","Space Requirements","Large chassis despite omnidirectional movement",
     "Aisles must accommodate its footprint and turning radius even with omnidirectional capability"),
]

ws_origin = wb.active
ws_origin.title = "Origin"
robot_sheet(ws_origin, "Origin", origin_data)

ws_array = wb.create_sheet("Array")
robot_sheet(ws_array, "Array", array_data)

ws_vector = wb.create_sheet("Vector")
robot_sheet(ws_vector, "Vector", vector_data)

# ═══════════════════════════════════════════════════════════════════════════════
# EXTERNAL SOFTWARE
# ═══════════════════════════════════════════════════════════════════════════════
ws_ext = wb.create_sheet("External Software")
setup_ws(ws_ext, "External Software")
title_cell(ws_ext, "External Software", 6, "LOCUS ROBOTICS  ·  EXTERNAL (CUSTOMER-FACING) SOFTWARE & PRODUCTS")
col_headers(ws_ext, 2, ["PRODUCT","TYPE","WHO USES IT","CORE FUNCTION","KEY METRICS / OUTPUTS","INTEGRATION POINT"])
cw(ws_ext,1,22); cw(ws_ext,2,20); cw(ws_ext,3,22); cw(ws_ext,4,35); cw(ws_ext,5,35); cw(ws_ext,6,28)

ext_rows = [
    ("LocusONE Platform","Orchestration Platform","Customer IT + ops leadership",
     "Central intelligence layer coordinating all robots, labor, and WMS",
     "Fleet management, order routing, WES functionality, multi-site visibility","WMS API (any system)"),
    ("LocusHub","Analytics Dashboard","Customer supervisors, ops managers",
     "Real-time KPI monitoring and reporting across all sites",
     "UPH, LPH, robot productivity, worker productivity, asset status, 24+ reports","LocusONE + WMS"),
    ("System Directed Labor (SDL)","AI Agent (patent-pending)","Floor associates",
     "Real-time labor coordination — directs workers to next optimal task via on-robot UI",
     "Task routing prompts, labor utilization, throughput balancing","LocusONE (on-robot screen)"),
    ("Mission Optimization","AI Routing Engine","Automated (no user-facing UI)",
     "Clusters picks by density, shortens cycle times, dynamically allocates tasks across robot types",
     "Pick density improvement, cycle time reduction, multi-workflow allocation","LocusONE (internal)"),
    ("Advanced Simulation","Pre-Deployment Modeling Tool","SE / Customer Success / Prospects",
     "Fleet sizing, ROI forecasting, and design validation before deployment",
     "Robot count recommendations, payback projections, throughput estimates, layout validation","Pre-deployment (standalone)"),
    ("NeuraGrasp","AI Grasping System","Array robot (onboard)",
     "Vision-guided picking AI enabling Array to grasp irregular SKUs including polybags",
     "60-70% e-comm SKU coverage solo; 99.9% accuracy; ~30% polybag coverage","Array hardware (Nexera Robotics acquisition)"),
    ("Robot User Interface","Associate-Facing Screen","Floor pickers (Origin workflow)",
     "Displays item image, quantity, and pick location on robot's touch screen",
     "Reduced pick errors, 80% reduction in training time (DHL)","Origin robot screen / LocusONE"),
]
for i, row in enumerate(ext_rows):
    data_row(ws_ext, i + 3, list(row), i % 2 == 0, height=50)

# ═══════════════════════════════════════════════════════════════════════════════
# INTERNAL STACK
# ═══════════════════════════════════════════════════════════════════════════════
ws_int = wb.create_sheet("Internal Stack")
setup_ws(ws_int, "Internal Stack")
title_cell(ws_int, "Internal Stack", 5, "LOCUS ROBOTICS  ·  INTERNAL TOOLS & TECHNOLOGY STACK")
col_headers(ws_int, 2, ["CATEGORY","TOOL / PLATFORM","CONFIDENCE","WHAT IT'S USED FOR","SOURCE"])
cw(ws_int,1,24); cw(ws_int,2,24); cw(ws_int,3,14); cw(ws_int,4,45); cw(ws_int,5,40)

int_sections = [
    ("DATA ANALYSIS / SE & PRE-SALES", [
        ("Excel (Advanced)","High","Customer data analysis, concept system designs, ROI models","Senior SE JD — Greenhouse (directly fetched)"),
        ("SQL","High","Data querying and manipulation of warehouse and customer data","Senior SE JD + Data Architect LinkedIn JD"),
        ("Python","High","Data analysis, scripting, and ML/AI workflows","Senior SE JD + AI Enterprise Architect JD (directly fetched)"),
        ("PowerBI","High","Reporting dashboards for SE work and customer-facing outputs","Senior SE JD — Greenhouse (directly fetched)"),
        ("AutoCAD","High","Facility layout design and warehouse mapping for concept designs","Senior SE JD + Deployment Engineer JD (both directly fetched)"),
        ("FlexSim","High","Simulation of warehouse throughput for fleet sizing and ROI forecasting","Senior SE JD — Greenhouse (directly fetched)"),
    ]),
    ("DATA ARCHITECTURE / BACKEND", [
        ("Databricks (Lakehouse)","High","Enterprise analytical data platform and data warehouse layer","AI Enterprise Architect JD — explicitly named (directly fetched)"),
        ("AWS / Azure / GCP","High","Cloud infrastructure (5+ yrs hands-on required in JD)","AI Enterprise Architect JD (directly fetched)"),
        ("ETL/ELT Pipelines","High","Data movement and integration across enterprise systems","AI Enterprise Architect JD (directly fetched)"),
        ("SQL Server, Oracle, MongoDB, AWS RDS & Aurora","Medium","Operational and analytical databases across the stack","Data Architect LinkedIn JD (search summary)"),
        ("Metadata / Data Catalog","Medium","Data governance, lineage tracking, and data quality frameworks","AI Enterprise Architect JD (directly fetched)"),
    ]),
    ("BI / REPORTING", [
        ("PowerBI","High","Internal reporting and dashboards; also used in SE pre-sales work","Senior SE JD (directly fetched)"),
        ("Looker","Medium","BI tool — listed as preferred in past Data Engineer posting","Data Engineer posting via aijobs.net (search summary)"),
        ("GA4 (Google Analytics 4)","High","Web analytics for locusrobotics.com and digital properties","Digital Experience Manager JD (directly fetched)"),
        ("Google Tag Manager","High","Tag management for web tracking and analytics","Digital Experience Manager JD (directly fetched)"),
    ]),
    ("AI / LLM STACK", [
        ("GPT-4 / Claude","High","Foundation models for enterprise AI workflows and agentic systems","AI Enterprise Architect JD — explicitly named (directly fetched)"),
        ("RAG Architecture","High","LLM-powered retrieval over enterprise data sources","AI Enterprise Architect JD (directly fetched)"),
        ("Agentic Workflows","High","Automated end-to-end business process automation across Sales, CS, Finance, Ops","AI Enterprise Architect JD (directly fetched)"),
        ("ROS (Robot Operating System)","High","Robot navigation, control, and sensor processing","Deployment Engineer JD (directly fetched)"),
        ("SLAM Navigation","High","Simultaneous Localization and Mapping for warehouse floor maps","Deployment Engineer JD + LocusONE product page (directly fetched)"),
    ]),
    ("MARKETING / CRM STACK", [
        ("Marketo","High","Marketing automation — email, nurture, campaign management","Digital Experience Manager JD (directly fetched)"),
        ("6sense / Demandbase","High","Intent data and account-based marketing (ABM) targeting","Digital Experience Manager JD (directly fetched)"),
        ("WordPress","High","Website CMS for locusrobotics.com","Digital Experience Manager JD (directly fetched)"),
        ("A/B Testing / Personalization Platforms","High","Conversion optimization and web personalization","Digital Experience Manager JD (directly fetched)"),
    ]),
]

r = 3
for section_name, tools in int_sections:
    section_hdr(ws_int, r, section_name, 5)
    r += 1
    shade = False
    for tool, conf, usage, source in tools:
        data_row(ws_int, r, [section_name, tool, conf, usage, source], shade)
        # Override confidence cell
        conf_cell = ws_int.cell(row=r, column=3)
        if conf == "High":
            conf_cell.font = bold(10, GREEN_FG); conf_cell.fill = fill(GREEN_BG)
        elif conf == "Medium":
            conf_cell.font = bold(10, YELLOW_FG); conf_cell.fill = fill(YELLOW_BG)
        shade = not shade
        r += 1

# ═══════════════════════════════════════════════════════════════════════════════
# TARGET CUSTOMER PROFILES
# ═══════════════════════════════════════════════════════════════════════════════
ws_cp = wb.create_sheet("Target Customer Profiles")
setup_ws(ws_cp, "Target Customer Profiles")
title_cell(ws_cp, "Target Customer Profiles", 4, "LOCUS ROBOTICS  ·  TARGET CUSTOMER PROFILES  —  Who to Prioritize")
col_headers(ws_cp, 2, ["CRITERIA","STRONG FIT","MID FIT","WEAK FIT / PASS"])
cw(ws_cp,1,26); cw(ws_cp,2,38); cw(ws_cp,3,38); cw(ws_cp,4,38)
ws_cp.row_dimensions[2].height = 20

cp_rows = [
    ("Volume (units/day)","30,000 – 500,000+","10,000 – 30,000","Under 10,000 — volume too low to justify RaaS economics"),
    ("Facility Size","50,000 sq ft – 1M+ sq ft","25,000 – 50,000 sq ft","Under 25,000 sq ft OR massive fixed-automation facility already locked in"),
    ("Labor Situation","High turnover, labor scarcity, rising wages, hard to recruit and retain pickers","Moderate labor stability; seasonal spikes create stress","Stable, low-cost labor with no retention issues — no urgency to automate"),
    ("WMS Maturity","Modern WMS with clean API (Manhattan Associates, Blue Yonder, Logiwa, Made4Net, Tecsys, etc.)","Older WMS that can integrate via middleware; willing to invest in integration work","No WMS, fully custom legacy system with no API, or IT bandwidth unavailable"),
    ("Order Profile","High-velocity, repetitive SKU picks; e-comm, retail, 3PL fulfillment; mixed small-item SKU catalog","Mixed profiles with some heavy goods; manageable with Origin + Vector combo","Very large/heavy-only SKUs; single-SKU bulk shipments; pure cold chain; manufacturing"),
    ("Budget / Pricing Model","Prefers OpEx over CapEx; open to RaaS subscription; values predictable monthly cost","Mixed CapEx/OpEx appetite; needs ROI proof; long procurement process","Requires full CapEx ownership; resistant to subscription model; CFO won't approve monthly fees"),
    ("Automation Readiness","Has evaluated or piloted AMRs; understands ROI timeline; executive champion in place","Exploring automation but early stage; needs education and proof-of-concept; no internal champion","No automation experience; skeptical of ROI; floor management resistance; no internal advocate"),
    ("Peak Volume Variability","Significant peak vs. off-peak swings (holiday, promotional surges) — RaaS elasticity is a direct advantage","Some seasonality but manageable with current staff plus overtime","Flat, predictable volume year-round — RaaS elasticity is not a selling point"),
    ("Customer Archetypes","DHL / GEODIS-style large 3PLs; major e-comm brands (apparel, beauty, healthcare); multi-site retail DCs","Regional 3PLs scaling up; mid-market specialty retail; food service wholesale distribution","Single-site boutique retailers; manufacturing plants; bulk commodity shippers"),
    ("Competitive Dynamic","Considering multiple AMR vendors (Locus, 6RS, Fetch) — Locus wins on track record and unified fleet","Evaluating automation broadly; not sure if AMR vs. ASRS or fixed conveyor is right","Already committed to a competitor or fixed automation; vendor relationship locked in"),
    ("Red Flags (pass quickly)","—","—","No WMS / Under 10K units/day / Locked into competitor / Fixed automation deployed / Pure cold chain / CFO opposed to OpEx"),
]

for i, (criteria, strong, mid, weak) in enumerate(cp_rows):
    r = i + 3
    ws_cp.row_dimensions[r].height = 55
    shade = i % 2 == 0
    for c, (v, fg) in enumerate(zip([criteria, strong, mid, weak],
                                     ["000000", GREEN_FG, YELLOW_FG, RED_FG]), 1):
        bg_base = LIGHT_BG if shade else WHITE
        bgs = [bg_base,
               "EBF5EB" if shade else "F5FFF5",
               "FFF9E6" if shade else "FFFFF5",
               "FFEDEC" if shade else "FFF5F5"]
        cell = ws_cp.cell(row=r, column=c, value=v)
        cell.font = bold(10) if c == 1 else reg(10, fg)
        cell.fill = fill(bgs[c - 1])
        cell.alignment = walign()
        cell.border = border()

# ═══════════════════════════════════════════════════════════════════════════════
# COMPETITORS
# ═══════════════════════════════════════════════════════════════════════════════
ws_comp = wb.create_sheet("Competitors")
setup_ws(ws_comp, "Competitors")
COMP_COLS = ["COMPETITOR","TYPE","ROBOT OFFERING","SOFTWARE OFFERING",
             "DEPLOYMENT SCALE","STRENGTHS VS. LOCUS","WEAKNESSES VS. LOCUS","CONFIDENCE / SOURCE"]
title_cell(ws_comp, "Competitors", 8, "LOCUS ROBOTICS  ·  COMPETITIVE LANDSCAPE  —  Researched & Sourced")
col_headers(ws_comp, 2, COMP_COLS)
cw(ws_comp,1,18); cw(ws_comp,2,15); cw(ws_comp,3,30); cw(ws_comp,4,26)
cw(ws_comp,5,26); cw(ws_comp,6,36); cw(ws_comp,7,36); cw(ws_comp,8,30)

competitors = [
    ("DIRECT AMR COMPETITORS", [
        ("Geek+ (Geekplus)",
         "Direct AMR\nP2G + R2G",
         "G-series AMRs: goods-to-person pods, picking robots, sorting bots. Supports 5,000+ AMRs in a single warehouse. Launched Gino 1 humanoid Feb 2026.",
         "GeekOS orchestration platform. Multi-robot, multi-workflow coordination. Comparable scope to LocusONE.",
         "66,000+ robots deployed\n950+ customers\n40+ countries\n23% global AMR market share\n$378.7M revenue (2024)\nIPO'd HKSE July 2025",
         "Largest global AMR install base by volume. Broadest robot type catalog. Strong APAC + EMEA footprint. Public company = greater R&D resources.",
         "Chinese HQ = US enterprise data security concerns. Less US warehouse expertise. US support network thinner than Locus. Humanoid pivot is unproven distraction.",
         "HIGH\nIPO filings, Robot Report,\nInteract Analysis market data"),
        ("6 River Systems\n(now Ocado)",
         "Direct AMR\nP2G Collaborative",
         "Chuck robot — collaborative P2G AMR. 90.7 kg, 1.3 m/s. Associates batch-pick alongside Chuck. No autonomous picking equivalent to Array.",
         "Cloud-based WES. WMS integration layer. Similar concept to LocusONE but narrower scope.",
         "100+ warehouses\n70+ customers\nCustomers include GXO, DHL, XPO\nAcquired by Ocado (2023)",
         "Strong 3PL customer overlap with Locus (GXO, DHL). Ocado brand = enterprise credibility. Solid P2G workflow parity with Origin.",
         "Ocado acquisition created roadmap uncertainty. No autonomous picking capability. Fewer robot types. Less US-centric post-acquisition.",
         "HIGH\nOcado investor docs,\nRobot Report, 6RS announcements"),
        ("GreyOrange",
         "Direct AMR\n+ HW-Agnostic Orch.",
         "Ranger AMRs (multiple models). Hardware-agnostic CRN (Collaborative Robot Network) can orchestrate third-party robots alongside Ranger fleet.",
         "GreyMatter AI orchestration platform. Google Cloud partnership for GreyMatter DeepNav. SOC2 + ISO 27001 certified.",
         "100,000+ active agents claimed\nCustomer count not disclosed\nActive in NA, EMEA, APAC",
         "Hardware-agnostic = can layer on existing robot fleets. Google Cloud AI partnership. Strong compliance posture (SOC2/ISO27001).",
         "Requires WiFi 6 and specific floor specs — brownfield friction. No equivalent to Array's autonomous picking arm. 'Active agents' may include non-Ranger hardware.",
         "MEDIUM-HIGH\nGreyOrange website,\nGoogle partnership press release"),
    ]),
    ("WINDING DOWN — MAJOR DISPLACEMENT OPPORTUNITY FOR LOCUS", [
        ("Zebra Technologies\n/ Fetch Robotics",
         "WINDING DOWN\nAMR Division",
         "Fetch AMR fleet (multiple autonomous models). Division being wound down — no new product development. Most staff cut by end of 2025.",
         "FetchCore cloud platform. WMS integrations. No active development roadmap.",
         "~100 customers at peak\nWINDING DOWN\nExisting customers need to migrate",
         "OPPORTUNITY: Displaced Fetch customers are actively seeking migration paths. Locus should target these accounts directly. Zebra enterprise relationships may open doors.",
         "Customers face real support risk as division winds down. No new features or robots. Existing deployments are depreciating assets with no upgrade path.",
         "HIGH\nRobot Report reporting on\nZebra AMR wind-down"),
    ]),
    ("ADJACENT COMPETITORS (Different Category — For Competitive Positioning Conversations)", [
        ("AutoStore",
         "Adjacent\nCube ASRS\n(NOT an AMR)",
         "Grid robots (R5, B1) moving across a proprietary cube storage grid. High-density goods-to-person. Fixed infrastructure — not mobile.",
         "AutoStore WCS + third-party WMS integration. Grid controller. No equivalent to LocusONE fleet orchestration.",
         "1,900+ installations\n65+ countries\n~$596M revenue\n$500K–$2M+ entry cost per site",
         "Extreme storage density. Very high throughput for fast-moving SKUs. Proven at massive scale globally.",
         "MASSIVE CapEx ($500K–$2M+) vs. Locus RaaS OpEx. Requires full facility redesign — not brownfield. Fixed infrastructure can't flex with demand changes.",
         "HIGH\nAutoStore investor materials,\nRobot Report, public financials"),
        ("Symbotic",
         "Adjacent\nFixed DC Automation\n(NOT an AMR)",
         "Symbotic bots operating within a proprietary fixed grid inside purpose-built DCs. Pallet-to-piece fulfillment. Not modular or brownfield-compatible.",
         "Symbotic AI platform for put-away, retrieval, and sortation. Optimized for hyperscale retail DC operations.",
         "70 systems deployed\n~85% Walmart revenue concentration\n$550–618M quarterly revenue\nPublicly traded (SYM)",
         "Extreme efficiency at hyperscale. AI-optimized put-away and retrieval. Proven with world's largest retailer.",
         "Requires $100M+ CapEx per installation. 85% Walmart concentration = single-customer risk. Requires purpose-built facility. Locus wins on flexibility and lower entry point.",
         "HIGH\nSymbotic 10-K / 10-Q SEC filings,\nearnings call transcripts"),
    ]),
]

r = 3
for section_label, rows in competitors:
    section_hdr(ws_comp, r, section_label, 8)
    r += 1
    shade = False
    for row_data in rows:
        ws_comp.row_dimensions[r].height = 90
        bg = LIGHT_BG if shade else WHITE
        for c, v in enumerate(row_data, 1):
            cell = ws_comp.cell(row=r, column=c, value=v)
            cell.font = bold(10) if c == 1 else reg(10)
            cell.fill = fill(bg)
            cell.alignment = walign()
            cell.border = border()
            # TYPE column
            if c == 2:
                if "WINDING DOWN" in v:
                    cell.font = bold(10, RED_FG);    cell.fill = fill(RED_BG)
                elif "Adjacent" in v:
                    cell.font = bold(10, YELLOW_FG); cell.fill = fill(YELLOW_BG)
                elif "Direct" in v:
                    cell.font = bold(10, "1B3A6B");  cell.fill = fill(MID_BG)
            # CONFIDENCE column
            if c == 8:
                if v.startswith("HIGH"):
                    cell.font = reg(9, GREEN_FG);    cell.fill = fill(GREEN_BG)
                elif v.startswith("MEDIUM"):
                    cell.font = reg(9, YELLOW_FG);   cell.fill = fill(YELLOW_BG)
        shade = not shade
        r += 1

# ═══════════════════════════════════════════════════════════════════════════════
# BUYER & USER PERSONAS
# ═══════════════════════════════════════════════════════════════════════════════
ws_p = wb.create_sheet("Buyer & User Personas")
setup_ws(ws_p, "Buyer & User Personas")
title_cell(ws_p, "Buyer & User Personas", 3,
           "LOCUS ROBOTICS  ·  BUYER & USER PERSONAS  —  Who You're Selling To vs. Who Uses the Product")
col_headers(ws_p, 2, ["ATTRIBUTE", "DETAIL", "SE ANGLE"])
cw(ws_p,1,26); cw(ws_p,2,46); cw(ws_p,3,46)

BUYER_SUB = "2E5C99"
USER_SUB  = "357A35"
BUYER_GRP = "1B3A6B"
USER_GRP  = "1E6B1E"

def persona_grp(ws, row, label, bg):
    section_hdr(ws, row, label, 3)
    ws.cell(row=row, column=1).fill = fill(bg)
    for col in range(2, 4):
        ws.cell(row=row, column=col).fill = fill(bg)

def persona_sub(ws, row, label, bg):
    ws.row_dimensions[row].height = 18
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=3)
    c = ws.cell(row=row, column=1, value=label)
    c.font = bold(10, WHITE)
    c.fill = fill(bg)
    c.alignment = walign("left", "center")
    c.border = border()
    for col in range(2, 4):
        mc = ws.cell(row=row, column=col)
        mc.fill = fill(bg)
        mc.border = border()

buyer_personas = [
    ("BUYER PERSONA 1  ·  'The Ops Champion'  —  VP / Director of Operations", [
        ("Title / Role","VP Operations, Director of Supply Chain, SVP Fulfillment",
         "Your primary internal champion. If this person is sold, they will pull the deal through."),
        ("Company Context","Mid-to-large 3PL or enterprise retailer. Owns DC P&L. Reports to COO or CEO. Accountable for throughput, cost-per-pick, and SLA compliance.",
         "Size the opportunity early: volume, site count, labor headcount, peak profile. Determine if they own budget or need finance approval."),
        ("Primary Focus","Throughput, labor efficiency, cost-per-unit, peak season readiness, reducing dependency on hard-to-find labor.",
         "Lead with operational outcomes: UPH gains, cost-per-pick reduction, peak elasticity. Speak their language — not tech specs."),
        ("Key Questions They Ask","How much will this reduce my cost-per-pick? Can I scale for peak without hiring? What do other 3PLs see for ROI? How long until payback?",
         "Have DHL, GEODIS, and Staples Canada case studies ready. Be specific: 2-3x UPH, 50% productivity gain (GEODIS), 1M picks in 70 days (Staples Canada)."),
        ("Budget / Authority","Often the budget owner OR strong influencer. In larger orgs, needs CFO sign-off for multi-year RaaS commitment.",
         "Identify early: do they own budget? If not, who does? Get CFO looped in at the right moment — too early and it stalls, too late and they feel blindsided."),
        ("Pain Points","Labor scarcity and rising wages. High turnover making training ROI negative. Missed SLAs during peak. Pressure from above to do more with less headcount.",
         "Mirror their pain directly. The RaaS elasticity story (scale up for peak, scale down after) is tailor-made for this buyer."),
        ("Win Signals","Has evaluated AMRs before. Knows competitor names. Has a live labor problem. Under pressure from CEO/Board to modernize. Has a peer who deployed Locus.",
         "Peer references are powerful here. Offer to connect them with a similar Locus customer. Get the intro to CFO and IT Director early."),
    ]),
    ("BUYER PERSONA 2  ·  'The Budget Gatekeeper'  —  CFO / VP Finance", [
        ("Title / Role","CFO, VP Finance, Controller, SVP Finance",
         "Can kill or delay a deal regardless of ops enthusiasm. Must be engaged, not just informed."),
        ("Company Context","Reports to CEO. Owns financial approvals for OpEx and CapEx. Risk-averse by nature. Measures success in IRR, payback period, and cost avoidance.",
         "Understand their financial lens before engaging. Have a clean TCO model ready. Know your contract flexibility story cold."),
        ("Primary Focus","Total cost of ownership, financial risk management, budget predictability, justifying spend to the board.",
         "Lead with the RaaS OpEx story: no CapEx outlay, predictable monthly cost, lower risk than buying hardware. Have a 3-year TCO model ready."),
        ("Key Questions They Ask","What is total cost over 3 years? Is this OpEx or CapEx? What happens if volume drops — am I locked in? What is the exit clause?",
         "Prepare a cost-of-labor vs. RaaS comparison. Address contract flexibility proactively — do not wait for them to ask about exit clauses."),
        ("Budget / Authority","Final sign-off in many deals. Can approve or kill even when ops team is fully sold. Budget cycles matter — understand their fiscal year.",
         "Time your pricing conversation carefully. Know their fiscal calendar. Try to get included in budget planning, not just a reactive approval request."),
        ("Pain Points","Unpredictable labor costs that blow budget. CapEx avoidance after write-off experiences. Subscription fatigue. Fear of long-term commitment to unproven tech.",
         "Validate ROI with third-party data (MHI industry median, customer case studies). The 6-month payback claim needs to be grounded in specifics, not just repeated."),
        ("Win Signals","Has approved SaaS/subscription tools before. Company burned by CapEx write-offs. CFO is asking questions rather than delegating. Finance team modeling scenarios.",
         "When the CFO starts modeling scenarios, that is a buy signal. Offer to provide a financial model they can run themselves — builds trust and speeds internal approval."),
    ]),
    ("BUYER PERSONA 3  ·  'The Integration Gatekeeper'  —  IT Director / VP Technology", [
        ("Title / Role","Director of IT, VP Technology, CTO (smaller company), Director of Enterprise Systems",
         "Can veto a deal on technical grounds. Must be a supporter — or at minimum, neutral — for the deal to close."),
        ("Company Context","Owns WMS, ERP, and all technology integrations. Reports to COO or CEO. Manages a lean team stretched across multiple systems.",
         "Get to IT early. If they feel ambushed by the project, they will find technical reasons to block it. Early engagement creates partnership, not gatekeeping."),
        ("Primary Focus","Technical feasibility, integration complexity, data security, system uptime, and not creating new tickets for their team.",
         "Reduce perceived technical risk immediately. Lead with pre-built WMS connectors and security credentials (Fortress Cybersecurity Award, 2 consecutive years)."),
        ("Key Questions They Ask","How does this connect to our WMS? What APIs do you use? Who owns the data? What is the uptime SLA? How do you handle security?",
         "Have the API architecture overview ready. Name the WMS integrations: Manhattan Associates, Blue Yonder, Logiwa, Made4Net, Tecsys. Offer to loop in Locus integration engineers early."),
        ("Budget / Authority","Rarely owns budget but can block or delay by raising technical concerns. A satisfied IT Director actively removes blockers for the ops team.",
         "Frame IT as a partner in success. Offer a technical deep-dive with Locus engineers. An IT Director who feels informed and respected will advocate for the deal."),
        ("Pain Points","Custom WMS integrations that break. Vendor lock-in. Data security compliance pressure. IT resource bandwidth — already stretched too thin.",
         "Emphasize that Locus pre-built connectors reduce custom integration work. LocusONE is maintained by Locus, not IT. Position Locus Deployment Engineers as an extension of their team."),
        ("Win Signals","Has done AMR or WMS integrations before. WMS is modern with REST API. IT team is lean (wants low-maintenance). IT Director joins follow-up call with their system architect.",
         "When they bring a system architect, match with a Locus technical resource. Peer-to-peer technical credibility closes the IT track of the deal."),
    ]),
]

user_personas = [
    ("USER PERSONA 1  ·  'The Daily Driver'  —  DC Operations Manager / Warehouse Manager", [
        ("Title / Role","DC Manager, Warehouse Manager, Shift Manager, Operations Manager",
         "Your post-go-live champion or your biggest detractor. How they feel about the robots in month 3 drives renewal and expansion."),
        ("Company Context","Manages day-to-day floor operations. Direct reports are supervisors and pickers. Reports to VP Operations. Accountable for daily throughput and labor management.",
         "This person was not at the sales table but lives with the outcome. Include them in deployment planning — it creates ownership, not resistance."),
        ("Primary Focus","Daily throughput targets, labor coordination with robots, robot uptime, shift-by-shift KPI attainment.",
         "Demo LocusHub live. Show how they monitor fleet performance, re-task robots, and escalate issues. Make them feel in control of the fleet."),
        ("Daily Workflows","Reviews LocusHub dashboard each morning. Monitors UPH and robot utilization. Coordinates robot-to-picker assignments. Handles exception management when a robot goes offline.",
         "Train them on LocusHub and SDL override capabilities early. Empower them to manage the fleet themselves. Dependency on Locus support for routine tasks creates resentment."),
        ("Frustrations","Robots going offline during peak hours. Unclear why throughput dipped. Manual workarounds when system errors occur. Training new pickers when robot is part of the workflow.",
         "Uptime SLA and support response time are critical talking points. Set realistic expectations during implementation, not after go-live."),
        ("Technical Skills","Moderate. Comfortable with dashboards and reports. Not a developer. Uses LocusHub and Robot UI daily. Escalates technical issues rather than debugging.",
         "Keep the UI conversation simple and outcome-focused. Show the 24+ report types in LocusHub. Emphasize they don't need IT to get performance data."),
        ("Win Signals (post-go-live)","Uses LocusHub daily without prompting. Shares performance screenshots with VP Ops. Requests more robots. Brings Locus up in their own team meetings as a success story.",
         "A DC Manager who is proud of the robots is your best reference. Proactively ask for their story at the 90-day mark. Connect them to Locus case study team."),
    ]),
    ("USER PERSONA 2  ·  'The Floor Worker'  —  Warehouse Associate (Picker)", [
        ("Title / Role","Warehouse Associate, Order Picker, Fulfillment Specialist, DC Associate",
         "Primary end-user of Robot UI and SDL. Floor resistance to robots can derail adoption even after go-live. Change management is your job here."),
        ("Company Context","Front-line worker walking alongside Origin robots during P2G picking. Varies widely in tenure, language, and technical comfort. Often skeptical of automation's impact on their job.",
         "Not your buyer, but a key adoption driver. A picker frustrated with robot pace or UI becomes a vocal detractor that managers hear about."),
        ("Primary Focus","Completing their daily pick quota. Physical safety near robots. Keeping up with robot pace. Not losing their job to a machine.",
         "Address the job security concern directly in change management conversations. Locus Origin robots augment pickers, they do not replace them — that is the model by design."),
        ("Daily Workflows","Follows pick prompts on Origin robot touchscreen. Places items in tote as directed. Responds to SDL task routing. Moves between pick zones as robot navigates.",
         "The 80% training time reduction (DHL) is the key stat here. A simple, visual UI on the robot is the product. Emphasize ease of use and low learning curve."),
        ("Frustrations","Robot pace that is too fast or inconsistent. Pick instructions that are unclear. Robot navigating to wrong zone. Supervisor overrides that disrupt their flow rhythm.",
         "Ask about associate experience during deployment planning. Customers who under-invest in associate onboarding have the worst adoption outcomes."),
        ("Technical Skills","Low to moderate. Uses robot touchscreen only. No system-level access. May not speak English as first language — icon-heavy UI matters.",
         "Mention the visual, icon-driven pick UI on Origin. Item image + quantity display reduces language barrier and pick errors simultaneously. Real SE talking point."),
        ("What They Need","A robot that matches their pace. Clear, simple screen prompts. Consistency in task flow. To feel the robot makes their job easier, not harder or threatening.",
         "Include a change management and floor training plan in your deployment proposal. This is often the difference between a smooth go-live and a rocky one."),
    ]),
    ("USER PERSONA 3  ·  'The System Owner'  —  IT Systems Admin / Integration Manager", [
        ("Title / Role","Systems Administrator, WMS Admin, Integration Manager, IT Manager",
         "Was likely involved in deployment. Now owns the day-to-day technical integration. They will know when things break before anyone else does."),
        ("Company Context","Manages the technical bridge between LocusONE and the customer's WMS and ERP. May be a single person covering multiple systems in a lean IT org.",
         "This person's daily experience determines long-term integration health. Poor documentation or slow support turns them into an internal critic of the Locus deployment."),
        ("Primary Focus","System uptime, API connection health, order sync accuracy, error resolution, data integrity between LocusONE and WMS.",
         "Make sure Locus's technical support model is clear before go-live. Who do they call? What is the escalation path? Ambiguity here creates frustration."),
        ("Daily Workflows","Monitors API connection health. Reviews error logs. Resolves order sync issues. Manages Locus software update windows. Escalates L2/L3 issues to Locus support.",
         "During sales, offer a technical integration overview document proactively. After go-live, their relationship with Locus integration support defines account health."),
        ("Frustrations","Black-box integrations they didn't build. Locus API changes that break existing connections without warning. Unclear documentation. Slow support during peak season.",
         "Set expectations around API versioning and change notification. A customer blindsided by a breaking API change becomes a churn risk. Address proactively in the sales cycle."),
        ("Technical Skills","High. Comfortable with REST APIs, JSON, system logs, and network troubleshooting. Will read the documentation. Will test the integration themselves before trusting it.",
         "Offer to share API documentation during the sales process, not just post-signature. A technical buyer who can validate the integration moves faster and trusts more."),
        ("What They Need","Clear API documentation. Proactive communication on software updates. A reliable Locus technical support contact. Low-maintenance integration after go-live.",
         "Position Locus Deployment Engineers as ongoing partners, not a one-time setup team. Facilitate an intro to the Locus integration team during the sales cycle."),
    ]),
]

r = 3
persona_grp(ws_p, r, "BUYER PERSONAS  ——  People Who Own the Purchasing Decision", BUYER_GRP)
r += 1
for persona_title, rows in buyer_personas:
    persona_sub(ws_p, r, persona_title, BUYER_SUB)
    r += 1
    shade = False
    for attr, detail, se_angle in rows:
        data_row(ws_p, r, [attr, detail, se_angle], shade, height=50)
        ws_p.cell(row=r, column=1).font = bold(10)  # bold attribute col
        shade = not shade
        r += 1
    spacer_row(ws_p, r); r += 1

persona_grp(ws_p, r, "USER PERSONAS  ——  People Who Use the Product Day-to-Day", USER_GRP)
r += 1
for persona_title, rows in user_personas:
    persona_sub(ws_p, r, persona_title, USER_SUB)
    r += 1
    shade = False
    for attr, detail, se_angle in rows:
        data_row(ws_p, r, [attr, detail, se_angle], shade, height=50)
        ws_p.cell(row=r, column=1).font = bold(10)
        shade = not shade
        r += 1
    spacer_row(ws_p, r); r += 1

# ═══════════════════════════════════════════════════════════════════════════════
# SAVE
# ═══════════════════════════════════════════════════════════════════════════════
out = "/sessions/intelligent-fervent-knuth/mnt/outputs/Locus_Quick_Reference.xlsx"
wb.save(out)
print("Saved:", out)
