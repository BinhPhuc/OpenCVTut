import cv2
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')

cv2.imshow("blank", blank)

# 1. Point the image with a certain color
# blank[:] = 0, 0, 255
blank[200:300, 300:400] = 0, 0, 255
cv2.imshow("Red", blank)

# 2. Draw a rectangle
cv2.rectangle(blank, (0, 0), (250, 250), (0, 250, 0) ,thickness=2) # thickness=-1 
cv2.imshow("Rectangle", blank)

# 3. Draw a circle
cv2.circle(blank, (250, 250), 250, (0, 255, 0), thickness=2)
cv2.imshow("Circle", blank)

# 4. Draw a line
cv2.line(blank, (250, 250), (300, 400), (0, 255, 0), thickness=2)
cv2.imshow("Line", blank)

#5. Write text
cv2.putText(blank, "hihihahalazada", (225, 225), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0))
cv2.imshow("Text", blank)

cv2.waitKey(0)
cv2.destroyAllWindows()