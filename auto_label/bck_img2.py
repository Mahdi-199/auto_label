import cv2
import numpy as np
# load image with alpha channel
img = cv2.imread('test.png')
# convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
# blue is 240 in range 0 to 360; so half in OpenCV
# green is 120 in range 0 to 360; so half in OpenCV
blue_hue = 120
green_hue = 60
# diff hue (blue_hue - green_hue)
diff_hue = blue_hue - green_hue
# create mask for green color in hsv
lower = (30,90,90)
upper = (90,170,180)
mask = cv2.inRange(hsv, lower, upper)
mask = cv2.merge([mask,mask,mask])
# apply morphology to clean mask
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
mask = cv2.morphologyEx(mask, cv2.MORPH_ERODE, kernel)
# modify hue channel by adding difference and modulo 180 
hnew = np.mod(h + diff_hue, 180).astype(np.uint8)
# recombine channels and bias value to make brighter
hsv_new = cv2.merge([hnew,s,v+60])
# convert back to bgr
bgr_new = cv2.cvtColor(hsv_new, cv2.COLOR_HSV2BGR)
# blend with original using mask
result = np.where(mask==(255, 255, 255), bgr_new, img)
# save output
cv2.imwrite('eyes_green_mask.png', mask)
cv2.imwrite('eyes_green2blue.png', result)
# Display various images to see the steps
cv2.imshow('mask',mask)
cv2.imshow('bgr_new',bgr_new)
cv2.imshow('result',result)
cv2.waitKey(0)
cv2.destroyAllWindows()