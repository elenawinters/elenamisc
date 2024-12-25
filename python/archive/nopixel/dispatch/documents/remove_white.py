from pathlib import Path
from PIL import Image
import glob
import csv
import os
import re

os.chdir(Path(Path(__file__).parent))

print(Path(__file__).parent)

# output_folder = Path.joinpath(Path(__file__).parent, 'output')
glist = glob.glob('output/*.png')
print(glist)
print(len(glist))

tolerance = 200

for fimg in glist:
    print(Path(fimg).name)
    img = Image.open(fimg).convert("RGBA")




    



    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    img.putdata(newData)
    img.save(Path.joinpath(Path('output/transparent'), Path(fimg).name), "PNG")

# img = Image.open('img.png')
# img = img.convert("RGBA")
# datas = img.getdata()

# newData = []
# for item in datas:
#     if item[0] == 255 and item[1] == 255 and item[2] == 255:
#         newData.append((255, 255, 255, 0))
#     else:
#         newData.append(item)

# img.putdata(newData)
# img.save("img2.png", "PNG")