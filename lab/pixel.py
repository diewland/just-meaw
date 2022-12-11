from PIL import Image, ImageDraw
import random

#create background
img0 = Image.new("RGBA",(8,8),"white")
img1 = ImageDraw.Draw(img0)

#create variable
Colour = random.sample(["Red","Blue","Green","Black","White"], counts=[4,6,10,30,50],k =64)

# (1/3) comment old drawing logic
#x = list(range(0,64))
#k = 0
#for i in x :
#    for j in x :
#        for k in x:
#            img1.line((i,j,i,j),fill=Colour[k])
#            k += 1

# (2/3) add new drawing logic
for y in range(0, 8):
    for x in range(0, 8):
        c = Colour[(y*8)+x]
        img1.point((y, x), fill=c)

#reaize and save
img2 = img0.resize((256,256), resample=Image.NEAREST) # <-- (3/3) add second parameter
img2.show()
#img2.save("draw.png")
