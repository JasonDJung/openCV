import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')

# Contours are different from edges!

'''
Contours: 
Edges:
'''

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)

canny = cv.Canny(blur, 125, 175)
#cv.imshow('Canny Edges', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')


# Can visualize treshold by drawing over the image

blank = np.zeros(img.shape, dtype = 'uint8') # same dimensions as cat img
cv.drawContours(blank, contours, -1, (0,0, 255), 1) # -1 is all of them
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)