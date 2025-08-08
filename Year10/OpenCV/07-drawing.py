import cv2 as cv5
import numpy as np

# let's draw some shapes!
img = np.zeros((500, 500), dtype=np.uint8)

# show canvas
cv5.imshow("display", img)

cv5.waitKey(0)

# draw a square & show
img[100:125, 100:125] = 255
cv5.imshow("display", img)

cv5.waitKey(0)

# draw another square & show
img[100:125, 200:225] = 255
cv5.imshow("display", img)

cv5.waitKey(0)

# draw line & show
img[150:175, 100:225] = 255
cv5.imshow("display", img)

cv5.waitKey(0)