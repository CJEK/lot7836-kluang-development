import shutil
import os
from PIL import Image

mapping = {
    # Style 2 (Main Focus)
    "assets/style2-ext.jpg": "/Users/cjmac2024/.gemini/antigravity/brain/d31ed8e3-4bdf-43c9-ba9e-4a9cb6b351c6/style2_single_front_1786874206654.jpg",
    "assets/style2-side.jpg": "/Users/cjmac2024/.gemini/antigravity/brain/d31ed8e3-4bdf-43c9-ba9e-4a9cb6b351c6/style2_single_side_1786874222024.jpg",
    "assets/style2-rear.jpg": "/Users/cjmac2024/.gemini/antigravity/brain/d31ed8e3-4bdf-43c9-ba9e-4a9cb6b351c6/style2_single_rear_1786874627239.jpg",
    "assets/style2-int.jpg": "/Users/cjmac2024/.gemini/antigravity/brain/d31ed8e3-4bdf-43c9-ba9e-4a9cb6b351c6/style2_single_int_1786874741980.jpg",

    # Style 1 (Terracotta)
    "assets/style1-ext.jpg": "/Users/cjmac2024/.gemini/antigravity/brain/d31ed8e3-4bdf-43c9-ba9e-4a9cb6b351c6/style1_single_front_1786874999500.jpg",
    "assets/style1-side.jpg": "/Users/cjmac2024/.gemini/antigravity/brain/d31ed8e3-4bdf-43c9-ba9e-4a9cb6b351c6/style1_single_side_1786875593181.jpg",
    "assets/style1-rear.jpg": "/Users/cjmac2024/.gemini/antigravity/brain/d31ed8e3-4bdf-43c9-ba9e-4a9cb6b351c6/style1_single_rear_1786875662885.jpg",
    "assets/style1-int.jpg": "/Users/cjmac2024/.gemini/antigravity/brain/d31ed8e3-4bdf-43c9-ba9e-4a9cb6b351c6/style1_single_int_1786875907443.jpg",

    # Style 3 (Pure White)
    "assets/style3-ext.jpg": "/Users/cjmac2024/.gemini/antigravity/brain/d31ed8e3-4bdf-43c9-ba9e-4a9cb6b351c6/style3_single_front_1786875978512.jpg",
    "assets/style3-side.jpg": "/Users/cjmac2024/.gemini/antigravity/brain/d31ed8e3-4bdf-43c9-ba9e-4a9cb6b351c6/style3_single_side_1786876110552.jpg",
    "assets/style3-rear.jpg": "/Users/cjmac2024/.gemini/antigravity/brain/d31ed8e3-4bdf-43c9-ba9e-4a9cb6b351c6/style3_single_rear_1786876182570.jpg",
    "assets/style3-int.jpg": "/Users/cjmac2024/.gemini/antigravity/brain/d31ed8e3-4bdf-43c9-ba9e-4a9cb6b351c6/style3_single_int_1786876234161.jpg",

    # Overall Viewports
    "assets/iso-3d.jpg": "/Users/cjmac2024/.gemini/antigravity/brain/d31ed8e3-4bdf-43c9-ba9e-4a9cb6b351c6/iso_single_3d_1786876253856.jpg",
    "assets/side-facade.jpg": "/Users/cjmac2024/.gemini/antigravity/brain/d31ed8e3-4bdf-43c9-ba9e-4a9cb6b351c6/style2_single_side_1786874222024.jpg",
    "assets/birds-eye.jpg": "/Users/cjmac2024/.gemini/antigravity/brain/d31ed8e3-4bdf-43c9-ba9e-4a9cb6b351c6/iso_single_3d_1786876253856.jpg"
}

os.makedirs("assets", exist_ok=True)

for dst, src in mapping.items():
    if os.path.exists(src):
        with Image.open(src) as img:
            # Save optimized JPEG
            img.convert("RGB").save(dst, "JPEG", quality=92, optimize=True)
            print(f"Copied and optimized {src} -> {dst}")
    else:
        print(f"Error: {src} not found!")

print("All 3D single-storey renders updated successfully!")
