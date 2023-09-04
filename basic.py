import cv2
import numpy as np

img = cv2.imread('Photos/cat.jpg')
cv2.imshow("original", img)

# 1. Converting to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)

# 2. Blur
blur = cv2.GaussianBlur(img, (9, 9), cv2.BORDER_DEFAULT)
cv2.imshow("blur", blur)

# 3. Edge Cascade
canny = cv2.Canny(blur, 125, 175)
cv2.imshow("canny", canny)

# 4. Dilation

kernel = np.ones((3, 3), np.uint8)
dilation = cv2.dilate(canny, kernel, iterations=1)
cv2.imshow("dilation", dilation)

# 5. Eroded   
eroded = cv2.erode(canny, kernel, iterations=1)
cv2.imshow("eroded", eroded)

# 6. Resize 
resized = cv2.resize(img, (500, 500), interpolation=cv2.INTER_AREA)
# shrinking the image to dimensions that are smaller than orginal image using cv2.INTER_AREA
# scale the image to a much larger dimensions using cv2.INTER_LINEAR or cv2.INTER_CUBIC 
# (cv2.INTER_CUBIC is slowest but higher quality)
cv2.imshow("resized", resized)

# 7. Cropping
cropped = img[50:200, 200:400]
cv2.imshow("cropped", cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()