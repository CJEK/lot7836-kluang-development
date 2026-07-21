import os
from PIL import Image, ImageDraw, ImageFont

gif_path = "assets/style2_container_to_breeze_block_build.gif"
if not os.path.exists(gif_path):
    print("GIF file not found!")
    exit(1)

orig_gif = Image.open(gif_path)
n_frames = orig_gif.n_frames

font_path = "/System/Library/Fonts/STHeiti Light.ttc"
try:
    font_zh = ImageFont.truetype(font_path, 26)
    font_en = ImageFont.truetype(font_path, 20)
    font_sub = ImageFont.truetype(font_path, 16)
except Exception:
    font_zh = font_en = font_sub = ImageFont.load_default()

stages = [
  ("阶段 01: 地块平整与 150mm 加厚地坪浇筑", "STAGE 01: 150mm Reinforced Concrete Ground Slab (FL ±0.00m)"),
  ("阶段 02: 25吨吊车进场定位双 40ft HC 集装箱", "STAGE 02: Hoisting Twin 40ft High Cube Containers via 25T Crane"),
  ("阶段 03: 锚固 M20 化学锚栓与底角件焊接锁定", "STAGE 03: M20 Chemical Anchor Bolts & Corner Casting Lock"),
  ("阶段 04: 集装箱侧墙切割开窗与 100mm 方钢圈加固", "STAGE 04: Cut-outs & 100x100mm RHS Steel Frame Reinforcement"),
  ("阶段 05: 24ft 中央挑高大厅 H-Beam 柱网与屋架安装", "STAGE 05: 24ft High Ceiling Hall H-Beam & Roof Truss Assembly"),
  ("阶段 06: Batu Angin 通风花砖防热屏风墙砌筑", "STAGE 06: Batu Angin Breeze Block Double-Skin Screen Wall"),
  ("阶段 07: 30° 斜屋顶与 Standing Seam 50mm PU 隔热板", "STAGE 07: 30° Roof & Standing Seam 50mm PU Insulation Panel"),
  ("阶段 08: +47ft Raised Jack Roof 拔风天窗封顶", "STAGE 08: +47ft Raised Jack Roof Monitor Passive Cooling Tower"),
  ("阶段 09: 水电管线、50L 隔油池与 8PE 化粪池接驳", "STAGE 09: MEP Piping, 50L Grease Trap & 8PE Septic Connection"),
  ("阶段 10: 完工交付 · 马六甲度假风 Bungalow", "STAGE 10: Final Handover · Malacca Breeze Block Resort Bungalow")
]

new_frames = []

for i in range(n_frames):
    orig_gif.seek(i)
    frame = orig_gif.convert("RGB")
    d = ImageDraw.Draw(frame)
    
    zh_text, en_text = stages[i % len(stages)]
    
    # Top Banner Box (Dark Semi-Transparent Navy)
    d.rectangle([(0, 0), (1280, 85)], fill=(15, 23, 42))
    d.line([(0, 85), (1280, 85)], fill=(56, 189, 248), width=3)
    
    # Text Overlays
    d.text((24, 12), f"🏗️ {zh_text}", font=font_zh, fill=(255, 255, 255))
    d.text((24, 48), f"ENGLISH: {en_text}", font=font_en, fill=(56, 189, 248))
    
    # Bottom Progress Indicator
    d.rectangle([(0, 710), (1280, 720)], fill=(30, 41, 59))
    progress_w = int(1280 * ((i + 1) / n_frames))
    d.rectangle([(0, 710), (progress_w, 720)], fill=(74, 222, 128))
    
    new_frames.append(frame)

# Save high quality GIF
new_frames[0].save(
    gif_path,
    save_all=True,
    append_images=new_frames[1:],
    optimize=False,
    duration=1200, # 1.2s per frame
    loop=0
)

print(f"Successfully generated bilingual GIF with {len(new_frames)} frames!")
