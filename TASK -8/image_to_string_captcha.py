from PIL import Image #importing python photo library
import pytesseract as tess #converting image to text
import cv2 #it is a python library for solving computer vision problem

my_img = cv2.imread("math(1).png") #here it loads the image from specified file

new = tess.image_to_string(my_img) # here image file is converted into string and stored in my_img_cv

my_characters = ['?','=', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#this is list of characters

for i in my_characters:
	new = new.replace(i , '') # now removing unwanted characters in the image file of captcha code

solver = eval(new) # it evaluates the string like python expression and returns the result as integer

print(solver)
