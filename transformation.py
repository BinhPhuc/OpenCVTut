import cv2
import numpy as np

img = cv2.imread('Photos/cat.jpg')

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# +x --> Right
# +y --> Down

translated = translate(img, 100, 100)
cv2.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if (rotPoint == None):
        rotPoint = (width//2, height//2)
    rotMat = cv2.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv2.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 90)
cv2.imshow('Rotated', rotated)

# Resizing
resized = cv2.resize(img, (500,500), interpolation=cv2.INTER_AREA)
cv2.imshow('Resized', resized)

# Flipping
flip = cv2.flip(img, 1) # 0: vertical, 1: horizontal, -1: both
cv2.imshow('Flip', flip)

# Cropping
cropped = img[200:400, 300:400]
cv2.imshow('Cropped', cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()

# https://docs.opencv.org/4.x/da/d6e/tutorial_py_geometric_transformations.html