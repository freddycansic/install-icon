#!/home/freddy/dev/install-icon/bin/python3

import sys

from PIL import Image

if len(sys.argv) < 2:
    print("supply an icon")
    sys.exit(-1)

icon = Image.open(sys.argv[1])

print("loaded icon:", icon.filename)
print("size:", icon.size)

if icon.size[0] < 1024 and icon.size[1] < 1024:
    print("WARNING: given icon will require upscaling")

sizes = [
    1024,
    512,
    256,
    192,
    128,
    96,
    72,
    64, 
    48,
    42, 
    36, 
    32, 
    24, 
    22, 
    16, 
    8
]

icon_name = sys.argv[1].split(".")[:-1]
icon_name = ".".join(icon_name)

for size in sizes:
    icon = icon.resize((size, size), Image.Resampling.LANCZOS)

    save_path = f"/usr/share/icons/hicolor/{size}x{size}/apps/{icon_name}.png"

    icon.save(save_path)

    print(f"saved {size} version at {save_path}")
