# imports
import cv2
import numpy as np
from pathlib import Path

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


def filter_colours(src: cv2.typing.MatLike, **kwargs) -> cv2.typing.MatLike:
    '''
    Creates an image with the colour channels specified\n
    src: the image to filter\n
    kwargs:\n
    colour: The colour to make the filtered image (lowercase)\n
    channels: a list of the colour channels to include (eg [1,0,0] for blue)
    '''

    _VALID_COLOURS = ["grey", "red", "green", "blue", "purple", "yellow"]

    # init blank img of src shape
    img = init_img(src.shape)

    # handle word filters
    if "colour" in kwargs:
        if kwargs["colour"] == "grey":
            img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

        elif kwargs["colour"] == "red":
            # put red (2) channel in img
            img[:,:,2] = src[:,:,2]

        elif kwargs["colour"] == "green":
            # green channel is 1
            img[:,:,1] = src[:,:,1]
        
        elif kwargs["colour"] == "blue":
            # channel is 0
            img[:,:,0] = src[:,:,0]
        
        elif kwargs["colour"] == "purple":
            # channels 0,2
            img[:,:,0] = src[:,:,0]
            img[:,:,2] = src[:,:,2]
        
        elif kwargs["colour"] == "yellow":
            # channels 0,1
            img[:,:,0] = src[:,:,0]
            img[:,:,1] = src[:,:,1]

        else:
            raise ValueError(f"Invalid colour: {kwargs['colour']}\nValid colours: {_VALID_COLOURS}")
    
    # handle list filters 
    elif "channels" in kwargs:
        # check kwarg is valid
                # channels is a list
        if not (isinstance(kwargs["channels"], list) or
                # all values are ints
                any(isinstance(channel, int) for channel in kwargs["channels"]) or 
                # only 3 channels
                len(kwargs["channels"]) != 3):
            
            # give ValueError if problem
            raise ValueError("Expected channels kwarg to be type list[int] of length 3")
        
        # add filtered channels to img
        for i, channel in enumerate(kwargs["channels"]):
            if channel == 1:
                img[:,:,i] = src[:,:,i]

    # return img
    return img


# === main logic ===

# load src
src = cv2.imread(str(src_path))

# get filtered imgs
filtered_imgs = [] # put imgs bere

for i in range(3):
    # channels to pass to filter_colours
    channels = [0,0,0]
    # set the index to filter
    channels[i] = 1

    # filter the img by only important colour channels
    # and append to filtered imgs
    filtered_imgs.append(filter_colours(src, channels=channels))