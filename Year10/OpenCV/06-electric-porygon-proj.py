# imports
import cv2
import numpy as np
from pathlib import Path
from sys import exit

# === paths ===

# path to imgs folder
imgs_path = Path(__file__).parent.absolute() / "imgs"
# path to src
src_path = imgs_path / "porygon.jfif"

# === useful funcs ===

def init_img(size: tuple):
    '''
    initializes a np array with 
    the dimensions provided
    '''
    return np.zeros(size, dtype = np.uint8) # ensure the zeros is one byte long


def filter_colours(src: cv2.typing.MatLike, channels: list[int]) -> cv2.typing.MatLike:
    '''
    Creates an image with the colour channels specified\n
    src: the image to filter\n
    channels: a list of the colour channels to include (eg [1,0,0] for blue)
    '''

    # init blank img of src shape
    img = init_img(src.shape)
        
    # add filtered channels to img
    for i, channel in enumerate(channels):
        if channel == 1:
            img[:,:,i] = src[:,:,i]

    # return img
    return img


# === main logic ===

# load src
src = cv2.imread(str(src_path))

# ask usr if they have photosensitive epilepsy
epilepsy = input("Do you have photosensitive epilepsy?\n(y/n) >>> ").lower()

# if they do, show src
if epilepsy == "y":
    cv2.imshow("Porygon", src)
    # show above terminal
    cv2.setWindowProperty("Porygon", cv2.WND_PROP_TOPMOST, 1)

    # hide img after keypresses
    cv2.waitKey(0)

# if they don't, load and show flashing imgs
elif epilepsy == "n":

    # get filtered imgs
    f_imgs = [] # put imgs bere

    for i in range(3):
        # channels to pass to filter_colours
        channels = [0,0,0]
        # set the index to filter
        channels[i] = 1

    	# filter only wanted colour channels from src
    	# and append to filtered imgs
        f_imgs.append(filter_colours(src, channels))
    
    # ask usr what speed they want to flash at
    speed = input("Do you want to have fast (0.1s) or slow (0.5s) flashing?\n(f/s) >>> ")
    
    # set delay time
    if speed == "f":
        delay = 50
    elif speed == "s":
        delay = 500
    else:
        # cry
        print("Just leave me alone :(")
        exit(1)
        
    # show all colours 10 times
    for _ in range(10):
        # show each img we've filtered
        for f_img in f_imgs:
            # show img in same window
            cv2.imshow("Filtered Porygon", f_img)
            # show in front of terminal
            cv2.setWindowProperty("Filtered Porygon", cv2.WND_PROP_TOPMOST, 1)
            # delay between imgs
            cv2.waitKey(delay)
                
else:
    # more crying
    print("Come on, I couldn't have made it easier for you :(")
    
cv2.destroyAllWindows()