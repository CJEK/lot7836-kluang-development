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
    f_title = ImageFont.truetype(font_path, 40)
    f_header = ImageFont.truetype(font_path, 30)
    f_body = ImageFont.truetype(font_path, 22)
    f_small = ImageFont.truetype(font_path, 18)
    f_dim = ImageFont.truetype(font_path, 16)
except Exception as e:
    print(f"Font error: {e}")
    f_title = f_header = f_body = f_small = f_dim = ImageFont.load_default()

def draw_cad_frame(title_zh, dwg_no, desc_zh):
    img = Image.new("RGB", (W, H), BG_COLOR)
    d = ImageDraw.Draw(img)
    
    for x in range(0, W, 50):
        d.line([(x, 0), (x, H)], fill=GRID_COLOR, width=1)
    for y in range(0, H, 50):
        d.line([(0, y), (W, y)], fill=GRID_COLOR, width=1)
        
    d.rectangle([(40, 40), (W - 40, H - 40)], outline=(100, 150, 200), width=3)
    d.rectangle([(46, 46), (W - 46, H - 46)], outline=(50, 90, 140), width=1)
    
    tb_left, tb_top = W - 750, H - 180
    d.rectangle([(tb_left, tb_top), (W - 50, H - 50)], fill=(18, 38, 64), outline=DIM_COLOR, width=2)
    d.line([(tb_left, tb_top + 45), (W - 50, tb_top + 45)], fill=DIM_COLOR, width=1)
    d.line([(tb_left, tb_top + 90), (W - 50, tb_top + 90)], fill=DIM_COLOR, width=1)
    d.line([(tb_left + 450, tb_top), (tb_left + 450, H - 50)], fill=DIM_COLOR, width=1)
    
    d.text((tb_left + 15, tb_top + 10), "PROJECT: LOT 7836 KLUANG DEVELOPMENT", font=f_small, fill=TEXT_MAIN)
    d.text((tb_left + 465, tb_top + 10), f"DWG NO: {dwg_no}", font=f_small, fill=TEXT_GOLD)
    
    d.text((tb_left + 15, tb_top + 55), f"TITLE: {title_zh}", font=f_body, fill=DIM_COLOR)
    d.text((tb_left + 465, tb_top + 55), "SCALE: 1:100 @ A3", font=f_small, fill=TEXT_MAIN)
    
    d.text((tb_left + 15, tb_top + 100), "DESIGN: CONTAINER MODULAR BUNGALOW", font=f_small, fill=TEXT_MAIN)
    d.text((tb_left + 465, tb_top + 100), "STATUS: APPROVED FOR C&S", font=f_small, fill=(74, 222, 128))

    d.rectangle([(50, 50), (W - 770, 120)], fill=(20, 45, 75), outline=DIM_COLOR, width=1)
    d.text((70, 65), f"CAD 施工工程规范图纸 | {title_zh}", font=f_title, fill=TEXT_MAIN)
    
    d.rectangle([(50, H - 240), (W - 770, H - 50)], fill=NOTE_BG, outline=DIM_COLOR, width=2)
    d.text((70, H - 225), "💡 施工方 & 合作伙伴读图指引 & 设计原理解析 (Design Logic & Layman Explanation):", font=f_body, fill=TEXT_GOLD)
    
    lines = desc_zh.split("\n")
    y_off = H - 190
    for line in lines:
        d.text((70, y_off), line, font=f_small, fill=TEXT_MAIN)
        y_off += 26
        
    return img, d

# 1. DWG A-101: Floor Plan 2D 平面工程图
def make_floorplan():
    img, d = draw_cad_frame(
        "2D 建筑平面布置工程图 (Architectural Floor Plan)",
        "DWG A-101",
        "1. 本建筑面宽 50ft (15.24m)，纵深 75ft (22.86m)。左右两边各摆放 1 个 40ft High Cube 集装箱 (宽 8ft)。\n"
        "2. 集装箱内侧墙打通后焊接 100x100mm 方钢圈补强，中间空出 34ft 大面宽挑高大厅 (High Ceiling Hall)。\n"
        "3. 后区 35ft 设独立双卫生间 (Restroom) 与开放式厨房 (Kitchen)，所有排水管均顺着斜度直排后方化粪池。"
    )
    
    ox, oy = 550, 200
    sw_px = 50 * 22  # 1100
    sd_px = 75 * 11  # 825
    
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
    
    d.text((ox + sw_px//2 - 200, by1 + 200), "34ft 挑高大厅 (High Ceiling Hall)\n净宽 10.36m / 净高 7.3m", font=f_header, fill=TEXT_MAIN)
    
    d.rectangle([(bx1 + 170, by1 + 50), (bx1 + 182, by1 + 390)], fill=STEEL_COLOR)
    d.text((bx1 + 190, by1 + 220), "← 100mm 方钢门框加固 (Cutout Steel Frame)", font=f_dim, fill=STEEL_COLOR)
    
    d.rectangle([(bx1, by1 + 440), (bx1 + 350, by2)], fill=(20, 60, 80), outline=(56, 189, 248), width=2)
    d.text((bx1 + 20, by1 + 500), "🍳 开放式厨房 (Kitchen)\n配 L型水槽 & 油烟机", font=f_body, fill=TEXT_MAIN)
    
    d.rectangle([(bx2 - 350, by1 + 440), (bx2, by2)], fill=(80, 40, 40), outline=AXIS_COLOR, width=2)
    d.text((bx2 - 330, by1 + 500), "🚽 独立双卫生间 (Restrooms)\n无障碍坡道 & 防滑地砖", font=f_body, fill=TEXT_MAIN)
    
    d.rectangle([(bx1 + 180, by1 + 440), (bx2 - 180, by2)], outline=(250, 204, 21), width=2)
    d.text((ox + sw_px//2 - 220, by1 + 600), "二层 900sqft Mezzanine Loft 办公平台 (净高 3.3m)", font=f_small, fill=TEXT_GOLD)

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/floorplan-bp.jpg", "JPEG", quality=92)
    print("Generated floorplan-bp.jpg DWG A-101")

# 2. DWG A-102: Elevation 正立面图
def make_elevation():
    img, d = draw_cad_frame(
        "建筑正立面结构工程图 (Front Elevation & Height Levels)",
        "DWG A-102",
        "1. 拔风塔顶标高 +36' 0\" (10.97m)，高坡屋檐标高 +24' 0\" (7.31m)，集装箱顶部标高 +9' 6\" (2.90m)。\n"
        "2. 屋顶采用 30° 高坡热带防雨设计，配合中央 raised monitor 拔风天窗，将室内积聚热气自然排出。\n"
        "3. 正面采用马六甲 Batu Angin 避光通风花砖屏风墙，双层墙结构阻挡阳光直射，降低室内温度 3-5°C。"
    )
    
    ox, oy = 450, 250
    w_px = 1100
    
    d.line([(ox - 100, oy + 500), (ox + w_px + 100, oy + 500)], fill=TEXT_MAIN, width=4)
    d.text((ox - 240, oy + 490), "▼ FL ±0.00m (地坪高度)", font=f_body, fill=TEXT_MAIN)
    
    d.line([(ox - 100, oy + 360), (ox + w_px + 100, oy + 360)], fill=DIM_COLOR, width=1)
    d.text((ox - 260, oy + 350), "▼ +9'6\" (2.90m 集装箱顶)", font=f_body, fill=DIM_COLOR)
    
    d.line([(ox - 100, oy + 200), (ox + w_px + 100, oy + 200)], fill=DIM_COLOR, width=1)
    d.text((ox - 260, oy + 190), "▼ +24'0\" (7.31m 主屋檐)", font=f_body, fill=DIM_COLOR)
    
    d.line([(ox - 100, oy + 60), (ox + w_px + 100, oy + 60)], fill=TEXT_GOLD, width=2)
    d.text((ox - 280, oy + 50), "▲ +36'0\" (10.97m 拔风塔顶)", font=f_body, fill=TEXT_GOLD)
    
    d.rectangle([(ox, oy + 360), (ox + 176, oy + 500)], outline=CONTAINER_COLOR, width=3)
    d.text((ox + 20, oy + 420), "左集装箱 8ft", font=f_small, fill=CONTAINER_COLOR)
    
    d.rectangle([(ox + w_px - 176, oy + 360), (ox + w_px, oy + 500)], outline=CONTAINER_COLOR, width=3)
    d.text((ox + w_px - 150, oy + 420), "右集装箱 8ft", font=f_small, fill=CONTAINER_COLOR)
    
    d.rectangle([(ox + 176, oy + 300), (ox + w_px - 176, oy + 500)], fill=(30, 50, 40), outline=(74, 222, 128), width=3)
    d.text((ox + w_px//2 - 160, oy + 400), "🧱 Batu Angin 通风花砖屏风墙 (34ft)", font=f_header, fill=(74, 222, 128))
    
    d.polygon([(ox, oy + 200), (ox + w_px//2, oy + 60), (ox + w_px, oy + 200)], outline=WALL_COLOR, width=3)
    
    d.rectangle([(ox + w_px//2 - 200, oy + 60), (ox + w_px//2 + 200, oy + 120)], fill=(40, 70, 100), outline=TEXT_GOLD, width=2)
    d.text((ox + w_px//2 - 140, oy + 80), "🪟 中央拔风天窗 (Monitor Window)", font=f_small, fill=TEXT_GOLD)

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/elevation-bp.jpg", "JPEG", quality=92)
    print("Generated elevation-bp.jpg DWG A-102")

# 3. DWG S-101: Container Modification Detail
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
    d.text((ox + 40, oy + 250), "40ft 集装箱钢波纹壁板\n(Corten Steel Corrugated Wall)", font=f_body, fill=TEXT_MAIN)
    
    d.rectangle([(ox + 350, oy + 60), (ox + 450, oy + 500)], fill=STEEL_COLOR, outline=TEXT_MAIN, width=2)
    d.text((ox + 360, oy + 230), "100x100mm\nRHS 方钢框\n(C-Channel Frame)", font=f_small, fill=TEXT_MAIN)
    
    d.polygon([(ox + 340, oy + 180), (ox + 360, oy + 160), (ox + 360, oy + 200)], fill=AXIS_COLOR)
    d.text((ox + 200, oy + 165), "全围连续缝焊 6mm 🛠️ ➔", font=f_body, fill=AXIS_COLOR)
    
    d.rectangle([(ox, oy + 500), (ox + 600, oy + 580)], fill=(80, 80, 90), outline=TEXT_MAIN, width=2)
    d.text((ox + 50, oy + 530), "150mm 加厚钢筋混凝土地坪 + M20 预埋化学锚栓 (Concrete Foundation)", font=f_body, fill=TEXT_MAIN)

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/container_splicing_blueprint.jpg", "JPEG", quality=92)
    print("Generated container_splicing_blueprint.jpg DWG S-101")

# 4. DWG M-101: Kitchen & Wet-Core Drainage Plan
def make_kitchen_drainage():
    img, d = draw_cad_frame(
        "厨房与集中排水系统工程施工图 (Kitchen & Wet-Core Drainage Plan)",
        "DWG M-101",
        "1. 厨房餐饮废水先经过 50L 不锈钢油脂拦截器 (Grease Trap) 过滤油脂后，接入灰水管 (Greywater Pipe)。\n"
        "2. 双卫生间黑水采用 DN100 PVC 高密度排污管，按 1:40 坡度直排后方 8PE HDPE 生化化粪池 (Septic Tank)。\n"
        "3. 地坪周圈开挖 300x300mm U型雨水沟，与居銮市政排水主渠接通，确保暴雨季零积水零倒灌。"
    )
    
    ox, oy = 450, 180
    
    d.rectangle([(ox, oy), (ox + 1200, oy + 650)], outline=WALL_COLOR, width=3)
    
    d.rectangle([(ox + 20, oy + 200), (ox + 350, oy + 630)], fill=(20, 60, 90), outline=(56, 189, 248), width=2)
    d.text((ox + 40, oy + 220), "🍳 开放式厨房区 (Kitchen Zone)", font=f_header, fill=(56, 189, 248))
    d.text((ox + 40, oy + 270), "• 双槽不锈钢洗菜盆 (DN50 排水)\n• 独立抽油烟管道出口\n• 50L 埋地式油脂拦截器 (Grease Trap)", font=f_small, fill=TEXT_MAIN)
    
    d.rectangle([(ox + 370, oy + 500), (ox + 470, oy + 600)], fill=(30, 80, 50), outline=(74, 222, 128), width=2)
    d.text((ox + 380, oy + 530), "油脂拦截器\nGrease Trap", font=f_small, fill=(74, 222, 128))
    
    d.rectangle([(ox + 850, oy + 200), (ox + 1180, oy + 630)], fill=(80, 30, 40), outline=AXIS_COLOR, width=2)
    d.text((ox + 870, oy + 220), "🚽 独立双卫生间 (Restrooms)", font=f_header, fill=AXIS_COLOR)
    d.text((ox + 870, oy + 270), "• 男/女独立蹲坐马桶\n• DN100 PVC 黑水排污管 (坡度 1:40)\n• 24h 闭水防漏沉箱结构", font=f_small, fill=TEXT_MAIN)
    
    d.line([(ox + 470, oy + 550), (ox + 650, oy + 550), (ox + 650, oy + 700)], fill=(74, 222, 128), width=4)
    d.text((ox + 480, oy + 520), "灰水管 DN75 ➔", font=f_small, fill=(74, 222, 128))
    
    d.line([(ox + 850, oy + 550), (ox + 750, oy + 550), (ox + 750, oy + 700)], fill=AXIS_COLOR, width=4)
    d.text((ox + 760, oy + 520), "⬅ 黑水管 DN100", font=f_small, fill=AXIS_COLOR)
    
    d.rectangle([(ox + 600, oy + 680), (ox + 800, oy + 760)], fill=(80, 60, 20), outline=TEXT_GOLD, width=3)
    d.text((ox + 615, oy + 710), "8PE 生化化粪池 (Septic Tank)", font=f_body, fill=TEXT_GOLD)

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/kitchen_drainage_blueprint.jpg", "JPEG", quality=92)
    print("Generated kitchen_drainage_blueprint.jpg DWG M-101")

# 5. DWG F-101: Fire Safety & Egress Plan
def make_fire_safety():
    img, d = draw_cad_frame(
        "BOMBA 消防安全设施与疏散逃生路线图 (Fire Safety & Egress Plan)",
        "DWG F-101",
        "1. 主逃生口 (Main Exit) 位于正面 50ft 面宽大门，后区设 6ft 紧急避难门 (Emergency Exit)。\n"
        "2. 全屋配备 6 处自吸式光感烟雾报警器 (Smoke Detector)，并于前门及后门放置 6kg ABC 干粉灭火器。\n"
        "3. 所有疏散通道宽度大于 1.5m，安全指示灯 (Exit Light) 具备 3 小时备用电池应急照明功能。"
    )
    
    ox, oy = 450, 180
    d.rectangle([(ox, oy), (ox + 1200, oy + 650)], outline=WALL_COLOR, width=3)
    
    d.rectangle([(ox + 450, oy - 20), (ox + 750, oy + 20)], fill=(0, 180, 90), outline=TEXT_MAIN, width=2)
    d.text((ox + 480, oy - 15), "🟢 主逃生出口 (MAIN EXIT 1)", font=f_body, fill=TEXT_MAIN)
    
    d.rectangle([(ox + 500, oy + 640), (ox + 700, oy + 670)], fill=(0, 180, 90), outline=TEXT_MAIN, width=2)
    d.text((ox + 510, oy + 645), "🟢 紧急逃生出口 (EXIT 2)", font=f_body, fill=TEXT_MAIN)
    
    d.line([(ox + 600, oy + 400), (ox + 600, oy + 50)], fill=(74, 222, 128), width=5)
    d.text((ox + 620, oy + 200), "⬆ 安全疏散主通道 (Egress Route)", font=f_header, fill=(74, 222, 128))

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/fire_safety_egress_blueprint.jpg", "JPEG", quality=92)
    print("Generated fire_safety_egress_blueprint.jpg DWG F-101")

# 6. DWG T-101: T&C Testing Blueprint
def make_tc_testing():
    img, d = draw_cad_frame(
        "5 大工程验收打压测试点位图 (T&C Inspection & Testing Blueprint)",
        "DWG T-101",
        "1. 给水 PPR 管 8 Bar 保压测试：1.5 倍工作压力保压 2 小时，压力计压降需为零。\n"
        "2. 24 小时湿区蓄水测试：厨房与卫生间沉箱注入 100mm 积水，底层无渗水记录。\n"
        "3. 30° 坡屋顶与拔风塔接缝 4 小时高压喷淋防漏水测试；30mA 漏电保护器 30ms 极速切断测试。"
    )
    
    ox, oy = 400, 180
    d.rectangle([(ox, oy), (ox + 1300, oy + 650)], outline=WALL_COLOR, width=3)
    
    d.rectangle([(ox + 50, oy + 50), (ox + 600, oy + 280)], fill=(20, 50, 90), outline=DIM_COLOR, width=2)
    d.text((ox + 70, oy + 70), "🧪 测试 1：给水管 8 Bar 打压测试", font=f_header, fill=DIM_COLOR)
    d.text((ox + 70, oy + 120), "• 给水主管压力表加压至 0.8MPa (8 Bar)\n• 保持 2 小时零压降即可验收合格", font=f_body, fill=TEXT_MAIN)
    
    d.rectangle([(ox + 700, oy + 50), (ox + 1250, oy + 280)], fill=(80, 30, 40), outline=AXIS_COLOR, width=2)
    d.text((ox + 720, oy + 70), "🧪 测试 2：24h 湿区闭水蓄水测试", font=f_header, fill=AXIS_COLOR)
    d.text((ox + 720, oy + 120), "• 厨房与卫生间注入 100mm 深积水 24h\n• 检验防水层与排污管口无渗漏", font=f_body, fill=TEXT_MAIN)
    
    d.rectangle([(ox + 50, oy + 350), (ox + 600, oy + 580)], fill=(30, 70, 50), outline=(74, 222, 128), width=2)
    d.text((ox + 70, oy + 370), "🧪 测试 3：4h 坡屋顶高压喷淋测试", font=f_header, fill=(74, 222, 128))
    d.text((ox + 70, oy + 420), "• 高压水枪对 30° 坡屋顶与接缝持续喷淋\n• 室内天花板与顶板零水渍验收", font=f_body, fill=TEXT_MAIN)
    
    d.rectangle([(ox + 700, oy + 350), (ox + 1250, oy + 580)], fill=(80, 70, 20), outline=TEXT_GOLD, width=2)
    d.text((ox + 720, oy + 370), "🧪 测试 4：30mA RCCB 漏电测试", font=f_header, fill=TEXT_GOLD)
    d.text((ox + 720, oy + 420), "• 模拟漏电信号，断路器必须在 30ms 切断\n• 测量接地电阻低于 10 欧姆", font=f_body, fill=TEXT_MAIN)

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/tc_testing_blueprint.jpg", "JPEG", quality=92)
    print("Generated tc_testing_blueprint.jpg DWG T-101")

# 7. DWG G-101: Site Plan
def make_siteplan():
    img, d = draw_cad_frame(
        "总平面工程规划图 (Site & Infrastructure Plan)",
        "DWG G-101",
        "1. 50ft 面宽 x 75ft 进深地块（3,750 sqft），正面临 Jalan Pakis 市政道路，前后满足退缩线要求。\n"
        "2. 周圈开挖 300mm U型雨水沟，右上角设置独立垃圾与检修通道，后方接通 8PE 生化化粪池。\n"
        "3. 提供 2 车位停车位与绿化植被隔离带，符合居銮市议会 (MPK) 规划报建标准。"
    )
    
    ox, oy = 500, 180
    d.rectangle([(ox, oy), (ox + 1100, oy + 650)], fill=(15, 32, 55), outline=TEXT_MAIN, width=3)
    d.text((ox + 20, oy + 20), "地块边界 50' x 75' (LOT 7836 SITE BOUNDARY)", font=f_header, fill=DIM_COLOR)
    
    d.rectangle([(ox + 100, oy + 100), (ox + 1000, oy + 550)], fill=(30, 50, 75), outline=TEXT_GOLD, width=2)
    d.text((ox + 400, oy + 300), "集装箱 Bungalow 主建筑\n(Building Footprint 50x75ft)", font=f_header, fill=TEXT_MAIN)

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/siteplan-bp.jpg", "JPEG", quality=92)
    print("Generated siteplan-bp.jpg DWG G-101")

if __name__ == "__main__":
    make_floorplan()
    make_elevation()
    make_container_detail()
    make_kitchen_drainage()
    make_fire_safety()
    make_tc_testing()
    make_siteplan()
