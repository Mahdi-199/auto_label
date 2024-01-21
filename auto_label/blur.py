import cv2  
  
# read input image. 
img = cv2.imread('test.png')  
  
# make sure that you have saved it in the same folder 
# You can change the kernel size as you want 
blurImg = cv2.blur(img,(10,10))
blur_image = cv2.GaussianBlur(img, (7,7), 0)  
cv2.imshow('simple blurred image',blurImg) 
cv2.imshow('gaussian blurred image',blur_image) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 