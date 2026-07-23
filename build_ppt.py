import sys
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_diagram_only_pptx(output_path="Chapter01_Overall_Pipeline.pptx"):
    prs = Presentation()
    # 16:9 Widescreen
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    COLOR_BLACK = RGBColor(0, 0, 0)
    COLOR_WHITE = RGBColor(255, 255, 255)
    COLOR_LINE = RGBColor(50, 50, 50)

    FONT_NAME = "Times New Roman"

    # Concise Chinese Tree Data
    phases_cn = [
        {
            "phase": "阶段一：智能数据采集",
            "chaps": [
                {
                    "title": "第 2 章：任务规划",
                    "subs": ["多机协同分配", "覆盖路径规划", "能耗感知优化"]
                },
                {
                    "title": "第 3 章：运动规划",
                    "subs": ["实时建图定位", "避障轨迹生成", "风场扰动控制"]
                }
            ]
        },
        {
            "phase": "阶段二：三维表达与数据基准",
            "chaps": [
                {
                    "title": "第 4 章：三维重建",
                    "subs": ["SfM 密集重建", "Mesh 神经渲染", "点云 BIM 对齐"]
                },
                {
                    "title": "第 5 章：巡检数据集",
                    "subs": ["多模态采集 (RGB/红外)", "缺陷标注规范", "语义分割基准"]
                }
            ]
        },
        {
            "phase": "阶段三：AI 缺陷感知",
            "chaps": [
                {
                    "title": "第 6 章：AI 检测模型",
                    "subs": ["机载低时延约束", "缺陷检测与分割", "严重程度量化", "边缘机载部署"]
                }
            ]
        },
        {
            "phase": "阶段四：数字孪生与 LLM 决策",
            "chaps": [
                {
                    "title": "第 7 章：GIS 与 GeoBIM",
                    "subs": ["GeoBIM 空间映射", "退化时空分析", "资产护照挂载"]
                },
                {
                    "title": "第 8 章：数字孪生与大模型",
                    "subs": ["LLM/VLM 推理底座", "孪生记忆与 RAG", "维保决策与报告"]
                },
                {
                    "title": "第 9 章：总结与展望",
                    "subs": ["端到端系统闭环总结", "法规与安全约束", "自主集群展望"]
                }
            ]
        }
    ]

    # Concise English Tree Data
    phases_en = [
        {
            "phase": "Phase I: Data Acquisition",
            "chaps": [
                {
                    "title": "Chapter 2: Task Planning",
                    "subs": ["Multi-UAV Routing", "Coverage Path Opt.", "Energy Management"]
                },
                {
                    "title": "Chapter 3: Motion Planning",
                    "subs": ["Mapping & Localiz.", "Obstacle Avoidance", "Wind Control"]
                }
            ]
        },
        {
            "phase": "Phase II: 3D Recon & Datasets",
            "chaps": [
                {
                    "title": "Chapter 4: 3D Reconstruction",
                    "subs": ["SfM & Point Clouds", "Mesh & Rendering", "BIM Alignment"]
                },
                {
                    "title": "Chapter 5: Datasets",
                    "subs": ["Multimodal Capture", "Defect Annotation", "Benchmark Splits"]
                }
            ]
        },
        {
            "phase": "Phase III: AI Defect Perception",
            "chaps": [
                {
                    "title": "Chapter 6: AI Defect Models",
                    "subs": ["On-board Latency", "Defect Detection", "Instance Seg.", "Edge Validation"]
                }
            ]
        },
        {
            "phase": "Phase IV: Digital Twin & LLM",
            "chaps": [
                {
                    "title": "Chapter 7: GIS & GeoBIM",
                    "subs": ["GeoBIM Mapping", "Degradation Analysis", "Asset Passports"]
                },
                {
                    "title": "Chapter 8: Digital Twin & LLM",
                    "subs": ["LLM/VLM Reasoning", "Twin Memory & RAG", "Maintenance DSS"]
                },
                {
                    "title": "Chapter 9: Conclusion",
                    "subs": ["System Summary", "Safety & Bounds", "Autonomous Swarms"]
                }
            ]
        }
    ]

    def build_diagram_slide(prs, phases_data):
        slide = prs.slides.add_slide(blank_layout)

        # Full Slide Metrics (Diagram Only, No Titles, No Captions)
        start_x = Inches(0.6)
        start_y = Inches(0.6)
        col_w = Inches(2.8)
        gap_x = Inches(0.24)
        total_h = Inches(6.3) # Fill full slide height

        for i, phase_info in enumerate(phases_data):
            col_x = start_x + i * (col_w + gap_x)

            # Phase Header Node
            phase_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, col_x, start_y, col_w, Inches(0.48))
            phase_box.fill.solid()
            phase_box.fill.fore_color.rgb = COLOR_WHITE
            phase_box.line.color.rgb = COLOR_BLACK
            phase_box.line.width = Pt(1.5)

            tf_p = phase_box.text_frame
            tf_p.vertical_anchor = MSO_ANCHOR.MIDDLE
            tf_p.margin_left = tf_p.margin_right = Inches(0.05)
            p_ph = tf_p.paragraphs[0]
            p_ph.text = phase_info["phase"]
            p_ph.font.name = FONT_NAME
            p_ph.font.size = Pt(13)
            p_ph.font.bold = True
            p_ph.font.color.rgb = COLOR_BLACK
            p_ph.alignment = PP_ALIGN.CENTER

            # Vertical Stem Line down from Phase Header
            stem_top_x = col_x + col_w / 2
            stem_top_y = start_y + Inches(0.48)

            chaps = phase_info["chaps"]
            num_ch = len(chaps)

            if num_ch == 1:
                ch_y_positions = [start_y + Inches(0.9)]
            elif num_ch == 2:
                ch_y_positions = [start_y + Inches(0.9), start_y + Inches(4.0)]
            else: # 3 chapters
                ch_y_positions = [start_y + Inches(0.9), start_y + Inches(3.0), start_y + Inches(5.0)]

            max_ch_y = ch_y_positions[-1]
            stem_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, stem_top_x - Inches(0.005), stem_top_y, Inches(0.01), max_ch_y - stem_top_y)
            stem_line.fill.solid()
            stem_line.fill.fore_color.rgb = COLOR_LINE
            stem_line.line.fill.background()

            # Render Chapters and Sub-points
            for ch_idx, ch in enumerate(chaps):
                curr_ch_y = ch_y_positions[ch_idx]

                # Chapter Box (Larger, Clearer)
                ch_w = Inches(2.6)
                ch_x = col_x + (col_w - ch_w) / 2
                ch_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, ch_x, curr_ch_y, ch_w, Inches(0.42))
                ch_box.fill.solid()
                ch_box.fill.fore_color.rgb = COLOR_WHITE
                ch_box.line.color.rgb = COLOR_BLACK
                ch_box.line.width = Pt(1.2)

                tf_c = ch_box.text_frame
                tf_c.vertical_anchor = MSO_ANCHOR.MIDDLE
                tf_c.margin_left = tf_c.margin_right = Inches(0.08)
                p_c = tf_c.paragraphs[0]
                p_c.text = ch['title']
                p_c.font.name = FONT_NAME
                p_c.font.size = Pt(11.5)
                p_c.font.bold = True
                p_c.font.color.rgb = COLOR_BLACK
                p_c.alignment = PP_ALIGN.CENTER

                # Sub-points Tree Branching
                sub_start_y = curr_ch_y + Inches(0.50)
                sub_indent_x = ch_x + Inches(0.20)
                sub_line_x = ch_x + Inches(0.10)

                num_subs = len(ch["subs"])
                sub_item_h = Inches(0.28) # Larger height for 10.5pt font
                
                if num_subs > 0:
                    tree_stem_h = (num_subs - 1) * (sub_item_h + Inches(0.06)) + Inches(0.14)
                    tree_stem = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, sub_line_x, sub_start_y - Inches(0.06), Inches(0.008), tree_stem_h)
                    tree_stem.fill.solid()
                    tree_stem.fill.fore_color.rgb = COLOR_LINE
                    tree_stem.line.fill.background()

                for s_idx, sub_text in enumerate(ch["subs"]):
                    s_y = sub_start_y + s_idx * (sub_item_h + Inches(0.06))

                    # Horizontal Connector Line
                    h_branch = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, sub_line_x, s_y + Inches(0.12), Inches(0.09), Inches(0.008))
                    h_branch.fill.solid()
                    h_branch.fill.fore_color.rgb = COLOR_LINE
                    h_branch.line.fill.background()

                    # Sub-point Pill Box (Larger font 10.5pt)
                    sub_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, sub_indent_x, s_y, Inches(2.28), sub_item_h)
                    sub_box.fill.solid()
                    sub_box.fill.fore_color.rgb = COLOR_WHITE
                    sub_box.line.color.rgb = COLOR_LINE
                    sub_box.line.width = Pt(0.75)

                    tf_s = sub_box.text_frame
                    tf_s.vertical_anchor = MSO_ANCHOR.MIDDLE
                    tf_s.margin_left = tf_s.margin_right = Inches(0.08)
                    p_s = tf_s.paragraphs[0]
                    p_s.text = f"• {sub_text}"
                    p_s.font.name = FONT_NAME
                    p_s.font.size = Pt(10.5)
                    p_s.font.color.rgb = COLOR_BLACK

            # Thin Connecting Arrow to Next Phase
            if i < len(phases_data) - 1:
                arrow_x = col_x + col_w + Inches(0.02)
                arrow_y = start_y + Inches(0.12)
                arrow = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, arrow_x, arrow_y, Inches(0.20), Inches(0.24))
                arrow.fill.solid()
                arrow.fill.fore_color.rgb = COLOR_BLACK
                arrow.line.fill.background()

    # Slide 1: Chinese
    build_diagram_slide(prs, phases_cn)

    # Slide 2: English
    build_diagram_slide(prs, phases_en)

    dirname = os.path.dirname(output_path)
    if dirname:
        os.makedirs(dirname, exist_ok=True)
    prs.save(output_path)
    print(f"Successfully generated diagram-only PPTX at: {output_path}")

    figures_src_path = "figures_src/overall_pipeline_ch01.pptx"
    prs.save(figures_src_path)
    print(f"Saved copy to: {figures_src_path}")

if __name__ == "__main__":
    create_diagram_only_pptx("Chapter01_Overall_Pipeline.pptx")
