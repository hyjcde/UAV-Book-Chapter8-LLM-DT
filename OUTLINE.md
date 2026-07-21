# Chapter 8 Outline  
## Digital Twin with LLMs in Inspection Analysis

**Book:** *AI-Driven UAV Building Inspection*  
**Subtitle (proposal):** *An End-to-End Framework from Autonomous Flight to Digital Twins*  
**Author / Lead:** Yijun Huang  
**Scope:** Chapter 8 only  
**Target length:** ~50 pages  
**Spine:** four-phase book → phase-4 decision support: language-ready twin + ready-to-use LLM/VLM → reports / historical query / DSS  

---

> **Springer book proposal (2026-07) + attached annotated TOC.**  
> Chapter order: 5 Dataset → 6 AI Models → 7 GIS → 8 DT+LLM.  
> Continuous Springer prose. **8.2 = L1/L2/L3.** Include **VLM positioning** (proposal thematic Part 4).  
> No site-training agenda in Ch.8. Target ~50 pages.  
> Build: `scripts/build.sh`. Figures: `literature/FIGURE_PLAN.md`.

---

## 0. One-liner

把 Digital Twin 升级为可检索、可引用、可决策的语言推理底座：用即用 LLM（及可选 VLM 阅读）接到立面巡检孪生，查询历史维修记录、产出可审计报告与预测性维护建议——不依赖现场微调。

---

## 1. Section map

| § | Title | Pages | Status |
|---|-------|-------|--------|
| 8.1 | Digital Twins for Building Inspection | 5–7 | draft+ (four-phase framing) |
| 8.2 | Foundations of LLMs for Civil Engineering Applications | 10–14 | **L1/L2/L3 continuous prose** |
| 8.3 | From Digital Twins to Language Reasoning | 7–9 | draft+ (historical-record intent) |
| 8.4 | Multi-Modal Fusion | 7–9 | draft+ (**VLM vs Ch.6 detector**) |
| 8.5 | Inspection Report Generation and Management | 5–7 | draft+ |
| 8.6 | Decision Support and Predictive Maintenance | 6–8 | draft+ (proposal USP wording) |

---

## 2. Reader path

```text
Ch.5–6 modality-tagged observations → Ch.7 GeoBIM hosts
  → observation records / asset passports / neighbour assembly
  → optional VLM crop reading under cite-or-abstain
  → L2–L3 grounded generation (historical + propagation)
  → report schema → optional work-system export → DSS / triage
```

---

## 3. Section goals

### 8.1 Twin contract
四阶段收束；语言可用孪生：Asset-ID、出处、邻域、时间、模态；成熟度三级。

### 8.2 LLM foundations（即用三层 + harness）
- L1 语言接口；L2 证据接地；L3 记忆与有界流程；model harness  
- 不写训练/微调议程

### 8.3 Twin → language
观测 / 护照 / 查询装配；**历史维修记录**为一等意图。

### 8.4 Multimodal + VLM + agents
模态标签保留；**VLM 可选阅读器，不替代 Ch.6 检测器**；有界智能体。

### 8.5 Reports
Schema、cite-or-abstain；CMMS 等仅为可选导出。

### 8.6 DSS
报告 / 历史查询 / 预测性维护建议（分诊 + 预后边界）；论文统计原图。

---

## 4. Sync

`python3 scripts/sync_check.py` → `bash scripts/build.sh`  
Unpublished ≠ `\cite`.
