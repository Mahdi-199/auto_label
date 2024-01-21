
# Python program to explain cv2.cvtColor() method  
   
# importing cv2  
import cv2  
   
# path  
path = 'test.png'
   
# Reading an image in default mode 
src = cv2.imread(path) 
     
# Using cv2.cvtColor() method 
# Using cv2.COLOR_BGR2GRAY color space 
# conversion code 
image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY ) 
image2 = cv2.cvtColor(src, cv2.COLOR_BGR2HSV ) 
image3 = cv2.cvtColor(src, cv2.COLOR_BGR2RGB ) 

# Displaying the image  
cv2.imshow('gray image', image)
cv2.imshow('HSV color space', image2)
cv2.imshow('RGB color space', image3)
cv2.waitKey(0)