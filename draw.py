# Draw and write images

import cv2 as cv
import numpy as np

blank = np.zeros((500,500, 3), dtype = 'uint8')
#cv.imshow('Blank', blank)

img = cv.imread('Photos/cat.jpg')
#cv.imshow('Cat', img)

blank[200:300, 360:400] = 0,255,255
# cv.imshow('Green', blank)

# Draw a rectangle
cv.rectangle(blank, (0, 0), (blank.shape[0]//2, blank.shape[1]//2), (0, 255, 0), thickness = -1)
#cv.imshow('Rectangle', blank)

# Draw a circle
cv.circle(blank, (blank.shape[0]//2, blank.shape[1]//2), 40, (0,0,255), thickness = -1)


#Draw a line
cv.line(blank, (0, 0), (blank.shape[0]//4, blank.shape[1]//2), (255, 255, 200), thickness = 2)

#Write text
cv.putText(blank, 'Hello World!', (255, 255), cv.FONT_HERSHEY_COMPLEX_SMALL, 1.0, (255,0,0), thickness = 2)
cv.imshow('modded', blank)
cv.waitKey(0)

