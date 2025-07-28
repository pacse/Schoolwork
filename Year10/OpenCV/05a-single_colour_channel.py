import cv2
import numpy as np
from pathlib import Path

def init_img(size: tuple):
    return np.zeros(size, dtype = np.uint8) # ensure the zeros is one byte long

def filter_colour(src: cv2.typing.MatLike, colour: str) -> cv2.typing.MatLike:
    '''
    Creates an image with the colour channels specified\n
    params:\n
    src: the image to filter\n
    colour: The colour to make the filtered image (lowercase)
    '''
    _VALID_COLOURS = ["grey", "red", "green", "blue", "purple", "yellow"]

    # init blank img of src shape
    img = init_img(src.shape)

    # add colour channels
    if colour == "grey":
        img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    elif colour == "red":
        # put red (2) channel in img
        img[:,:,2] = src[:,:,2]

    elif colour == "green":
        # green channel is 1
        img[:,:,1] = src[:,:,1]
    
    elif colour == "blue":
        # channel is 0
        img[:,:,0] = src[:,:,0]
    
    elif colour == "purple":
        # channels 0,2
        img[:,:,0] = src[:,:,0]
        img[:,:,2] = src[:,:,2]
    
    elif colour == "yellow":
        # channels 0,1
        img[:,:,0] = src[:,:,0]
        img[:,:,1] = src[:,:,1]

    else:
        raise ValueError(f"Invalid colour: {colour}\nValid colours: {_VALID_COLOURS}")
    
    # return
    return img
    

# paths
imgs_path = Path(__file__).parent.absolute()
img_path = imgs_path / "imgs" / "git.jpg"

# image to play with
src = cv2.imread(str(img_path))

# sneaky resize
s = src.shape
resized = (s[1]//2, s[0]//2)
src = cv2.resize(src, resized)

_VALID_COLOURS = ["grey", "red", "green", "blue", "purple", "yellow"]

cv2.imshow("Original", src)

while True:
    key = chr(cv2.waitKey(0))
    print(key)

    if key == "q":
        break

    elif key == "d": # dull
        img = filter_colour(src, "grey")
    elif key == "r":
        img = filter_colour(src, "red")
    elif key == "g":
        img = filter_colour(src, "green")
    elif key == "b":
        img = filter_colour(src, "blue")
    elif key == "p":
        img = filter_colour(src, "purple")
    elif key == "y":
        img = filter_colour(src, "yellow")
    else:
        print(f"INVALID KEY: {key!r}")
        continue
    
    cv2.imshow("Filtered", img)

cv2.destroyAllWindows()