# Locus Robotics SE Engagement Example

**Brandon Hazelton | Solutions Engineering Portfolio**

A complete SE engagement walkthrough built as a hiring portfolio for Locus Robotics. Raw customer data in, phased deployment recommendation and ROI model out. Built to show how I think through a customer problem, not just that I have done it before.

## Live Site

**[brandorandos.github.io/RobotCalculatorExampleLR](https://brandorandos.github.io/RobotCalculatorExampleLR/)**

---

## What Is In Here

| File | Description |
|------|-------------|
| `index.html` | Main portfolio landing page - start here |
| `about.html` | Personal SE reflection: background, process, AI philosophy, honest gaps |
| `calculators/slotting_optimizer.html` | Pre-deployment operations analysis - SKU slotting health check |
| `calculators/robot_applicability.html` | Robot applicability scorer: Origin vs Array category routing and fleet sizing |
| `outputs/customer_presentation.html` | Customer-facing presentation with three-phase deployment plan and ROI |
| `outputs/warehouse_baseline_report.docx` | Full 9-section analysis report |
| `outputs/facility_layout.svg` | Overhead warehouse schematic - five zones, cross aisle, dock layout |
| `outputs/pick_face_layout.svg` | Pick face diagram with ergonomic tier coding for Array arm-reach assessment |
| `data/` | Trimmed sample datasets (OB transactions, IB receipts, inventory, SKU master) |

---

## The Engagement

A mid-size e-commerce fulfillment center running two product categories (Health & Beauty, Apparel) across five pick zones. Running at 112% capacity on a typical weekday before factoring in any growth. Overtime required every day just to keep up with current volume.

**Step 1 - Data Request:** Outbound transactions (60-day), inbound receipts (180-day), inventory snapshot, SKU master.

**Step 2 - Baseline Analysis:** 1M+ OB pick transactions analyzed. 75 UPH baseline, 6 miles of picker walk per shift, 32% of SKUs not in optimal slot zones.

**Step 3 - Operations Health Check:** Slotting health reviewed before sizing any robot fleet. 1,618 SKUs identified as candidates for repositioning. If the fastest SKUs are in the wrong zones, any robot zone assignment built on top of that is wrong by definition.

**Step 4 - Robot Applicability Scoring:** H&B scores strongly for Array + NeuraGrasp (72% of volume, uniform rigid items, extended schedule). Apparel scores for Origin + human collaboration (non-uniform items, human dexterity required).

**Step 5 - Phased Deployment and ROI:** One starting point, two expansion paths.

| Scenario | Robots | Net Annual Benefit | CapEx |
|----------|--------|-------------------|-------|
| Phase 1 - Origin in Apparel | 2 Origin | ~$200K | $0 |
| Phase 2A - Scale Origin to all aisles | 6 Origin | ~$580K | $0 |
| Phase 2B - Add Array to H&B | 2 Origin + 4 Array | $1.4M | $50K-$400K |

Phase 2A and 2B are evaluated after Phase 1 is in production. The right path depends on the customer's appetite for CapEx and autonomous picking.

---

## On AI Usage

AI was used to build the code, calculators, and outputs in this project. It was not used to generate the analytical framework, make deployment decisions, or validate outputs - that was done against domain knowledge from five years in warehouse automation SE roles.

The long-term goal of these tools is to remove AI from the daily process entirely. AI helps build the calculator. Once verified, the calculator runs on its own.

---

## Data Note

All data is synthetic - statistically realistic for a mid-size e-commerce DC but not tied to any real customer or facility.

---

*Brandon Hazelton - brandohazelton@gmail.com*
