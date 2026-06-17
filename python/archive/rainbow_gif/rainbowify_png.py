from PIL import Image, ImageDraw
from pathlib import Path
import numpy as np

# Load base image
input_path = Path(__file__).parent / 'Elfdroid_Full_Crop.png'
im = Image.open(input_path).convert('RGBA')

# Rainbow color stops (seamless wrap)
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

def make_gradient(size, cols, tiles=1, alpha=64, offset_px=0):
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

    # Offset the gradient if needed
    full_color_list = np.roll(full_color_list, offset_px, axis=0)

    gradient = Image.new('RGBA', size, color=0)
    draw = ImageDraw.Draw(gradient)
    for x, color in enumerate(full_color_list):
        draw.line([(x, 0), (x, height)], tuple(color) + (alpha,), width=1)
    return gradient

def add_noise_to_gradient(gradient, amount=8):
    arr = np.array(gradient)
    noise = np.random.randint(-amount, amount+1, arr.shape, dtype=np.int16)
    arr = np.clip(arr.astype(np.int16) + noise, 0, 255).astype(np.uint8)
    return Image.fromarray(arr, mode='RGBA')

# Parameters
tiles = 1           # Number of rainbow repeats across the image
alpha = 64          # Rainbow overlay alpha (0-255)
offset_px = 0       # Horizontal offset of the rainbow
add_noise = True    # Add subtle noise to break up banding

# Create rainbow overlay
gradient = make_gradient(im.size, cols, tiles=tiles, alpha=alpha, offset_px=offset_px)
if add_noise:
    gradient = add_noise_to_gradient(gradient, amount=8)

# Composite and save
result = Image.alpha_composite(im, gradient)
result.save("rainbow_overlay.png")
print("Saved as rainbow_overlay.png")