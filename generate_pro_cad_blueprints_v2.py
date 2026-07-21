import os
from PIL import Image, ImageDraw, ImageFont

W, H = 2560, 1440

# CAD Professional Palette
BG_COLOR = (11, 22, 34)           # Deep Slate Navy CAD Background
GRID_COLOR = (24, 42, 62)         # Fine CAD Grid Lines
BORDER_COLOR = (70, 130, 180)     # Drawing Outer Border
BORDER_INNER = (35, 75, 115)     # Drawing Inner Border
AXIS_COLOR = (239, 68, 68)        # Red Axis Lines
DIM_COLOR = (56, 189, 248)        # Cyan Dimension Lines & Text
WALL_COLOR = (255, 255, 255)      # Pure White Wall Structure
CONTAINER_COLOR = (250, 204, 21)  # Yellow Container Profile
STEEL_COLOR = (249, 115, 22)      # Orange RHS Steel Frame
TEXT_MAIN = (241, 245, 249)       # Pure White Text
TEXT_GOLD = (234, 179, 8)         # Gold Highlight Text
NOTE_BG = (18, 35, 58)            # Note Box Background

font_path = "/System/Library/Fonts/STHeiti Light.ttc"
try:
    f_title = ImageFont.truetype(font_path, 34)
    f_header = ImageFont.truetype(font_path, 24)
    f_body = ImageFont.truetype(font_path, 18)
    f_small = ImageFont.truetype(font_path, 15)
    f_dim = ImageFont.truetype(font_path, 13)
except Exception as e:
    f_title = f_header = f_body = f_small = f_dim = ImageFont.load_default()

def draw_cad_base(title_zh, dwg_no, desc_zh, category_code):
    img = Image.new("RGB", (W, H), BG_COLOR)
    d = ImageDraw.Draw(img)
    
    # 1. Fine CAD Grid (50px step)
    for x in range(0, W, 50):
        d.line([(x, 0), (x, H)], fill=GRID_COLOR, width=1)
    for y in range(0, H, 50):
        d.line([(0, y), (W, y)], fill=GRID_COLOR, width=1)
        
    # 2. Double Drawing Frames
    d.rectangle([(40, 40), (W - 40, H - 40)], outline=BORDER_COLOR, width=3)
    d.rectangle([(46, 46), (W - 46, H - 46)], outline=BORDER_INNER, width=1)
    
    # 3. Standard Title Block (Bottom Right)
    tb_left, tb_top = W - 820, H - 220
    d.rectangle([(tb_left, tb_top), (W - 50, H - 50)], fill=(15, 32, 52), outline=DIM_COLOR, width=2)
    d.line([(tb_left, tb_top + 50), (W - 50, tb_top + 50)], fill=DIM_COLOR, width=1)
    d.line([(tb_left, tb_top + 105), (W - 50, tb_top + 105)], fill=DIM_COLOR, width=1)
    d.line([(tb_left + 520, tb_top), (tb_left + 520, H - 50)], fill=DIM_COLOR, width=1)
    
    d.text((tb_left + 15, tb_top + 12), "PROJECT: LOT 7836 KLUANG DEVELOPMENT", font=f_small, fill=TEXT_MAIN)
    d.text((tb_left + 535, tb_top + 12), f"DWG NO: {dwg_no}", font=f_small, fill=TEXT_GOLD)
    
    d.text((tb_left + 15, tb_top + 65), f"TITLE: {title_zh}", font=f_body, fill=DIM_COLOR)
    d.text((tb_left + 535, tb_top + 65), "SCALE: 1:100 NTS", font=f_small, fill=TEXT_MAIN)
    
    d.text((tb_left + 15, tb_top + 120), "STAGE: CONCEPTUAL DIAGRAM (PRE-SUBMISSION)", font=f_small, fill=TEXT_MAIN)
    d.text((tb_left + 535, tb_top + 120), "REV: C04", font=f_small, fill=(74, 222, 128))

    # 4. Top Title Banner
    d.rectangle([(50, 50), (W - 850, 125)], fill=(18, 40, 68), outline=DIM_COLOR, width=1)
    d.text((70, 62), f"2D 概念工程规图 | {title_zh}", font=f_title, fill=TEXT_MAIN)
    d.text((70, 98), f"类别代号: {category_code} | 控制参数: 50'x75' 地块 | 双 40' HC 箱体 | 24' 挑高大厅 (40' 建筑面宽，预留 5' 侧退缩)", font=f_dim, fill=DIM_COLOR)
    
    # 5. Layman Engineering Callout Box (Bottom Left)
    d.rectangle([(50, H - 260), (W - 850, H - 50)], fill=NOTE_BG, outline=DIM_COLOR, width=2)
    d.text((70, H - 245), "💡 施工方 & 合作伙伴读图指引 (Layman & Engineering Guide):", font=f_body, fill=TEXT_GOLD)
    d.text((70, H - 222), "⚠️ 免责声明: 本图为概念工程示意图。所有结构、排水、消防及退缩最终须由注册建筑师(Ar.)、P.Eng及主管机构(MPK/BOMBA/IWK)签核。", font=f_dim, fill=(248, 113, 113))
    
    lines = desc_zh.split("\n")
    y_off = H - 192
    for line in lines:
        d.text((70, y_off), line, font=f_small, fill=TEXT_MAIN)
        y_off += 23
        
    return img, d

def draw_axis_bubble(d, cx, cy, label, radius=18):
    d.ellipse([(cx - radius, cy - radius), (cx + radius, cy + radius)], fill=(20, 35, 55), outline=AXIS_COLOR, width=2)
    d.text((cx - 7, cy - 10), label, font=f_small, fill=TEXT_MAIN)

# 1. DWG A-101: Floor Plan (包含轴网与完整尺寸链)
def make_floorplan():
    img, d = draw_cad_base(
        "2D 建筑平面控制示意图 (Architectural Floor Plan)",
        "DWG A-101",
        "1. 地块总尺寸 50ft W x 75ft D。左右侧配置 2 个 40ft HC 集装箱 (各 8ft W)，中央打通 24ft 挑高大厅 (40ft 建筑总面宽)。\n"
        "2. 退缩与轴网：两侧预留 5ft 侧退缩线，轴 1-3 纵向进深，轴 A-D 横向面宽。集装箱切口焊 100x100x4.5mm RHS 方钢圈。\n"
        "3. 水电分区：左箱后段设开放式厨房与油脂拦截器，右箱设双卫生间集中排污，后区二层设立 750sqft Mezzanine Loft。",
        "ARCHITECTURAL / A"
    )
    
    ox, oy = 580, 170
    sw_px, sd_px = 1000, 750
    bx1, by1 = ox, oy
    bx2, by2 = ox + sw_px, oy + sd_px
    
    # Building Boundary
    d.rectangle([(bx1, by1), (bx2, by2)], outline=WALL_COLOR, width=4)
    
    # Dimension lines & text
    d.line([(bx1 - 40, by1), (bx1 - 40, by2)], fill=DIM_COLOR, width=2)
    d.line([(bx1 - 50, by1), (bx1 - 30, by1)], fill=DIM_COLOR, width=2)
    d.line([(bx1 - 50, by2), (bx1 - 30, by2)], fill=DIM_COLOR, width=2)
    d.text((bx1 - 170, oy + sd_px//2 - 10), "50' 0\" (15.24m) 进深", font=f_body, fill=DIM_COLOR)
    
    d.line([(bx1, by1 - 40), (bx2, by1 - 40)], fill=DIM_COLOR, width=2)
    d.line([(bx1, by1 - 50), (bx1, by1 - 30)], fill=DIM_COLOR, width=2)
    d.line([(bx2, by1 - 50), (bx2, by1 - 30)], fill=DIM_COLOR, width=2)
    d.text((ox + sw_px//2 - 140, by1 - 70), "40' 0\" (12.19m) 建筑面宽 (预留两侧 5' 退缩)", font=f_body, fill=DIM_COLOR)
    
    # Axis lines
    d.line([(bx1 - 60, by1), (bx2 + 60, by1)], fill=AXIS_COLOR, width=1)
    d.line([(bx1 - 60, by2), (bx2 + 60, by2)], fill=AXIS_COLOR, width=1)
    d.line([(bx1, by1 - 60), (bx1, by2 + 60)], fill=AXIS_COLOR, width=1)
    d.line([(bx2, by1 - 60), (bx2, by2 + 60)], fill=AXIS_COLOR, width=1)
    
    draw_axis_bubble(d, bx1 - 80, by1, "①")
    draw_axis_bubble(d, bx1 - 80, by2, "②")
    draw_axis_bubble(d, bx1, by1 - 80, "Ⓐ")
    draw_axis_bubble(d, bx2, by1 - 80, "Ⓓ")
    
    # Left & Right Containers
    c1 = (bx1, by1, bx1 + 180, by1 + 600)
    d.rectangle(c1, fill=(35, 50, 35), outline=CONTAINER_COLOR, width=3)
    d.text((bx1 + 15, by1 + 140), "左箱 40ft HC\n(8' x 40')", font=f_small, fill=CONTAINER_COLOR)
    
    c2 = (bx2 - 180, by1, bx2, by1 + 600)
    d.rectangle(c2, fill=(35, 50, 35), outline=CONTAINER_COLOR, width=3)
    d.text((bx2 - 165, by1 + 140), "右箱 40ft HC\n(8' x 40')", font=f_small, fill=CONTAINER_COLOR)
    
    # Central Hall
    d.text((ox + sw_px//2 - 180, by1 + 180), "24ft 挑高中央大厅 (High Ceiling Hall)\n净宽 7.32m / 净高 7.30m", font=f_header, fill=TEXT_MAIN)
    
    # RHS Frames
    d.rectangle([(bx1 + 175, by1 + 40), (bx1 + 185, by1 + 560)], fill=STEEL_COLOR)
    d.text((bx1 + 195, by1 + 280), "← 100x100mm RHS 方钢加固框", font=f_dim, fill=STEEL_COLOR)
    
    # Kitchen & Restrooms
    d.rectangle([(bx1, by1 + 600), (bx1 + 320, by2)], fill=(20, 60, 85), outline=(56, 189, 248), width=2)
    d.text((bx1 + 20, by1 + 635), "🍳 开放式厨房 (Kitchen)\n配 DN75 灰水管 & 油脂拦截器", font=f_small, fill=TEXT_MAIN)
    
    d.rectangle([(bx2 - 320, by1 + 600), (bx2, by2)], fill=(75, 35, 40), outline=AXIS_COLOR, width=2)
    d.text((bx2 - 300, by1 + 635), "🚽 双卫生间 (Wet Core)\n配 DN100 黑水管直连化粪池", font=f_small, fill=TEXT_MAIN)

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/floorplan-bp.jpg", "JPEG", quality=93)
    print("Generated floorplan-bp.jpg DWG A-101")

# 2. DWG A-102: Elevation (包含绝对标高控制)
def make_elevation():
    img, d = draw_cad_base(
        "建筑正立面与控制标高示意图 (Front Elevation & Height Controls)",
        "DWG A-102",
        "1. 严格统一控制标高：FL ±0.00m 地坪, +9'6\" 集装箱顶, +24'0\" 主屋檐, +38'5\" 主屋脊, +47'0\" Raised Jack Roof 拔风塔顶！\n"
        "2. 30° 坡屋顶与中央 Raised Monitor 拔风天窗，依靠自然热浮力向上快速排出室内积热。\n"
        "3. 正面设置 Batu Angin 通风花砖屏风墙，隔绝 85% 太阳辐射热，打造高质感度假别墅气场。",
        "ARCHITECTURAL / A"
    )
    
    ox, oy = 450, 170
    w_px = 1100
    
    # Ground Line
    d.line([(ox - 100, oy + 540), (ox + w_px + 100, oy + 540)], fill=TEXT_MAIN, width=4)
    d.text((ox - 240, oy + 530), "▼ FL ±0.00m (地坪标高)", font=f_body, fill=TEXT_MAIN)
    
    # Height Level Lines
    d.line([(ox - 100, oy + 430), (ox + w_px + 100, oy + 430)], fill=DIM_COLOR, width=1)
    d.text((ox - 260, oy + 420), "▼ +9' 6\" (2.90m 集装箱顶)", font=f_body, fill=DIM_COLOR)
    
    d.line([(ox - 100, oy + 250), (ox + w_px + 100, oy + 250)], fill=DIM_COLOR, width=1)
    d.text((ox - 260, oy + 240), "▼ +24' 0\" (7.31m 主屋檐)", font=f_body, fill=DIM_COLOR)
    
    d.line([(ox - 100, oy + 120), (ox + w_px + 100, oy + 120)], fill=(250, 204, 21), width=1)
    d.text((ox - 270, oy + 110), "▲ +38' 5\" (11.71m 主屋脊)", font=f_body, fill=(250, 204, 21))

    d.line([(ox - 100, oy + 40), (ox + w_px + 100, oy + 40)], fill=AXIS_COLOR, width=2)
    d.text((ox - 290, oy + 30), "▲ +47' 0\" (14.33m 拔风塔顶)", font=f_body, fill=AXIS_COLOR)
    
    # Containers left & right
    d.rectangle([(ox, oy + 430), (ox + 180, oy + 540)], outline=CONTAINER_COLOR, width=3)
    d.text((ox + 15, oy + 475), "左集装箱 8ft", font=f_small, fill=CONTAINER_COLOR)
    
    d.rectangle([(ox + w_px - 180, oy + 430), (ox + w_px, oy + 540)], outline=CONTAINER_COLOR, width=3)
    d.text((ox + w_px - 165, oy + 475), "右集装箱 8ft", font=f_small, fill=CONTAINER_COLOR)
    
    # Breeze Block Wall
    d.rectangle([(ox + 180, oy + 340), (ox + w_px - 180, oy + 540)], fill=(25, 45, 35), outline=(74, 222, 128), width=3)
    d.text((ox + w_px//2 - 160, oy + 430), "🧱 Batu Angin 通风花砖屏风墙 (24ft)", font=f_header, fill=(74, 222, 128))
    
    # 30 Roof & Jack Roof
    d.polygon([(ox, oy + 250), (ox + w_px//2, oy + 120), (ox + w_px, oy + 250)], outline=WALL_COLOR, width=3)
    d.rectangle([(ox + w_px//2 - 180, oy + 40), (ox + w_px//2 + 180, oy + 120)], fill=(35, 65, 95), outline=AXIS_COLOR, width=2)
    d.text((ox + w_px//2 - 140, oy + 70), "🪟 Raised Jack Roof (+47' 拔风塔)", font=f_small, fill=TEXT_MAIN)

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/elevation-bp.jpg", "JPEG", quality=93)
    print("Generated elevation-bp.jpg DWG A-102")

# 3. DWG G-101: Site Plan (包含 Jalan Pakis 及退缩线)
def make_siteplan():
    img, d = draw_cad_base(
        "总平面规划与退缩示意图 (Site Plan & Setback Layout)",
        "DWG G-101",
        "1. 50ft 面宽 x 75ft 进深地块 (3,750 sqft)，正面沿 Jalan Pakis 市政道路。建筑真实占地 40ft W x 50ft D。\n"
        "2. 物理退缩：前退缩 15ft (停车/绿化缓冲区)、后退缩 10ft (8PE 生化化粪池与排水沟)、两侧退缩各 5ft。\n"
        "3. 消防接近方案：采用消防人员步行接近通道 (Foot Access Path)，BOMBA 消防车停靠在 Jalan Pakis 沿街道路。",
        "CIVIL & SITE / G"
    )
    
    ox, oy = 550, 170
    d.rectangle([(ox, oy), (ox + 1050, oy + 650)], fill=(12, 28, 48), outline=TEXT_MAIN, width=3)
    
    # North Arrow
    d.line([(ox + 980, oy + 80), (ox + 980, oy + 20)], fill=AXIS_COLOR, width=4)
    d.polygon([(ox + 980, oy + 10), (ox + 970, oy + 35), (ox + 990, oy + 35)], fill=AXIS_COLOR)
    d.text((ox + 970, oy + 90), "NORTH (北)", font=f_body, fill=AXIS_COLOR)
    
    # Jalan Pakis Road
    d.rectangle([(ox, oy - 60), (ox + 1050, oy)], fill=(35, 35, 45), outline=DIM_COLOR, width=2)
    d.text((ox + 300, oy - 45), "🛣️ JALAN PAKIS 沿街市政道路 (BOMBA 消防车停靠区)", font=f_header, fill=TEXT_MAIN)
    
    # Building Footprint (40ft x 50ft)
    d.rectangle([(ox + 100, oy + 130), (ox + 940, oy + 560)], fill=(25, 45, 70), outline=TEXT_GOLD, width=2)
    d.text((ox + 300, oy + 300), "集装箱 Bungalow 建筑占地 (40ft W x 50ft D)\n前退缩 15ft | 后退缩 10ft | 侧退缩 5ft", font=f_header, fill=TEXT_MAIN)
    
    # Foot Access Path
    d.line([(ox + 40, oy), (ox + 40, oy + 650)], fill=(74, 222, 128), width=3)
    d.text((ox + 50, oy + 240), "🚶 消防员步行接近通道 (Foot Access)", font=f_small, fill=(74, 222, 128))
    
    # Septic Tank
    d.rectangle([(ox + 800, oy + 570), (ox + 1000, oy + 630)], fill=(75, 55, 15), outline=TEXT_GOLD, width=2)
    d.text((ox + 810, oy + 590), "8PE 化粪池与维护通道", font=f_small, fill=TEXT_GOLD)

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/siteplan-bp.jpg", "JPEG", quality=93)
    print("Generated siteplan-bp.jpg DWG G-101")

# 4. DWG F-101: Fire Safety Plan
def make_fire_safety():
    img, d = draw_cad_base(
        "BOMBA 消防安全与疏散逃生路线图 (Fire Safety & Egress Plan)",
        "DWG F-101",
        "1. 正面设 1.5m 净宽双开主逃生门 (Exit 1)，后区 Loft 预留第二逃生钢梯 (Exit 2)。\n"
        "2. 图中精准标注 6 处光感烟雾报警器 (SD1-SD6) 与 4 处 6kg ABC 干粉灭火器 (FE1-FE4) 点位。\n"
        "3. 主大厅与 Loft 疏散行走距离限制在 18.5m 内 (小于 UBBL 22.5m 规范上限)。",
        "FIRE SAFETY / F"
    )
    
    ox, oy = 450, 170
    d.rectangle([(ox, oy), (ox + 1150, oy + 650)], outline=WALL_COLOR, width=3)
    
    d.rectangle([(ox + 420, oy - 20), (ox + 720, oy + 20)], fill=(0, 180, 90), outline=TEXT_MAIN, width=2)
    d.text((ox + 440, oy - 15), "🟢 主逃生门 (1.5m 净宽 Exit 1)", font=f_body, fill=TEXT_MAIN)
    
    d.rectangle([(ox + 480, oy + 640), (ox + 680, oy + 670)], fill=(0, 180, 90), outline=TEXT_MAIN, width=2)
    d.text((ox + 490, oy + 645), "🟢 Loft 第二逃生梯 Exit 2", font=f_body, fill=TEXT_MAIN)
    
    # SD1-SD6
    sd_pts = [(ox + 180, oy + 150, "SD1"), (ox + 180, oy + 450, "SD2"), (ox + 580, oy + 200, "SD3"), (ox + 580, oy + 500, "SD4"), (ox + 980, oy + 150, "SD5"), (ox + 980, oy + 450, "SD6")]
    for pt in sd_pts:
        d.ellipse([(pt[0]-15, pt[1]-15), (pt[0]+15, pt[1]+15)], fill=(200, 50, 50), outline=TEXT_MAIN, width=2)
        d.text((pt[0]-12, pt[1]-8), pt[2], font=f_small, fill=TEXT_MAIN)
        
    # FE1-FE4
    fe_pts = [(ox + 70, oy + 50, "FE1"), (ox + 1070, oy + 50, "FE2"), (ox + 70, oy + 600, "FE3"), (ox + 1070, oy + 600, "FE4")]
    for pt in fe_pts:
        d.rectangle([(pt[0]-15, pt[1]-15), (pt[0]+15, pt[1]+15)], fill=(220, 180, 20), outline=AXIS_COLOR, width=2)
        d.text((pt[0]-12, pt[1]-8), pt[2], font=f_small, fill=BG_COLOR)
        
    d.line([(ox + 580, oy + 400), (ox + 580, oy + 50)], fill=(74, 222, 128), width=4)
    d.text((ox + 600, oy + 200), "⬆ 最大疏散行走距离 18.5m (< 22.5m 规范上限)", font=f_header, fill=(74, 222, 128))

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/fire_safety_egress_blueprint.jpg", "JPEG", quality=93)
    print("Generated fire_safety_egress_blueprint.jpg DWG F-101")

# 5. DWG M-101: Drainage Plan
def make_kitchen_drainage():
    img, d = draw_cad_base(
        "厨房与集中排水系统工程图 (Kitchen & Wet-Core Drainage Plan)",
        "DWG M-101",
        "1. 厨房排水：DN75 灰水管 + 50L 不锈钢油脂拦截器 (Grease Trap)，设 DN50 存水弯 (Trap) 与通气管 (Vent)。\n"
        "2. 卫生间黑水：DN100 PVC 管 (坡度 1:40) 设清扫口 (Cleanout CO) 与 检查井 (IC1, IC2)，连接 8PE 化粪池。\n"
        "3. 排水管底标高 (Invert Level IL) 控制：进水 IL -0.45m，出水 IL -0.60m，符合 IWK 卫生工程要求。",
        "MECHANICAL & PLUMBING / M"
    )
    
    ox, oy = 450, 170
    d.rectangle([(ox, oy), (ox + 1150, oy + 650)], outline=WALL_COLOR, width=3)
    
    d.rectangle([(ox + 20, oy + 200), (ox + 340, oy + 630)], fill=(18, 55, 85), outline=(56, 189, 248), width=2)
    d.text((ox + 40, oy + 220), "🍳 开放式厨房 (Kitchen)", font=f_header, fill=(56, 189, 248))
    d.text((ox + 40, oy + 270), "• DN50 存水弯 (P-Trap)\n• 独立通气管 (Vent Pipe VP)\n• 50L 油脂拦截器 (Grease Trap GT)", font=f_small, fill=TEXT_MAIN)
    
    d.rectangle([(ox + 810, oy + 200), (ox + 1130, oy + 630)], fill=(75, 30, 40), outline=AXIS_COLOR, width=2)
    d.text((ox + 830, oy + 220), "🚽 双卫生间 (Wet Core)", font=f_header, fill=AXIS_COLOR)
    d.text((ox + 830, oy + 270), "• DN100 PVC 排污管 (坡度 1:40)\n• 清扫口 (Cleanout CO)\n• 检查井 (Inspection Chamber IC1)", font=f_small, fill=TEXT_MAIN)

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/kitchen_drainage_blueprint.jpg", "JPEG", quality=93)
    print("Generated kitchen_drainage_blueprint.jpg DWG M-101")

# 6. DWG T-101: T&C Testing Plan
def make_tc_testing():
    img, d = draw_cad_base(
        "5 大工程验收打压测试点位图 (T&C Inspection & Testing Blueprint)",
        "DWG T-101",
        "1. 测1: PPR 8 Bar 给水保压 (SPAN 规范) | 测2: 24h 湿区沉箱蓄水零渗漏 | 测3: 4h 屋顶高压喷淋。\n"
        "2. 测4: 30mA RCCB 漏电 30ms 断路及 <10Ω 接地 | 测5: Raised Monitor 拔风塔风速与热负压排热测试。\n"
        "3. 每项测试均标明测试方法、验收标准、责任方与复测条件。",
        "TESTING & COMMISSIONING / T"
    )
    
    ox, oy = 400, 160
    d.rectangle([(ox, oy), (ox + 1250, oy + 680)], outline=WALL_COLOR, width=3)
    
    # 5 Test Boxes
    d.rectangle([(ox + 30, oy + 30), (ox + 390, oy + 310)], fill=(18, 48, 85), outline=DIM_COLOR, width=2)
    d.text((ox + 45, oy + 45), "🧪 测1：PPR 8 Bar 打压", font=f_body, fill=DIM_COLOR)
    d.text((ox + 45, oy + 85), "• 依据 SPAN 规范\n• 1.5倍压力保压 2h\n• 责任: 水务承包商\n• 验收: 压降 = 0", font=f_small, fill=TEXT_MAIN)
    
    d.rectangle([(ox + 430, oy + 30), (ox + 790, oy + 310)], fill=(75, 30, 40), outline=AXIS_COLOR, width=2)
    d.text((ox + 445, oy + 45), "🧪 测2：24h 湿区蓄水", font=f_body, fill=AXIS_COLOR)
    d.text((ox + 445, oy + 85), "• 注入 100mm 水 24h\n• 检验沉箱防水层\n• 责任: 防水承包商\n• 验收: 底部零渗漏", font=f_small, fill=TEXT_MAIN)

    d.rectangle([(ox + 830, oy + 30), (ox + 1210, oy + 310)], fill=(25, 65, 45), outline=(74, 222, 128), width=2)
    d.text((ox + 845, oy + 45), "🧪 测3：4h 高压喷淋", font=f_body, fill=(74, 222, 128))
    d.text((ox + 845, oy + 85), "• 对屋顶与接缝高压喷淋\n• 责任: 屋面承包商\n• 验收: 天花板零水渍", font=f_small, fill=TEXT_MAIN)

    d.rectangle([(ox + 180, oy + 350), (ox + 580, oy + 630)], fill=(75, 65, 18), outline=TEXT_GOLD, width=2)
    d.text((ox + 195, oy + 365), "🧪 测4：30mA RCCB 漏电测试", font=f_body, fill=TEXT_GOLD)
    d.text((ox + 195, oy + 405), "• 30ms 极速切断保护\n• 测量接地电阻低于 10 欧姆\n• 责任: 电气工程师", font=f_small, fill=TEXT_MAIN)

    d.rectangle([(ox + 660, oy + 350), (ox + 1060, oy + 630)], fill=(45, 35, 75), outline=TEXT_MAIN, width=2)
    d.text((ox + 675, oy + 365), "🧪 测5：拔风塔热对流测试", font=f_body, fill=TEXT_MAIN)
    d.text((ox + 675, oy + 405), "• 测量室内外热负压压差\n• 检验自然拔风降温效率\n• 责任: 通风顾问", font=f_small, fill=TEXT_MAIN)

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/tc_testing_blueprint.jpg", "JPEG", quality=93)
    print("Generated tc_testing_blueprint.jpg DWG T-101")

# 7. DWG S-101: Container Detail
def make_container_detail():
    img, d = draw_cad_base(
        "集装箱切割与 100mm 方钢加固 Detail (Container Splicing Detail)",
        "DWG S-101",
        "1. 40ft High Cube 集装箱切割侧墙开窗后，必须沿着开窗切口四周全焊接 100x100x4.5mm RHS 方钢框架。\n"
        "2. 方钢框架与地面 150mm 加厚混凝土地坪通过 M20 预埋化学锚栓 (Anchor Bolts) 焊接锁死，防止变形。\n"
        "3. 集装箱底角件 (Corner Castings) 采用扭锁 (Twist Locks) 与 20mm 厚钢底板无缝焊接，保证抗震稳定。",
        "STRUCTURAL / S"
    )
    
    ox, oy = 400, 200
    d.text((ox, oy), "【集装箱侧墙切割 & 100mm 方钢框焊接剖面节点大样】", font=f_header, fill=TEXT_GOLD)
    d.rectangle([(ox, oy + 60), (ox + 350, oy + 500)], fill=(28, 42, 60), outline=CONTAINER_COLOR, width=3)
    d.rectangle([(ox + 350, oy + 60), (ox + 450, oy + 500)], fill=STEEL_COLOR, outline=TEXT_MAIN, width=2)
    d.rectangle([(ox, oy + 500), (ox + 600, oy + 580)], fill=(75, 75, 85), outline=TEXT_MAIN, width=2)
    d.text((ox + 50, oy + 530), "150mm 加厚钢筋混凝土地坪 + M20 预埋化学锚栓 (Concrete Foundation)", font=f_body, fill=TEXT_MAIN)

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/container_splicing_blueprint.jpg", "JPEG", quality=93)
    print("Generated container_splicing_blueprint.jpg DWG S-101")

if __name__ == "__main__":
    make_floorplan()
    make_elevation()
    make_container_detail()
    make_kitchen_drainage()
    make_fire_safety()
    make_tc_testing()
    make_siteplan()
