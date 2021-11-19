import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# if pixel intensity is below this treshhold, set to 0
# if above, set to 255

# Simple threshholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Threshhold', thresh)

# Simple threshholding
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshhold INV', thresh_inv)

# Adaptive Thresholding: lets computer determine threshhold
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("Adaptive Thresholding", adaptive_thresh)



cv.waitKey(0)