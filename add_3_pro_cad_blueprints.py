import os
from PIL import Image, ImageDraw, ImageFont

W, H = 2560, 1440

BG_COLOR = (11, 22, 34)
GRID_COLOR = (24, 42, 62)
BORDER_COLOR = (70, 130, 180)
BORDER_INNER = (35, 75, 115)
DIM_COLOR = (56, 189, 248)
WALL_COLOR = (255, 255, 255)
STEEL_COLOR = (249, 115, 22)
TEXT_MAIN = (241, 245, 249)
TEXT_GOLD = (234, 179, 8)
NOTE_BG = (18, 35, 58)

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
    
    for x in range(0, W, 50):
        d.line([(x, 0), (x, H)], fill=GRID_COLOR, width=1)
    for y in range(0, H, 50):
        d.line([(0, y), (W, y)], fill=GRID_COLOR, width=1)
        
    d.rectangle([(40, 40), (W - 40, H - 40)], outline=BORDER_COLOR, width=3)
    d.rectangle([(46, 46), (W - 46, H - 46)], outline=BORDER_INNER, width=1)
    
    tb_left, tb_top = W - 850, H - 220
    d.rectangle([(tb_left, tb_top), (W - 50, H - 50)], fill=(15, 32, 52), outline=DIM_COLOR, width=2)
    d.line([(tb_left, tb_top + 50), (W - 50, tb_top + 50)], fill=DIM_COLOR, width=1)
    d.line([(tb_left, tb_top + 105), (W - 50, tb_top + 105)], fill=DIM_COLOR, width=1)
    d.line([(tb_left + 540, tb_top), (tb_left + 540, H - 50)], fill=DIM_COLOR, width=1)
    
    d.text((tb_left + 15, tb_top + 12), "PROJECT: LOT 7836 KLUANG SINGLE-STOREY RESIDENTIAL", font=f_small, fill=TEXT_MAIN)
    d.text((tb_left + 555, tb_top + 12), f"DWG NO: {dwg_no}", font=f_small, fill=TEXT_GOLD)
    
    d.text((tb_left + 15, tb_top + 65), f"TITLE: {title_zh}", font=f_body, fill=DIM_COLOR)
    d.text((tb_left + 555, tb_top + 65), "SCALE: 1:20 / 1:50", font=f_small, fill=TEXT_MAIN)
    
    d.text((tb_left + 15, tb_top + 120), "STAGE: STATUTORY ARCHITECTURAL & MEP DETAIL PACK", font=f_small, fill=TEXT_MAIN)
    d.text((tb_left + 555, tb_top + 120), "REV: DET-01", font=f_small, fill=(74, 222, 128))

    d.rectangle([(50, 50), (W - 880, 125)], fill=(18, 40, 68), outline=DIM_COLOR, width=1)
    d.text((70, 62), f"2D 单层住宅专项大样图 | {title_zh}", font=f_title, fill=TEXT_MAIN)
    d.text((70, 98), f"类别代号: {category_code} | 规范: 50'x75' 地块 | 模组化单层独栋 | 毫米级节点与选型控制", font=f_dim, fill=DIM_COLOR)
    
    d.rectangle([(50, H - 260), (W - 880, H - 50)], fill=NOTE_BG, outline=DIM_COLOR, width=2)
    d.text((70, H - 245), "💡 施工方 & 工程师读图指引 (Layman & Engineering Guide):", font=f_body, fill=TEXT_GOLD)
    d.text((70, H - 222), "⚠️ 免责声明: 本图为单层热带住宅专项工程大样图。所有构件加固与管路走向须由注册专业工程师(P.Eng)复核。", font=f_dim, fill=(248, 113, 113))
    
    lines = desc_zh.split("\n")
    y_off = H - 192
    for line in lines:
        d.text((70, y_off), line, font=f_small, fill=TEXT_MAIN)
        y_off += 23
        
    return img, d

# 10. DWG D-101: Batu Angin Breeze Block Foyer Masonry Detail
def make_breeze_block_detail():
    img, d = draw_cad_base(
        "Batu Angin 通风花砖屏风门廊砌筑与抗震拉结大样图 (Breeze Block Detail)",
        "DWG D-101",
        "1. 构件规格：200×200×100mm 赤陶与纯白防裂陶土水泥通风花砖，孔隙透光率 42%。\n"
        "2. 抗震拉结：每隔 600mm 设 Y10 镀锌竖向钢筋贯穿灌浆，顶部与 100mm 方钢梁焊接锚固。\n"
        "3. 防热遮阳：52° 正午太阳直射角全遮挡，阻断西晒热辐射，形成 3-5°C 自然降温微气候。",
        "DETAIL & MASONRY / D"
    )
    ox, oy = 400, 160
    d.rectangle([(ox, oy), (ox + 1250, oy + 680)], outline=WALL_COLOR, width=3)
    
    # Diagram 1: Elevation Block Grid
    d.rectangle([(ox + 60, oy + 60), (ox + 560, oy + 620)], fill=(35, 25, 20), outline=STEEL_COLOR, width=2)
    d.text((ox + 80, oy + 80), "🧱 200x200mm 花砖屏风正立面排布", font=f_body, fill=TEXT_GOLD)
    for bx in range(ox + 80, ox + 540, 45):
        for by in range(oy + 130, oy + 580, 45):
            d.rectangle([(bx, by), (bx + 35, by + 35)], outline=(217, 119, 6), width=1)
            d.ellipse([(bx + 8, by + 8), (bx + 27, by + 27)], outline=(251, 191, 36), width=1)
            
    # Diagram 2: Structural Tie Section
    d.rectangle([(ox + 620, oy + 60), (ox + 1190, oy + 620)], fill=(20, 40, 60), outline=DIM_COLOR, width=2)
    d.text((ox + 640, oy + 80), "⚙️ Y10 竖向钢筋拉结与方钢梁锚固剖面", font=f_body, fill=DIM_COLOR)
    d.text((ox + 640, oy + 130), 
           "1. 顶部 100x100mm 镀锌方钢挑梁 (RHS Steel Beam)\n"
           "2. Y10 镀锌竖向拉结钢筋 (每隔 600mm 贯穿花砖孔)\n"
           "3. Grade 25 细石微膨胀混凝土灌浆 (Non-shrink Grout)\n"
           "4. 底部 100mm 防水反坎 (Plinth Kerb) 预埋化学锚栓\n"
           "5. 水泥砂浆 1:3 配合 Sika-1 防水添加剂抹缝\n"
           "6. 防热效能：阻挡 85% 直射太阳强光辐射热", font=f_small, fill=TEXT_MAIN)
           
    img.save("assets/breeze_block_detail_blueprint.jpg", "JPEG", quality=93)
    print("Generated breeze_block_detail_blueprint.jpg DWG D-101")

# 11. DWG K-101: Kitchen Millwork & Grease Trap Plumbing Detail
def make_kitchen_millwork():
    img, d = draw_cad_base(
        "干湿双厨房全套橱柜排布与 50L 隔油池节点详图 (Kitchen Millwork & GT)",
        "DWG K-101",
        "1. 开放干厨房：12ft (3.6m) 白色石英石台面岛台 + 早餐吧台 + 咖啡电器柜 + 净水器点位。\n"
        "2. 封闭湿厨房：16ft (4.8m) 304 不锈钢耐磨台面 + 双水槽 + 300x600mm 全高防油釉面砖 + 后门。\n"
        "3. 油水分离：水槽下方设 50L 不锈钢隔油池 (GT)，DN75 灰水管独立接驳室外侧向排水渠。",
        "KITCHEN & PLUMBING / K"
    )
    ox, oy = 400, 160
    d.rectangle([(ox, oy), (ox + 1250, oy + 680)], outline=WALL_COLOR, width=3)
    
    # Dry Kitchen Section
    d.rectangle([(ox + 60, oy + 60), (ox + 560, oy + 620)], fill=(20, 50, 40), outline=(74, 222, 128), width=2)
    d.text((ox + 80, oy + 80), "🍸 12ft 开放式干厨房与吧台 (Dry Kitchen)", font=f_body, fill=(74, 222, 128))
    d.text((ox + 80, oy + 130), 
           "• 20mm 厚无孔抗菌石英石台面 (Quartz Countertop)\n"
           "• 850mm 人体工学操作高度，预留咖啡机/微波炉位\n"
           "• 台下盆不锈钢单水槽 + 3M 净水器专用龙头\n"
           "• 吧台下方集成 4 组 13A 五孔带开关插座\n"
           "• 抛光水磨石地面平接，与中央客厅视觉连通", font=f_small, fill=TEXT_MAIN)
           
    # Wet Kitchen Section
    d.rectangle([(ox + 620, oy + 60), (ox + 1190, oy + 620)], fill=(50, 30, 20), outline=TEXT_GOLD, width=2)
    d.text((ox + 640, oy + 80), "🍳 16ft 封闭式重油烟湿厨房 (Wet Kitchen)", font=f_body, fill=TEXT_GOLD)
    d.text((ox + 640, oy + 130), 
           "• 1.2mm 304 食品级拉丝不锈钢台面 (耐高温防油污)\n"
           "• 1200 m³/h 强力吸油烟机 + DN150 不锈钢排烟风管\n"
           "• 炉灶四周全高 300x600mm 亮光釉面瓷砖铺贴\n"
           "• 水槽下方设 50L 304 不锈钢隔油池 (GT) 沉箱位\n"
           "• 地坪下沉 20mm 设防臭地漏，支持高压水枪擦洗\n"
           "• 直通 10ft 后服务院落，方便食材搬运与垃圾清运", font=f_small, fill=TEXT_MAIN)
           
    img.save("assets/kitchen_millwork_blueprint.jpg", "JPEG", quality=93)
    print("Generated kitchen_millwork_blueprint.jpg DWG K-101")

# 12. DWG M-102: HVAC Air-Conditioning & Pre-Embedded Condensate Drain Scheme
def make_hvac_aircon():
    img, d = draw_cad_base(
        "全屋空调冷媒管路、预埋保温冷凝水暗管与室外机位图 (HVAC Layout)",
        "DWG M-102",
        "1. 冷量配置：中央客餐厅 2.5HP (变频) + 主卧 1.5HP + 次卧2 1.0HP + 次卧3 1.0HP (全屋总计 6.0HP)。\n"
        "2. 冷凝水防漏：预埋 25mm PVC 加厚管，外覆 9mm 闭孔橡塑保温，按 1:50 顺水坡度直通外沟。\n"
        "3. 室外机机位：4 台室外机集中落座于右侧 5ft 服务退缩区减震地台，远离卧室窗户降噪。",
        "HVAC & MECHANICAL / M"
    )
    ox, oy = 400, 160
    d.rectangle([(ox, oy), (ox + 1250, oy + 680)], outline=WALL_COLOR, width=3)
    
    # Left Zone
    d.rectangle([(ox + 60, oy + 60), (ox + 560, oy + 620)], fill=(20, 35, 65), outline=DIM_COLOR, width=2)
    d.text((ox + 80, oy + 80), "❄️ 全屋 4 处空调室内机与冷量分布", font=f_body, fill=DIM_COLOR)
    d.text((ox + 80, oy + 130), 
           "1. AC-1: 24ft 客餐厅 2.5HP Inverter (24,000 BTU)\n"
           "2. AC-2: 主卧套房 1.5HP Inverter (12,000 BTU)\n"
           "3. AC-3: 次卧 2 (前段) 1.0HP Inverter (9,000 BTU)\n"
           "4. AC-4: 次卧 3 (后段) 1.0HP Inverter (9,000 BTU)\n"
           "• 选用 5 星级节能能效，日均运行电费节省 35%\n"
           "• 室内静音运行声压级 < 22dB(A) 图书馆级静音", font=f_small, fill=TEXT_MAIN)
           
    # Right Zone
    d.rectangle([(ox + 620, oy + 60), (ox + 1190, oy + 620)], fill=(30, 50, 40), outline=(74, 222, 128), width=2)
    d.text((ox + 640, oy + 80), "💧 25mm PVC 保温冷凝管与室外机安装", font=f_body, fill=(74, 222, 128))
    d.text((ox + 640, oy + 130), 
           "• 25mm PVC 加厚给水管，暗敷在 50mm PU 墙体内部\n"
           "• 全程包裹 9mm Armaflex 橡塑保温管，绝不结露\n"
           "• 保证最小 1:50 (2%) 顺水坡度，零存水防霉斑\n"
           "• 冷凝水独立排入室外散水沟，严禁接入排污立管\n"
           "• 室外机落座于 100mm 混凝土减震基座上\n"
           "• 预留冷媒铜管检修阀门与独立电源隔离开关 (Isolator)", font=f_small, fill=TEXT_MAIN)
           
    img.save("assets/hvac_aircon_blueprint.jpg", "JPEG", quality=93)
    print("Generated hvac_aircon_blueprint.jpg DWG M-102")

if __name__ == "__main__":
    make_breeze_block_detail()
    make_kitchen_millwork()
    make_hvac_aircon()
