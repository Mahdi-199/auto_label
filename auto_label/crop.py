# Import packages
import cv2
import numpy as np
from random import randint
 
img = cv2.imread('test.png')
Height, Width, Depth = img.shape
print('image Height = ', Height, '\nimage Width = ', Width) # Print image shape


def new_img(img):
    img_size = []
    x0 = randint(0,Height)
    print('x0=',x0)
    x1 = randint(x0+30,Height)
    print('x1=',x1)
    y0 = randint(0, Width)
    print('y0=',y0)
    y1 = randint(y0+30, Width)
    print('y1=',y1)
    if abs(x1-x0) or abs(y1-y0) <20:
        print('image size is not correct')
        # img_size.append(cropped_image.)
    else :
        cropped_image = img[x0:x1, y0:y1]
    return cropped_image


image_generator = 0
while image_generator<10:
    try:
        result = new_img(img)
        cv2.imshow('generated image', result)
        cv2.waitKey()
        image_generator += 1
    except:
        print('Error')
