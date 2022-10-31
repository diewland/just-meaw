import json, os, glob, random
from datetime import datetime
from pprint import pprint as pp
 
NAME = "Just Meaw 😺"
DESC = "Just Meaw now Rebranded to Just Meaw USD Real world Money used in Meawtaverse Project🌎 You Can Buy Anything 🏡🚕🥬🍷💎🛸🗿🎡🏓🔧 If Anyone Accept Just Meaw USD💰 even L❤️VE 10,000/10,000 No $, Just Meaw UsD"
IMG = "https://diewland.github.io/just-meaw/assets/{}.png"
ENGINE = "Jigsaw Engine"

OUTPUT_DIR = "./json"
MAX_SUPPLY = 10_000
SHUFFLE_TIME = 99

CONFIG = (
    # pattern
    (
        ( "None",       6 ),
        ( "Luna",       3 ),
        ( "Artemis",    1 ),
    ),
    # eyes
    (
        ( "Dot",        6 ),
        ( "Cross",      3 ),
        ( "Star",       1 ),
    ),
    # hat
    (
        ( "None",       6 ),
        ( "Mini Hat",   3 ),
        ( "Crown",      1 ),
    ),
    # right
    (
        ( "None",       6 ),
        ( "Pawn",       3 ),
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

                    # TODO
                    #print(i4+1, '/', copy, IMG.format(code))

                    # template
                    metadata = {
                      "name": "***",
                      "description": DESC,
                      "image": "***",
                      "attributes": [
                        {
                          "trait_type": "Volume",
                          "value": "***",
                        },
                      ],
                      "compiler": ENGINE,
                    }

                    # update data
                    #metadata["name"] = "{} #{:02}".format(NAME, id)
                    #metadata["image"] = IMG.format(id)
                    #metadata["attributes"][0]["value"] = ".{:02}".format(id)

                    # add to chunk
                    chunk.append(metadata)

pp(chunk)
print(len(chunk))
exit() # TODO

# helper TODO remove ???
def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))
def now():
    return format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# build chunk
chunk = []
for id in range(0, MAX_SUPPLY):

    # template
    metadata = {
      "name": "***",
      "description": DESC,
      "image": "***",
      "attributes": [
        {
          "trait_type": "Volume",
          "value": "***",
        },
      ],
      "compiler": ENGINE,
    }

    # update data
    metadata["name"] = "{} #{:02}".format(NAME, id)
    metadata["image"] = IMG.format(id)
    metadata["attributes"][0]["value"] = ".{:02}".format(id)

    # add to chunk
    chunk.append(metadata)

# shuffle
for rnd in range(1, SHUFFLE_TIME+1):
    random.shuffle(chunk)
    # log
    print("<{}> shuffle #{:02}".format(now(), rnd))
    for cc in chunker(chunk, 25):
        print('-'.join([ c['name'].split('#')[1] for c in cc ]))
    print('')

# write file
for id, metadata in enumerate(chunk):
    with open("./{}/{}.json".format(OUTPUT_DIR, id), "w") as f:
        json.dump(metadata, f, ensure_ascii=False)
    # log
    print("<{}> ID {:02} -> {}".format(now(), id, metadata['name']))
