import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt

img = cv.imread('Photos/park.jpg')
cv.imshow('Original', img)
# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)
# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#cv.imshow('hsv', hsv)
# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
#cv.imshow('LAB', lab)

# BGR to RGB: OpenCV is in BGR format, rest of python is in RGB format; they are inverses
rgb = cv.cvtColor(img, cv.COLOR_BayerRG2RGB)
cv.imshow('RGB', rgb)


plt.imshow(img)
plt.show()


cv.waitKey(0)