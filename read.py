import cv2 
import numpy as np

# img = cv2.imread('Photos/cat.jpg')
# cv2.imshow("img", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

capture = cv2.VideoCapture('Videos/1.mp4')

while True:
    isTrue, frame = capture.read()
    cv2.imshow('capture', frame)
    if(cv2.waitKey(20) and 0xFF==ord('d')):
        break
capture.release()
cv2.destroyAllWindows()
