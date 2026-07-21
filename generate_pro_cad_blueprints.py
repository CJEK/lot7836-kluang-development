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
    f_title = ImageFont.truetype(font_path, 36)
    f_header = ImageFont.truetype(font_path, 26)
    f_body = ImageFont.truetype(font_path, 19)
    f_small = ImageFont.truetype(font_path, 15)
    f_dim = ImageFont.truetype(font_path, 14)
except Exception as e:
    print(f"Font error: {e}")
    f_title = f_header = f_body = f_small = f_dim = ImageFont.load_default()

def draw_cad_frame(title_zh, dwg_no, desc_zh):
    img = Image.new("RGB", (W, H), BG_COLOR)
    d = ImageDraw.Draw(img)
    
    # Grid
    for x in range(0, W, 50):
        d.line([(x, 0), (x, H)], fill=GRID_COLOR, width=1)
    for y in range(0, H, 50):
        d.line([(0, y), (W, y)], fill=GRID_COLOR, width=1)
        
    # Borders
    d.rectangle([(40, 40), (W - 40, H - 40)], outline=(100, 150, 200), width=3)
    d.rectangle([(46, 46), (W - 46, H - 46)], outline=(50, 90, 140), width=1)
    
    # Title Block
    tb_left, tb_top = W - 780, H - 210
    d.rectangle([(tb_left, tb_top), (W - 50, H - 50)], fill=(18, 38, 64), outline=DIM_COLOR, width=2)
    d.line([(tb_left, tb_top + 50), (W - 50, tb_top + 50)], fill=DIM_COLOR, width=1)
    d.line([(tb_left, tb_top + 100), (W - 50, tb_top + 100)], fill=DIM_COLOR, width=1)
    d.line([(tb_left + 480, tb_top), (tb_left + 480, H - 50)], fill=DIM_COLOR, width=1)
    
    d.text((tb_left + 15, tb_top + 12), "PROJECT: LOT 7836 KLUANG DEVELOPMENT", font=f_small, fill=TEXT_MAIN)
    d.text((tb_left + 495, tb_top + 12), f"DWG NO: {dwg_no}", font=f_small, fill=TEXT_GOLD)
    
    d.text((tb_left + 15, tb_top + 62), f"TITLE: {title_zh}", font=f_body, fill=DIM_COLOR)
    d.text((tb_left + 495, tb_top + 62), "SCALE: N.T.S CONCEPTUAL", font=f_small, fill=TEXT_MAIN)
    
    d.text((tb_left + 15, tb_top + 112), "STAGE: CONCEPTUAL DIAGRAM (PRE-SUBMISSION)", font=f_small, fill=TEXT_MAIN)
    d.text((tb_left + 495, tb_top + 112), "STATUS: FOR REVIEW", font=f_small, fill=(248, 113, 113))

    # Title Banner
    d.rectangle([(50, 50), (W - 800, 120)], fill=(20, 45, 75), outline=DIM_COLOR, width=1)
    d.text((70, 65), f"2D 概念工程示意图 | {title_zh}", font=f_title, fill=TEXT_MAIN)
    
    # Note Box
    d.rectangle([(50, H - 260), (W - 800, H - 50)], fill=NOTE_BG, outline=DIM_COLOR, width=2)
    d.text((70, H - 245), "⚠️ 概念预留与专业免责声明 (Conceptual & Regulatory Disclaimer):", font=f_body, fill=TEXT_GOLD)
    d.text((70, H - 220), "本图为概念意向示意图。所有结构、消防、排水及土地退缩最终须由注册建筑师(Ar.)、专业工程师(P.Eng)及相关主管机构(MPK/BOMBA/IWK)确认。", font=f_dim, fill=(248, 113, 113))
    
    lines = desc_zh.split("\n")
    y_off = H - 190
    for line in lines:
        d.text((70, y_off), line, font=f_small, fill=TEXT_MAIN)
        y_off += 24
        
    return img, d

# 1. DWG A-101: Floor Plan 2D 平面工程图
def make_floorplan():
    img, d = draw_cad_frame(
        "2D 建筑平面布置示意图 (Architectural Floor Plan)",
        "DWG A-101",
        "1. 建筑占地 40ft W x 50ft D。左右配置 2 个 40ft HC 集装箱 (单箱 8ft W x 40ft L)。\n"
        "2. 切割集装箱内墙后焊接 100x100x4.5mm RHS 方钢框补强，打通中央 34ft 挑高大厅。\n"
        "3. 后区预留 10ft 设立开放式厨房与双卫生间，后方二层为 900sqft Mezzanine Loft 阁楼。"
    )
    
    ox, oy = 550, 180
    sw_px, sd_px = 1100, 825
    bx1, by1 = ox, oy
    bx2, by2 = ox + sw_px, oy + sd_px
    
    d.rectangle([(bx1, by1), (bx2, by2)], outline=WALL_COLOR, width=4)
    d.line([(bx1 - 40, by1), (bx1 - 40, by2)], fill=DIM_COLOR, width=2)
    d.text((bx1 - 160, oy + sd_px//2), "50' 0\" 建筑进深", font=f_body, fill=DIM_COLOR)
    
    d.line([(bx1, by1 - 40), (bx2, by1 - 40)], fill=DIM_COLOR, width=2)
    d.text((ox + sw_px//2 - 140, by1 - 75), "50' 0\" 土地面宽", font=f_body, fill=DIM_COLOR)
    
    c1 = (bx1, by1, bx1 + 176, by1 + 660)
    d.rectangle(c1, fill=(40, 50, 30), outline=CONTAINER_COLOR, width=3)
    d.text((bx1 + 15, by1 + 150), "左集装箱 40ft HC\n(8ft x 40ft)", font=f_small, fill=CONTAINER_COLOR)
    
    c2 = (bx2 - 176, by1, bx2, by1 + 660)
    d.rectangle(c2, fill=(40, 50, 30), outline=CONTAINER_COLOR, width=3)
    d.text((bx2 - 160, by1 + 150), "右集装箱 40ft HC\n(8ft x 40ft)", font=f_small, fill=CONTAINER_COLOR)
    
    d.text((ox + sw_px//2 - 200, by1 + 200), "34ft 挑高大厅 (High Ceiling Hall)\n净宽 10.36m / 净高 7.3m", font=f_header, fill=TEXT_MAIN)
    
    d.rectangle([(bx1 + 170, by1 + 50), (bx1 + 182, by1 + 600)], fill=STEEL_COLOR)
    d.text((bx1 + 190, by1 + 300), "← 100x100x4.5mm 方钢加固框", font=f_dim, fill=STEEL_COLOR)
    
    d.rectangle([(bx1, by1 + 660), (bx1 + 350, by2)], fill=(20, 60, 80), outline=(56, 189, 248), width=2)
    d.text((bx1 + 20, by1 + 700), "🍳 开放式厨房 (Kitchen)", font=f_body, fill=TEXT_MAIN)
    
    d.rectangle([(bx2 - 350, by1 + 660), (bx2, by2)], fill=(80, 40, 40), outline=AXIS_COLOR, width=2)
    d.text((bx2 - 330, by1 + 700), "🚽 独立双卫生间 (Wet Core)", font=f_body, fill=TEXT_MAIN)

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/floorplan-bp.jpg", "JPEG", quality=92)
    print("Generated floorplan-bp.jpg DWG A-101")

# 2. DWG A-102: Elevation 正立面图 (严格执行：+24' 檐高 / +38'-5" 屋脊 / +47' 拔风塔顶)
def make_elevation():
    img, d = draw_cad_frame(
        "建筑正立面结构示意图 (Front Elevation & Height Controls)",
        "DWG A-102",
        "1. 严格控制标高：FL ±0.00m 地坪、+9' 6\" 集装箱顶、+24' 0\" 主屋檐、+38' 5\" 主屋脊、+47' 0\" 拔风塔顶！\n"
        "2. 30° 高坡热带防雨屋顶与中央 Raised Monitor 拔风天窗，利用热浮力排出热气。\n"
        "3. 正面设置马六甲 Batu Angin 避光通风花砖屏风墙，形成双层隔热墙结构。"
    )
    
    ox, oy = 450, 180
    w_px = 1100
    
    d.line([(ox - 100, oy + 550), (ox + w_px + 100, oy + 550)], fill=TEXT_MAIN, width=4)
    d.text((ox - 240, oy + 540), "▼ FL ±0.00m (地坪标高)", font=f_body, fill=TEXT_MAIN)
    
    d.line([(ox - 100, oy + 440), (ox + w_px + 100, oy + 440)], fill=DIM_COLOR, width=1)
    d.text((ox - 260, oy + 430), "▼ +9' 6\" (2.90m 集装箱顶)", font=f_body, fill=DIM_COLOR)
    
    d.line([(ox - 100, oy + 260), (ox + w_px + 100, oy + 260)], fill=DIM_COLOR, width=1)
    d.text((ox - 260, oy + 250), "▼ +24' 0\" (7.31m 主屋檐)", font=f_body, fill=DIM_COLOR)
    
    d.line([(ox - 100, oy + 120), (ox + w_px + 100, oy + 120)], fill=(250, 204, 21), width=1)
    d.text((ox - 270, oy + 110), "▲ +38' 5\" (11.71m 主屋脊)", font=f_body, fill=(250, 204, 21))

    d.line([(ox - 100, oy + 40), (ox + w_px + 100, oy + 40)], fill=AXIS_COLOR, width=2)
    d.text((ox - 290, oy + 30), "▲ +47' 0\" (14.33m 拔风塔顶)", font=f_body, fill=AXIS_COLOR)
    
    d.rectangle([(ox, oy + 440), (ox + 176, oy + 550)], outline=CONTAINER_COLOR, width=3)
    d.text((ox + 20, oy + 480), "左集装箱 8ft", font=f_small, fill=CONTAINER_COLOR)
    
    d.rectangle([(ox + w_px - 176, oy + 440), (ox + w_px, oy + 550)], outline=CONTAINER_COLOR, width=3)
    d.text((ox + w_px - 150, oy + 480), "右集装箱 8ft", font=f_small, fill=CONTAINER_COLOR)
    
    d.rectangle([(ox + 176, oy + 360), (ox + w_px - 176, oy + 550)], fill=(30, 50, 40), outline=(74, 222, 128), width=3)
    d.text((ox + w_px//2 - 160, oy + 450), "🧱 Batu Angin 通风花砖屏风墙 (34ft)", font=f_header, fill=(74, 222, 128))
    
    d.polygon([(ox, oy + 260), (ox + w_px//2, oy + 120), (ox + w_px, oy + 260)], outline=WALL_COLOR, width=3)
    d.rectangle([(ox + w_px//2 - 200, oy + 40), (ox + w_px//2 + 200, oy + 120)], fill=(40, 70, 100), outline=AXIS_COLOR, width=2)
    d.text((ox + w_px//2 - 150, oy + 70), "🪟 Raised Jack Roof (+47' 拔风塔)", font=f_small, fill=TEXT_MAIN)

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/elevation-bp.jpg", "JPEG", quality=92)
    print("Generated elevation-bp.jpg DWG A-102")

# 3. DWG G-101: Corrected Site Plan (修正物理退缩与消防车道逻辑)
def make_siteplan():
    img, d = draw_cad_frame(
        "总平面工程规划示意图 (Site & Infrastructure Plan)",
        "DWG G-101",
        "1. 50ft 面宽 x 75ft 进深地块 (3,750 sqft)，正面沿 Jalan Pakis。建筑占地 40ft W x 50ft D。\n"
        "2. 修正物理退缩：前退缩 15ft (停车/绿化)，后退缩 10ft (8PE 化粪池与雨水沟)，两侧各退 5ft。\n"
        "3. 消防接近方案：采用消防人员步行接近路径 (Foot Access Path)，消防车停靠在 Jalan Pakis 沿街路边。"
    )
    
    ox, oy = 550, 180
    d.rectangle([(ox, oy), (ox + 1100, oy + 650)], fill=(15, 32, 55), outline=TEXT_MAIN, width=3)
    
    # North Arrow
    d.line([(ox + 1020, oy + 80), (ox + 1020, oy + 20)], fill=AXIS_COLOR, width=4)
    d.polygon([(ox + 1020, oy + 10), (ox + 1010, oy + 35), (ox + 1030, oy + 35)], fill=AXIS_COLOR)
    d.text((ox + 1010, oy + 90), "NORTH (北)", font=f_body, fill=AXIS_COLOR)
    
    # Jalan Pakis Road
    d.rectangle([(ox, oy - 60), (ox + 1100, oy)], fill=(40, 40, 50), outline=DIM_COLOR, width=2)
    d.text((ox + 350, oy - 45), "🛣️ JALAN PAKIS 沿街市政道路 (BOMBA 消防车停靠区)", font=f_header, fill=TEXT_MAIN)
    
    # Corrected Building Footprint (40ft W x 50ft D -> 880px x 440px inside 1100px x 650px)
    d.rectangle([(ox + 110, oy + 130), (ox + 990, oy + 570)], fill=(30, 50, 75), outline=TEXT_GOLD, width=2)
    d.text((ox + 320, oy + 300), "集装箱 Bungalow 建筑占地 (40ft W x 50ft D)\n前退缩 15ft | 后退缩 10ft | 侧退缩 5ft", font=f_header, fill=TEXT_MAIN)
    
    # Foot Access Path
    d.line([(ox + 40, oy), (ox + 40, oy + 650)], fill=(74, 222, 128), width=3)
    d.text((ox + 50, oy + 250), "🚶 消防员步行接近通道 (Foot Access)", font=f_small, fill=(74, 222, 128))
    
    # Septic Tank at Rear
    d.rectangle([(ox + 850, oy + 580), (ox + 1050, oy + 640)], fill=(80, 60, 20), outline=TEXT_GOLD, width=2)
    d.text((ox + 860, oy + 600), "8PE 化粪池与维护通道", font=f_small, fill=TEXT_GOLD)

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/siteplan-bp.jpg", "JPEG", quality=92)
    print("Generated siteplan-bp.jpg DWG G-101")

# 4. DWG F-101: Fire Safety & Egress Plan (具体点位与参数图)
def make_fire_safety():
    img, d = draw_cad_frame(
        "BOMBA 消防安全设施与疏散逃生路线示意图 (Fire Safety & Egress Plan)",
        "DWG F-101",
        "1. 正面设 1.5m 净宽双开主逃生门 (Exit 1)，后区 Loft 预留第二逃生钢梯 (Exit 2)。\n"
        "2. 图中精准标注 6 处光感烟雾报警器 (SD1-SD6) 与 4 处 6kg ABC 干粉灭火器 (FE1-FE4) 点位。\n"
        "3. 主大厅与 Loft 疏散行走距离限制在 22.5m 内。注：须经 BOMBA 最终审查签核。"
    )
    
    ox, oy = 450, 180
    d.rectangle([(ox, oy), (ox + 1200, oy + 650)], outline=WALL_COLOR, width=3)
    
    d.rectangle([(ox + 450, oy - 20), (ox + 750, oy + 20)], fill=(0, 180, 90), outline=TEXT_MAIN, width=2)
    d.text((ox + 470, oy - 15), "🟢 主逃生门 (1.5m 净宽 Exit 1)", font=f_body, fill=TEXT_MAIN)
    
    d.rectangle([(ox + 500, oy + 640), (ox + 700, oy + 670)], fill=(0, 180, 90), outline=TEXT_MAIN, width=2)
    d.text((ox + 510, oy + 645), "🟢 Loft 第二逃生梯 Exit 2", font=f_body, fill=TEXT_MAIN)
    
    # Draw Specific Points SD1-SD6 and FE1-FE4
    sd_pts = [(ox + 200, oy + 150, "SD1"), (ox + 200, oy + 450, "SD2"), (ox + 600, oy + 200, "SD3"), (ox + 600, oy + 500, "SD4"), (ox + 1000, oy + 150, "SD5"), (ox + 1000, oy + 450, "SD6")]
    for pt in sd_pts:
        d.ellipse([(pt[0]-15, pt[1]-15), (pt[0]+15, pt[1]+15)], fill=(200, 50, 50), outline=TEXT_MAIN, width=2)
        d.text((pt[0]-12, pt[1]-8), pt[2], font=f_small, fill=TEXT_MAIN)
        
    fe_pts = [(ox + 80, oy + 50, "FE1"), (ox + 1120, oy + 50, "FE2"), (ox + 80, oy + 600, "FE3"), (ox + 1120, oy + 600, "FE4")]
    for pt in fe_pts:
        d.rectangle([(pt[0]-15, pt[1]-15), (pt[0]+15, pt[1]+15)], fill=(220, 180, 20), outline=AXIS_COLOR, width=2)
        d.text((pt[0]-12, pt[1]-8), pt[2], font=f_small, fill=BG_COLOR)
        
    d.line([(ox + 600, oy + 400), (ox + 600, oy + 50)], fill=(74, 222, 128), width=4)
    d.text((ox + 620, oy + 200), "⬆ 最大疏散行走距离 18.5m (< 22.5m 规范上限)", font=f_header, fill=(74, 222, 128))

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/fire_safety_egress_blueprint.jpg", "JPEG", quality=92)
    print("Generated fire_safety_egress_blueprint.jpg DWG F-101")

# 5. DWG M-101: Kitchen & Wet-Core Drainage Plan (完整管线与参数)
def make_kitchen_drainage():
    img, d = draw_cad_frame(
        "厨房与集中排水系统工程施工示意图 (Kitchen & Wet-Core Drainage Plan)",
        "DWG M-101",
        "1. 厨房排水：DN75 灰水管 + 50L 不锈钢油脂拦截器 (Grease Trap)，设 DN50 存水弯 (Trap) 与通气管 (Vent)。\n"
        "2. 卫生间黑水：DN100 PVC 管 (坡度 1:40) 设清扫口 (Cleanout CO) 与 检查井 (IC1, IC2)，连接 8PE 化粪池。\n"
        "3. 排水管底标高 (Invert Level IL) 控制：进水 IL -0.45m，出水 IL -0.60m，符合 IWK 卫生工程要求。"
    )
    
    ox, oy = 450, 180
    d.rectangle([(ox, oy), (ox + 1200, oy + 650)], outline=WALL_COLOR, width=3)
    
    d.rectangle([(ox + 20, oy + 200), (ox + 350, oy + 630)], fill=(20, 60, 90), outline=(56, 189, 248), width=2)
    d.text((ox + 40, oy + 220), "🍳 开放式厨房 (Kitchen)", font=f_header, fill=(56, 189, 248))
    d.text((ox + 40, oy + 270), "• DN50 存水弯 (Trap, P-Trap)\n• 独立通气管 (Vent Pipe VP)\n• 50L 油脂拦截器 (Grease Trap GT)", font=f_small, fill=TEXT_MAIN)
    
    d.rectangle([(ox + 850, oy + 200), (ox + 1180, oy + 630)], fill=(80, 30, 40), outline=AXIS_COLOR, width=2)
    d.text((ox + 870, oy + 220), "🚽 独立双卫生间 (Wet Core)", font=f_header, fill=AXIS_COLOR)
    d.text((ox + 870, oy + 270), "• DN100 PVC 排污管 (坡度 1:40)\n• 清扫口 (Cleanout CO)\n• 检查井 (Inspection Chamber IC1)", font=f_small, fill=TEXT_MAIN)

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/kitchen_drainage_blueprint.jpg", "JPEG", quality=92)
    print("Generated kitchen_drainage_blueprint.jpg DWG M-101")

# 6. DWG T-101: T&C Testing Blueprint 5大独立打压测试 (5框完全对应)
def make_tc_testing():
    img, d = draw_cad_frame(
        "5 大工程验收打压测试点位示意图 (T&C Inspection & Testing Blueprint)",
        "DWG T-101",
        "1. 测1: PPR 8 Bar 给水保压 (SPAN 规范) | 测2: 24h 湿区沉箱蓄水零渗漏 | 测3: 4h 屋顶高压喷淋。\n"
        "2. 测4: 30mA RCCB 漏电 30ms 断路及 <10Ω 接地 | 测5: Raised Monitor 拔风塔风速与热负压排热测试。\n"
        "3. 每项测试均标明测试方法、验收标准、责任方与复测条件。"
    )
    
    ox, oy = 400, 160
    d.rectangle([(ox, oy), (ox + 1300, oy + 680)], outline=WALL_COLOR, width=3)
    
    # 5 Test Boxes (Grid 3 Top, 2 Bottom)
    d.rectangle([(ox + 40, oy + 30), (ox + 410, oy + 310)], fill=(20, 50, 90), outline=DIM_COLOR, width=2)
    d.text((ox + 55, oy + 45), "🧪 测1：PPR 8 Bar 打压", font=f_body, fill=DIM_COLOR)
    d.text((ox + 55, oy + 85), "• 依据 SPAN 规范\n• 1.5倍压力保压 2h\n• 责任: 水务承包商\n• 验收: 压降 = 0", font=f_small, fill=TEXT_MAIN)
    
    d.rectangle([(ox + 450, oy + 30), (ox + 820, oy + 310)], fill=(80, 30, 40), outline=AXIS_COLOR, width=2)
    d.text((ox + 465, oy + 45), "🧪 测2：24h 湿区蓄水", font=f_body, fill=AXIS_COLOR)
    d.text((ox + 465, oy + 85), "• 注入 100mm 水 24h\n• 检验沉箱防水层\n• 责任: 防水承包商\n• 验收: 底部零渗漏", font=f_small, fill=TEXT_MAIN)

    d.rectangle([(ox + 860, oy + 30), (ox + 1250, oy + 310)], fill=(30, 70, 50), outline=(74, 222, 128), width=2)
    d.text((ox + 875, oy + 45), "🧪 测3：4h 高压喷淋", font=f_body, fill=(74, 222, 128))
    d.text((ox + 875, oy + 85), "• 对屋顶与接缝高压喷淋\n• 责任: 屋面承包商\n• 验收: 天花板零水渍", font=f_small, fill=TEXT_MAIN)

    d.rectangle([(ox + 200, oy + 350), (ox + 600, oy + 630)], fill=(80, 70, 20), outline=TEXT_GOLD, width=2)
    d.text((ox + 215, oy + 365), "🧪 测4：30mA RCCB 漏电测试", font=f_body, fill=TEXT_GOLD)
    d.text((ox + 215, oy + 405), "• 30ms 极速切断保护\n• 测量接地电阻低于 10 欧姆\n• 责任: 电气工程师", font=f_small, fill=TEXT_MAIN)

    d.rectangle([(ox + 680, oy + 350), (ox + 1080, oy + 630)], fill=(50, 40, 80), outline=TEXT_MAIN, width=2)
    d.text((ox + 695, oy + 365), "🧪 测5：拔风塔热对流测试", font=f_body, fill=TEXT_MAIN)
    d.text((ox + 695, oy + 405), "• 测量室内外热负压压差\n• 检验自然拔风降温效率\n• 责任: 通风顾问", font=f_small, fill=TEXT_MAIN)

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/tc_testing_blueprint.jpg", "JPEG", quality=92)
    print("Generated tc_testing_blueprint.jpg DWG T-101")

# 7. DWG S-101: Container Cutting Detail
def make_container_detail():
    img, d = draw_cad_frame(
        "集装箱切墙与方钢加固节点示意图 (Container Modification Detail)",
        "DWG S-101",
        "1. 40ft High Cube 集装箱切割侧墙开窗后，必须沿着开窗切口四周全焊接 100x100x4.5mm RHS 方钢框架。\n"
        "2. 方钢框架与地面 150mm 加厚混凝土地坪通过 M20 预埋化学锚栓 (Anchor Bolts) 焊接锁死，防止变形。\n"
        "3. 集装箱底角件 (Corner Castings) 采用扭锁 (Twist Locks) 与 20mm 厚钢底板无缝焊接，保证抗震稳定。"
    )
    
    ox, oy = 400, 200
    d.text((ox, oy), "【集装箱侧墙切割 & 100mm 方钢框焊接剖面节点大样】", font=f_header, fill=TEXT_GOLD)
    d.rectangle([(ox, oy + 60), (ox + 350, oy + 500)], fill=(30, 45, 65), outline=CONTAINER_COLOR, width=3)
    d.rectangle([(ox + 350, oy + 60), (ox + 450, oy + 500)], fill=STEEL_COLOR, outline=TEXT_MAIN, width=2)
    d.rectangle([(ox, oy + 500), (ox + 600, oy + 580)], fill=(80, 80, 90), outline=TEXT_MAIN, width=2)
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
