from PIL import Image
from pprint import pprint as pp
from random import random
from os.path import exists

# test shuffle
DEBUG = False

# img folder
DIR_INPUT = './traits'
DIR_OUTPUT = './assets'

# trait config
LAYER_0 = [
    ("pattern_none.png", 1.0),
    ("pattern_half.png", 1.0),
    ("pattern_full.png", 1.0),
]
LAYER_1 = [
    ("eyes_none.png",    1.0),
    ("eyes_cross.png",   1.0),
    ("eyes_star.png",    1.0),
]
LAYER_2 = [
    ("blank.png",        1.0),
    ("hat_mini_hat.png", 1.0),
    ("hat_crown.png",    1.0),
]
LAYER_3 = [
    ("blank.png",        1.0),
    ("right_pawn.png",   1.0),
    ("right_candy.png",  1.0),
]

# save image
def craft(out, l0, l1, l2, l3):
    outpath = "{}/{}".format(DIR_OUTPUT, out)
    print('crafting...', outpath)
    if DEBUG: return

    # skip existing file
    if exists(outpath):
        return

    layers = [
        Image.open("{}/{}".format(DIR_INPUT, l0)),
        Image.open("{}/{}".format(DIR_INPUT, l1)),
        Image.open("{}/{}".format(DIR_INPUT, l2)),
        Image.open("{}/{}".format(DIR_INPUT, l3)),
    ]
    new_img = Image.new("RGBA", layers[0].size)

    for layer in layers:
        #new_img.paste(layer, (0, 0), layer.convert('RGBA')) --- not good border
        #new_img.paste(layer, (0, 0), layer.convert('RGBa')) --- overlay bug
        new_img = Image.alpha_composite(new_img, layer)    # --- perfect!
    new_img.save(outpath, "PNG")

# loop
for i0, l0 in enumerate(LAYER_0):
    for i1, l1 in enumerate(LAYER_1):
        for i2, l2 in enumerate(LAYER_2):
            for i3, l3 in enumerate(LAYER_3):

                # skip from rarity
                r = random()
                if r > l0[1]: continue
                if r > l1[1]: continue
                if r > l2[1]: continue
                if r > l3[1]: continue

                # craft image
                out = "{}{}{}{}.png".format(i0, i1, i2, i3)
                craft(out, l0[0], l1[0], l2[0], l3[0])
