from PIL import Image, ImageEnhance
from matplotlib import pyplot
import numpy
import cv2

# https://stackoverflow.com/a/6496793
# https://stackoverflow.com/a/2563883
if __name__ == '__main__':
    img = Image.open(r"C:\Users\elena\OneDrive\Pictures\untitled-f1141477.png")
    
    skip_pixels = 22
    done_initial = False

    index = skip_pixels / 2
    print(index)
    pos = (0, index, 1080, index + 7)

    crop = img.crop((0, index, 1080, index + 7))
    test = ImageEnhance.Brightness(crop).enhance(1.1)
    test.paste(img, (int(index), 0))

    # img.show()

    
    pyplot.imshow(img)
    pyplot.show()