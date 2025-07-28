'''
Crops an image
'''
import cv2 as c

img = c.imread("./img.jpg")
shp = img.shape # get the image's dimensions

cropped_img = img[40:320, 100:500] # X, Y


c.imshow("Cropped img", cropped_img) # show
c.waitKey(0) # wait for keypress
c.destroyAllWindows() # hide window
