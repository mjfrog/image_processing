#image processing
from PIL import Image
import time
import timeit

start = timeit.default_timer()

im = Image.open('samus.jpg')
#print(im.format, im.size, im.mode)
pix = im.load()


width = im.size[0]
height = im.size[1]
#print (pix[1,952])
#print (pix[500,500][1] ** 2)
#print (max(pix[500,500]))
#time.sleep(5)
#for x in range (1, 10, 2):
#	print (x)





def invert_color():
#inverts the color of every pixel in the image
	for x in range (0,width-1):
		for y in range (0,height-1):
			#print (pix[x,y])
			#invert each pixel, aka subtract from 255
			pix[x,y] = (255 - pix[x,y][0], 255 - pix[x,y][1], 255 - pix[x,y][2])

def grayscale():
	for x in range (0,width-1):
		for y in range (0,height-1):
			#print (pix[x,y])
			#invert each pixel, aka subtract from 255
			val = max(pix[x,y])
			pix[x,y] = (val, val, val)


def min_grayscale():
	for x in range (0,width-1):
		for y in range (0,height-1):
			#print (pix[x,y])
			#invert each pixel, aka subtract from 255
			val = min(pix[x,y])
			pix[x,y] = (val, val, val)

def simple_blur(depth):
	#based on depth, this should look at a pixel and take all the pixels depth pixels away and average them all
	#eg with a depth of 1, 9 pixels will be averaged at a time

	side = (depth * 2 + 1)
	num = side ** 2 
	#print (num)
	for x in range (depth,width-depth):
		for y in range (depth,height-depth):
			#skip to next "box" or just iterate?
			#we're now at the pixel in quetsion, need to first take the average of all pixels around
			#number of squares = (depth x 2 + 1) ^ 2
			r_a = 0
			g_a = 0
			b_a = 0
			#iterate over the square and get the average
			for a in range (x - depth, x + depth + 1):
				for b in range (y - depth, y + depth + 1):
					r_a += pix[a,b][0]
					g_a += pix[a,b][1]
					b_a += pix[a,b][2]
					#print (a, b)
					#print (pix[a,b])
			#now that we have the sums, average them
			r_a /= num
			g_a /= num
			b_a /= num
			#print ('average')
			#print (r_a)
			#print (g_a)
			#print (b_a)
			#loop over the values again and then reassign the pixels
			for a in range (x - depth, x + depth):
				for b in range (y - depth, y + depth):
					pix[a,b] = (int(r_a), int(g_a), int(b_a))
			#done

def pixel_blur(depth):
	#based on depth, this should look at a pixel and take all the pixels depth pixels away and average them all
	#eg with a depth of 1, 9 pixels will be averaged at a time

	side = (depth * 2 + 1)
	num = side ** 2 
	#print (num)
	for x in range (depth,width-depth,side):
		for y in range (depth,height-depth,side):
			#skip to next "box" or just iterate?
			#we're now at the pixel in quetsion, need to first take the average of all pixels around
			#number of squares = (depth x 2 + 1) ^ 2
			r_a = 0
			g_a = 0
			b_a = 0
			#iterate over the square and get the average
			for a in range (x - depth, x + depth + 1):
				for b in range (y - depth, y + depth + 1):
					r_a += pix[a,b][0]
					g_a += pix[a,b][1]
					b_a += pix[a,b][2]
					#print (a, b)
					#print (pix[a,b])
			#now that we have the sums, average them
			r_a /= num
			g_a /= num
			b_a /= num
			#print ('average')
			#print (r_a)
			#print (g_a)
			#print (b_a)
			#loop over the values again and then reassign the pixels
			for a in range (x - depth, x + depth):
				for b in range (y - depth, y + depth):
					pix[a,b] = (int(r_a), int(g_a), int(b_a))
			#done




#invert_color()
#grayscale()
min_grayscale()
#simple_blur(6)
#pixel_blur(5)

im.save('samus_out.jpg')
#print (pix[0,0])

stop = timeit.default_timer()

print('Time: ', stop - start) 