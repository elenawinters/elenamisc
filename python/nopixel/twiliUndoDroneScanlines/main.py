from PIL import Image, ImageEnhance
from matplotlib import pyplot
import numpy
import cv2

# https://stackoverflow.com/a/6496793
# https://stackoverflow.com/a/2563883
if __name__ == '__main__':
    img = Image.open(r"C:\Users\elena\OneDrive\Pictures\untitled-f1141477.png")
    
    index = 11
    skip_pixels = index * 2
    done_initial = False

    while index <= 1080:
        print(index)
        pos = (0, index, 1080, index + 7)

        # img.crop((0, index-1, 1920, index-1))
        # leading = ImageEnhance.Brightness((0, index-1, 1920, index-1)).enhance(1.02)


        leading = ImageEnhance.Brightness(img.crop((0, index-1, 1920, index))).enhance(1.02)
        img.paste(leading, (0, index-1))
        proceeding = ImageEnhance.Brightness(img.crop((0, index+7, 1920, index+8))).enhance(1.02)
        img.paste(proceeding, (0, index+7))
        # img.paste(ImageEnhance.Brightness(img.crop((0, index-1, 1920, index-1))).enhance(20), (0, index-1))
        # img.paste(ImageEnhance.Brightness(img.crop((0, index, 1920, index + 7))).enhance(1.05), (0, index))
        # # img.paste(ImageEnhance.Brightness(img.crop((0, index+7, 1920, index+7))).enhance(1.02), (0, index+7))
        # img.paste(ImageEnhance.Brightness(img.crop((0, index+8, 1920, index+8))).enhance(2), (0, index+8))

        center = ImageEnhance.Brightness(img.crop((0, index, 1920, index + 7))).enhance(1.05)
        img.paste(center, (0, index))

        index += skip_pixels

    # img.show()

    
    pyplot.imshow(img)
    pyplot.show()