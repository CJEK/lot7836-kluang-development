import os
from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1920, 1080
BG_COLOR = (10, 25, 47)       # Deep blueprint navy blue
GRID_COLOR = (20, 45, 80)     # Subtle grid lines
TEXT_WHITE = (240, 246, 252)
TEXT_CYAN = (56, 189, 248)
TEXT_YELLOW = (250, 204, 21)
TEXT_RED = (248, 113, 113)
TEXT_GREEN = (74, 222, 128)
LINE_WHITE = (200, 220, 240)
LINE_CYAN = (14, 165, 233)
LINE_YELLOW = (234, 179, 8)
LINE_RED = (239, 68, 68)
LINE_GREEN = (34, 197, 94)

font_path = "/System/Library/Fonts/STHeiti Light.ttc"
try:
    font_title = ImageFont.truetype(font_path, 32)
    font_header = ImageFont.truetype(font_path, 24)
    font_body = ImageFont.truetype(font_path, 18)
    font_sub = ImageFont.truetype(font_path, 14)
except Exception as e:
    print(f"Font load error: {e}")
    font_title = font_header = font_body = font_sub = ImageFont.load_default()

def create_base_blueprint(title, subtitle):
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    for x in range(0, WIDTH, 40):
        draw.line([(x, 0), (x, HEIGHT)], fill=GRID_COLOR, width=1)
    for y in range(0, HEIGHT, 40):
        draw.line([(0, y), (WIDTH, y)], fill=GRID_COLOR, width=1)
        
    draw.rectangle([(40, 30), (WIDTH - 40, 90)], fill=(15, 35, 65), outline=LINE_CYAN, width=2)
    draw.text((60, 42), title, font=font_title, fill=TEXT_CYAN)
    draw.text((WIDTH - 450, 48), subtitle, font=font_body, fill=TEXT_YELLOW)
    
    draw.rectangle([(40, 100), (WIDTH - 40, HEIGHT - 40)], outline=LINE_CYAN, width=2)
    return img, draw

# 1. Kitchen & Drainage Layout Blueprint
def generate_kitchen_drainage():
    img, draw = create_base_blueprint(
        "LOT 7836 厨房与集中排水系统工程图 (Kitchen & Wet-Core Drainage Plan)",
        "SCALE 1:100 | JKR & MPK STANDARD"
    )
    
    box = (350, 140, 1570, 960)
    draw.rectangle(box, outline=TEXT_WHITE, width=3)
    draw.text((360, 150), "50ft FRONTAGE (JALAN PAKIS)", font=font_body, fill=TEXT_CYAN)
    draw.text((1400, 150), "75ft DEPTH", font=font_body, fill=TEXT_CYAN)
    
    c_left = (350, 140, 520, 640)
    draw.rectangle(c_left, outline=TEXT_YELLOW, width=3)
    draw.text((360, 200), "40ft HC CONTAINER (LEFT)", font=font_body, fill=TEXT_YELLOW)
    
    c_right = (1400, 140, 1570, 640)
    draw.rectangle(c_right, outline=TEXT_YELLOW, width=3)
    draw.text((1410, 200), "40ft HC CONTAINER (RIGHT)", font=font_body, fill=TEXT_YELLOW)
    
    draw.text((800, 350), "34ft HIGH-CEILING CENTRAL HALL", font=font_header, fill=TEXT_WHITE)
    
    k_zone = (355, 340, 515, 635)
    draw.rectangle(k_zone, fill=(20, 60, 90), outline=LINE_GREEN, width=2)
    draw.text((365, 350), "🍳 开放式厨房 (Kitchen)", font=font_body, fill=TEXT_GREEN)
    draw.text((365, 380), "- L型不锈钢厨柜台面", font=font_sub, fill=TEXT_WHITE)
    draw.text((365, 400), "- 双槽洗菜盆 (Sink)", font=font_sub, fill=TEXT_WHITE)
    draw.text((365, 420), "- 独立排烟风道出口", font=font_sub, fill=TEXT_WHITE)
    
    draw.rectangle([(230, 580), (330, 640)], fill=(40, 80, 50), outline=LINE_GREEN, width=2)
    draw.text((235, 595), "油脂拦截器\nGrease Trap", font=font_sub, fill=TEXT_GREEN)
    draw.line([(360, 600), (330, 600)], fill=LINE_GREEN, width=4)
    
    w_zone = (1405, 400, 1565, 635)
    draw.rectangle(w_zone, fill=(70, 30, 40), outline=LINE_RED, width=2)
    draw.text((1415, 410), "🚽 双卫生间 (Restrooms)", font=font_body, fill=TEXT_RED)
    draw.text((1415, 440), "- 男/女双独立马桶", font=font_sub, fill=TEXT_WHITE)
    draw.text((1415, 460), "- DN100 污水主管", font=font_sub, fill=TEXT_WHITE)
    
    draw.rectangle([(850, 870), (1070, 940)], fill=(80, 40, 20), outline=LINE_YELLOW, width=2)
    draw.text((860, 890), "8PE 生化化粪池 (Septic Tank)", font=font_body, fill=TEXT_YELLOW)
    
    draw.line([(280, 640), (280, 900), (850, 900)], fill=LINE_GREEN, width=3)
    draw.text((300, 750), "灰水管 ➔", font=font_sub, fill=TEXT_GREEN)
    
    draw.line([(1480, 640), (1480, 900), (1070, 900)], fill=LINE_RED, width=3)
    draw.text((1330, 750), "⬅ 黑水管 DN100", font=font_sub, fill=TEXT_RED)
    
    draw.rectangle([(330, 120), (1590, 975)], outline=LINE_CYAN, width=2)
    draw.text((880, 125), "周圈 300mm U型雨水排水沟 (Perimeter Rainwater U-Drain)", font=font_sub, fill=TEXT_CYAN)

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/kitchen_drainage_blueprint.jpg", "JPEG", quality=92)
    print("Generated kitchen_drainage_blueprint.jpg")

# 2. Fire Safety & Egress Blueprint
def generate_fire_safety():
    img, draw = create_base_blueprint(
        "LOT 7836 BOMBA 消防安全与紧急逃生路线图 (Fire Safety & Egress Plan)",
        "COMPLIANCE WITH MALAYSIAN BOMBA FIRE CODE"
    )
    
    box = (350, 140, 1570, 960)
    draw.rectangle(box, outline=TEXT_WHITE, width=3)
    draw.text((360, 150), "50ft FRONTAGE", font=font_body, fill=TEXT_CYAN)
    
    draw.rectangle([(800, 130), (1120, 150)], fill=(0, 200, 100), outline=LINE_GREEN, width=3)
    draw.text((850, 105), "🟢 主入口逃生门 (MAIN EXIT 1)", font=font_body, fill=TEXT_GREEN)
    
    draw.rectangle([(880, 950), (1040, 970)], fill=(0, 200, 100), outline=LINE_GREEN, width=3)
    draw.text((860, 975), "🟢 后方紧急出口 (EMERGENCY EXIT 2)", font=font_body, fill=TEXT_GREEN)
    
    draw.rectangle([(350, 140), (520, 640)], outline=TEXT_YELLOW, width=2)
    draw.rectangle([(1400, 140), (1570, 640)], outline=TEXT_YELLOW, width=2)
    
    sd_points = [(435, 250), (435, 500), (960, 300), (960, 600), (1485, 250), (1485, 500)]
    for pt in sd_points:
        draw.ellipse([(pt[0]-15, pt[1]-15), (pt[0]+15, pt[1]+15)], fill=(200, 50, 50), outline=TEXT_WHITE, width=2)
        draw.text((pt[0]-10, pt[1]-8), "SD", font=font_sub, fill=TEXT_WHITE)
    draw.text((980, 290), "← 烟雾感应器 Smoke Detector", font=font_sub, fill=TEXT_RED)
    
    fe_points = [(540, 160), (1380, 160), (540, 620), (1380, 620)]
    for pt in fe_points:
        draw.rectangle([(pt[0]-12, pt[1]-12), (pt[0]+12, pt[1]+12)], fill=(220, 30, 30), outline=TEXT_YELLOW, width=2)
        draw.text((pt[0]-8, pt[1]-8), "FE", font=font_sub, fill=TEXT_WHITE)
    draw.text((560, 165), "← 6kg ABC 干粉灭火器", font=font_sub, fill=TEXT_YELLOW)
    
    draw.line([(960, 500), (960, 180)], fill=LINE_GREEN, width=4)
    draw.polygon([(960, 160), (950, 185), (970, 185)], fill=LINE_GREEN)
    
    draw.line([(960, 650), (960, 930)], fill=LINE_GREEN, width=4)
    draw.polygon([(960, 950), (950, 925), (970, 925)], fill=LINE_GREEN)
    
    draw.text((980, 400), "⬆ 安全疏散路线 (Egress Route)", font=font_header, fill=TEXT_GREEN)

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/fire_safety_egress_blueprint.jpg", "JPEG", quality=92)
    print("Generated fire_safety_egress_blueprint.jpg")

# 3. T&C Inspection & Testing Blueprint
def generate_tc_testing():
    img, draw = create_base_blueprint(
        "LOT 7836 5 大工程验收打压测试点位图 (T&C Inspection & Testing Blueprint)",
        "HANDOVER TESTING & COMMISSIONING PROTOCOL"
    )
    
    box = (350, 140, 1570, 960)
    draw.rectangle(box, outline=TEXT_WHITE, width=3)
    
    draw.rectangle([(380, 780), (700, 920)], fill=(20, 50, 90), outline=LINE_CYAN, width=2)
    draw.text((390, 790), "🧪 测试 1：给水管 8 Bar 打压测试", font=font_body, fill=TEXT_CYAN)
    draw.text((390, 820), "- 1.5 倍工作压力保压 2 小时", font=font_sub, fill=TEXT_WHITE)
    draw.text((390, 840), "- 主进水管阀门施压无压降", font=font_sub, fill=TEXT_WHITE)
    
    draw.rectangle([(1200, 450), (1550, 630)], fill=(80, 30, 40), outline=LINE_RED, width=2)
    draw.text((1210, 460), "🧪 测试 2：24小时湿区闭水测试", font=font_body, fill=TEXT_RED)
    draw.text((1210, 490), "- 沉箱注入 100mm 积水 24h", font=font_sub, fill=TEXT_WHITE)
    draw.text((1210, 510), "- 检查底盘与管道周圈零渗漏", font=font_sub, fill=TEXT_WHITE)
    
    draw.rectangle([(750, 160), (1170, 300)], fill=(30, 70, 50), outline=LINE_GREEN, width=2)
    draw.text((760, 170), "🧪 测试 3：4小时高压喷淋防漏水测试", font=font_body, fill=TEXT_GREEN)
    draw.text((760, 200), "- 30° 坡屋顶与拔风塔接缝喷淋", font=font_sub, fill=TEXT_WHITE)
    draw.text((760, 220), "- 天花板与集装箱顶板防漏验收", font=font_sub, fill=TEXT_WHITE)
    
    draw.rectangle([(380, 180), (700, 320)], fill=(80, 70, 20), outline=LINE_YELLOW, width=2)
    draw.text((390, 190), "🧪 测试 4：电气接地与 RCCB 测试", font=font_body, fill=TEXT_YELLOW)
    draw.text((390, 220), "- 30mA 漏电断路器 30ms 切断", font=font_sub, fill=TEXT_WHITE)
    draw.text((390, 240), "- 接地电阻实测小于 10 欧姆", font=font_sub, fill=TEXT_WHITE)
    
    draw.rectangle([(750, 500), (1170, 650)], fill=(50, 40, 80), outline=TEXT_WHITE, width=2)
    draw.text((760, 510), "🧪 测试 5：拔风塔风速与排热测试", font=font_body, fill=TEXT_WHITE)
    draw.text((760, 540), "- 测量室内外热负压对流风速", font=font_sub, fill=TEXT_WHITE)
    draw.text((760, 560), "- 自然拔风降温效率实测", font=font_sub, fill=TEXT_WHITE)

    img.save("/Users/cjmac2024/Documents/antigravity/charming-darwin/assets/tc_testing_blueprint.jpg", "JPEG", quality=92)
    print("Generated tc_testing_blueprint.jpg")

if __name__ == "__main__":
    generate_kitchen_drainage()
    generate_fire_safety()
    generate_tc_testing()
