# https://github.com/python-pillow/Pillow/discussions/6276
# https://gist.github.com/weihanglo/1e754ec47fdd683a42fdf6a272904535
# https://stackoverflow.com/a/69406586

# Left to right gradient
# Left = red, Right = Purple
# Opacity = 0.5
# Red, Orange, Yellow, Green, Cyan, Blue, Purple

from PIL import Image, ImageDraw
from pathlib import Path
import numpy as np
import os
import math

print(Path(Path(__file__).parent.resolve(), 'Elfdroid_Full_Crop.png'))

tile_number = 2

im = Image.open(Path(Path(__file__).parent.resolve(), 'Elfdroid_Full_Crop.png'))

cols = [
    (255, 0 , 0),   # Red
    (255, 127, 0), # Orange
    (255, 255, 0), # Yellow
    (0, 255, 0),   # Green
    (0, 255, 255), # Cyan
    (0, 0, 255),   # Blue
    (127, 0, 255),  # Purpl
    (255, 0, 0),    # Red again for seamless wrape
]

# im = Image.open('/Elfdroid_Full_Crop.png')

def interpolate(f_co, t_co, interval):
    det_co =[(t - f) / interval for f , t in zip(f_co, t_co)]
    for i in range(interval):
        yield [round(f + det * i) for f, det in zip(f_co, det_co)]

gradient = Image.new('RGBA', im.size, color=0)
draw = ImageDraw.Draw(gradient)

def draw_tiled_gradient(draw, size, cols, offset_px=0):
    width, height = size
    n_segments = len(cols) - 1

    # Generate the seamless gradient for the whole width
    color_list = []
    for s in range(n_segments):
        seg_len = (width + n_segments - 1) // n_segments
        if s == n_segments - 1:
            seg_len = width - len(color_list)
        for color in interpolate(cols[s], cols[s + 1], seg_len):
            color_list.append(color)
    color_list = color_list[:width]

    # Offset (roll) the gradient so purple is at the right edge
    # Find the index where color is closest to purple
    purple = np.array([127, 0, 255])
    arr = np.array(color_list)
    dists = np.linalg.norm(arr - purple, axis=1)
    idx_purple = np.argmin(dists)
    # Offset so that purple is at the last pixel
    offset = width - 1 - idx_purple
    color_list = np.roll(color_list, offset, axis=0)

    for x, color in enumerate(color_list):
        draw.line([(x, 0), (x, height)], tuple(color) + (128,), width=1)



draw_tiled_gradient(draw, im.size, cols, 100)
gradient = gradient.crop((0, 0, im.width, im.height))

im_composite = Image.blend(im, gradient, 0.5)
im_composite.show()

# draw

# cols = [
#     (255, 0 , 0),   # Red
#     (255, 127, 0), # Orange
#     (255, 255, 0), # Yellow
#     (0, 255, 0),   # Green
#     (0, 255, 255), # Cyan
#     (0, 0, 255),   # Blue
#     (127, 0, 255)  # Purple
# ]
# f_co = (13, 255, 154)
# t_co = (4, 128, 30)
# for i, color in enumerate(interpolate(cols[0], cols[1], round(im.width / len(cols)))):
#     draw.line([(i, 0), (0, i)], tuple(color), width=1)

# im_composite = Image.blend(im, gradient, 0.5)
# im_composite.show()

# with open('./img_result.png', 'wb') as f:
#     im_composite.save(f)