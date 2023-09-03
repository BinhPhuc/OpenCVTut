import cv2

img = cv2.imread('Photos/cat.jpg')

def rescale(frame, scale=0.7):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)
    # Short hand
    # return cv2.resize(frame, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)

cv2.waitKey(0)