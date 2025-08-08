import cv2

img = cv2.imread("./imgs/porygon.jfif")

# make img big
img = cv2.resize(img, (img.shape[1] * 2, img.shape[0] * 2))

cv2.imshow("img", img)
cv2.waitKey(0)

# blur img
blur = cv2.blur(img, (225,225))

cv2.imshow("img", blur)
cv2.waitKey(0)

# vertical motion blur
v_motion_blur = cv2.blur(img, (5,25))

cv2.imshow("img", v_motion_blur)
cv2.waitKey(0)

# horizonal motion blur
h_motion_blur = cv2.blur(img, (25,5))

cv2.imshow("img", h_motion_blur)
cv2.waitKey(0)

cv2.destroyAllWindows()