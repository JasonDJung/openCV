import cv2 as cv

def changeRes(width, height):
    vid.set(3, width)
    vid.set(4, height)

vid = cv.VideoCapture(0)

while True:
    ret, frame = vid.read()

    cv.imshow('frame', frame)
    cv.imshow('resized_frame', changeRes(3, 4))

    if cv.waitKey(1) & 0xFF==ord('q'):
        break

vid.release()
cv.destroyAllWindows()