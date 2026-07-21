import os
from PIL import Image

mapping = {
    "a-101": "assets/floorplan-bp.jpg",
    "a-102": "assets/elevation-bp.jpg",
    "s-101": "assets/container_splicing_blueprint.jpg",
    "m-101": "assets/kitchen_drainage_blueprint.jpg",
    "f-101": "assets/fire_safety_egress_blueprint.jpg",
    "t-101": "assets/tc_testing_blueprint.jpg",
    "g-101": "assets/siteplan-bp.jpg"
}

os.makedirs("assets/drawings", exist_ok=True)

for code, src in mapping.items():
    if os.path.exists(src):
        with Image.open(src) as img:
            # Resize for crisp thumbnail preview (640x360)
            img_resized = img.resize((640, 360), Image.Resampling.LANCZOS)
            out_path = f"assets/drawings/{code}-preview.png"
            img_resized.save(out_path, "PNG", optimize=True)
            print(f"Updated {out_path} from {src}")
    else:
        print(f"Error: {src} does not exist!")
