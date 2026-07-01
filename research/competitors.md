# Locus Robotics — Competitive Landscape

**Research compiled for SE interview prep | Brandon Hazelton**  
*Sources listed per competitor. All sourced October–November 2025.*

---

## Direct AMR Competitors

### Geek+ (Geekplus)
**Type:** Direct AMR — P2G + R2G  
**Confidence:** HIGH — IPO filings, Robot Report, Interact Analysis market share data

**Robot offering:** G-series AMRs (goods-to-person pods, picking robots, sorting bots). Supports 5,000+ AMRs in a single warehouse. Launched Gino 1 humanoid robot Feb 2026.

**Software:** GeekOS orchestration platform. Multi-robot, multi-workflow coordination — comparable scope to LocusONE.

**Scale:**
- 66,000+ robots deployed
- 950+ customers
- 40+ countries
- 23% global AMR market share (Interact Analysis)
- $378.7M revenue (2024)
- IPO'd on HKSE, July 2025

**Strengths vs. Locus:** Largest global AMR install base by volume. Broadest robot type catalog. Dominant APAC + EMEA footprint. Public company = greater R&D resources and financial runway.

**Weaknesses vs. Locus:** Chinese HQ = US enterprise data security concerns (ITAR adjacency, procurement sensitivity). Less US warehouse-specific expertise. US support network thinner than Locus. Humanoid pivot is unproven distraction from core AMR business.

---

### 6 River Systems (now Ocado)
**Type:** Direct AMR — P2G Collaborative  
**Confidence:** HIGH — Ocado investor docs, Robot Report, 6RS customer announcements

**Robot offering:** Chuck robot — collaborative P2G AMR. 90.7 kg, 1.3 m/s. Associates batch-pick alongside Chuck. No autonomous picking equivalent to Array.

**Software:** Cloud-based WES. WMS integration layer. Similar concept to LocusONE but narrower scope.

**Scale:**
- 100+ warehouses
- 70+ customers
- Customers include GXO, DHL, XPO
- Acquired by Ocado (2023) after being sold by Shopify

**Strengths vs. Locus:** Strong 3PL customer overlap with Locus (GXO, DHL are both customers — head-to-head competition). Ocado brand = enterprise credibility. Solid P2G workflow parity with Origin.

**Weaknesses vs. Locus:** Ocado acquisition created integration uncertainty — 6RS roadmap unclear post-acquisition. No autonomous picking capability (no Array equivalent). Fewer robot types. Less US-centric post-acquisition.

---

### GreyOrange
**Type:** Direct AMR + Hardware-Agnostic Orchestration  
**Confidence:** MEDIUM-HIGH — GreyOrange website, Google partnership press release

**Robot offering:** Ranger AMRs (multiple models). Hardware-agnostic CRN (Collaborative Robot Network) can orchestrate third-party robots alongside Ranger fleet.

**Software:** GreyMatter AI orchestration platform. Google Cloud partnership for GreyMatter DeepNav (AI navigation). SOC2 + ISO 27001 certified.

**Scale:**
- 100,000+ "active agents" claimed (note: includes non-Ranger hardware)
- Customer count not publicly disclosed
- Active in NA, EMEA, APAC

**Strengths vs. Locus:** Hardware-agnostic = can layer on top of existing robot fleets (different value prop than Locus). Google Cloud AI partnership. Strong compliance posture for enterprise procurement. SOC2/ISO27001 certified.

**Weaknesses vs. Locus:** Requires WiFi 6 and specific floor spec compliance — brownfield friction. No equivalent to Array's autonomous picking arm. "100K active agents" metric may include non-Ranger hardware (inflates perceived scale).

---

## Winding Down — Major Displacement Opportunity

### Zebra Technologies / Fetch Robotics
**Type:** WINDING DOWN AMR Division  
**Confidence:** HIGH — Robot Report, multiple industry sources

**Robot offering:** Fetch AMR fleet (multiple autonomous models for transport and picking). Division being wound down — no new product development. Most staff cut by end of 2025.

**Software:** FetchCore cloud platform. WMS integrations. No active development roadmap.

**Scale:**
- ~100 customers at peak
- Division wind-down underway
- Existing customer base actively seeking migration paths

**Strengths vs. Locus:** Zebra enterprise relationships may still open IT doors. Existing customers are motivated to move.

**Weaknesses vs. Locus:** Customers face real support risk. No new features or robots. Existing deployments are depreciating assets with no upgrade path.

> **⚡ SE Opportunity:** Displaced Fetch customers are actively seeking migration paths. Locus should be targeting these accounts directly. Lead with continuity of support, proven deployment track record, and RaaS flexibility.

---

## Adjacent Competitors (Different Category)

*These are not direct AMR competitors — they compete for the same budget and modernization conversation, but from a fundamentally different technology approach. Frame accordingly in customer conversations.*

### AutoStore
**Type:** Cube ASRS (NOT an AMR)  
**Confidence:** HIGH — AutoStore investor materials, Robot Report, public financials

**Robot offering:** Grid robots (R5, B1 models) moving across a proprietary cube storage grid. High-density goods-to-person. Fixed infrastructure — not mobile.

**Software:** AutoStore WCS + third-party WMS integration. No equivalent to LocusONE fleet orchestration for dynamic environments.

**Scale:**
- 1,900+ installations
- 65+ countries
- ~$596M revenue
- Entry cost: $500K–$2M+ per site

**Strengths vs. Locus:** Extreme storage density. Very high throughput for fast-moving SKUs. Proven at massive scale globally.

**Weaknesses vs. Locus:** Massive CapEx ($500K–$2M+) vs. Locus RaaS OpEx model. Requires full facility redesign — not brownfield-compatible. Fixed infrastructure can't flex with demand changes. Locus wins when prospect can't commit large capital or needs flexibility.

**When this comes up in conversation:** Prospect is considering cube storage for high-density SKU consolidation. Locus angle: OpEx model, brownfield compatibility, scalability without facility reconstruction.

---

### Symbotic
**Type:** Fixed DC Automation (NOT an AMR)  
**Confidence:** HIGH — Symbotic 10-K / 10-Q SEC filings, earnings call transcripts

**Robot offering:** Symbotic bots operating within a proprietary fixed grid inside purpose-built distribution centers. Pallet-to-piece fulfillment. Not modular or brownfield-compatible.

**Software:** Symbotic AI platform for put-away, retrieval, and sortation. Optimized for hyperscale retail DC operations.

**Scale:**
- 70 systems deployed
- ~85% Walmart revenue concentration
- $550–618M quarterly revenue
- Publicly traded (SYM)

**Strengths vs. Locus:** Extreme efficiency at hyperscale. AI-optimized put-away and retrieval. Proven with the world's largest retailer.

**Weaknesses vs. Locus:** Requires $100M+ CapEx per installation. 85% Walmart concentration = single-customer risk. Requires purpose-built facility. Locus wins on flexibility, lower entry point, and multi-customer model.

**When this comes up in conversation:** Prospect is a hyperscale retailer considering massive DC overhaul. This is not typically a Locus competitive scenario — different buyer profile entirely.

---

## Competitive Summary

| Competitor | Direct/Adjacent | Biggest Locus Advantage |
|------------|----------------|------------------------|
| Geek+ | Direct | US market expertise, support network, no data security concerns |
| 6 River Systems | Direct | Array (no autonomous picking equivalent), more robot types |
| GreyOrange | Direct | Array, brownfield simplicity, no WiFi 6 requirement |
| Zebra/Fetch | Displacement Opp | Active support, modern roadmap, proven migration path |
| AutoStore | Adjacent | RaaS OpEx vs. $500K–$2M CapEx, brownfield compatible |
| Symbotic | Adjacent | Flexibility, multi-customer model, lower entry point |
