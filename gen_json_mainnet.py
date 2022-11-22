import json, os, glob, random
from datetime import datetime
from pprint import pprint as pp
 
NAME = "Just Meaw 😺"
DESC = "Just Meaw now Rebranded to Just Meaw USD Real world Money used in Meawtaverse Project🌎 You Can Buy Anything 🏡🚕🥬🍷💎🛸🗿🎡🏓🔧 If Anyone Accept Just Meaw USD💰 even L❤️VE 10,000/10,000 No $, Just Meaw UsD"
IMG = "https://diewland.github.io/just-meaw/assets_mainnet/{}.png"
ENGINE = "Jigsaw Engine"

OUTPUT_DIR = "./json_mainnet"
MAX_SUPPLY = 1296
SHUFFLE_TIME = 99

CONFIG = (
    # pattern
    (
        ( "Meaw",       3 ),
        ( "Luna",       2 ),
        ( "Artemis",    1 ),
    ),
    # eyes
    (
        ( "Dot",        3 ),
        ( "Cross",      2 ),
        ( "Star",       1 ),
    ),
    # hat
    (
        ( "Fur",        3 ),
        ( "Mini Hat",   2 ),
        ( "Crown",      1 ),
    ),
    # right
    (
        ( "Empty",      3 ),
        ( "Pawn",       2 ),
        ( "Candy",      1 ),
    ),
)

# build chunk
chunk = []
for i0, (patt, s0) in enumerate(CONFIG[0]):
    for i1, (eyes, s1) in enumerate(CONFIG[1]):
        for i2, (hat, s2) in enumerate(CONFIG[2]):
            for i3, (right, s3) in enumerate(CONFIG[3]):
                copy = s0 * s1 * s2 * s3
                code = "{}{}{}{}".format(i0, i1, i2, i3)
                for i4 in range(0, copy):
                    # template
                    metadata = {
                      "name": "***",
                      "description": DESC,
                      "image": IMG.format(code),
                      "attributes": [
                        { "trait_type": "Pattern",  "value": CONFIG[0][i0][0] },
                        { "trait_type": "Eyes",     "value": CONFIG[1][i1][0] },
                        { "trait_type": "Hat",      "value": CONFIG[2][i2][0] },
                        { "trait_type": "Right",    "value": CONFIG[3][i3][0] },
                      ],
                      "compiler": ENGINE,
                    }
                    # add to chunk
                    chunk.append(metadata)

# shuffle
for rnd in range(1, SHUFFLE_TIME+1):
    random.shuffle(chunk)

# update name
for id, metadata in enumerate(chunk):
    metadata["name"] = "{} #{}".format(NAME, id)

# write file
for id, metadata in enumerate(chunk):
    with open("./{}/{}.json".format(OUTPUT_DIR, id), "w") as f:
        json.dump(metadata, f, ensure_ascii=False)
