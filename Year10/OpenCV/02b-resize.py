'''
Resizes an image
'''
import cv2 as c

img = c.imread("./imgs/arch.jpg")
shp = img.shape # get the image's dimensions

resize_dim = 0.5 # 50%

# compute resized image dimensions
resized = (round(shp[1] * resize_dim), round(shp[0] * resize_dim)) # x first, then y

resized_img = c.resize(img, resized) # resize img

c.imshow("Smaller img", resized_img) # show
c.waitKey(0) # wait for keypress
c.destroyAllWindows() # hide window