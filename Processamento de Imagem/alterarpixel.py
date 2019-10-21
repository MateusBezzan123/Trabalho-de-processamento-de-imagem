from PIL import Image
im = Image.open('buildings05.jpg')
pixelMap = im.load()

img = Image.new( im.mode, im.size)
pixelsNew = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        if 205 in pixelMap[i,j]:
            pixelsNew[i,j] = (0,0,0,255)
        else:
            pixelsNew[i,j] = pixelMap[i,j]
im.close()
img.show()       
img.save("out.tif") 
img.close()