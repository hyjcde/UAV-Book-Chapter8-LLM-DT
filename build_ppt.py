import sys
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_academic_pipeline_pptx(output_path="Chapter01_Overall_Pipeline.pptx"):
    prs = Presentation()
    # 16:9 Widescreen Dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Pure Academic Palette: Black & White
    COLOR_BLACK = RGBColor(0, 0, 0)
    COLOR_WHITE = RGBColor(255, 255, 255)
    COLOR_MUTED = RGBColor(90, 90, 90)

    FONT_TITLE = "Times New Roman"
    FONT_BODY = "Times New Roman"

    # =========================================================================
    # SLIDE 1: 中文版 (Chinese Version - 1 Page)
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)

    # Title Box
    title_box1 = slide1.shapes.add_textbox(Inches(0.8), Inches(0.45), Inches(11.733), Inches(0.85))
    tf1 = title_box1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_top = tf1.margin_right = tf1.margin_bottom = 0

    p1 = tf1.paragraphs[0]
    p1.text = "专著总体框架与章节结构图"
    p1.font.name = FONT_TITLE
    p1.font.size = Pt(22)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_BLACK

    p1_sub = tf1.add_paragraph()
    p1_sub.text = "AI-Driven UAV Building Inspection: An End-to-End Framework from Autonomous Flight to Digital Twins"
    p1_sub.font.name = FONT_TITLE
    p1_sub.font.size = Pt(12)
    p1_sub.font.color.rgb = COLOR_MUTED

    phases_cn = [
        {
            "phase_title": "阶段一：自主采集与规划",
            "chapters": [
                {
                    "ch_num": "第 2 章：任务规划",
                    "ch_desc": "• 立面巡检覆盖路径规划\n• ROI 区域定义与多机协同"
                },
                {
                    "ch_num": "第 3 章：运动规划",
                    "ch_desc": "• 实时避障与轨迹优化\n• 风场扰动适应与自主控制"
                }
            ]
        },
        {
            "phase_title": "阶段二：重建与数据表达",
            "chapters": [
                {
                    "ch_num": "第 4 章：三维重建",
                    "ch_desc": "• 倾斜摄影测量与点云建模\n• Mesh 构网与 BIM 坐标对齐"
                },
                {
                    "ch_num": "第 5 章：巡检数据集",
                    "ch_desc": "• RGB / 热成像多模态采集\n• 缺陷标注规范与基准集"
                }
            ]
        },
        {
            "phase_title": "阶段三：AI 缺陷感知",
            "chapters": [
                {
                    "ch_num": "第 6 章：AI 缺陷检测模型",
                    "ch_desc": "• 深度学习目标检测\n• 构件实例分割与定量量化\n• 缺陷严重程度评估"
                }
            ]
        },
        {
            "phase_title": "阶段四：数字孪生与决策",
            "chapters": [
                {
                    "ch_num": "第 7 章：GIS 与 GeoBIM 集成",
                    "ch_desc": "• 空间数据库与 GeoBIM 映射\n• 缺陷与资产护照 (Passport) 挂载"
                },
                {
                    "ch_num": "第 8 章：数字孪生与大模型",
                    "ch_desc": "• LLM / VLM 检索增强推理 (RAG)\n• 历史维保查询与预测性维护"
                },
                {
                    "ch_num": "第 9 章：总结与展望",
                    "ch_desc": "• 现场部署经验审计\n• 开放挑战与下一代系统展望"
                }
            ]
        }
    ]

    start_x = Inches(0.8)
    start_y = Inches(1.5)
    col_w = Inches(2.65)
    gap_x = Inches(0.38)
    total_h = Inches(5.1)

    for i, phase in enumerate(phases_cn):
        col_x = start_x + i * (col_w + gap_x)

        # Header Box (Phase Title)
        header = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, col_x, start_y, col_w, Inches(0.5))
        header.fill.solid()
        header.fill.fore_color.rgb = COLOR_WHITE
        header.line.color.rgb = COLOR_BLACK
        header.line.width = Pt(1.25)

        tf_h = header.text_frame
        tf_h.vertical_anchor = MSO_ANCHOR.MIDDLE
        p_h = tf_h.paragraphs[0]
        p_h.text = phase["phase_title"]
        p_h.font.name = FONT_BODY
        p_h.font.size = Pt(11)
        p_h.font.bold = True
        p_h.font.color.rgb = COLOR_BLACK
        p_h.alignment = PP_ALIGN.CENTER

        # Stack Chapter Boxes
        num_ch = len(phase["chapters"])
        top_y = start_y + Inches(0.6)
        avail_h = total_h - Inches(0.6)
        ch_h = (avail_h - Inches(0.12) * (num_ch - 1)) / num_ch

        curr_y = top_y
        for ch in phase["chapters"]:
            card = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, col_x, curr_y, col_w, ch_h)
            card.fill.solid()
            card.fill.fore_color.rgb = COLOR_WHITE
            card.line.color.rgb = COLOR_BLACK
            card.line.width = Pt(1.0)

            tf_c = card.text_frame
            tf_c.word_wrap = True
            tf_c.margin_left = Inches(0.12)
            tf_c.margin_right = Inches(0.12)
            tf_c.margin_top = Inches(0.12)
            tf_c.vertical_anchor = MSO_ANCHOR.TOP

            p_c1 = tf_c.paragraphs[0]
            p_c1.text = ch["ch_num"]
            p_c1.font.name = FONT_BODY
            p_c1.font.size = Pt(10.5)
            p_c1.font.bold = True
            p_c1.font.color.rgb = COLOR_BLACK
            p_c1.space_after = Pt(4)

            p_c2 = tf_c.add_paragraph()
            p_c2.text = ch["ch_desc"]
            p_c2.font.name = FONT_BODY
            p_c2.font.size = Pt(9.5)
            p_c2.font.color.rgb = COLOR_BLACK

            curr_y += ch_h + Inches(0.12)

        # Connecting Arrow
        if i < len(phases_cn) - 1:
            arrow_x = col_x + col_w + Inches(0.08)
            arrow_y = start_y + total_h / 2 - Inches(0.12)
            arrow = slide1.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, arrow_x, arrow_y, Inches(0.22), Inches(0.24))
            arrow.fill.solid()
            arrow.fill.fore_color.rgb = COLOR_BLACK
            arrow.line.fill.background()

    # Caption
    footer1 = slide1.shapes.add_textbox(Inches(0.8), Inches(6.8), Inches(11.733), Inches(0.4))
    p_ft1 = footer1.text_frame.paragraphs[0]
    p_ft1.text = "图 1.1：专著四阶段端到端技术路线与章节映射关系（从物理采集、三维重建到大模型决策支持）"
    p_ft1.font.name = FONT_BODY
    p_ft1.font.size = Pt(10)
    p_ft1.font.bold = True
    p_ft1.font.color.rgb = COLOR_BLACK


    # =========================================================================
    # SLIDE 2: 英文版 (English Version - 1 Page)
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)

    # Title Box
    title_box2 = slide2.shapes.add_textbox(Inches(0.8), Inches(0.45), Inches(11.733), Inches(0.85))
    tf2 = title_box2.text_frame
    tf2.word_wrap = True
    tf2.margin_left = tf2.margin_top = tf2.margin_right = tf2.margin_bottom = 0

    p2 = tf2.paragraphs[0]
    p2.text = "Overall Framework and Chapter Map"
    p2.font.name = FONT_TITLE
    p2.font.size = Pt(22)
    p2.font.bold = True
    p2.font.color.rgb = COLOR_BLACK

    p2_sub = tf2.add_paragraph()
    p2_sub.text = "AI-Driven UAV Building Inspection: An End-to-End Framework from Autonomous Flight to Digital Twins"
    p2_sub.font.name = FONT_TITLE
    p2_sub.font.size = Pt(12)
    p2_sub.font.color.rgb = COLOR_MUTED

    phases_en = [
        {
            "phase_title": "Phase I: Flight & Acquisition",
            "chapters": [
                {
                    "ch_num": "Chapter 2: Task Planning",
                    "ch_desc": "• Façade inspection path planning\n• ROI definition & multi-UAV routing"
                },
                {
                    "ch_num": "Chapter 3: Motion Planning",
                    "ch_desc": "• Obstacle avoidance & trajectory opt.\n• Wind disturbance adaptation"
                }
            ]
        },
        {
            "phase_title": "Phase II: Reconstruction & Data",
            "chapters": [
                {
                    "ch_num": "Chapter 4: 3D Reconstruction",
                    "ch_desc": "• Photogrammetry & point clouds\n• Mesh modeling & BIM alignment"
                },
                {
                    "ch_num": "Chapter 5: Inspection Datasets",
                    "ch_desc": "• Multimodal RGB / Thermal capture\n• Defect annotation & benchmarks"
                }
            ]
        },
        {
            "phase_title": "Phase III: AI Defect Perception",
            "chapters": [
                {
                    "ch_num": "Chapter 6: AI Defect Models",
                    "ch_desc": "• Deep learning defect detection\n• Instance segmentation & quantification\n• Severity rating"
                }
            ]
        },
        {
            "phase_title": "Phase IV: Digital Twin & LLM",
            "chapters": [
                {
                    "ch_num": "Chapter 7: GIS & GeoBIM",
                    "ch_desc": "• Spatial database & GeoBIM mapping\n• Defect & Asset Passport attachment"
                },
                {
                    "ch_num": "Chapter 8: Digital Twin & LLM",
                    "ch_desc": "• LLM / VLM RAG reasoning\n• Maintenance query & decision support"
                },
                {
                    "ch_num": "Chapter 9: Conclusion & Future",
                    "ch_desc": "• Field deployment audit\n• Open challenges & future outlook"
                }
            ]
        }
    ]

    for i, phase in enumerate(phases_en):
        col_x = start_x + i * (col_w + gap_x)

        # Header Box
        header = slide2.shapes.add_shape(MSO_SHAPE.RECTANGLE, col_x, start_y, col_w, Inches(0.5))
        header.fill.solid()
        header.fill.fore_color.rgb = COLOR_WHITE
        header.line.color.rgb = COLOR_BLACK
        header.line.width = Pt(1.25)

        tf_h = header.text_frame
        tf_h.vertical_anchor = MSO_ANCHOR.MIDDLE
        p_h = tf_h.paragraphs[0]
        p_h.text = phase["phase_title"]
        p_h.font.name = FONT_BODY
        p_h.font.size = Pt(11)
        p_h.font.bold = True
        p_h.font.color.rgb = COLOR_BLACK
        p_h.alignment = PP_ALIGN.CENTER

        # Stack Chapter Boxes
        num_ch = len(phase["chapters"])
        top_y = start_y + Inches(0.6)
        avail_h = total_h - Inches(0.6)
        ch_h = (avail_h - Inches(0.12) * (num_ch - 1)) / num_ch

        curr_y = top_y
        for ch in phase["chapters"]:
            card = slide2.shapes.add_shape(MSO_SHAPE.RECTANGLE, col_x, curr_y, col_w, ch_h)
            card.fill.solid()
            card.fill.fore_color.rgb = COLOR_WHITE
            card.line.color.rgb = COLOR_BLACK
            card.line.width = Pt(1.0)

            tf_c = card.text_frame
            tf_c.word_wrap = True
            tf_c.margin_left = Inches(0.12)
            tf_c.margin_right = Inches(0.12)
            tf_c.margin_top = Inches(0.12)
            tf_c.vertical_anchor = MSO_ANCHOR.TOP

            p_c1 = tf_c.paragraphs[0]
            p_c1.text = ch["ch_num"]
            p_c1.font.name = FONT_BODY
            p_c1.font.size = Pt(10.5)
            p_c1.font.bold = True
            p_c1.font.color.rgb = COLOR_BLACK
            p_c1.space_after = Pt(4)

            p_c2 = tf_c.add_paragraph()
            p_c2.text = ch["ch_desc"]
            p_c2.font.name = FONT_BODY
            p_c2.font.size = Pt(9.5)
            p_c2.font.color.rgb = COLOR_BLACK

            curr_y += ch_h + Inches(0.12)

        # Connecting Arrow
        if i < len(phases_en) - 1:
            arrow_x = col_x + col_w + Inches(0.08)
            arrow_y = start_y + total_h / 2 - Inches(0.12)
            arrow = slide2.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, arrow_x, arrow_y, Inches(0.22), Inches(0.24))
            arrow.fill.solid()
            arrow.fill.fore_color.rgb = COLOR_BLACK
            arrow.line.fill.background()

    # Caption
    footer2 = slide2.shapes.add_textbox(Inches(0.8), Inches(6.8), Inches(11.733), Inches(0.4))
    p_ft2 = footer2.text_frame.paragraphs[0]
    p_ft2.text = "Figure 1.1: End-to-end four-phase methodology and chapter mapping of the monograph."
    p_ft2.font.name = FONT_BODY
    p_ft2.font.size = Pt(10)
    p_ft2.font.bold = True
    p_ft2.font.color.rgb = COLOR_BLACK

    # Save PPTX
    dirname = os.path.dirname(output_path)
    if dirname:
        os.makedirs(dirname, exist_ok=True)
    prs.save(output_path)
    print(f"Successfully generated academic presentation at: {output_path}")

    # Copy to figures_src
    figures_src_path = "figures_src/overall_pipeline_ch01.pptx"
    prs.save(figures_src_path)
    print(f"Successfully saved copy at: {figures_src_path}")

if __name__ == "__main__":
    create_academic_pipeline_pptx("Chapter01_Overall_Pipeline.pptx")
