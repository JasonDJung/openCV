import cv2 as cv

# Either takes in Integer values (If using cameras): 0 if webcam, 
# Or takes in file path of video
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    # capture.read() reads in the video frame by frame, returns the frame and a boolean if the frame was successfully returned
    isTrue, frame = capture.read()

    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
# cv.waitKey(0)