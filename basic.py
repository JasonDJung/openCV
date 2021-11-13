import cv2 as cv

img = cv.imread('Photos/park.jpg')

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('image', gray)

#Blur 
blur = cv.GaussianBlur(img, (7,51), cv.BORDER_DEFAULT)
# cv.imshow('image', blur)

# Edge Cascade
canny = cv.Canny(img, 500, 175)
cv.imshow('canny edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations = 1)
cv.imshow('dilated', dilated)

#Eroding
eroded = cv.erode(dilated, (7,7), iterations = 1)
cv.imshow('eroded', eroded)

# Resize
resized = cv.resize(img, (500, 500), interpolation = cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)
cv.waitKey(0)