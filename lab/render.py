from PIL import Image

# define static img
img_body = Image.open('01Body.png').convert('RGBA')
img_eyes = Image.open('02eye.png').convert('RGBA')

# defind patterns
patterns = [
    "03Blue.png",
    "03Green.png",
    "03RB.png",
    "03Red.png",
]

for p in patterns:

    # create bg
    bg = Image.new("RGBA",(288,288),"white")

    # merge body to bg
    bg = Image.alpha_composite(bg, img_body)

    # merge pattern to bg
    pat = Image.open(p).convert('RGBA')
    bg = Image.alpha_composite(bg, pat)

    # merge eyes to bg
    bg = Image.alpha_composite(bg, img_eyes)

    # save to output file
    bg.save("zzz_{}".format(p), "PNG")
