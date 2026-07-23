import sys
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_tree_pipeline_pptx(output_path="Chapter01_Overall_Pipeline.pptx"):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    COLOR_BLACK = RGBColor(0, 0, 0)
    COLOR_WHITE = RGBColor(255, 255, 255)
    COLOR_MUTED = RGBColor(90, 90, 90)
    COLOR_LINE = RGBColor(40, 40, 40)

    FONT_NAME = "Times New Roman"

    # Full proposal structure with exact sub-sections
    phases_cn = [
        {
            "phase": "阶段一：智能数据采集",
            "en_phase": "Phase I: Intelligent Data Acquisition",
            "chaps": [
                {
                    "title": "第 2 章：无人机任务规划",
                    "lead": "（Xinyi Wang）",
                    "subs": ["2.2 多机协同与任务分配", "2.4 立面巡检覆盖路径规划", "2.5 能耗感知优化控制"]
                },
                {
                    "title": "第 3 章：环境运动规划",
                    "lead": "（Chuanxiang Gao）",
                    "subs": ["3.2 实时建图与定位", "3.3 复杂环境避障轨迹生成", "3.4 风场扰动下自主控制"]
                }
            ]
        },
        {
            "phase": "阶段二：三维表达与数据基准",
            "en_phase": "Phase II: Digital Representation & Data",
            "chaps": [
                {
                    "title": "第 4 章：三维重建与映射",
                    "lead": "（Guidong Yang）",
                    "subs": ["4.2 SfM 稀疏与密集重建", "4.4 神经渲染与 Mesh 构网", "4.5 点云配准与 BIM 对齐"]
                },
                {
                    "title": "第 5 章：数据集与基准",
                    "lead": "（Benyun Zhao）",
                    "subs": ["5.2 多模态图像预处理与标注", "5.3 建筑立面缺陷 Detection", "5.4 缺陷 Instance Segmentation"]
                }
            ]
        },
        {
            "phase": "阶段三：AI 缺陷感知分析",
            "en_phase": "Phase III: AI Defect Perception",
            "chaps": [
                {
                    "title": "第 6 章：巡检 AI 检测模型",
                    "lead": "（Benyun Zhao）",
                    "subs": ["6.1 机载算力与低时延约束", "6.3 缺陷检测深度学习架构", "6.4 实例分割与定量评估", "6.6 边缘部署与机载实测校验"]
                }
            ]
        },
        {
            "phase": "阶段四：数字孪生与大模型",
            "en_phase": "Phase IV: Digital Twin & LLM",
            "chaps": [
                {
                    "title": "第 7 章：GIS 与 GeoBIM 集成",
                    "lead": "（Jihan Zhang）",
                    "subs": ["7.2 UAV 数据映射 GeoBIM", "7.3 结构退化时空分析", "7.5 城市级资产护照挂载"]
                },
                {
                    "title": "第 8 章：数字孪生与大模型",
                    "lead": "（Yijun Huang）",
                    "subs": ["8.2 LLM / VLM 领域推理底座", "8.3 孪生记忆与 RAG 检索", "8.5/8.6 报告生成与预测维护"]
                },
                {
                    "title": "第 9 章：总结与展望",
                    "lead": "（Ben M. Chen et al.）",
                    "subs": ["9.1 端到端系统闭环总结", "9.2 法规、安全与隐私约束", "9.3 自主集群与下一代 AI"]
                }
            ]
        }
    ]

    phases_en = [
        {
            "phase": "Phase I: Data Acquisition",
            "chaps": [
                {
                    "title": "Chapter 2: Task Planning",
                    "lead": "(Xinyi Wang)",
                    "subs": ["2.2 Multi-UAV Task Allocation", "2.4 Façade Coverage Path Planning", "2.5 Energy-Aware Optimization"]
                },
                {
                    "title": "Chapter 3: Motion Planning",
                    "lead": "(Chuanxiang Gao)",
                    "subs": ["3.2 Real-time Mapping & Localiz.", "3.3 Obstacle Trajectory Generation", "3.4 Wind Disturbance Control"]
                }
            ]
        },
        {
            "phase": "Phase II: 3D Recon. & Datasets",
            "chaps": [
                {
                    "title": "Chapter 4: 3D Reconstruction",
                    "lead": "(Guidong Yang)",
                    "subs": ["4.2 SfM Sparse & Dense Recon.", "4.4 Neural Rendering & Mesh", "4.5 Point Cloud & BIM Alignment"]
                },
                {
                    "title": "Chapter 5: Inspection Datasets",
                    "lead": "(Benyun Zhao)",
                    "subs": ["5.2 Multimodal Preproc. & Annot.", "5.3 Façade Defect Detection", "5.4 Instance Segmentation"]
                }
            ]
        },
        {
            "phase": "Phase III: AI Defect Perception",
            "chaps": [
                {
                    "title": "Chapter 6: AI Defect Models",
                    "lead": "(Benyun Zhao)",
                    "subs": ["6.1 On-board Compute & Latency", "6.3 Defect Detection Architectures", "6.4 Instance Seg. & Metrics", "6.6 Edge Deployment Validation"]
                }
            ]
        },
        {
            "phase": "Phase IV: Digital Twin & LLM",
            "chaps": [
                {
                    "title": "Chapter 7: GIS & GeoBIM",
                    "lead": "(Jihan Zhang)",
                    "subs": ["7.2 Mapping UAV/3D to GeoBIM", "7.3 Spatiotemporal Degradation", "7.5 City Asset Passport Mgmt"]
                },
                {
                    "title": "Chapter 8: Digital Twin & LLM",
                    "lead": "(Yijun Huang)",
                    "subs": ["8.2 LLM / VLM Domain Reasoning", "8.3 Twin Memory & RAG Retrieval", "8.5/8.6 Report & Maintenance DSS"]
                },
                {
                    "title": "Chapter 9: Conclusion & Outlook",
                    "lead": "(Ben M. Chen et al.)",
                    "subs": ["9.1 End-to-End System Summary", "9.2 Regulatory & Safety Bounds", "9.3 Autonomous Swarms & AI"]
                }
            ]
        }
    ]

    def build_tree_slide(prs, title_text, subtitle_text, caption_text, phases_data, is_chinese=True):
        slide = prs.slides.add_slide(blank_layout)

        # Slide Title Header
        title_box = slide.shapes.add_textbox(Inches(0.6), Inches(0.4), Inches(12.133), Inches(0.85))
        tf = title_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p = tf.paragraphs[0]
        p.text = title_text
        p.font.name = FONT_NAME
        p.font.size = Pt(20)
        p.font.bold = True
        p.font.color.rgb = COLOR_BLACK

        p_sub = tf.add_paragraph()
        p_sub.text = subtitle_text
        p_sub.font.name = FONT_NAME
        p_sub.font.size = Pt(11)
        p_sub.font.color.rgb = COLOR_MUTED

        # Grid Layout Metrics
        start_x = Inches(0.6)
        start_y = Inches(1.35)
        col_w = Inches(2.8)
        gap_x = Inches(0.24)

        for i, phase_info in enumerate(phases_data):
            col_x = start_x + i * (col_w + gap_x)

            # Phase Header Box (Compact Rounded Rectangle)
            phase_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, col_x, start_y, col_w, Inches(0.38))
            phase_box.fill.solid()
            phase_box.fill.fore_color.rgb = COLOR_WHITE
            phase_box.line.color.rgb = COLOR_BLACK
            phase_box.line.width = Pt(1.25)

            tf_p = phase_box.text_frame
            tf_p.vertical_anchor = MSO_ANCHOR.MIDDLE
            tf_p.margin_left = tf_p.margin_right = Inches(0.05)
            p_ph = tf_p.paragraphs[0]
            p_ph.text = phase_info["phase"]
            p_ph.font.name = FONT_NAME
            p_ph.font.size = Pt(10)
            p_ph.font.bold = True
            p_ph.font.color.rgb = COLOR_BLACK
            p_ph.alignment = PP_ALIGN.CENTER

            # Vertical Stem Line down from Phase Header
            stem_top_x = col_x + col_w / 2
            stem_top_y = start_y + Inches(0.38)

            chaps = phase_info["chaps"]
            num_ch = len(chaps)

            # Y Positions for Chapters in this Column
            if num_ch == 1:
                ch_y_positions = [start_y + Inches(0.75)]
            elif num_ch == 2:
                ch_y_positions = [start_y + Inches(0.75), start_y + Inches(3.5)]
            else: # 3 chapters
                ch_y_positions = [start_y + Inches(0.75), start_y + Inches(2.65), start_y + Inches(4.55)]

            # Draw Vertical Connector Line for Column Stem
            max_ch_y = ch_y_positions[-1]
            stem_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, stem_top_x - Inches(0.005), stem_top_y, Inches(0.01), max_ch_y - stem_top_y)
            stem_line.fill.solid()
            stem_line.fill.fore_color.rgb = COLOR_LINE
            stem_line.line.fill.background()

            # Render Chapters and Sub-points Tree
            for ch_idx, ch in enumerate(chaps):
                curr_ch_y = ch_y_positions[ch_idx]

                # Chapter Box (Compact Small Rounded Rectangle)
                ch_w = Inches(2.55)
                ch_x = col_x + (col_w - ch_w) / 2
                ch_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, ch_x, curr_ch_y, ch_w, Inches(0.36))
                ch_box.fill.solid()
                ch_box.fill.fore_color.rgb = COLOR_WHITE
                ch_box.line.color.rgb = COLOR_BLACK
                ch_box.line.width = Pt(1.0)

                tf_c = ch_box.text_frame
                tf_c.vertical_anchor = MSO_ANCHOR.MIDDLE
                tf_c.margin_left = tf_c.margin_right = Inches(0.08)
                p_c = tf_c.paragraphs[0]
                p_c.text = f"{ch['title']} {ch['lead']}"
                p_c.font.name = FONT_NAME
                p_c.font.size = Pt(9.2)
                p_c.font.bold = True
                p_c.font.color.rgb = COLOR_BLACK

                # Sub-points Tree Branching
                sub_start_y = curr_ch_y + Inches(0.42)
                sub_indent_x = ch_x + Inches(0.18)
                sub_line_x = ch_x + Inches(0.08)

                num_subs = len(ch["subs"])
                sub_item_h = Inches(0.24)
                
                # Draw Tree Branch Vertical Stem for Sub-points
                if num_subs > 0:
                    tree_stem_h = (num_subs - 1) * (sub_item_h + Inches(0.04)) + Inches(0.12)
                    tree_stem = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, sub_line_x, sub_start_y - Inches(0.06), Inches(0.008), tree_stem_h)
                    tree_stem.fill.solid()
                    tree_stem.fill.fore_color.rgb = COLOR_LINE
                    tree_stem.line.fill.background()

                for s_idx, sub_text in enumerate(ch["subs"]):
                    s_y = sub_start_y + s_idx * (sub_item_h + Inches(0.04))

                    # Horizontal Branch Connector Line
                    h_branch = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, sub_line_x, s_y + Inches(0.1), Inches(0.08), Inches(0.008))
                    h_branch.fill.solid()
                    h_branch.fill.fore_color.rgb = COLOR_LINE
                    h_branch.line.fill.background()

                    # Sub-point Node (Small Pill / Rounded Card)
                    sub_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, sub_indent_x, s_y, Inches(2.28), sub_item_h)
                    sub_box.fill.solid()
                    sub_box.fill.fore_color.rgb = COLOR_WHITE
                    sub_box.line.color.rgb = COLOR_LINE
                    sub_box.line.width = Pt(0.5)

                    tf_s = sub_box.text_frame
                    tf_s.vertical_anchor = MSO_ANCHOR.MIDDLE
                    tf_s.margin_left = tf_s.margin_right = Inches(0.06)
                    p_s = tf_s.paragraphs[0]
                    p_s.text = sub_text
                    p_s.font.name = FONT_NAME
                    p_s.font.size = Pt(8.2)
                    p_s.font.color.rgb = COLOR_BLACK

            # Thin Horizontal Inter-Phase Arrow
            if i < len(phases_data) - 1:
                arrow_x = col_x + col_w + Inches(0.02)
                arrow_y = start_y + Inches(0.08)
                arrow = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, arrow_x, arrow_y, Inches(0.20), Inches(0.22))
                arrow.fill.solid()
                arrow.fill.fore_color.rgb = COLOR_BLACK
                arrow.line.fill.background()

        # Caption Footer
        footer = slide.shapes.add_textbox(Inches(0.6), Inches(6.82), Inches(12.133), Inches(0.4))
        p_ft = footer.text_frame.paragraphs[0]
        p_ft.text = caption_text
        p_ft.font.name = FONT_NAME
        p_ft.font.size = Pt(9.5)
        p_ft.font.bold = True
        p_ft.font.color.rgb = COLOR_BLACK

    # Slide 1: Chinese
    build_tree_slide(
        prs,
        title_text="专著总体大纲与四阶段技术路线树状映射图",
        subtitle_text="AI-Driven UAV Building Inspection: An End-to-End Framework from Autonomous Flight to Digital Twins",
        caption_text="图 1.1：专著四阶段端到端技术路线树状映射图（全书 9 章从物理采集、三维重建、AI 感知到数字孪生大模型决策）",
        phases_data=phases_cn,
        is_chinese=True
    )

    # Slide 2: English
    build_tree_slide(
        prs,
        title_text="Monograph Overall Structure and Four-Phase Chapter Tree Roadmap",
        subtitle_text="AI-Driven UAV Building Inspection: An End-to-End Framework from Autonomous Flight to Digital Twins",
        caption_text="Figure 1.1: Four-phase end-to-end methodology and detailed chapter tree roadmap of the monograph (Chapters 1–9).",
        phases_data=phases_en,
        is_chinese=False
    )

    dirname = os.path.dirname(output_path)
    if dirname:
        os.makedirs(dirname, exist_ok=True)
    prs.save(output_path)
    print(f"Successfully generated tree pipeline presentation at: {output_path}")

    figures_src_path = "figures_src/overall_pipeline_ch01.pptx"
    prs.save(figures_src_path)
    print(f"Saved copy to: {figures_src_path}")

if __name__ == "__main__":
    create_tree_pipeline_pptx("Chapter01_Overall_Pipeline.pptx")
