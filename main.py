#image processing
from PIL import Image

im = Image.open('chartres.jpg')
print(im.format, im.size, im.mode)
pix = im.load()


width = im.size[0]
height = im.size[1]

def invert_color():
#inverts the color of every pixel in the image
	for x in range (0,width-1):
		for y in range (0,height-1):
			#print (pix[x,y])
			#invert each pixel, aka subtract from 255
			pix[x,y] = (255 - pix[x,y][0], 255 - pix[x,y][1], 255 - pix[x,y][2])

invert_color()

im.save('out.jpg')
#print (pix[0,0])