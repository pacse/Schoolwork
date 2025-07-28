'''
Opens an image and closes it after a keypress
'''
import cv2 as c

path = "C:/Users/User2/Documents/Code/OpenCV/img.jpg"

img = c.imread(path)

c.imshow("Display Window", img) # show image
key = c.waitKey(0) # wait for keypress
c.destroyAllWindows() # close window

print(f"Key pressed: {chr(key)!r} ({key})") # prints key pressed