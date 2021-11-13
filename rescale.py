import cv2 as cv

img = cv.imread('Photos/cat_large.jpg')
# cv.imshow('Cat', img)

# Rescale value is 0.75, works for video, images, and live video
def rescaleFrame(frame, scale):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

# cv.imshow('Image', rescaleFrame(img))

#capture.set() works only for live video
def changeRes(width, height):
    # Number refers to values of the image
    capture.set(3, width)
    capture.set(4, height)
    
# Reading Video
capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, 0.4)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
# cv.waitKey(0)