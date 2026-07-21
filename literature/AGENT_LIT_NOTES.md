# Chapter 8 literature notes — Agents beyond RAG（2023–2026）

论文 DefectGPT / IAP-RAG 主线是 **asset-centric topology-aware RAG**。书章 50 页目标需要补齐：**Agent / tool-use / multi-agent / robot–DT 闭环**。

## A. Foundations（通用 Agent）

| Key | Contribution | Use in Ch.8 |
|-----|--------------|-------------|
| Yao et al. 2023 ReAct | Reason+Act interleaved | 8.2 / 8.5 工具调用范式 |
| Schick et al. 2023 Toolformer | Self-supervised tool use | 8.2 |
| Wang et al. 2024 survey | LLM autonomous agents taxonomy | 8.2 综述骨架 |
| Li et al. 2024 multi-agent survey | Workflow / infra / challenges | 8.5 多智能体编排 |

## B. AEC / BIM / Facility（强相关）

| Key | Contribution | Use in Ch.8 |
|-----|--------------|-------------|
| Luo et al. 2025 CCC | LLM + DT + **robot** for FM inspection | 8.5 case：自然语言→机器人任务→更新 DT |
| Gao et al. 2026 AUTCON IFC-Agent | Schema-guided **multi-agent** + tools on IFC | 8.5：schema-guided vs 我们的 IAP/VDPP |
| Zhang et al. 2025 AUTCON | Agent schema/library for building energy | 8.2/8.5 领域 agent 组件化 |
| Guo et al. 2025 AUTCON | LLM query ↔ DSL/library alignment for BIM IR | 与 RAG 检索对照 |
| Akhavian et al. 2025 BIM2RDT (arXiv) | **Agentic** BIM→robot-ready DT, safety-first | 8.1/8.5 施工现场孪生+机器人 |
| Multi-agent VBM in BIM (AUTCON 2025) | Multi-agent 自动建虚拟建筑模型 | 8.1 DT 从设计到运维 |
| Shi et al. 2025 Cognitive DT | RAG toward cognitive digital twins (industry) | 8.3 与认知孪生表述对齐 |

## C. Agentic RAG（方法层）

| Theme | Takeaway for façade inspection |
|-------|--------------------------------|
| Static RAG vs Agentic RAG | Agent 可多步检索、改写查询、调用工具；但更难审计 |
| Graph-/topology-aware retrieval | 与 VDPP / IAP-RAG 同族；书中强调 **asset ID + citation** 约束 |
| Bridge evidence (2026 arXiv) | 静态检索效用 ≠ agent 多步因果效用 → 评测要对齐任务 |

## D. Positioning vs our DefectGPT paper

```
Paper (IAP-RAG):   structured knowledge + topology RAG + grounded answers
Book Ch.8 adds:    agent loop (plan→tool→observe→update DT) + multi-agent roles
                   + robot/FM interfaces + report/DSS at textbook depth (~50 pp)
```

**不要**把 Agent 写成替代 RAG；写成：

> RAG 解决「找对证据」；Agent 解决「多步行动与工具编排」；巡检决策两者都需要，并以 Asset-ID / schema 约束可审计性。

## E. Must-cite clusters in chapter prose

1. RAG core: Lewis 2020; Gao HyDE; Edge GraphRAG; Self-RAG; Adaptive-RAG（已在 AIC.bib）  
2. Agent core: ReAct; Toolformer; agent surveys  
3. AEC agents: Luo2025; Gao2026 IFC-Agent; Zhang2025; BIM2RDT; Guo2025  
4. Our stack: IDP/IAP/VDPP experimental numbers (locked)

## F. Local draft to consult — Memory 综述（未发表，勿直接当书章引用）

**Path (actual):**  
`~/Desktop/02_学术研究/论文/[撰写中]_Memory综述/`  
（不是 `期刊投稿/撰写中/...`；同级在 `论文/[撰写中]_*` 下）

**File:** `大模型Agent自演化综述.md`  
主线：推理态 → 经验记忆生成 → 更新 → 演进；记忆类型学（工作 / 情景 / 语义 / 程序 / 元记忆）；强调 **externalization + harness**（能力增长多在运行时结构，而非静默改权重）。

### Mapping → Chapter 8 memory ladder (teaching, not 1:1 copy)

| Survey typology | Ch.8 ladder box | Inspection reading |
|-----------------|-----------------|--------------------|
| Working memory | Contextual | prompt + session aliases |
| Episodic / semantic digests | Retrieval (RAG) | editioned manuals + observation cards |
| Procedural memory | (harness tools / gates) | typed tools, revisit workflows — *not* free twin writes |
| Parametric / weight memory | Parametric | language only; never site DB |
| Authoritative long-term store | Twin store (Asset-ID) | geometry + topology + time — beyond flat vector “memory stream” |

**Use for prose:** keep Ch.8 ladder four boxes; when mentioning agents, stress that rejected drafts / tool traces are *procedural* memory under gates, and that unchecked memory streams (Generative Agents–style) must not overwrite Asset-ID facts.  
**Do not** cite the unpublished survey itself in `ch08.tex`; pull only peer-published items already in `references.bib` (or add published DOIs first).

### Applied in chapter (2026-07-21)

| Symbol / table | Role |
|----------------|------|
| `eq:ch8-mem-loop` | Externalised generate-update-evolve (weights frozen) |
| `tab:ch8-mem-app` | Survey operators → already-built twin/harness artefacts |
| `eq:ch8-passport`, `eq:ch8-khop`, `eq:ch8-package` | Passport + BIM $k$-hop package |
| `eq:ch8-cite` | Cite-or-abstain ID subset gate |
