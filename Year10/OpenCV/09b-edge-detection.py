import cv2

'''img = cv2.imread("./imgs/porygon.jfif")

# make img big
img = cv2.resize(img, (img.shape[1] * 2, img.shape[0] * 2))

cv2.imshow("img", img)
cv2.waitKey(0)

# detect edges with Canny
# thresholds are how sensitive it is?
edges = cv2.Canny(img, 200, 200)

cv2.imshow("edges", edges)
cv2.waitKey(0)

cv2.destroyAllWindows()'''

# Now video!
print("Working . . .")

c_idx = 0

cam = cv2.VideoCapture(c_idx) # default camera (webcam)
print("Opened cam")

# check we got a feed
if not cam.isOpened():
    raise ValueError(f"Could not open camera {c_idx}")

detecting = False # are we edge detecting
th1 = 150
th2 = 125
increment = 10

print("Done!")

while True:
    # capture frame
    has_frame, frame = cam.read()

    # ensure we have a frame
    if not has_frame:
        cv2.destroyAllWindows()
        raise Exception("Did not receive frame")
    
    # show frame
    if detecting:
        img = cv2.Canny(frame, th1, th2)
    else:
        img = frame

    # handle keypresses
    kp = cv2.waitKey(1)

    if kp == 27:
        break
    
    elif kp == ord("d"):
        detecting = not detecting
    
    # change thresholds
    elif kp in [ord("q"),ord("a"),ord("w"),ord("s")]:
        if kp == ord("q") and th1 > increment:
            th1 += increment
        elif kp == ord("a") and th1 > increment:
            th1 -= increment

        elif kp == ord("w") and th2 > increment:
            th2 += increment
        elif kp == ord("s") and th2 > increment:
            th2 -= increment

        print(f"Threshold 1: {th1}")
        print(f"Threshold 2: {th2}")
    
    # change threshold increment
    elif kp in [ord("z"), ord("x")] and increment > 5:
        if kp == ord("z"):
            increment += 5
        else:
            increment -= 5
        
        print(f"Increment: {increment}")
    
    
    cv2.imshow("feed", img)