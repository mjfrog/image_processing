#image processing
from PIL import Image
import time
import timeit
import random

start = timeit.default_timer()

#im = Image.open('samus.jpg')
im = Image.open('coal.jpeg')
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

#pix[500,500] = (-1, 1, 1)



def invert_simple(val):
	return 255 - val

def invert_color():
#inverts the color of every pixel in the image
	for x in range (0,width-1):
		for y in range (0,height-1):
			#print (pix[x,y])
			#invert each pixel, aka subtract from 255
			pix[x,y] = (255 - pix[x,y][0], 255 - pix[x,y][1], 255 - pix[x,y][2])

def negative():
	for x in range (0,width-1):
		for y in range (0,height-1):
			#print (pix[x,y])
			#invert each pixel, aka subtract from 255
			pix[x,y] = (-1 * pix[x,y][0], -1 * pix[x,y][1], -1 * pix[x,y][2])

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
	#this function takes a million years to run and im pretty sure its O(n^4)

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
	#interating in increments of side increases efficiency 
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

def swap(val):
	#just swaps values, R -> G, G -> B, B -> R, or the reverse if 1
	#this is actually prety cool, might be sweet to use in conjuction with other filters 
	if val == 0:
		for x in range (0,width-1):
			for y in range (0,height-1):
				pix[x,y] = (pix[x,y][2], pix[x,y][0], pix[x,y][1])
	elif val == 1:
		for x in range (0,width-1):
			for y in range (0,height-1):
				pix[x,y] = (pix[x,y][1], pix[x,y][2], pix[x,y][0])


def contrast(val):
	#if a value is greater than 128, mutliply it times the val, if not divide 
	for x in range (0,width-1):
		for y in range (0,height-1):
			r_a = pix[x,y][0]
			g_a = pix[x,y][1]
			b_a = pix[x,y][2]
			#print ("r_a " + str(r_a))

			if r_a < 128:
				r_a /= val
			else:
				r_a *= val

			if g_a < 128:
				g_a /= val
			else:
				g_a *= val

			if b_a < 128:
				b_a /= val
			else:
				b_a *= val 

			pix[x,y] = (int(r_a), int(g_a), int(b_a))

			#print ("r_a new " + str(r_a))

def limited_colors(val):
	#idea here is that pixel values can only be a multiple of val
	#modulu forces it to always round down
	#later, another function that ties 3 values together as a "color" and only allows limited colors, instead of per pixel
	for x in range (0,width-1):
		for y in range (0,height-1):
			pix[x,y] = (pix[x,y][0] - (pix[x,y][0] % val), pix[x,y][1] - (pix[x,y][1] % val), pix[x,y][2] - (pix[x,y][2] % val))


#random suite
#return random.randint(1,5)
def pure_random():
	#this just randomizes every pixel
	for x in range (0,width-1):
		for y in range (0,height-1):
			pix[x,y] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

def one_random(val):
	#randomizes only one of the RBG values, based on val
	if val == 0:
		for x in range (0,width-1):
			for y in range (0,height-1):
				pix[x,y] = (random.randint(0,255), pix[x,y][1], pix[x,y][2])

	elif val == 1:
		for x in range (0,width-1):
			for y in range (0,height-1):
				pix[x,y] = (pix[x,y][0],random.randint(0,255), pix[x,y][2])

	elif val == 2:
		for x in range (0,width-1):
			for y in range (0,height-1):
				pix[x,y] = (pix[x,y][0],pix[x,y][1], random.randint(0,255))		

def randomize_range(val):
	#randomizes each RGB value using range. e.g. range of 10, R = 150, set it anywhere between 140 and 160
	#this just randomizes every pixel
	for x in range (0,width-1):
		for y in range (0,height-1):
			pix[x,y] = (random.randint(pix[x,y][0] - val, pix[x,y][0] + val), random.randint(pix[x,y][1] - val, pix[x,y][1] + val), random.randint(pix[x,y][2] - val, pix[x,y][2] + val))




#invert_color()
#grayscale()
#min_grayscale()
#simple_blur(6)
#pixel_blur(5)
#pure_random()
#one_random(2)
#swap(1)
#pixel_blur(4)
#negative()
#randomize_range(60)
#im.point(invert_simple)
#contrast(1.5)
#swap(0)
limited_colors(32)

im.save('coal_limited.jpg')
#print (pix[0,0])

stop = timeit.default_timer()

print('Time: ', stop - start) 