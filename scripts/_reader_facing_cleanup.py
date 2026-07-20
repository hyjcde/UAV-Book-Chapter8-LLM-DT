# -*- coding: utf-8 -*-
"""Make Ch.8 reader-facing: no proposal jargon; define asset IDs; fix CN punctuation."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def fix_cn_punct(t: str) -> str:
    t = t.replace("，。", "。")
    t = t.replace("。，", "。")
    t = t.replace("，，", "，")
    t = re.sub(r"。{2,}", "。", t)
    t = t.replace("检测，重建，配准", "检测—重建—配准")
    return t


def main() -> None:
    en_path = ROOT / "latex/en/ch08.tex"
    cn_path = ROOT / "latex/cn/ch08_cn.tex"
    en = en_path.read_text(encoding="utf-8")
    cn = cn_path.read_text(encoding="utf-8")

    # ---- EN abstract rewrite (broken grammar + no Phase 4) ----
    en = re.sub(
        r"\\abstract\{Chapters~2--7 of this monograph.*?auditable workflows\.\}",
        r"""\\abstract{Chapters~2--7 of this monograph explain how to fly, reconstruct, detect, and map. Chapter~8 asks what an inspector or facility manager can do next with that twin: query it in ordinary language, fuse modality-tagged evidence already produced by perception, obtain answers that name real assets, and move toward reports and schedules. The chapter first clarifies what a language-ready twin must expose; then develops three layers of LLM technique for inspection---language interface, evidence grounding, and memory with bounded procedures---using off-the-shelf models. Site-specific training lies outside the scope of this chapter. Twin records, multimodal evidence, reports, and decision metrics then close the loop. Perception remains the source of typed defect findings; the LLM reads structured twin memory under citation rules. The primary readers are graduate students and researchers building inspection decision layers, facility engineers who must audit AI-assisted reports, and implementers who need harness contracts and auditable workflows.}""",
        en,
        count=1,
        flags=re.S,
    )
    # user asked no emdash - fix abstract --- again to commas
    en = en.replace(
        "three layers of LLM technique for inspection---language interface, evidence grounding, and memory with bounded procedures---using",
        "three layers of LLM technique for inspection (language interface, evidence grounding, and memory with bounded procedures), using",
    )

    en_reps = [
        (
            "Matching Book Proposal Phase~4 and the frozen TOC~8.1--8.6, the chapter first clarifies",
            "The chapter first clarifies",
        ),
        (
            "Book Proposal Phase~4 asks this chapter to introduce generative language technology for civil engineering and then attach it to inspection analysis. This chapter organises",
            "This section introduces generative language technology for civil engineering and attaches it to inspection analysis. It organises",
        ),
        (
            "That order is the practical meaning of ``ready-to-use LLMs for civil engineering applications'' in Book Proposal Phase~4: the technology families and the harness are introduced so that they can be applied to inspection analysis without pretending that training a site-specific model will keep a living fa\\c{c}ade up to date.",
            "That order is the practical meaning of ready-to-use LLMs for civil engineering inspection: the technology families and the harness are introduced so that they can be applied to analysis without pretending that training a site-specific model will keep a living fa\\c{c}ade up to date.",
        ),
        (
            "(proposal-aligned teaching map)",
            "(teaching map)",
        ),
        (
            "The teaching point for readers of this book is not to re-derive reconstruction or GIS methods. It is to treat Chapters~4--7 as an \\emph{interface contract}",
            "Readers need not re-derive reconstruction or GIS methods here. Chapters~4--7 should be treated as an \\emph{interface contract}",
        ),
        (
            "That scene is the pedagogical target of the rest of the chapter:",
            "That scene is the running example for the rest of the chapter:",
        ),
        (
            "A teaching decomposition of the inspection harness",
            "The inspection harness can be decomposed into",
        ),
        (
            "has five cooperating parts (Table~\\ref{tab:ch8-harness}).",
            "five cooperating parts (Table~\\ref{tab:ch8-harness}).",
        ),
        (
            "What we deliberately do \\emph{not} copy from training-heavy monitoring pipelines is a site-specific fine-tuning agenda; campaign facts belong in editioned twin memory and RAG indexes, not in weights that will be stale after the next flight",
            "Site-specific fine-tuning is outside the agenda of this chapter. Campaign facts belong in editioned twin memory and RAG indexes, not in weights that will be stale after the next flight",
        ),
        (
            "Teaching objectives for this chapter can be stated as four checkable outcomes. After reading, a student or implementer should be able to",
            "After reading this chapter, a student or implementer should be able to",
        ),
        (
            "Those outcomes are the chapter's research-framework analogue: not a new detector, but a decision-layer contract that earlier chapters can satisfy and later chapters can harden.",
            "Those outcomes define a decision-layer contract that earlier chapters can satisfy and later chapters can harden. They do not introduce a new detector.",
        ),
        (
            "Checkable teaching outcomes for Chapter~8 (monograph-style roadmap).",
            "Checkable outcomes for Chapter~8.",
        ),
        (
            "A monograph-style reading of structural monitoring books reinforces the same spine without changing the chapter's ready-to-use stance. Those books typically open with background and gaps, state objectives, then present a technical roadmap before methods and cases. Chapter~8 follows that order inside one decision layer: twin contract and gaps first, L1--L3 and harness second, assembly and multimodal agents third, reports and operability metrics last.",
            "The remainder of the chapter follows a single decision-layer order: twin contract and gaps first, L1--L3 and harness second, assembly and multimodal agents third, reports and operability metrics last.",
        ),
        (
            "For fa\\c{c}ade O\\&M we recommend a simple rule:",
            "For fa\\c{c}ade O\\&M a simple rule applies:",
        ),
        (
            "For fa\\c{c}ade inspection we recommend \\emph{bounded agency}",
            "For fa\\c{c}ade inspection, \\emph{bounded agency} is",
        ),
        (
            "realised inside the model harness",
            "realised inside the model harness",
        ),
        (
            "Group work on GeoBIM-coupled twin modelling",
            "Published GeoBIM-coupled twin modelling",
        ),
        (
            "Two consequences follow for procurement and teaching.",
            "Two consequences follow for procurement and system design.",
        ),
        (
            "Classroom TRACE grading then becomes a five-item checklist against those posters, not a taste test for fluent English",
            "TRACE grading can use a five-item checklist against those posters. Fluent phrasing is not the scoring target",
        ),
        (
            "Readers implementing course projects can treat Figures",
            "Figures",
        ),
        (
            "as the only wall posters they need.",
            "summarise the same spine for laboratory and procurement reviews.",
        ),
    ]
    for a, b in en_reps:
        if a not in en:
            print("EN miss:", a[:70])
        else:
            en = en.replace(a, b)

    # Define asset identifier before first Asset-ID table use
    old_geo = (
        "A geometric twin answers location. A language-ready twin for inspection must also expose three further commitments. "
        "First, stable asset identifiers that facility teams already use in work orders, not ad-hoc filenames invented at capture time."
    )
    new_geo = (
        "A geometric twin answers location. A language-ready twin for inspection must also expose three further commitments. "
        "First, a stable \\emph{asset identifier} for each maintainable host: the code that facility teams already use in work orders and registers. "
        "This chapter writes that code as Asset-ID after the first mention, so that language answers can name the same host that a CMMS ticket would name. "
        "Ad-hoc filenames invented at capture time are not Asset-IDs."
    )
    if old_geo in en:
        en = en.replace(old_geo, new_geo)
    else:
        print("EN asset intro miss")

    # Soften abrupt W-3-17: introduce once
    en = en.replace(
        "Parse intent=propagation for a moisture-path question on W-3-17;",
        "Parse intent=propagation for a moisture-path question on an illustrative west-elevation host coded \\texttt{W-3-17} in the facility register;",
        1,
    )
    en = en.replace(
        "Consider again: ``Is mid-storey hollow on the west elevation related to upstairs staining, and should we stage a gondola this quarter?''",
        "Consider again a manager question: ``Is mid-storey hollow on the west elevation related to upstairs staining, and should we stage a gondola this quarter?''",
    )

    # Extra LLM foundations paragraph (reader-facing, no Phase jargon)
    llm_extra = r"""

Beyond architecture and prompting, three LLM behaviours matter for civil deployment. Instruction-following models can adopt an answer template when the orchestrator supplies one, which is how observation and hypothesis can be kept apart in a short reply~\cite{ouyang2022instructgpt,brown2020}. Tool-calling models can request typed functions instead of inventing world state, which is how passport fetch and neighbour expansion stay outside the weights~\cite{schick2023toolformer,yao2023react}. Long-context models can hold a packed evidence digest, yet they still require validators: length does not create Asset-IDs that were never retrieved~\cite{lewis2020,ji2023,liang2023helm}. Construction-oriented GPT reviews and building-application agendas therefore treat governance, data readiness, and human oversight as first-class design variables alongside model choice~\cite{saka2024gptconstruction,ma2026tenquestions}. For fa\c{c}ade inspection those variables become concrete: edition pins, modality tags, cite-or-abstain checks, and write gates.

"""
    marker = "Contemporary LLMs rest on the Transformer architecture"
    if "Beyond architecture and prompting, three LLM behaviours" not in en:
        # insert after first paragraph of foundations
        idx = en.find(marker)
        if idx >= 0:
            # find end of that paragraph (double newline after)
            end = en.find("\n\n", idx)
            if end > 0:
                en = en[:end] + "\n" + llm_extra + en[end:]

    # ---- CN ----
    cn = fix_cn_punct(cn)
    cn_reps = [
        (
            "对齐书稿提案 Phase~4 与冻结目录 8.1--8.6，本章先澄清语言可用孪生必须暴露什么；再按三层展开 LLM 技术（语言接口、证据接地、记忆与有界流程），强调使用现成模型而非现场微调；然后说明孪生记录、多模态证据、报告与决策指标如何闭环。缺陷发现仍由感知负责；LLM 在引用规则下阅读结构化孪生记忆。主要读者包括：构建巡检决策层的研究生与研究者、必须审计 AI 辅助报告的设施工程师，以及需要 harness 契约而非聊天演示的实现者。",
            "本章先澄清语言可用孪生必须暴露什么，再按三层展开 LLM 技术（语言接口、证据接地、记忆与有界流程），并使用现成模型；现场微调不在本章范围。随后说明孪生记录、多模态证据、报告与决策指标如何闭环。缺陷发现仍由感知负责；LLM 在引用规则下阅读结构化孪生记忆。主要读者包括构建巡检决策层的研究生与研究者、必须审计 AI 辅助报告的设施工程师，以及需要 harness 契约与可审计工作流的实现者。",
        ),
        (
            "课题组在 GeoBIM 耦合孪生建模",
            "已发表的 GeoBIM 耦合孪生建模",
        ),
        (
            "对本书读者，教学重点不是重推重建或 GIS 方法，而是把第4--7章当作\\emph{接口契约}",
            "此处不必重推重建或 GIS 方法。第4--7章应被当作\\emph{接口契约}",
        ),
        (
            "此处视为语言分析的输入接口。",
            "本章把它视为语言分析的输入接口。",
        ),
        (
            "这一场景是后文的教学靶心：",
            "这一场景是后文的贯穿例子：",
        ),
        (
            "我们刻意\\emph{不}照搬训练密集型监测管线中的现场微调议程；航次事实属于带版本孪生记忆与 RAG 索引，。这些事实也不应写入下一班飞行后就会过时的权重",
            "现场微调不在本章议程内。航次事实属于带版本孪生记忆与 RAG 索引，也不应写入下一班飞行后就会过时的权重",
        ),
        (
            "本章教学目标可写成四条可核对结果。读完后，学生或实现者应能：",
            "读完本章后，学生或实现者应能：",
        ),
        (
            "这些结果是本章的``研究框架''类比：不是新检测器，而是前几章可满足、后几章可加硬的决策层契约。",
            "这些结果定义的是决策层契约：前几章可以满足它，后几章可以加硬它。本章并不引入新的检测器。",
        ),
        (
            "第8章可核对教学目标（专著式路线图表）。",
            "第8章可核对结果。",
        ),
        (
            "用专著式结构监测读物来对照，会强化同一脊柱，却不必改变本章的即用立场。这类书通常先写背景与缺口、再写目标、再给技术路线，然后才进入方法与案例。第8章在一个决策层内遵循同一顺序：先孪生契约与缺口，再 L1--L3 与 harness，再装配与多模态智能体，最后才是报告与可运维指标。",
            "后文在一个决策层内按同一顺序展开：先孪生契约与缺口，再 L1--L3 与 harness，再装配与多模态智能体，最后才是报告与可运维指标。",
        ),
        (
            "对立面巡检，我们推荐把\\emph{有界智能体}实现在第\\ref{sec:ch8-llm-foundations}节的模型 harness 之内。",
            "对立面巡检，\\emph{有界智能体}实现在第\\ref{sec:ch8-llm-foundations}节的模型 harness 之内。",
        ),
        (
            "书稿提案 Phase~4",
            "本章",
        ),
        (
            "书稿提案",
            "本章议题",
        ),
        (
            "教材级查询类型",
            "常用查询类型",
        ),
        (
            "课题组在仓立面上的进行中实验可以用来教学同一结构教训，但未发表数字不作为本章参考文献主张。",
            "仓立面现场项目可以用来说明同一结构教训；未发表数字不作为本章参考文献主张。",
        ),
    ]
    for a, b in cn_reps:
        if a not in cn:
            print("CN miss:", a[:60])
        else:
            cn = cn.replace(a, b)

    # remaining Phase / 书稿
    cn = cn.replace("Phase~4", "")
    cn = cn.replace("Phase 4", "")
    cn = re.sub(r"对齐本章议题\s*", "", cn)
    cn = cn.replace("在本章中：介绍技术族类与 harness", "介绍技术族类与 harness")

    # CN asset identifier intro
    old = (
        "几何孪生回答``在哪里''。面向巡检、语言可用的孪生还必须再承诺三件事。"
        "其一，设施团队在工单里已经使用的稳定资产标识，。采集时临时发明的文件名不符合契约。"
    )
    new = (
        "几何孪生回答``在哪里''。面向巡检、语言可用的孪生还必须再承诺三件事。"
        "其一，每个可维护宿主都要有稳定的\\emph{资产标识}：设施团队在工单与台账里已经使用的编码。"
        "本章在首次说明之后将其简写为 Asset-ID，以便语言答案与 CMMS 工单点名同一宿主。"
        "采集时临时发明的文件名不是 Asset-ID。"
    )
    # also handle if punct already fixed
    old2 = old.replace("，。", "。")
    if old in cn:
        cn = cn.replace(old, new)
    elif old2 in cn:
        cn = cn.replace(old2, new)
    else:
        # try looser
        if "稳定的\\emph{资产标识}" not in cn and "稳定资产标识" in cn:
            cn = cn.replace(
                "其一，设施团队在工单里已经使用的稳定资产标识。采集时临时发明的文件名不符合契约。",
                "其一，每个可维护宿主都要有稳定的\\emph{资产标识}：设施团队在工单与台账里已经使用的编码。"
                "本章在首次说明之后将其简写为 Asset-ID，以便语言答案与 CMMS 工单点名同一宿主。"
                "采集时临时发明的文件名不是 Asset-ID。",
                1,
            )
        else:
            print("CN asset intro miss")

    cn = cn.replace(
        "意图=传播，一跳扩展后打包三份护照与三条观测",
        "意图=传播；以设施台账中的示例宿主 \\texttt{W-3-17} 为种子，一跳扩展后打包三份护照与三条观测",
        1,
    )

    # CN LLM extra
    cn_llm = r"""

除架构与提示之外，土木部署还要分清三种 LLM 行为。遵从指令的模型可以在编排器给出模板时按字段作答，从而在短回复里区分观测与假说~\cite{ouyang2022instructgpt,brown2020}。会调用工具的模型可以请求类型化函数，而不把世界状态写进权重，从而使护照读取与邻域扩展落在模型之外~\cite{schick2023toolformer,yao2023react}。长上下文模型可以装下打包后的证据摘要，但仍需要校验器：上下文变长并不会创造出从未检索到的 Asset-ID~\cite{lewis2020,ji2023,liang2023helm}。面向施工的 GPT 综述与建筑应用议程因此把治理、数据就绪与人机监督当作与模型选型并列的设计变量~\cite{saka2024gptconstruction,ma2026tenquestions}。对立面巡检，这些变量落到实处，就是版本钉扎、模态标签、引用或拒答检查，以及写入门禁。

"""
    if "除架构与提示之外，土木部署还要分清三种 LLM 行为" not in cn:
        m = "当代 LLM 建立在 Transformer 架构之上"
        i = cn.find(m)
        if i >= 0:
            e = cn.find("\n\n", i)
            if e > 0:
                cn = cn[:e] + "\n" + cn_llm + cn[e:]

    cn = fix_cn_punct(cn)
    # remove leftover "此处" meta where easy
    cn = cn.replace("此处不必重推", "读者不必重推")
    cn = cn.replace("此处的厚度意味着", "本章厚度意味着")

    en_path.write_text(en, encoding="utf-8")
    cn_path.write_text(cn, encoding="utf-8")

    print(
        "EN Phase",
        en.count("Phase"),
        "Proposal",
        en.count("Book Proposal"),
        "we recommend",
        en.count("we recommend"),
    )
    print(
        "CN Phase",
        cn.count("Phase"),
        "书稿",
        cn.count("书稿"),
        "课题组",
        cn.count("课题组"),
        "，。",
        cn.count("，。"),
    )


if __name__ == "__main__":
    main()
