from PIL import Image #importing python photo library
import pytesseract as tess #conerting image to text
import cv2 #it is a python library for solving computer vision problem

my_img_cv = cv2.imread("math(1).png") #this is file name

new = tess.image_to_string(my_img_cv) # here image file is converted into string and stored in my_img_cv


solver = eval(new) # it evaluates the string like python expression and returns the result as integer

print(solver)
