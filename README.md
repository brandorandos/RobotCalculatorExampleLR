# Locus Robotics SE Portfolio — Brandon Hazelton

**Brandon Hazelton | Solutions Engineering Portfolio**  
brandohazelton@gmail.com

A collection of work built in preparation for a Locus Robotics Solutions Engineer role. Two distinct deliverables live here: a live SE engagement walkthrough built as a hiring demo, and a quick reference knowledge base built through deep independent research.

---

## Live Site

**[brandorandos.github.io/RobotCalculatorExampleLR](https://brandorandos.github.io/RobotCalculatorExampleLR/)**

---

## What's in Here

### `/` — SE Engagement Example (the original deliverable)
A complete mock SE engagement: raw customer data in, phased deployment recommendation and ROI model out. Built to demonstrate how I think through a customer problem end-to-end.

| File | Description |
|------|-------------|
| `index.html` | Main portfolio landing page |
| `about.html` | Personal SE reflection: background, process, AI philosophy, honest gaps |
| `calculators/slotting_optimizer.html` | Pre-deployment operations analysis — SKU slotting health check |
| `calculators/robot_applicability.html` | Robot applicability scorer: Origin vs Array routing and fleet sizing |
| `outputs/customer_presentation.html` | Customer-facing presentation with three-phase deployment plan and ROI |
| `outputs/warehouse_baseline_report.docx` | Full 9-section analysis report |
| `outputs/facility_layout.svg` | Overhead warehouse schematic — five zones, cross aisle, dock layout |
| `outputs/pick_face_layout.svg` | Pick face diagram with ergonomic tier coding for Array arm-reach assessment |
| `data/` | Trimmed synthetic datasets (OB transactions, IB receipts, inventory, SKU master) |

---

### `/quick-reference` — SE Interview Quick Reference
A self-contained Excel workbook built for rapid recall during interviews and customer conversations. 8 tabs covering the full Locus product and competitive landscape.

| File | Description |
|------|-------------|
| `Locus_Quick_Reference.xlsx` | 8-tab Excel reference: robots, software, stack, customer profiles, competitors, personas |

**Tabs:**
- **Origin / Array / Vector** — robot specs, operational metrics, deployment scale, limitations
- **External Software** — LocusONE, LocusHub, SDL, Mission Optimization, NeuraGrasp, Robot UI
- **Internal Stack** — SE tools, data architecture, BI, AI/LLM stack, marketing/CRM (sourced from JDs)
- **Target Customer Profiles** — Strong / Mid / Weak fit criteria across 11 dimensions
- **Competitors** — 6 competitors: robot offering, software, scale, strengths/weaknesses vs. Locus
- **Buyer & User Personas** — 3 buyer personas (VP Ops, CFO, IT Director) + 3 user personas (DC Manager, Floor Associate, IT Admin)

---

### `/research` — Sourced Research Notes
Markdown docs behind the quick reference. Useful for reviewing sources or going deeper on any topic.

| File | Description |
|------|-------------|
| `locus_products_and_stack.md` | Full product breakdown (Origin, Array, Vector, LocusONE) + internal tech stack with confidence ratings |
| `deployment_metrics.md` | Fleet scale, throughput, ROI data, RaaS pricing, notable customer deployments |
| `competitors.md` | 6 competitors with sourced data, strengths/weaknesses, and SE conversation framing |

---

### `/tools` — Build Scripts
Scripts used to generate deliverables. Lets the Excel be regenerated or extended as new info comes in.

| File | Description |
|------|-------------|
| `build_quick_reference.py` | Python/openpyxl script that builds `Locus_Quick_Reference.xlsx` from scratch |

**Requirements:** `pip install openpyxl`

---

## The SE Engagement (original deliverable)

A mid-size e-commerce fulfillment center running two product categories (Health & Beauty, Apparel) across five pick zones. Running at 112% capacity on a typical weekday before factoring in any growth.

**Step 1 — Data Request:** Outbound transactions (60-day), inbound receipts (180-day), inventory snapshot, SKU master.

**Step 2 — Baseline Analysis:** 1M+ OB pick transactions analyzed. 75 UPH baseline, 6 miles of picker walk per shift, 32% of SKUs not in optimal slot zones.

**Step 3 — Operations Health Check:** Slotting health reviewed before sizing any robot fleet. 1,618 SKUs identified as candidates for repositioning.

**Step 4 — Robot Applicability Scoring:** H&B scores strongly for Array + NeuraGrasp (72% of volume, uniform rigid items). Apparel scores for Origin + human collaboration (non-uniform items, human dexterity required).

**Step 5 — Phased Deployment and ROI:** One starting point, two expansion paths.

| Scenario | Robots | Net Annual Benefit | CapEx |
|----------|--------|-------------------|-------|
| Phase 1 — Origin in Apparel | 2 Origin | ~$200K | $0 |
| Phase 2A — Scale Origin to all aisles | 6 Origin | ~$580K | $0 |
| Phase 2B — Add Array to H&B | 2 Origin + 4 Array | $1.4M | $50K–$400K |

---

## On AI Usage

AI was used to build the code, calculators, research synthesis, and Excel outputs in this project. The analytical framework, deployment decisions, and source validation were done against domain knowledge from five years in warehouse automation SE roles.

The research docs include explicit confidence ratings and source citations so any claim can be traced back to where it came from.

---

*Brandon Hazelton — brandohazelton@gmail.com*
