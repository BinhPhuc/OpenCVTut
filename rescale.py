import cv2

img = cv2.imread('Photos/cat.jpg')

def rescale(frame, scale=0.7):
    # Images, Videos and Live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)
    # Short hand
    # return cv2.resize(frame, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)

def changeRes(width, height):
    # Live videos
    capture.set(3, width)
    capture.set(4, height)

capture = cv2.VideoCapture('Videos/1.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescale(frame, scale=0.7)
    cv2.imshow("video", frame)
    cv2.imshow("video_resized", frame_resized)
    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv2.destroyAllWindows()