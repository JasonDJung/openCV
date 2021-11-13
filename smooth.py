import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

# Averaging: Define a kernel window, compute the middle pixel intensity as the average of the surrounding pixels
# Higher kernel size = more blur
# Useful 

average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur
# Each pixel is given a weight, the middle pixel is the average of the products of weights around the surrounding pixel
# More natural compared to averaging
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur: similar to average blurring, except it finds the median of the surrounding pixels
median = cv.medianBlur(img, 7)
cv.imshow('MedianBlur', median)

# Bilateral Blurring
# Most Commonly used blurring methods: Blurs the image while retaining the edges in the image
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)