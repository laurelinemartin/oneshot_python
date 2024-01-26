from PIL import Image
import noise

shape = (512 , 512)
NomFich = "Image.png"
scale = 25
persi = 1.75
lacu = 0.16
octa = 2

img = Image.new (mode = "RGB",size = shape)

def setcolor(i,j,img,pixel):
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    montagne = (125, 55, 0)
    mer = (0, 175, 255)
    profondeur = (0, 120, 255)
    plaines = (0, 155, 50)
    plage = (225, 206, 101)
    neige = (223, 242, 255)

    if pixel >= -1 and pixel < -0.5 :
        img.putpixel((i,j), profondeur)
    elif pixel >= -0.5 and pixel < -0.1:
        img.putpixel((i,j),mer)
    elif pixel >= -0.1 and pixel < 0:
        img.putpixel((i,j), plage)
    elif pixel >= 0 and pixel < 0.25:
        img.putpixel((i,j), plaines)
    elif pixel >= 0.25 and pixel < 0.5:
        img.putpixel((i,j), montagne)
    elif pixel >= 0.5 and pixel < 1:
        img.putpixel((i,j), neige)


for i in range(shape[0]):
    for j in range(shape[1]):
        pixel = noise.pnoise2(i/scale,j/scale, octaves = octa , persistence = persi , lacunarity = lacu)
        setcolor(i,j,img,pixel)
img.save(NomFich)
