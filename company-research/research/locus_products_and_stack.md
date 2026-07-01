# Locus Robotics — Products & Technology Stack

**Research compiled for SE interview prep | Brandon Hazelton**  
*Sources: Locus Robotics Greenhouse JDs (directly fetched), locusrobotics.com, LinkedIn job postings, Robot Report*

---

## Robot Fleet

### Locus Origin (2016)
Person-to-Goods (P2G) collaborative AMR. The flagship robot. Associates walk alongside and place items into the robot's tote.

| Spec | Value |
|------|-------|
| Payload | 36 kg / 79 lbs |
| Dimensions | 558 × 558 × 1,468 mm |
| Max Speed | 5 m/s (~11 mph) |
| UPH improvement | 2–3× vs. manual (120–150 UPH with robots vs. 30–40 manual) |
| Training time reduction | 80% (DHL benchmark) |
| Track record | 2B+ picks, 300+ deployments |

**Key differentiator:** Drops into existing brownfield operations with no facility redesign. Fastest path to ROI in the Locus fleet.

**Honest limitations:** Labor-dependent — if you can't staff the floor, it sits idle. Throughput ceiling tied to picker count. Not omnidirectional.

---

### Locus Array (April 2026)
Robots-to-Goods (R2G) fully autonomous picking robot. No human required in the picking zone. Built on Vector chassis with AI-guided picking arm.

| Spec | Value |
|------|-------|
| Tote capacity | 6 simultaneous order totes (up to 66 lbs each) |
| Reach height | Up to 10 ft (3 m) |
| Mobility | Omnidirectional |
| SKU coverage (solo) | 60–70% of e-comm SKUs |
| SKU coverage (fleet) | 100% when paired with Origin + Vector |
| Labor reduction in zone | Up to 90% |
| Accuracy | 99.9% (stated) |
| AI grasping | NeuraGrasp™ (acquired from Nexera Robotics) |

**Key differentiator:** Only Locus robot with zero labor dependency in its zone. Autonomous picking arm handles irregular SKUs including ~30% of polybags.

**Honest limitations:** Launched April 2026 — very limited track record. DHL Supply Chain is primary early access customer. Requires dedicated narrow-aisle racking up to 10 ft. Premium pricing tier (unpublished).

---

### Locus Vector (2023)
Heavy-payload transport AMR. Acquired from Waypoint Robotics. Moves heavy goods between zones — not a picking solution.

| Spec | Value |
|------|-------|
| Payload | Up to 272 kg / 600 lbs |
| Mobility | Omnidirectional |
| Navigation | Dual safety-rated LiDAR + 3-stage safety system |
| Productivity gain | 50% (GEODIS Dallas TX — 12 Vectors, 40,000 sq ft) |

**Key differentiator:** Only robot in the fleet that handles heavy payloads. Omnidirectional movement in spaces forklifts can't reach.

**Honest limitations:** Transport only — cannot fulfill orders. Niche use case; most standard e-comm operations won't need it as primary robot.

---

## LocusONE Platform (External Software)

The central intelligence layer orchestrating all robots, labor, and WMS integration.

| Product | Type | What It Does |
|---------|------|--------------|
| **LocusONE** | Orchestration Platform | Coordinates all robots, labor, and WMS. Multi-site visibility. WES functionality. |
| **LocusHub** | Analytics Dashboard | Real-time KPIs: UPH, LPH, robot + worker productivity, 24+ report types |
| **System Directed Labor (SDL)** | AI Agent (patent-pending) | Directs associates to their next optimal task via on-robot UI in real time |
| **Mission Optimization** | AI Routing Engine | Clusters picks by density, shortens cycle times, dynamically allocates across robot types |
| **Advanced Simulation** | Pre-Deployment Modeling | Fleet sizing, ROI forecasting, design validation before deployment |
| **NeuraGrasp™** | AI Grasping System | Vision-guided picking for Array; 99.9% accuracy; ~30% polybag coverage |
| **Robot UI** | Associate-Facing Screen | Item image + quantity + location on Origin touchscreen; 80% training time reduction |

**WMS integrations (named):** Manhattan Associates, Blue Yonder, Logiwa, Made4Net, Tecsys — plus any WMS with a clean API.

---

## Internal Technology Stack

*Confidence ratings based on how directly each tool was evidenced in JDs I personally fetched from Greenhouse.*

### SE / Pre-Sales Tools (High confidence — directly in Senior SE JD)
- Excel (Advanced) — customer data analysis, concept system designs, ROI models
- SQL — data querying, warehouse and customer data manipulation
- Python — data analysis, scripting, ML/AI workflows
- PowerBI — reporting dashboards for SE work and customer-facing outputs
- AutoCAD — facility layout design, warehouse mapping, concept designs
- FlexSim — warehouse throughput simulation, fleet sizing, ROI forecasting

### Data Architecture / Backend (High confidence — AI Enterprise Architect JD)
- Databricks (Lakehouse) — enterprise analytical data platform
- AWS / Azure / GCP — cloud infrastructure (5+ years hands-on in JD)
- ETL/ELT Pipelines — data movement and integration
- Metadata / Data Catalog — governance, lineage, data quality

### BI / Reporting
- PowerBI (High — Senior SE JD)
- Looker (Medium — past Data Engineer posting via aijobs.net)
- GA4 + Google Tag Manager (High — Digital Experience Manager JD)

### AI / LLM Stack (High confidence — AI Enterprise Architect JD)
- GPT-4 / Claude — foundation models, explicitly named
- RAG Architecture — LLM-powered retrieval over enterprise data
- Agentic Workflows — automated end-to-end business process automation
- ROS (Robot Operating System) — robot navigation and sensor processing
- SLAM Navigation — Simultaneous Localization and Mapping for warehouse floors

### Marketing / CRM Stack (High confidence — Digital Experience Manager JD)
- Marketo — marketing automation
- 6sense / Demandbase — intent data and ABM targeting
- WordPress — CMS for locusrobotics.com

---

## Industry Recognition (as of 2025–2026)
- 8× RBR50 Robotics Innovation Award (most recent: 2025)
- 5× Gartner Hype Cycle appearances
- 2025 Fortress Cybersecurity Award (second consecutive year)
- Forrester: "Top 10 Emerging Technologies in 2025 (Autonomous Mobility Technology)"
- 2026 AI Breakthrough Award for Cognitive Robotics Innovation
