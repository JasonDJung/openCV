import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

# Dimensions of shape has to be same as the img, or else will not work
blank = np.zeros(img.shape[:2], dtype='uint8')

# Mask can be circle, rectangle, any shape. shape[1] = width, shape[0] = height
mask = cv.circle(blank,(img.shape[1]//2, img.shape[0]//2 + 45), 100, 255, -1)
cv.imshow('Mask', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked Img', masked)



cv.waitKey(0)