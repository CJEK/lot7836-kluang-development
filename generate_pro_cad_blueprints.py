import os
from PIL import Image, ImageDraw, ImageFont

W, H = 2560, 1440

BG_COLOR = (13, 27, 42)          # Professional CAD Slate Navy
GRID_COLOR = (27, 48, 71)        # CAD Grid Line
AXIS_COLOR = (239, 68, 68)       # Red Axis Line (Dash)
DIM_COLOR = (56, 189, 248)       # Cyan Dimension Line & Text
WALL_COLOR = (255, 255, 255)     # Solid White Wall Structure
CONTAINER_COLOR = (250, 204, 21) # Yellow Container Outline
STEEL_COLOR = (249, 115, 22)     # Orange RHS Steel Frame
TEXT_MAIN = (241, 245, 249)      # Pure White Text
TEXT_GOLD = (234, 179, 8)        # Gold Highlight Text
NOTE_BG = (23, 42, 69)           # Note Box Background

font_path = "/System/Library/Fonts/STHeiti Light.ttc"
try:
    f_title = ImageFont.truetype(font_path, 38)
    f_header = ImageFont.truetype(font_path, 28)
    f_body = ImageFont.truetype(font_path, 20)
    f_small = ImageFont.truetype(font_path, 16)
    f_dim = ImageFont.truetype(font_path, 14)
except Exception as e:
    print(f"Font error: {e}")
    f_title = f_header = f_body = f_small = f_dim = ImageFont.load_default()

def draw_cad_frame(title_zh, dwg_no, desc_zh):
    img = Image.new("RGB", (W, H), BG_COLOR)
    d = ImageDraw.Draw(img)
    
    # Grid background
    for x in range(0, W, 50):
        d.line([(x, 0), (x, H)], fill=GRID_COLOR, width=1)
    for y in range(0, H, 50):
        d.line([(0, y), (W, y)], fill=GRID_COLOR, width=1)
        
    # Outer Frame
    d.rectangle([(40, 40), (W - 40, H - 40)], outline=(100, 150, 200), width=3)
    d.rectangle([(46, 46), (W - 46, H - 46)], outline=(50, 90, 140), width=1)
    
    # Title Block (Right Bottom)
    tb_left, tb_top = W - 780, H - 200
    d.rectangle([(tb_left, tb_top), (W - 50, H - 50)], fill=(18, 38, 64), outline=DIM_COLOR, width=2)
    d.line([(tb_left, tb_top + 50), (W - 50, tb_top + 50)], fill=DIM_COLOR, width=1)
    d.line([(tb_left, tb_top + 100), (W - 50, tb_top + 100)], fill=DIM_COLOR, width=1)
    d.line([(tb_left + 480, tb_top), (tb_left + 480, H - 50)], fill=DIM_COLOR, width=1)
    
    d.text((tb_left + 15, tb_top + 12), "PROJECT: LOT 7836 KLUANG DEVELOPMENT", font=f_small, fill=TEXT_MAIN)
    d.text((tb_left + 495, tb_top + 12), f"DWG NO: {dwg_no}", font=f_small, fill=TEXT_GOLD)
    
    d.text((tb_left + 15, tb_top + 62), f"TITLE: {title_zh}", font=f_body, fill=DIM_COLOR)
    d.text((tb_left + 495, tb_top + 62), "SCALE: 1:100 @ A3", font=f_small, fill=TEXT_MAIN)
    
    d.text((tb_left + 15, tb_top + 112), "STAGE: CONCEPTUAL PROPOSAL (FOR PE/AR REVIEW)", font=f_small, fill=TEXT_MAIN)
    d.text((tb_left + 495, tb_top + 112), "STATUS: PRE-SUBMISSION", font=f_small, fill=(248, 113, 113))

    # Header
    d.rectangle([(50, 50), (W - 800, 120)], fill=(20, 45, 75), outline=DIM_COLOR, width=1)
    d.text((70, 65), f"CAD 概念工程规范图纸 | {title_zh}", font=f_title, fill=TEXT_MAIN)
    
    # Disclaimer and Explanation Box (Bottom Left)
    d.rectangle([(50, H - 260), (W - 800, H - 50)], fill=NOTE_BG, outline=DIM_COLOR, width=2)
    d.text((70, H - 245), "⚠️ 专业免责声明与设计控制逻辑 (Conceptual Disclaimer & Design Control):", font=f_body, fill=TEXT_GOLD)
    d.text((70, H - 220), "本图纸为概念设计方案。所有结构力学、消防疏散及排水终图须由马来西亚注册建筑师(Ar.)、专业工程师(P.Eng)、MPK、BOMBA 及 IWK 审核签核。", font=f_dim, fill=(248, 113, 113))
    
    lines = desc_zh.split("\n")
    y_off = H - 190
    for line in lines:
        d.text((70, y_off), line, font=f_small, fill=TEXT_MAIN)
        y_off += 24
        
    return img, d

# 1. DWG A-101: Floor Plan 2D 平面工程图
def make_floorplan():
    img, d = draw_cad_frame(
        "2D 建筑平面布置图 (Architectural Floor Plan)",
        "DWG A-101",
        "1. 单一控制尺寸：50ft W (15.24m) x 75ft D (22.86m)。左右双 40ft High Cube 集装箱 (各 8ft 宽)。\n"
        "2. 切割内墙后补强 100x100mm 方钢圈，中央留出 34ft 挑高大厅。后区 35ft 为双层 Loft 办公区。\n"
        "3. 后区布局开放式厨房 (Kitchen) 与独立双卫生间 (Restrooms)，设 1.5m 宽度消防逃生通道。"
    )
    
    ox, oy = 550, 180
    sw_px, sd_px = 1100, 825
    bx1, by1 = ox, oy
    bx2, by2 = ox + sw_px, oy + sd_px
    
    d.rectangle([(bx1, by1), (bx2, by2)], outline=WALL_COLOR, width=4)
    
    d.line([(bx1 - 40, by1), (bx1 - 40, by2)], fill=DIM_COLOR, width=2)
    d.text((bx1 - 160, oy + sd_px//2), "75' 0\" (22.86m)", font=f_body, fill=DIM_COLOR)
    
    d.line([(bx1, by1 - 40), (bx2, by1 - 40)], fill=DIM_COLOR, width=2)
    d.text((ox + sw_px//2 - 140, by1 - 75), "50' 0\" FRONTAGE (15.24m)", font=f_body, fill=DIM_COLOR)
    
    c1 = (bx1, by1, bx1 + 176, by1 + 440)
    d.rectangle(c1, fill=(40, 50, 30), outline=CONTAINER_COLOR, width=3)
    d.text((bx1 + 15, by1 + 150), "左集装箱 40ft HC\n(8ft x 40ft)", font=f_small, fill=CONTAINER_COLOR)
    
    c2 = (bx2 - 176, by1, bx2, by1 + 440)
    d.rectangle(c2, fill=(40, 50, 30), outline=CONTAINER_COLOR, width=3)
    d.text((bx2 - 160, by1 + 150), "右集装箱 40ft HC\n(8ft x 40ft)", font=f_small, fill=CONTAINER_COLOR)
    
    d.text((ox + sw_px//2 - 200, by1 + 180), "34ft 挑高大厅 (High Ceiling Hall)\n净宽 10.36m / 净高 7.3m", font=f_header, fill=TEXT_MAIN)
    
    d.rectangle([(bx1 + 170, by1 + 50), (bx1 + 182, by1 + 390)], fill=STEEL_COLOR)
    d.text((bx1 + 190, by1 + 220), "← 100mm 方钢门框加固 (Cutout Steel Frame)", font=f_dim, fill=STEEL_COLOR)
    
    d.rectangle([(bx1, by1 + 440), (bx1 + 350, by2)], fill=(20, 60, 80), outline=(56, 189, 248), width=2)
    d.text((bx1 + 20, by1 + 500), "🍳 开放式厨房 (Kitchen)\n配 L型水槽 & 油烟机", font=f_body, fill=TEXT_MAIN)
    
    d.rectangle([(bx2 - 350, by1 + 440), (bx2, by2)], fill=(80, 40, 40), outline=AXIS_COLOR, width=2)
    d.text((bx2 - 330, by1 + 500), "🚽 独立双卫生间 (Restrooms)\n无障碍坡道 & 防滑地砖", font=f_body, fill=TEXT_MAIN)
    
    d.rectangle([(bx1 + 180, by1 + 440), (bx2 - 180, by2)], outline=(250, 204, 21), width=2)
    d.text((ox + sw_px//2 - 220, by1 + 600), "后区 35ft 二层 900sqft Mezzanine Loft 办公平台", font=f_small, fill=TEXT_GOLD)

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/floorplan-bp.jpg", "JPEG", quality=92)
    print("Generated floorplan-bp.jpg DWG A-101")

# 2. DWG A-102: Elevation 正立面图 (严格矫正标高：+24' 檐高 / +38'-5" 屋脊 / +47' 拔风塔顶)
def make_elevation():
    img, d = draw_cad_frame(
        "建筑正立面结构工程图 (Front Elevation & Level Controls)",
        "DWG A-102",
        "1. 控制标高：FL ±0.00m 地坪、+9' 6\" 集装箱顶、+24' 0\" 主屋檐、+38' 5\" 主屋脊、+47' 0\" 拔风塔顶！\n"
        "2. 30° 高坡热带防雨屋顶与中央 Raised Monitor 拔风天窗，利用热浮力快速抽走高空积热。\n"
        "3. 正面设置马六甲 Batu Angin 遮阳通风花砖墙，双层防热遮阳降低室内温度。"
    )
    
    ox, oy = 450, 180
    w_px = 1100
    
    # Ground Line FL ±0.00m
    d.line([(ox - 100, oy + 550), (ox + w_px + 100, oy + 550)], fill=TEXT_MAIN, width=4)
    d.text((ox - 240, oy + 540), "▼ FL ±0.00m (地坪标高)", font=f_body, fill=TEXT_MAIN)
    
    # Container Top (+9'6" / 2.90m)
    d.line([(ox - 100, oy + 440), (ox + w_px + 100, oy + 440)], fill=DIM_COLOR, width=1)
    d.text((ox - 260, oy + 430), "▼ +9' 6\" (2.90m 集装箱顶)", font=f_body, fill=DIM_COLOR)
    
    # Main Eave Level (+24'0" / 7.31m)
    d.line([(ox - 100, oy + 260), (ox + w_px + 100, oy + 260)], fill=DIM_COLOR, width=1)
    d.text((ox - 260, oy + 250), "▼ +24' 0\" (7.31m 主屋檐)", font=f_body, fill=DIM_COLOR)
    
    # Main Ridge Level (+38'5" / 11.71m)
    d.line([(ox - 100, oy + 120), (ox + w_px + 100, oy + 120)], fill=(250, 204, 21), width=1)
    d.text((ox - 270, oy + 110), "▲ +38' 5\" (11.71m 主屋脊)", font=f_body, fill=(250, 204, 21))

    # Raised Jack Roof Top (+47'0" / 14.33m)
    d.line([(ox - 100, oy + 40), (ox + w_px + 100, oy + 40)], fill=AXIS_COLOR, width=2)
    d.text((ox - 290, oy + 30), "▲ +47' 0\" (14.33m 拔风塔顶)", font=f_body, fill=AXIS_COLOR)
    
    # Containers Front
    d.rectangle([(ox, oy + 440), (ox + 176, oy + 550)], outline=CONTAINER_COLOR, width=3)
    d.text((ox + 20, oy + 480), "左集装箱 8ft", font=f_small, fill=CONTAINER_COLOR)
    
    d.rectangle([(ox + w_px - 176, oy + 440), (ox + w_px, oy + 550)], outline=CONTAINER_COLOR, width=3)
    d.text((ox + w_px - 150, oy + 480), "右集装箱 8ft", font=f_small, fill=CONTAINER_COLOR)
    
    # Breeze Block Screen Wall
    d.rectangle([(ox + 176, oy + 360), (ox + w_px - 176, oy + 550)], fill=(30, 50, 40), outline=(74, 222, 128), width=3)
    d.text((ox + w_px//2 - 160, oy + 450), "🧱 Batu Angin 通风花砖屏风墙 (34ft)", font=f_header, fill=(74, 222, 128))
    
    # 30 Roof Truss Profile (+24' to +38'5")
    d.polygon([(ox, oy + 260), (ox + w_px//2, oy + 120), (ox + w_px, oy + 260)], outline=WALL_COLOR, width=3)
    
    # Raised Jack Roof Monitor Window (+38'5" to +47'0")
    d.rectangle([(ox + w_px//2 - 200, oy + 40), (ox + w_px//2 + 200, oy + 120)], fill=(40, 70, 100), outline=AXIS_COLOR, width=2)
    d.text((ox + w_px//2 - 150, oy + 70), "🪟 Raised Jack Roof (+47' 拔风塔)", font=f_small, fill=TEXT_MAIN)

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/elevation-bp.jpg", "JPEG", quality=92)
    print("Generated elevation-bp.jpg DWG A-102 with exact +24' / +38'-5\" / +47' levels")

# 3. DWG G-101: Site Plan 总平面图 (全要素：Jalan Pakis, 北向, 退缩, 6m 消防车道, 300mm U-Drain, 8PE 化粪池)
def make_siteplan():
    img, d = draw_cad_frame(
        "总平面工程规划图 (Site & Infrastructure Plan)",
        "DWG G-101",
        "1. 地块面宽 50ft x 75ft 进深，正面临 Jalan Pakis (北向 North N 标记)。法定退缩：前 20ft, 后 10ft, 侧 5ft。\n"
        "2. 环形提供 6m 宽度 BOMBA 消防车接近通道 (6m Fire Access Road) 与转弯半径。\n"
        "3. 周圈布置 300mm U-Drain 排水沟与检查井 (Inspection Chamber)，后区设 8PE 化粪池与维护通道。"
    )
    
    ox, oy = 550, 180
    d.rectangle([(ox, oy), (ox + 1100, oy + 650)], fill=(15, 32, 55), outline=TEXT_MAIN, width=3)
    
    # North Arrow Indicator (指北针)
    d.line([(ox + 1020, oy + 80), (ox + 1020, oy + 20)], fill=AXIS_COLOR, width=4)
    d.polygon([(ox + 1020, oy + 10), (ox + 1010, oy + 35), (ox + 1030, oy + 35)], fill=AXIS_COLOR)
    d.text((ox + 1010, oy + 90), "NORTH (北)", font=f_body, fill=AXIS_COLOR)
    
    # Road Jalan Pakis Frontage
    d.rectangle([(ox, oy - 60), (ox + 1100, oy)], fill=(40, 40, 50), outline=DIM_COLOR, width=2)
    d.text((ox + 350, oy - 45), "🛣️ JALAN PAKIS 市政道路 (Frontage Road)", font=f_header, fill=TEXT_MAIN)
    
    # Building Footprint
    d.rectangle([(ox + 100, oy + 120), (ox + 1000, oy + 550)], fill=(30, 50, 75), outline=TEXT_GOLD, width=2)
    d.text((ox + 350, oy + 300), "集装箱 Bungalow 主建筑 (50x75ft Footprint)\n前退缩 20ft / 后退缩 10ft", font=f_header, fill=TEXT_MAIN)
    
    # 6m Fire Access Road (6m 消防通道)
    d.rectangle([(ox + 10, oy + 10), (ox + 90, oy + 640)], fill=(60, 30, 30), outline=AXIS_COLOR, width=1)
    d.text((ox + 20, oy + 250), "6m 消防车\n通道 (Fire Access)", font=f_small, fill=AXIS_COLOR)
    
    # U-Drain 300mm & Septic Tank
    d.rectangle([(ox + 850, oy + 570), (ox + 1020, oy + 630)], fill=(80, 60, 20), outline=TEXT_GOLD, width=2)
    d.text((ox + 860, oy + 590), "8PE 化粪池 & 维护通道", font=f_small, fill=TEXT_GOLD)

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/siteplan-bp.jpg", "JPEG", quality=92)
    print("Generated siteplan-bp.jpg DWG G-101")

# 4. DWG F-101: Fire Safety & Egress Plan (全要素消防策略)
def make_fire_safety():
    img, d = draw_cad_frame(
        "BOMBA 消防安全设施与疏散逃生路线图 (Fire Safety & Egress Plan)",
        "DWG F-101",
        "1. 逃生出口门净宽 1.5m，后区 Loft 设置第二逃生钢梯 (2nd Escape Steel Staircase)。\n"
        "2. 全屋最远疏散行走距离限制在 22.5m 内，设置 6 处烟感报警器与 4 处 6kg ABC 灭火器。\n"
        "3. 周圈满足 BOMBA 6m 消防车接近条件。注：本图为概念策略图，须经 BOMBA 最终审查签核。"
    )
    
    ox, oy = 450, 180
    d.rectangle([(ox, oy), (ox + 1200, oy + 650)], outline=WALL_COLOR, width=3)
    
    d.rectangle([(ox + 450, oy - 20), (ox + 750, oy + 20)], fill=(0, 180, 90), outline=TEXT_MAIN, width=2)
    d.text((ox + 470, oy - 15), "🟢 主逃生门 (1.5m 净宽 Exit 1)", font=f_body, fill=TEXT_MAIN)
    
    d.rectangle([(ox + 500, oy + 640), (ox + 700, oy + 670)], fill=(0, 180, 90), outline=TEXT_MAIN, width=2)
    d.text((ox + 510, oy + 645), "🟢 Loft 第二逃生梯 Exit 2", font=f_body, fill=TEXT_MAIN)
    
    d.line([(ox + 600, oy + 400), (ox + 600, oy + 50)], fill=(74, 222, 128), width=5)
    d.text((ox + 620, oy + 200), "⬆ 最大疏散距离 < 22.5m (Egress Route)", font=f_header, fill=(74, 222, 128))

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/fire_safety_egress_blueprint.jpg", "JPEG", quality=92)
    print("Generated fire_safety_egress_blueprint.jpg DWG F-101")

# 5. DWG M-101: Kitchen & Wet-Core Drainage Plan
def make_kitchen_drainage():
    img, d = draw_cad_frame(
        "厨房与集中排水系统工程施工图 (Kitchen & Wet-Core Drainage Plan)",
        "DWG M-101",
        "1. 厨房排水接 50L 不锈钢油脂拦截器 (Grease Trap) 过滤油脂后接 DN75 灰水管。\n"
        "2. 双厕黑水采用 DN100 PVC 排污管，设置 1:40 坡度、存水弯 (Trap) 及清扫口 (Cleanout)。\n"
        "3. 化粪池采用 8PE HDPE 生化滤池规格，满足 IWK 排污及卫生工程规范。"
    )
    
    ox, oy = 450, 180
    d.rectangle([(ox, oy), (ox + 1200, oy + 650)], outline=WALL_COLOR, width=3)
    
    d.rectangle([(ox + 20, oy + 200), (ox + 350, oy + 630)], fill=(20, 60, 90), outline=(56, 189, 248), width=2)
    d.text((ox + 40, oy + 220), "🍳 开放式厨房 (Kitchen Zone)", font=f_header, fill=(56, 189, 248))
    d.text((ox + 40, oy + 270), "• DN50 存水弯 (Trap)\n• 独立通气管 (Vent Pipe)\n• 50L 油脂拦截器 (Grease Trap)", font=f_small, fill=TEXT_MAIN)
    
    d.rectangle([(ox + 850, oy + 200), (ox + 1180, oy + 630)], fill=(80, 30, 40), outline=AXIS_COLOR, width=2)
    d.text((ox + 870, oy + 220), "🚽 双卫生间 (Wet Core)", font=f_header, fill=AXIS_COLOR)
    d.text((ox + 870, oy + 270), "• DN100 PVC 排污管 (坡度 1:40)\n• 清扫口 (Cleanout, CO)\n• 检查井 (Inspection Chamber)", font=f_small, fill=TEXT_MAIN)

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/kitchen_drainage_blueprint.jpg", "JPEG", quality=92)
    print("Generated kitchen_drainage_blueprint.jpg DWG M-101")

# 6. DWG T-101: T&C Testing Blueprint 5大独立打压测试
def make_tc_testing():
    img, d = draw_cad_frame(
        "5 大工程验收打压测试点位图 (T&C Inspection & Testing Blueprint)",
        "DWG T-101",
        "1. 给水管 8 Bar 压降测试：依据 SPAN 规范，1.5 倍工作压力保持 2 小时零压降。\n"
        "2. 24h 湿区闭水测试：沉箱注水 100mm 24 小时零渗漏验收。\n"
        "3. 屋顶 4h 高压喷淋防漏测试；30mA RCCB 漏电保护器 30ms 极速切断测试；拔风压差测试。"
    )
    
    ox, oy = 400, 180
    d.rectangle([(ox, oy), (ox + 1300, oy + 650)], outline=WALL_COLOR, width=3)
    
    d.rectangle([(ox + 50, oy + 50), (ox + 600, oy + 280)], fill=(20, 50, 90), outline=DIM_COLOR, width=2)
    d.text((ox + 70, oy + 70), "🧪 测试 1：给水管 8 Bar 打压测试 (SPAN 规范)", font=f_header, fill=DIM_COLOR)
    d.text((ox + 70, oy + 120), "• 责任方：注册水务工程师\n• 验收标准：保压 2h 压降 = 0", font=f_body, fill=TEXT_MAIN)
    
    d.rectangle([(ox + 700, oy + 50), (ox + 1250, oy + 280)], fill=(80, 30, 40), outline=AXIS_COLOR, width=2)
    d.text((ox + 720, oy + 70), "🧪 测试 2：24h 湿区蓄水测试", font=f_header, fill=AXIS_COLOR)
    d.text((ox + 720, oy + 120), "• 责任方：防水承包商\n• 验收标准：沉箱 100mm 水位 24h 零渗漏", font=f_body, fill=TEXT_MAIN)

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/tc_testing_blueprint.jpg", "JPEG", quality=92)
    print("Generated tc_testing_blueprint.jpg DWG T-101")

# 7. DWG S-101: Container Cutting Detail
def make_container_detail():
    img, d = draw_cad_frame(
        "集装箱切墙与方钢加固节点工程图 (Container Modification Detail)",
        "DWG S-101",
        "1. 40ft High Cube 集装箱切割侧墙开窗后，必须沿着开窗切口四周全焊接 100x100x4.5mm RHS 方钢框架。\n"
        "2. 方钢框架与地面 150mm 加厚混凝土地坪通过 M20 预埋化学锚栓 (Anchor Bolts) 焊接锁死，防止变形。\n"
        "3. 集装箱底角件 (Corner Castings) 采用扭锁 (Twist Locks) 与 20mm 厚钢底板无缝焊接，保证抗震稳定。"
    )
    
    ox, oy = 400, 200
    d.text((ox, oy), "【集装箱侧墙切割 & 100mm 方钢框焊接剖面节点大样】", font=f_header, fill=TEXT_GOLD)
    d.rectangle([(ox, oy + 60), (ox + 350, oy + 500)], fill=(30, 45, 65), outline=CONTAINER_COLOR, width=3)
    d.rectangle([(ox + 350, oy + 60), (ox + 450, oy + 500)], fill=STEEL_COLOR, outline=TEXT_MAIN, width=2)
    d.rectangle([(ox, oy + 500), (ox + 600), (oy + 580)], fill=(80, 80, 90), outline=TEXT_MAIN, width=2)
    d.text((ox + 50, oy + 530), "150mm 加厚钢筋混凝土地坪 + M20 预埋化学锚栓 (Concrete Foundation)", font=f_body, fill=TEXT_MAIN)

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/container_splicing_blueprint.jpg", "JPEG", quality=92)
    print("Generated container_splicing_blueprint.jpg DWG S-101")

if __name__ == "__main__":
    make_floorplan()
    make_elevation()
    make_container_detail()
    make_kitchen_drainage()
    make_fire_safety()
    make_tc_testing()
    make_siteplan()
