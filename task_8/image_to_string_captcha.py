from PIL import Image #importing python photo library
import pytesseract as tess #converting image to text
import cv2 #it is a python library for solving computer vision problem

my_img = cv2.imread("math(1).png") #here it loads the image from specified file

new = tess.image_to_string(my_img) # here image file is converted into string and stored in my_img_cv


solver = eval(new) # it evaluates the string like python expression and returns the result as integer

print(solver)
