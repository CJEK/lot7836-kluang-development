import os
from PIL import Image, ImageDraw, ImageFont

# Source clean images for 8-phase construction sequence
frame_sources = [
    ("assets/siteplan-bp.jpg", "PHASE 01: GROUND SLAB & SITE BOUNDARY (50' x 75' / 150mm SLAB)", "阶段 01: 50x75ft 地块平整与 150mm 加厚地坪浇筑"),
    ("assets/iso-3d.jpg", "PHASE 02: HOISTING TWIN 40ft HIGH CUBE CONTAINERS", "阶段 02: 吊装双 40ft HC 集装箱至地坪锚固点"),
    ("assets/container_splicing_blueprint.jpg", "PHASE 03: CUT-OUT & 100x100mm RHS STEEL FRAME WELDING", "阶段 03: 集装箱侧墙切割开窗与 100mm 方钢框焊接"),
    ("assets/side-facade.jpg", "PHASE 04: BATU ANGIN BREEZE BLOCK & 75ft SIDE DRAINAGE", "阶段 04: 75ft 侧立面与周圈 300mm U 型服务排水沟"),
    ("assets/elevation-bp.jpg", "PHASE 05: 30° PITCHED ROOF & +47ft JACK ROOF MONITOR", "阶段 05: 30° 坡屋顶与 +47ft Raised Jack Roof 拔风塔"),
    ("assets/style2-ext.jpg", "PHASE 06: STYLE 02 RESORT BUNGALOW FRONT FACADE", "阶段 06: 风格 2 马六甲风砖屏风墙外观全景"),
    ("assets/style2-int.jpg", "PHASE 07: INTERIOR SUNLIT ATRIUM & 24ft HIGH CEILING HALL", "阶段 07: 室内 24ft 挑高大厅与日光风砖中庭"),
    ("assets/birds-eye.jpg", "PHASE 08: COMPLETED 2,830 sqft CONTAINER LOFT BUNGALOW", "阶段 08: 2,830 sqft 全案建成交付 (CCC HANDOVER)")
]

font_path = "/System/Library/Fonts/STHeiti Light.ttc"
try:
    font_en = ImageFont.truetype(font_path, 24)
    font_zh = ImageFont.truetype(font_path, 16)
except Exception:
    font_en = font_zh = ImageFont.load_default()

gif_frames = []
W, H = 1280, 720

for src, en_title, zh_title in frame_sources:
    if os.path.exists(src):
        with Image.open(src) as img:
            # Crop/Resize to exact 16:9 1280x720 canvas
            img_c = img.convert("RGB")
            img_resized = img_c.resize((W, H), Image.Resampling.LANCZOS)
            d = ImageDraw.Draw(img_resized)
            
            # Sleek Dark Slate Header Banner
            d.rectangle([(0, 0), (W, 85)], fill=(15, 23, 42))
            d.line([(0, 85), (W, 85)], fill=(56, 189, 248), width=3)
            
            # Pure English Main Header
            d.text((24, 14), f"🏗️ {en_title}", font=font_en, fill=(255, 255, 255))
            
            # Clean Chinese Secondary Subtitle
            d.text((24, 52), f"中文说明: {zh_title}", font=font_zh, fill=(56, 189, 248))
            
            # Bottom Progress Indicator
            i_idx = len(gif_frames)
            d.rectangle([(0, H - 10), (W, H)], fill=(30, 41, 59))
            p_w = int(W * ((i_idx + 1) / len(frame_sources)))
            d.rectangle([(0, H - 10), (p_w, H)], fill=(74, 222, 128))
            
            gif_frames.append(img_resized)
    else:
        print(f"Warning: {src} missing!")

gif_out_path = "assets/style2_container_to_breeze_block_build.gif"
if gif_frames:
    gif_frames[0].save(
        gif_out_path,
        save_all=True,
        append_images=gif_frames[1:],
        optimize=False,
        duration=1500, # 1.5 seconds per frame
        loop=0
    )
    print(f"Successfully generated pure, crisp English construction GIF with {len(gif_frames)} frames!")
