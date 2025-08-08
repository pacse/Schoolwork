# annotate images with OpenCV
# draw shapes, text, lines, etc.
import cv2

img = cv2.imread("./imgs/porygon.jfif")

# make img big
img = cv2.resize(img, (img.shape[1] * 2, img.shape[0] * 2))

cv2.imshow("img", img)

# draw a line
img = cv2.line(img, # img to draw line on
               (50,40), # staering cords (cartesian: x,y)
               (200,40), # ending cords (cartesian: x,y)
               (0,0,255), # line colour (BGR)
               thickness=5, # line thickness
               lineType=cv2.LINE_AA # make a slightly prettier line (anti-aliasing)
               )

cv2.imshow("img", img)

# draw a few lines
for y in range(50,256, 25):
    img = cv2.line(img, (50, y), (200, y), (y,0,0), 2, cv2.LINE_AA)

cv2.imshow("img", img)

# draw a square
img = cv2.rectangle(img, 
                    (225,100),  # one corner
                    (425,300),  # opposite corner
                    (0,255,0),  # line colour
                    5,          # line thickness
                    cv2.LINE_AA # line styling
                    )

cv2.imshow("img", img)

# and now a circle in the square
img = cv2.circle(img,
                 (325,200), # circle center
                 100,       # circle radius
                 (0,255,0), 5, cv2.LINE_AA)

cv2.imshow("img", img)

# and now text at the bottom
img = cv2.putText(img,
                  "Porygon",                # text to write
                  (50, 425),                  # where to begin writing (x,y)
                  cv2.FONT_HERSHEY_COMPLEX, # font
                  2.3,                      # font size (height of chars)
                  (128,128,0),              # font colour
                  2,                        # line thickness
                  cv2.LINE_AA)              # line style

# underline text
img = cv2.line(img,(50,435),(375,435), (128,128,0), 3,cv2.LINE_AA)

cv2.imshow("img", img)
cv2.waitKey(0)

cv2.destroyAllWindows()