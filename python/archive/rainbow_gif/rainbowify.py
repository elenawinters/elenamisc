from PIL import Image, ImageDraw
from pathlib import Path
import numpy as np

print(Path(Path(__file__).parent.resolve(), 'Elfdroid_Full_Crop.png'))

tile_number = 1
im = Image.open(Path(Path(__file__).parent.resolve(), 'Elfdroid_Full_Crop.png'))

cols = [
    (255, 0 , 0),   # Red
    (255, 127, 0),  # Orange
    (255, 255, 0),  # Yellow
    (0, 255, 0),    # Green
    (0, 255, 255),  # Cyan
    (0, 0, 255),    # Blue
    (127, 0, 255),  # Purple
    (255, 0, 0),    # Red again for seamless wrap
]

def interpolate(f_co, t_co, interval):
    det_co = [(t - f) / interval for f, t in zip(f_co, t_co)]
    for i in range(interval):
        yield [round(f + det * i) for f, det in zip(f_co, det_co)]

def make_gradient(size, cols, offset_px=0, tiles=2):
    width, height = size
    tile_width = width // tiles
    n_segments = len(cols) - 1

    # Generate one seamless tile
    color_list = []
    for s in range(n_segments):
        seg_len = (tile_width + n_segments - 1) // n_segments
        if s == n_segments - 1:
            seg_len = tile_width - len(color_list)
        for color in interpolate(cols[s], cols[s + 1], seg_len):
            color_list.append(color)
    color_list = color_list[:tile_width]

    # Repeat the tile to fill the width
    full_color_list = (color_list * (width // tile_width + 1))[:width]

    # Offset the gradient
    full_color_list = np.roll(full_color_list, offset_px, axis=0)

    gradient = Image.new('RGBA', size, color=0)
    draw = ImageDraw.Draw(gradient)
    # for x, color in enumerate(full_color_list):
    #     draw.line([(x, 0), (x, height)], tuple(color) + (128,), width=1)
    for x, color in enumerate(full_color_list):
        draw.line([(x, 0), (x, height)], tuple(color) + (64,), width=1)
    return gradient

frames = []
n_frames = im.width  # One frame per pixel shift for smoothness
step = 8  # Move 2 pixels per frame for faster animation

import numpy as np

def add_noise_to_gradient(gradient, amount=16):
    arr = np.array(gradient)
    noise = np.random.randint(-amount, amount+1, arr.shape, dtype=np.int16)
    arr = np.clip(arr.astype(np.int16) + noise, 0, 255).astype(np.uint8)
    return Image.fromarray(arr, mode='RGBA')

# In your animation loop:
for offset in range(0, n_frames, step):
    gradient = make_gradient(im.size, cols, offset_px=offset, tiles=tile_number)
    gradient = add_noise_to_gradient(gradient, amount=8)  # Add subtle noise
    # Make sure your gradient alpha is lower, e.g., 64 instead of 128

    frame = Image.alpha_composite(im.convert('RGBA'), gradient)
    # frame = Image.blend(im.convert('RGBA'), gradient, 0.5)
    frames.append(frame.convert('P', palette=Image.ADAPTIVE, dither=Image.FLOYDSTEINBERG))

# Save as GIF
frames[0].save(
    "rainbow_animated.gif",
    save_all=True,
    append_images=frames[1:],
    duration=15,  # ms per frame (faster)
    loop=0,
    optimize=True,
    disposal=2
)
print("Saved as rainbow_animated.gif")

# frames[0].convert('RGBA').save("rainbow_static.png")
# print("Saved as rainbow_static.png")