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
except Exception:
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
    tb_left, tb_top = W - 850, H - 220
    d.rectangle([(tb_left, tb_top), (W - 50, H - 50)], fill=(15, 32, 52), outline=DIM_COLOR, width=2)
    d.line([(tb_left, tb_top + 50), (W - 50, tb_top + 50)], fill=DIM_COLOR, width=1)
    d.line([(tb_left, tb_top + 105), (W - 50, tb_top + 105)], fill=DIM_COLOR, width=1)
    d.line([(tb_left + 540, tb_top), (tb_left + 540, H - 50)], fill=DIM_COLOR, width=1)
    
    d.text((tb_left + 15, tb_top + 12), "PROJECT: LOT 7836 KLUANG SINGLE-STOREY RESIDENTIAL", font=f_small, fill=TEXT_MAIN)
    d.text((tb_left + 555, tb_top + 12), f"DWG NO: {dwg_no}", font=f_small, fill=TEXT_GOLD)
    
    d.text((tb_left + 15, tb_top + 65), f"TITLE: {title_zh}", font=f_body, fill=DIM_COLOR)
    d.text((tb_left + 555, tb_top + 65), "SCALE: 1:100 NTS", font=f_small, fill=TEXT_MAIN)
    
    d.text((tb_left + 15, tb_top + 120), "STAGE: MALAYSIAN SINGLE-STOREY BUNGALOW PRE-SUBMISSION", font=f_small, fill=TEXT_MAIN)
    d.text((tb_left + 555, tb_top + 120), "REV: RES-01", font=f_small, fill=(74, 222, 128))

    # 4. Top Title Banner
    d.rectangle([(50, 50), (W - 880, 125)], fill=(18, 40, 68), outline=DIM_COLOR, width=1)
    d.text((70, 62), f"2D 单层住宅工程规图 | {title_zh}", font=f_title, fill=TEXT_MAIN)
    d.text((70, 98), f"类别代号: {category_code} | 规范: 50'x75' 地块 | 单层独栋 3房2卫+双车位车廊 | 40' 建筑面宽 (预留 5' 侧退缩)", font=f_dim, fill=DIM_COLOR)
    
    # 5. Layman Engineering Callout Box (Bottom Left)
    d.rectangle([(50, H - 260), (W - 880, H - 50)], fill=NOTE_BG, outline=DIM_COLOR, width=2)
    d.text((70, H - 245), "💡 施工方 & 合作伙伴读图指引 (Layman & Engineering Guide):", font=f_body, fill=TEXT_GOLD)
    d.text((70, H - 222), "⚠️ 免责声明: 本图为单层热带住宅概念工程图。所有结构、排水、消防及退缩最终须由注册建筑师(Ar.)、P.Eng及主管机构(MPK/BOMBA/IWK)签核。", font=f_dim, fill=(248, 113, 113))
    
    lines = desc_zh.split("\n")
    y_off = H - 192
    for line in lines:
        d.text((70, y_off), line, font=f_small, fill=TEXT_MAIN)
        y_off += 23
        
    return img, d

def draw_axis_bubble(d, cx, cy, label, radius=18):
    d.ellipse([(cx - radius, cy - radius), (cx + radius, cy + radius)], fill=(20, 35, 55), outline=AXIS_COLOR, width=2)
    d.text((cx - 7, cy - 10), label, font=f_small, fill=TEXT_MAIN)

# 1. DWG A-101: Floor Plan (单层 3 房 2 卫 + 双车位车廊)
def make_floorplan():
    img, d = draw_cad_base(
        "2D 单层热带住宅建筑平面图 (Single-Storey Bungalow Floor Plan)",
        "DWG A-101",
        "1. 纯单层平地住宅格局：总建筑面积 2,300 sqft (室内净使用 2,000 sqft + 双车位车廊 300 sqft)。\n"
        "2. 户型配置：24ft 宽中央客厅/餐厅 + 独立豪华主卧套房 + 2 间次卧 + 开放干厨房 + 独立重油烟湿厨房 + 家政洗衣房。\n"
        "3. 退缩与尺寸：正面 20x15ft 双车位车廊 (前退缩 15ft)、后院 10ft (8PE 化粪池)、两侧各 5ft 排水退缩。",
        "ARCHITECTURAL / A"
    )
    
    ox, oy = 580, 160
    sw_px, sd_px = 1000, 750
    bx1, by1 = ox, oy
    bx2, by2 = ox + sw_px, oy + sd_px
    
    # Building Boundary
    d.rectangle([(bx1, by1), (bx2, by2)], outline=WALL_COLOR, width=4)
    
    # Front Car Porch (20ft x 15ft)
    d.rectangle([(bx1 + 250, by1 - 100), (bx1 + 750, by1)], fill=(20, 35, 50), outline=TEXT_GOLD, width=2)
    d.text((bx1 + 320, by1 - 65), "🚗 双车位遮阳车廊 (2-Car Porch 20'x15')", font=f_small, fill=TEXT_GOLD)
    
    # Dimension lines & text
    d.line([(bx1 - 40, by1), (bx1 - 40, by2)], fill=DIM_COLOR, width=2)
    d.text((bx1 - 170, oy + sd_px//2 - 10), "50' 0\" (15.24m) 进深", font=f_body, fill=DIM_COLOR)
    
    d.line([(bx1, by1 - 110), (bx2, by1 - 110)], fill=DIM_COLOR, width=2)
    d.text((ox + sw_px//2 - 140, by1 - 135), "40' 0\" (12.19m) 建筑面宽 (预留两侧 5' 退缩)", font=f_body, fill=DIM_COLOR)
    
    # Left Container: Master Suite & Wet Kitchen
    c1 = (bx1, by1, bx1 + 180, by1 + 750)
    d.rectangle(c1, fill=(35, 50, 35), outline=CONTAINER_COLOR, width=3)
    d.text((bx1 + 15, by1 + 60), "🛏️ 主卧套房\n(Master Suite)\n8' x 24'", font=f_small, fill=CONTAINER_COLOR)
    d.rectangle([(bx1, by1 + 240), (bx1 + 180, by1 + 380)], fill=(45, 60, 45), outline=TEXT_MAIN, width=1)
    d.text((bx1 + 15, by1 + 290), "🚿 主卫 (En-suite)", font=f_small, fill=TEXT_MAIN)
    d.rectangle([(bx1, by1 + 450), (bx1 + 180, by2)], fill=(20, 60, 85), outline=(56, 189, 248), width=2)
    d.text((bx1 + 15, by1 + 550), "🍳 重油烟湿厨房\n(Wet Kitchen)\n配 50L 隔油池", font=f_small, fill=TEXT_MAIN)
    
    # Right Container: Bed 2, Common Bath, Bed 3, Laundry/Utility
    c2 = (bx2 - 180, by1, bx2, by1 + 750)
    d.rectangle(c2, fill=(35, 50, 35), outline=CONTAINER_COLOR, width=3)
    d.text((bx2 - 165, by1 + 60), "🛏️ 次卧 2 (Bed 2)\n8' x 14'", font=f_small, fill=CONTAINER_COLOR)
    d.rectangle([(bx2 - 180, by1 + 220), (bx2, by1 + 340)], fill=(75, 35, 40), outline=AXIS_COLOR, width=2)
    d.text((bx2 - 165, by1 + 265), "🚽 公共浴室 (Bath)", font=f_small, fill=TEXT_MAIN)
    d.rectangle([(bx2 - 180, by1 + 340), (bx2, by1 + 540)], fill=(35, 50, 35), outline=CONTAINER_COLOR, width=2)
    d.text((bx2 - 165, by1 + 420), "🛏️ 次卧 3 (Bed 3)\n8' x 14'", font=f_small, fill=CONTAINER_COLOR)
    d.rectangle([(bx2 - 180, by1 + 540), (bx2, by2)], fill=(30, 45, 65), outline=DIM_COLOR, width=2)
    d.text((bx2 - 165, by1 + 610), "🧺 家政洗衣房\n(Laundry/DB)", font=f_small, fill=TEXT_MAIN)
    
    # Central Hall: Living & Dining & Dry Kitchen
    d.text((ox + sw_px//2 - 180, by1 + 120), "🛋️ 中央客厅与餐厅 (Living & Dining)\n24ft 宽 × 28ft 进深 (挑高 3.8m 木桁架)", font=f_header, fill=TEXT_MAIN)
    d.rectangle([(ox + sw_px//2 - 160, by1 + 450), (ox + sw_px//2 + 160, by2 - 40)], fill=(40, 55, 75), outline=TEXT_GOLD, width=2)
    d.text((ox + sw_px//2 - 120, by1 + 530), "☕ 开放式干厨房 & 吧台\n(Dry Kitchen / Breakfast Bar)", font=f_body, fill=TEXT_GOLD)

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/floorplan-bp.jpg", "JPEG", quality=93)
    print("Generated floorplan-bp.jpg DWG A-101 (Single-Storey)")

# 2. DWG A-102: Elevation (真实热带单层住宅标高)
def make_elevation():
    img, d = draw_cad_base(
        "单层建筑正立面与真实住宅标高示意图 (Single-Storey Front Elevation)",
        "DWG A-102",
        "1. 严格统一住宅控制标高：FL ±0.00m 地坪, +2.90m (+9'6\") 箱体顶, +3.65m (+12'0\") 主屋檐, +5.80m (+19'0\") 坡屋脊！\n"
        "2. 22° 经典热带坡屋顶设计，配置 1.2m 宽深挑檐 (Cucur Atap)，完美阻挡热带暴雨与猛烈西晒阳光。\n"
        "3. 正面设置 Batu Angin 通风花砖屏风玄关与 20x15ft 双车位车廊，打造典雅现代热带度假住宅气质。",
        "ARCHITECTURAL / A"
    )
    
    ox, oy = 450, 180
    w_px = 1100
    
    # Ground Line
    d.line([(ox - 100, oy + 520), (ox + w_px + 100, oy + 520)], fill=TEXT_MAIN, width=4)
    d.text((ox - 240, oy + 510), "▼ FL ±0.00m (地坪标高)", font=f_body, fill=TEXT_MAIN)
    
    # Levels
    d.line([(ox - 100, oy + 400), (ox + w_px + 100, oy + 400)], fill=DIM_COLOR, width=1)
    d.text((ox - 260, oy + 390), "▼ +2.90m (+9' 6\" 集装箱顶)", font=f_body, fill=DIM_COLOR)
    
    d.line([(ox - 100, oy + 280), (ox + w_px + 100, oy + 280)], fill=DIM_COLOR, width=1)
    d.text((ox - 260, oy + 270), "▼ +3.65m (+12' 0\" 主屋檐)", font=f_body, fill=DIM_COLOR)
    
    d.line([(ox - 100, oy + 120), (ox + w_px + 100, oy + 120)], fill=AXIS_COLOR, width=2)
    d.text((ox - 270, oy + 110), "▲ +5.80m (+19' 0\" 热带屋脊)", font=f_body, fill=AXIS_COLOR)
    
    # Containers left & right
    d.rectangle([(ox, oy + 400), (ox + 180, oy + 520)], outline=CONTAINER_COLOR, width=3)
    d.text((ox + 15, oy + 445), "左集装箱 8ft", font=f_small, fill=CONTAINER_COLOR)
    
    d.rectangle([(ox + w_px - 180, oy + 400), (ox + w_px, oy + 520)], outline=CONTAINER_COLOR, width=3)
    d.text((ox + w_px - 165, oy + 445), "右集装箱 8ft", font=f_small, fill=CONTAINER_COLOR)
    
    # Breeze Block Wall & Entrance
    d.rectangle([(ox + 180, oy + 360), (ox + w_px - 180, oy + 520)], fill=(25, 45, 35), outline=(74, 222, 128), width=3)
    d.text((ox + w_px//2 - 160, oy + 430), "🧱 Batu Angin 通风花砖屏风玄关 (24ft)", font=f_header, fill=(74, 222, 128))
    
    # 22 Roof (Eaves extend 1.2m beyond building)
    d.polygon([(ox - 40, oy + 280), (ox + w_px//2, oy + 120), (ox + w_px + 40, oy + 280)], outline=WALL_COLOR, width=3)
    d.rectangle([(ox + w_px//2 - 120, oy + 90), (ox + w_px//2 + 120, oy + 120)], fill=(35, 65, 95), outline=AXIS_COLOR, width=2)
    d.text((ox + w_px//2 - 100, oy + 98), "🪟 持续对流排热脊瓦天窗", font=f_small, fill=TEXT_MAIN)
    d.text((ox + w_px + 50, oy + 270), "← 1.2m 深挑檐 (Cucur Atap)", font=f_small, fill=TEXT_GOLD)

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/elevation-bp.jpg", "JPEG", quality=93)
    print("Generated elevation-bp.jpg DWG A-102 (Single-Storey)")

# 3. DWG G-101: Site Plan (单层住宅总图与双车位车廊)
def make_siteplan():
    img, d = draw_cad_base(
        "单层住宅总平面规划与退缩示意图 (Single-Storey Site Plan & Setbacks)",
        "DWG G-101",
        "1. 50ft 面宽 x 75ft 进深地块 (3,750 sqft)，正面沿 Jalan Pakis 市政道路。\n"
        "2. 退缩规范：前退缩 15ft (设 20x15ft 双车位遮阳车廊)、后退缩 10ft (8PE 化粪池与晾衣院)、两侧退缩各 5ft。\n"
        "3. 纯单层全平地布局，无楼梯阻碍，周边设 300mm U 型混凝土雨水渠，保障雨季排水顺畅。",
        "CIVIL & SITE / G"
    )
    
    ox, oy = 550, 160
    d.rectangle([(ox, oy), (ox + 1050, oy + 680)], fill=(12, 28, 48), outline=TEXT_MAIN, width=3)
    
    # North Arrow
    d.line([(ox + 980, oy + 80), (ox + 980, oy + 20)], fill=AXIS_COLOR, width=4)
    d.polygon([(ox + 980, oy + 10), (ox + 970, oy + 35), (ox + 990, oy + 35)], fill=AXIS_COLOR)
    d.text((ox + 970, oy + 90), "NORTH (北)", font=f_body, fill=AXIS_COLOR)
    
    # Jalan Pakis Road
    d.rectangle([(ox, oy - 55), (ox + 1050, oy)], fill=(35, 35, 45), outline=DIM_COLOR, width=2)
    d.text((ox + 300, oy - 40), "🛣️ JALAN PAKIS 沿街市政道路 (BOMBA 消防车停靠区)", font=f_header, fill=TEXT_MAIN)
    
    # Car Porch
    d.rectangle([(ox + 200, oy + 20), (ox + 700, oy + 130)], fill=(20, 45, 65), outline=TEXT_GOLD, width=2)
    d.text((ox + 280, oy + 65), "🚗 20'x15' 双车位车廊 (前退缩 15ft)", font=f_small, fill=TEXT_GOLD)
    
    # Building Footprint (40ft x 50ft)
    d.rectangle([(ox + 80, oy + 130), (ox + 920, oy + 580)], fill=(25, 45, 70), outline=WALL_COLOR, width=2)
    d.text((ox + 260, oy + 320), "单层独栋住宅占地 (40ft W x 50ft D / 2,000 sqft)\n前退缩 15ft | 后退缩 10ft | 侧退缩 5ft", font=f_header, fill=TEXT_MAIN)
    
    # Septic Tank
    d.rectangle([(ox + 750, oy + 590), (ox + 950, oy + 660)], fill=(75, 55, 15), outline=TEXT_GOLD, width=2)
    d.text((ox + 760, oy + 615), "8PE 生化化粪池 (后退缩 10ft)", font=f_small, fill=TEXT_GOLD)

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/siteplan-bp.jpg", "JPEG", quality=93)
    print("Generated siteplan-bp.jpg DWG G-101 (Single-Storey)")

# 4. DWG F-101: Fire Safety Plan (单层消防逃生)
def make_fire_safety():
    img, d = draw_cad_base(
        "单层住宅 BOMBA 消防与平地逃生路线图 (Single-Storey Fire & Egress Plan)",
        "DWG F-101",
        "1. 纯单层零楼梯平地逃生：正面设 1.5m 净宽双开主逃生门 (Exit 1)，后方湿厨房设直通后院第二逃生门 (Exit 2)。\n"
        "2. 图中精准标注 4 处光感烟雾报警器 (SD1-SD4) 与 3 处 6kg ABC 干粉灭火器 (FE1-FE3) 点位。\n"
        "3. 全屋任意卧室至室外逃生门行走距离均低于 12m (远优于 UBBL 22.5m 规范上限)。",
        "FIRE SAFETY / F"
    )
    ox, oy = 450, 160
    d.rectangle([(ox, oy), (ox + 1150, oy + 650)], outline=WALL_COLOR, width=3)
    
    d.rectangle([(ox + 420, oy - 20), (ox + 720, oy + 20)], fill=(0, 180, 90), outline=TEXT_MAIN, width=2)
    d.text((ox + 440, oy - 15), "🟢 主逃生门 Exit 1 (1.5m 净宽)", font=f_body, fill=TEXT_MAIN)
    
    d.rectangle([(ox + 60, oy + 640), (ox + 300, oy + 670)], fill=(0, 180, 90), outline=TEXT_MAIN, width=2)
    d.text((ox + 80, oy + 645), "🟢 湿厨房后院逃生门 Exit 2", font=f_body, fill=TEXT_MAIN)
    
    sd_pts = [(ox + 180, oy + 200, "SD1 主卧"), (ox + 580, oy + 250, "SD2 客厅"), (ox + 980, oy + 200, "SD3 次卧"), (ox + 180, oy + 520, "SD4 厨房")]
    for pt in sd_pts:
        d.ellipse([(pt[0]-15, pt[1]-15), (pt[0]+15, pt[1]+15)], fill=(200, 50, 50), outline=TEXT_MAIN, width=2)
        d.text((pt[0]-12, pt[1]-8), pt[2][:3], font=f_small, fill=TEXT_MAIN)
        d.text((pt[0]+22, pt[1]-8), pt[2][4:], font=f_small, fill=TEXT_MAIN)
        
    fe_pts = [(ox + 380, oy + 60, "FE1 玄关"), (ox + 980, oy + 60, "FE2 走廊"), (ox + 180, oy + 420, "FE3 湿厨房")]
    for pt in fe_pts:
        d.rectangle([(pt[0]-15, pt[1]-15), (pt[0]+15, pt[1]+15)], fill=(220, 180, 20), outline=AXIS_COLOR, width=2)
        d.text((pt[0]+22, pt[1]-8), pt[2], font=f_small, fill=TEXT_GOLD)
        
    d.line([(ox + 580, oy + 500), (ox + 580, oy + 50)], fill=(74, 222, 128), width=4)
    d.text((ox + 600, oy + 250), "⬆ 单层直线逃生距离 < 12m (极速安全逃生)", font=f_header, fill=(74, 222, 128))

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/fire_safety_egress_blueprint.jpg", "JPEG", quality=93)
    print("Generated fire_safety_egress_blueprint.jpg DWG F-101 (Single-Storey)")

# 5. DWG M-101: Drainage Plan (干湿双厨房与排水分离)
def make_kitchen_drainage():
    img, d = draw_cad_base(
        "单层住宅干湿双厨房与集中排水系统工程图 (Drainage Plan)",
        "DWG M-101",
        "1. 湿厨房排水：DN75 灰水管 + 50L 不锈钢油脂拦截器 (Grease Trap)，设 DN50 存水弯与通气管，排入侧边 U 型渠。\n"
        "2. 卫生间黑水：主卫与客卫 DN100 PVC 污水管 (1:40 坡度) 设清扫口 (CO) 与检查井 (IC)，直连后区 8PE 化粪池。\n"
        "3. 排水标高：进水 IL -0.45m，出水 IL -0.60m，符合 IWK 与 SPAN 卫生工程规范。",
        "MECHANICAL & PLUMBING / M"
    )
    ox, oy = 450, 160
    d.rectangle([(ox, oy), (ox + 1150, oy + 650)], outline=WALL_COLOR, width=3)
    
    d.rectangle([(ox + 20, oy + 350), (ox + 320, oy + 630)], fill=(18, 55, 85), outline=(56, 189, 248), width=2)
    d.text((ox + 40, oy + 370), "🍳 重油烟湿厨房 (Wet Kitchen)", font=f_header, fill=(56, 189, 248))
    d.text((ox + 40, oy + 420), "• DN75 灰水专用管 (1:50 坡度)\n• 50L 不锈钢油脂拦截器 (GT)\n• 独立通气管 (VP) 伸出屋顶", font=f_small, fill=TEXT_MAIN)
    
    d.rectangle([(ox + 810, oy + 100), (ox + 1130, oy + 450)], fill=(75, 30, 40), outline=AXIS_COLOR, width=2)
    d.text((ox + 830, oy + 120), "🚽 主卫 & 客卫集中湿区", font=f_header, fill=AXIS_COLOR)
    d.text((ox + 830, oy + 170), "• DN100 PVC 黑水排污管 (1:40)\n• 清扫口 (Cleanout CO)\n• 检查井直连 8PE 生化化粪池", font=f_small, fill=TEXT_MAIN)

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/kitchen_drainage_blueprint.jpg", "JPEG", quality=93)
    print("Generated kitchen_drainage_blueprint.jpg DWG M-101 (Single-Storey)")

# 6. DWG T-101: T&C Testing Plan
def make_tc_testing():
    img, d = draw_cad_base(
        "单层住宅 5 大工程验收打压测试点位图 (T&C Testing Blueprint)",
        "DWG T-101",
        "1. 测1: PPR 8 Bar 给水保压 (SPAN 规范) | 测2: 24h 卫浴/厨房闭水零渗漏 | 测3: 4h 坡屋顶与深挑檐高压喷淋。\n"
        "2. 测4: 30mA RCCB 漏电 30ms 保护及 <10Ω 接地电阻 | 测5: 热带屋脊对流通风与温降测试。\n"
        "3. 每项测试均明确验收标准、责任方与复测机制，保障单层住宅 CCC 钥匙交付质量。",
        "TESTING & COMMISSIONING / T"
    )
    ox, oy = 400, 160
    d.rectangle([(ox, oy), (ox + 1250, oy + 680)], outline=WALL_COLOR, width=3)
    
    d.rectangle([(ox + 30, oy + 30), (ox + 390, oy + 310)], fill=(18, 48, 85), outline=DIM_COLOR, width=2)
    d.text((ox + 45, oy + 45), "🧪 测1：PPR 8 Bar 给水打压", font=f_body, fill=DIM_COLOR)
    d.text((ox + 45, oy + 85), "• 依据 SPAN 规范\n• 1.5倍压力保压 2h\n• 责任: 水务承包商\n• 验收: 压降 = 0", font=f_small, fill=TEXT_MAIN)
    
    d.rectangle([(ox + 430, oy + 30), (ox + 790, oy + 310)], fill=(75, 30, 40), outline=AXIS_COLOR, width=2)
    d.text((ox + 445, oy + 45), "🧪 测2：24h 湿区蓄水闭水", font=f_body, fill=AXIS_COLOR)
    d.text((ox + 445, oy + 85), "• 注入 100mm 水 24h\n• 检验主客卫防水层\n• 责任: 防水承包商\n• 验收: 零渗漏", font=f_small, fill=TEXT_MAIN)

    d.rectangle([(ox + 830, oy + 30), (ox + 1210, oy + 310)], fill=(25, 65, 45), outline=(74, 222, 128), width=2)
    d.text((ox + 845, oy + 45), "🧪 测3：4h 坡屋顶防雨喷淋", font=f_body, fill=(74, 222, 128))
    d.text((ox + 845, oy + 85), "• 对 22° 坡顶及挑檐喷淋\n• 责任: 屋面承包商\n• 验收: 天花板零水渍", font=f_small, fill=TEXT_MAIN)

    d.rectangle([(ox + 180, oy + 350), (ox + 580, oy + 630)], fill=(75, 65, 18), outline=TEXT_GOLD, width=2)
    d.text((ox + 195, oy + 365), "🧪 测4：30mA RCCB 漏电测试", font=f_body, fill=TEXT_GOLD)
    d.text((ox + 195, oy + 405), "• 30ms 极速切断保护\n• 测量接地电阻 < 10 欧姆\n• 责任: 电气工程师", font=f_small, fill=TEXT_MAIN)

    d.rectangle([(ox + 660, oy + 350), (ox + 1060, oy + 630)], fill=(45, 35, 75), outline=TEXT_MAIN, width=2)
    d.text((ox + 675, oy + 365), "🧪 测5：屋脊自然对流通风测试", font=f_body, fill=TEXT_MAIN)
    d.text((ox + 675, oy + 405), "• 测量热带对流风速\n• 检验室内降温 3-5°C 效率\n• 责任: 通风顾问", font=f_small, fill=TEXT_MAIN)

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/tc_testing_blueprint.jpg", "JPEG", quality=93)
    print("Generated tc_testing_blueprint.jpg DWG T-101 (Single-Storey)")

# 7. DWG S-101: Container Detail
def make_container_detail():
    img, d = draw_cad_base(
        "集装箱切口与 100mm 方钢框焊接加固大样图 (Structural Detail)",
        "DWG S-101",
        "1. 40ft High Cube 集装箱侧墙切割开窗后，切口四周必须连续满焊 100x100x4.5mm RHS 方钢增强框。\n"
        "2. 箱体底角件与 150mm 加厚钢筋混凝土地坪通过 M20 预埋化学锚栓 (深度 200mm) 焊接锁死，抗拔力达 45kN。\n"
        "3. 中央 24ft 跨度采用 200x100mm H-beam 柱梁与 22° 轻钢坡屋架无缝连接，抗震抗风完全合规。",
        "STRUCTURAL / S"
    )
    ox, oy = 400, 200
    d.text((ox, oy), "【单层住宅集装箱侧墙切割 & 100mm 方钢框焊接剖面节点大样】", font=f_header, fill=TEXT_GOLD)
    d.rectangle([(ox, oy + 60), (ox + 350, oy + 500)], fill=(28, 42, 60), outline=CONTAINER_COLOR, width=3)
    d.rectangle([(ox + 350, oy + 60), (ox + 450, oy + 500)], fill=STEEL_COLOR, outline=TEXT_MAIN, width=2)
    d.rectangle([(ox, oy + 500), (ox + 600, oy + 580)], fill=(75, 75, 85), outline=TEXT_MAIN, width=2)
    d.text((ox + 50, oy + 530), "150mm 加厚钢筋混凝土地坪 + M20 预埋化学锚栓 (Concrete Foundation)", font=f_body, fill=TEXT_MAIN)

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/container_splicing_blueprint.jpg", "JPEG", quality=93)
    print("Generated container_splicing_blueprint.jpg DWG S-101 (Single-Storey)")

# 8. DWG E-101: Electrical & Solar Wiring Blueprint
def make_electrical_wiring():
    img, d = draw_cad_base(
        "单层住宅 TNB 三相供电、太阳能与避雷示意图 (Electrical & Solar)",
        "DWG E-101",
        "1. 电源配置：TNB 3-Phase 63A (415V, 50Hz) 三相配电箱，设 30mA RCCB 漏电保护，均衡分配空调用电。\n"
        "2. 防雷接地：+19ft 屋脊顶装纯铜避雷针 (Air Terminal)，紫铜引下线接地电阻测试 < 10 欧姆。\n"
        "3. 绿能预留：22° 坡屋顶预留 10kW 太阳能光伏板 (Solar PV) 支架与双向电表接口。",
        "ELECTRICAL / E"
    )
    ox, oy = 400, 160
    d.rectangle([(ox, oy), (ox + 1250, oy + 680)], outline=WALL_COLOR, width=3)
    
    d.rectangle([(ox + 50, oy + 50), (ox + 550, oy + 320)], fill=(18, 48, 85), outline=DIM_COLOR, width=2)
    d.text((ox + 70, oy + 70), "⚡ TNB 3-Phase 63A 主配电箱 (Main DB)", font=f_body, fill=DIM_COLOR)
    d.text((ox + 70, oy + 115), "• 415V, 50Hz 三相供电均衡相负荷\n• 30mA RCCB 30ms 极速漏电切断\n• 位于家政区，预留充电桩专线", font=f_small, fill=TEXT_MAIN)

    d.rectangle([(ox + 650, oy + 50), (ox + 1150, oy + 320)], fill=(75, 55, 18), outline=TEXT_GOLD, width=2)
    d.text((ox + 670, oy + 70), "🌩️ +19ft 屋脊纯铜避雷针与接地 (Earthing)", font=f_body, fill=TEXT_GOLD)
    d.text((ox + 670, oy + 115), "• 纯铜避雷针 (Air Terminal Rod)\n• 70mm² 紫铜接地引下线\n• 铜沉盘接地电阻测试 < 10 欧姆", font=f_small, fill=TEXT_MAIN)

    d.rectangle([(ox + 350, oy + 360), (ox + 850, oy + 630)], fill=(25, 65, 45), outline=(74, 222, 128), width=2)
    d.text((ox + 370, oy + 380), "☀️ 10kW 太阳能光伏预留 (Solar PV Ready)", font=f_body, fill=(74, 222, 128))
    d.text((ox + 370, oy + 425), "• 22° 坡屋顶 Colorbond 支架预留\n• 预敷 6mm² DC 太阳能专线\n• 预留三相双向电表与逆变器位", font=f_small, fill=TEXT_MAIN)

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/electrical_wiring_blueprint.jpg", "JPEG", quality=93)
    print("Generated electrical_wiring_blueprint.jpg DWG E-101 (Single-Storey)")

# 9. DWG X-101: Soil Termite & Standing Seam Waterproof Blueprint
def make_soil_termite_waterproof():
    img, d = draw_cad_base(
        "单层住宅地基防白蚁防潮膜与直立锁边坡屋面大样图 (Specs Detail)",
        "DWG X-101",
        "1. 地基防潮：150mm 加厚混凝土地坪下方整铺 0.2mm 高密度 HDPE 防潮隔气膜 (DPM)。\n"
        "2. 化学防蚁：浇筑前对原土全面施加 MS 828 标准 Fipronil 化学屏障，防止散白蚁侵蚀底盘。\n"
        "3. 屋面防漏：22° 热带坡屋顶采用 Standing Seam 直立锁边 50mm PU 夹芯板，配合 1.2m 深挑檐无外露螺丝。",
        "DETAIL & SPEC / X"
    )
    ox, oy = 400, 160
    d.rectangle([(ox, oy), (ox + 1250, oy + 680)], outline=WALL_COLOR, width=3)
    
    d.rectangle([(ox + 50, oy + 50), (ox + 580, oy + 630)], fill=(25, 45, 65), outline=DIM_COLOR, width=2)
    d.text((ox + 70, oy + 70), "🧱 地坪防潮与 MS 828 防白蚁剖面", font=f_body, fill=DIM_COLOR)
    d.text((ox + 70, oy + 120), "1. 150mm Grade 30 钢筋混凝土地坪\n2. 0.2mm 高密度 HDPE 防潮隔气膜 (DPM)\n3. Fipronil 化学防白蚁化学屏障 (MS 828)\n4. 150mm 压实碎石级配垫层", font=f_small, fill=TEXT_MAIN)

    d.rectangle([(ox + 650, oy + 50), (ox + 1180, oy + 630)], fill=(75, 45, 25), outline=STEEL_COLOR, width=2)
    d.text((ox + 670, oy + 70), "🏠 Standing Seam 直立锁边坡屋面大样", font=f_body, fill=STEEL_COLOR)
    d.text((ox + 670, oy + 120), "1. 50mm 高密度 PU 隔热夹芯彩钢板\n2. Standing Seam 270° 机械直立锁边 (无螺丝)\n3. 1.2m 宽深挑檐 (Cucur Atap) 挡风雨\n4. 降噪 28dB 暴雨雨击声学吸音层", font=f_small, fill=TEXT_MAIN)

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/soil_termite_waterproof_blueprint.jpg", "JPEG", quality=93)
    print("Generated soil_termite_waterproof_blueprint.jpg DWG X-101 (Single-Storey)")

if __name__ == "__main__":
    make_floorplan()
    make_elevation()
    make_siteplan()
    make_fire_safety()
    make_kitchen_drainage()
    make_tc_testing()
    make_container_detail()
    make_electrical_wiring()
    make_soil_termite_waterproof()
