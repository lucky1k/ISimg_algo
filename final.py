from PIL import Image

img=Image.open(r"rplace.png")
img =img.convert('RGB')
px=img.load()

new_img=[]

x,y=39,39

print(px[x,y])
(r,g,b)=px[x,y]
print("Pixel at",x,"",y," - Red: {}, Green: {}, Blue: {}".format(r,g,b))

new_img.append((104,105,105))

print("##################")

if px[x, y] == (r,g,b):
    px[x, y] = (104, 105, 105)

img.save("f_rplace.jpg")
print(px[x,y])
print("Pixel at",x,"",y," - Red: {}, Green: {}, Blue: {}".format(r,g,b))




img.show()

key = x,y


print(hash(key))
