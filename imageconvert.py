import os
from skimage import io
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import numpy as np

#file is name of file you want to convert
#pixellation is square width of how many pixels of original should be in one pixel of output
def img2ascii(image, pixellation):
	#converting image to grayscale
	gray_image = rgb2gray(image)
	#defining array that stores the value of each pixel in the new image array
	ascii_length = int(len(gray_image[1]) / pixellation)
	ascii_height = int(len(gray_image) / pixellation / 2)
	ascii_image_values = np.ndarray(shape=(ascii_height, ascii_length), dtype = float)
	ascii_image = np.ndarray(shape=(ascii_height, ascii_length), dtype = object)
	#high will he highest value, low lowest. This will be used to decide what the range of values for each 'color' will be
	high = 0.0
	low = 1.0
	#x and y are the position in the new ascii image
	for x in range(ascii_length):
		for y in range(2 * ascii_height):
			#find the average value of the pixe in the grayscale original image
			count = 0
			total = 0
			#gray_x and gray_y are the x and y position in the original grayscale image
			for gray_x in range((x * pixellation), ((x + 1) * pixellation)):
				for gray_y in range((y * pixellation), ((y + 1) * pixellation)):
					count = count + 1
					total = total + gray_image[gray_y][gray_x]
			avg = total / count
			if avg > high:
				high = avg
			if avg < low:
				low = avg
			ascii_image_values[int(y / 2)][x] = avg


	spectrum = []
	spect_length = high - low
	for x in range(5):
		spectrum.append(x * (spect_length / 5))

	for y in range(ascii_height):
		for x in range(ascii_length):
			ascii_image[y][x] = to_ascii(ascii_image_values[y][x], spectrum)

	return ascii_image

def to_ascii(value, range):
	if value > range[4]:
		return '█'
	if value > range[3]:
		return '▓'
	if value > range[2]:
		return '▒'
	if value > range[1]:
		return '░'
	return ' '

def print_ascii(ascii_image):
	for x in range(len(ascii_image)):
		line = ''
		for y in range(len(ascii_image[0])):
			line = line + ascii_image[x][y]
		print(line)



#name of file you want to convert
file = io.imread(os.path.join('mountain.jpg'))
#square width of how many pixels of original should be in one pixel of output
pixellation = 10

print_ascii(img2ascii(file, pixellation))