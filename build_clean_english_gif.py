import os
from PIL import Image, ImageDraw, ImageFont

# Source clean images for 8-phase single-storey construction sequence (100% Pure International English)
frame_sources = [
    (
        "assets/siteplan-bp.jpg",
        "PHASE 01 / 08 : 50'x75' LOT PREPARATION & 150mm REINFORCED SLAB",
        "MS 828 Soil Anti-Termite Treatment & 0.2mm HDPE Moisture Barrier"
    ),
    (
        "assets/iso-3d.jpg",
        "PHASE 02 / 08 : 25T CRANE HOISTING TWIN 40ft HIGH CUBE CONTAINERS",
        "Modular High Cube containers placed onto 100mm reinforced concrete plinth kerbs"
    ),
    (
        "assets/container_splicing_blueprint.jpg",
        "PHASE 03 / 08 : WALL CUT-OUTS & 100x100mm RHS STEEL FRAME WELDING",
        "Perimeter structural reinforcement with M20 chemical anchor bolts (45kN tension)"
    ),
    (
        "assets/side-facade.jpg",
        "PHASE 04 / 08 : 20'x15' COVERED 2-CAR PORCH & 300mm U-DRAIN NETWORK",
        "Integrated front setback 2-car porch canopy & perimeter storm drainage channel"
    ),
    (
        "assets/elevation-bp.jpg",
        "PHASE 05 / 08 : 22° TROPICAL PITCHED ROOF & 1.2m DEEP EAVE OVERHANG",
        "50mm PU insulated standing seam roof & 250x150mm Colorbond rainwater gutters"
    ),
    (
        "assets/style2-ext.jpg",
        "PHASE 06 / 08 : BATU ANGIN BREEZE BLOCK RESORT FOYER SCREEN",
        "Double-skin passive thermal barrier reducing indoor temperature by 3-5°C"
    ),
    (
        "assets/style2-int.jpg",
        "PHASE 07 / 08 : 24ft OPEN-PLAN LIVING HALL & DRY/WET KITCHEN SUITE",
        "3.8m vaulted timber truss ceiling, 50L grease trap & DN100 blackwater plumbing"
    ),
    (
        "assets/birds-eye.jpg",
        "PHASE 08 / 08 : COMPLETED 2,300 sqft SINGLE-STOREY BUNGALOW (CCC)",
        "5 mandatory T&C testing certifications, BOMBA approval & turnkey key handover"
    )
]

font_path = "/System/Library/Fonts/STHeiti Light.ttc"
try:
    font_en_title = ImageFont.truetype(font_path, 22)
    font_en_sub = ImageFont.truetype(font_path, 15)
    font_brand = ImageFont.truetype(font_path, 12)
except Exception:
    font_en_title = font_en_sub = font_brand = ImageFont.load_default()

gif_frames = []
W, H = 1280, 720

for idx, (src, en_title, en_sub) in enumerate(frame_sources):
    if os.path.exists(src):
        with Image.open(src) as img:
            img_c = img.convert("RGB")
            img_resized = img_c.resize((W, H), Image.Resampling.LANCZOS)
            d = ImageDraw.Draw(img_resized)
            
            # 1. Sleek Top Engineering Header Banner (Dark Slate Blue + Cyan Accent)
            d.rectangle([(0, 0), (W, 80)], fill=(15, 23, 42))
            d.line([(0, 80), (W, 80)], fill=(56, 189, 248), width=3)
            
            # Project ID Tag (Top Right)
            d.rectangle([(W - 260, 14), (W - 20, 42)], fill=(30, 41, 59), outline=(56, 189, 248), width=1)
            d.text((W - 248, 20), "LOT 7836 · KLUANG DEVELOPMENT", font=font_brand, fill=(56, 189, 248))
            
            # Pure English Main Phase Title
            d.text((24, 14), f"🏗️ {en_title}", font=font_en_title, fill=(255, 255, 255))
            
            # Pure English Engineering Subtitle
            d.text((24, 48), f"⚙️ Spec: {en_sub}", font=font_en_sub, fill=(148, 163, 184))
            
            # 2. Bottom Progress Bar
            d.rectangle([(0, H - 8), (W, H)], fill=(30, 41, 59))
            p_w = int(W * ((idx + 1) / len(frame_sources)))
            d.rectangle([(0, H - 8), (p_w, H)], fill=(74, 222, 128))
            
            # Bottom Corner Stage Indicator
            d.rectangle([(W - 120, H - 34), (W - 16, H - 12)], fill=(15, 23, 42), outline=(74, 222, 128), width=1)
            d.text((W - 108, H - 30), f"STAGE {idx + 1} OF 8", font=font_brand, fill=(74, 222, 128))
            
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
        duration=1600, # 1.6 seconds per frame
        loop=0
    )
    print(f"Successfully generated 100% pure English single-storey construction GIF with {len(gif_frames)} frames!")
