import cv2 as cv
import numpy as np

img = cv.imread('Photos/group 1.jpg')
cv.imshow('Person', img)

# face detection doesn't involve color, uses edges
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

# Returns rectangle coordinates of face as a list: haar cascades are very sensitive to noise in an image
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0, 255,0), thickness=2)
cv.imshow("detected face", img)

cv.waitKey(0)