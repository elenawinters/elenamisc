"""
    THIS SCRIPT USES PYTHON 3.9
    -----------------------------------
    BEFORE RELEASE ON GITHUB

    COMMAND LINE THIS SHIT

    TODO: COPY CODE FROM OTHER FILES RELATING TO START TESTS



    lol this is broken

"""

from PIL import Image
import os

image_folder = 'C:\\Users\\wesle\\OneDrive\\Pictures\\Profile Pictures\\Emotes\\zaquelle'
image_file = 'zaqAwwClap.gif'
expansion = 3

im = Image.open(os.path.join(image_folder, image_file))
# gif_dur = im.info['duration']
width, height = im.size
width, height = 56, 56
# palette = None

# _ifr = im.resize((width * expansion, height))
# offset = width
# for x in range(expansion):
#     print(x)
#     _icr = _ifr.crop((offset * x, 0, 128 * (x + 1), 128))
#     _icr.save(os.path.join(image_folder, 'zaqRavies', f'out{x}.png'), **_icr.info)


# https://stackoverflow.com/a/4905209/14125122
def iter_frames():
    # global palette
    try:
        i = 0
        while 1:
            im.seek(i)
            imframe = im.copy()
            if i == 0:
                palette = imframe.getpalette()
            else:
                imframe.putpalette(palette)
            yield imframe
            i += 1
    except EOFError:
        pass


def split_image(_im, _limit):
    """
        _start INDEXES AT 0 FIRST.
    """
    for x in range(_limit):
        yield _im.crop((width * x, 0, width * (x + 1), height))


# def selection_crop(im):
#     pass

"""
    DICT LAYOUT FOR IMAGE DATA TO RECONSTRUCT
    "NEW_GIF_NUMBER": {
        "GIF_FRAME": Image
    }

"""


_idata = {}


for i, frame in enumerate(iter_frames()):
    fwide = frame.resize((width * expansion, height))
    for x, split in enumerate(split_image(fwide, expansion)):
        _idata[(x, i)] = split
        # _idata[(x, i)] = split.convert('P')

        # split.save(os.path.join(image_folder, 'test', f'o{x}-{i}.png'), **split.info)


for index in range(expansion):
    img, *imgs = [_idata[i] for i in _idata if i[0] == index]
    img.save(fp=os.path.join(image_folder, image_file.split('.')[0], f"{index}.{image_file.split('.')[1]}"),
             append_images=imgs, save_all=True, loop=0, **im.info, palette=im.getpalette(), disposal=2)
