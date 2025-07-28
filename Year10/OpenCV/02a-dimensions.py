'''
Gets the dimensions of an image
'''
import cv2 as c

img = c.imread("./img.jpg")
shp = img.shape # get the image's dimensions


print(f"""The image dimensions are:
y (height): {shp[0]}
x (width): {shp[1]}
z (colour depth): {shp[2]}""") # default colour sequence: Blue, Green, Red