import cv2
from copy import deepcopy

print("Working . . .")

c_idx = 0 # cam to use

cam = cv2.VideoCapture(c_idx) # default camera (webcam)

# check we got a feed
if not cam.isOpened():
    raise ValueError(f"Could not open camera {c_idx}")
else:
    print("Opened camera")

# important vars
detecting = False   # are we edge detecting
th1 = 60            # threshold 1
th2 = 60            # threshold 2
blurring = False    # are we blurring
ksize = 10          # kernal size for blurring
increment = 10      # increment for thresholds, ksise, etc

# which channels to apply the filter to
filter_channels = [True, True, True]

print("Done!")

while True:
    # capture frame
    has_frame, frame = cam.read()

    # ensure we have a frame
    if not has_frame:
        cv2.destroyAllWindows()
        raise Exception("Did not receive frame")
    
    # handle img filtering
    if detecting:
        tmp = cv2.Canny(frame, th1, th2)
        # make array 3d
        img = deepcopy(frame)
        img[:,:,0] = tmp
        img[:,:,1] = tmp
        img[:,:,2] = tmp
    elif blurring:
        img = cv2.blur(frame, (ksize, ksize))
    else:
        img = frame

    # apply filter to specified channel
    for i in range(3):
        if filter_channels[i]:
            frame[:,:,i] = img[:,:,i]

    # handle keypresses
    kp = cv2.waitKey(1)

    if kp == 27:
        break
    
    elif kp == ord("d"):
        detecting = not detecting
    
    elif kp == ord("b"):
        blurring = not blurring
    
    # change which channels are shown
    elif kp == ord("r"):
        filter_channels[0] = not filter_channels[0]
        print(f"Active Channels: {filter_channels}")
    elif kp == ord("t"):
        filter_channels[1] = not filter_channels[1]
        print(f"Active Channels: {filter_channels}")
    elif kp == ord("y"):
        filter_channels[2] = not filter_channels[2]
        print(f"Active Channels: {filter_channels}")

    '''
    # change thresholds or blur
    elif kp == ord("q"):
        # threshold
        if detecting:
            th1 += increment
        
        # blur
        elif blurring:
            ksize += increment

    elif kp == ord("a"):
        # threshold
        if detecting and th1 > increment:
            th1 -= increment

        # blur
        elif blurring and ksize > increment:
            ksize -= increment

    elif kp == ord("w"):
        th2 += increment

    elif kp == ord("s") and th2 > increment:
        th2 -= increment
    
    # change threshold increment
    elif kp in [ord("z"), ord("x")] and increment > 5:
        if kp == ord("z"):
            increment += 5
        else:
            increment -= 5
        
        print(f"Increment: {increment}")
'''    
    
    cv2.imshow("feed", frame)

# cleanup after loop
cam.release()
cv2.destroyAllWindows()