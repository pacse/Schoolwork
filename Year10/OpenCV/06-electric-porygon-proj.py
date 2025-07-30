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


def filter_colours(src: cv2.typing.MatLike, channels: list[int]) -> cv2.typing.MatLike:
    '''
    Filters only selected colour channels from src
    
    Args:
        src: the image to filter
        channels: a list of the colour channels to include (eg [1,0,0] for blue)
    
    Returns:
        The filtered image
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

# ✨Sanity check✨
if not src:
    raise ValueError("Could not load source img")

# ask usr if they have photosensitive epilepsy
epilepsy = input("Do you have photosensitive epilepsy?\n(y/n) >>> ").lower()

if epilepsy == "y":
    # if they do, show src
    cv2.imshow("Porygon", src)
    # show above terminal
    cv2.setWindowProperty("Porygon", cv2.WND_PROP_TOPMOST, 1)

    # hide img after keypresses
    cv2.waitKey(0)

# if they don't, load and show flashing imgs
elif epilepsy == "n":

    # get filtered imgs

    filtered_imgs: list[cv2.typing.MatLike] = []

    for i in range(3):
        # channels to pass to filter_colours
        channels = [0,0,0]

        # set the index to filter
        channels[i] = 1

    	# filter only wanted colour channels from src
    	# and append to filtered imgs
        filtered_imgs.append(filter_colours(src, channels))
    
    # ask usr what speed they want to flash at
    speed = input("Do you want to have fast (0.1s) or slow (0.5s) flashing?\n(f/s) >>> ")
    
    # set delay time
    if speed == "f": # fast flash
        delay = 50
    elif speed == "s": # slow flash
        delay = 500

    else:
        # cry
        raise ValueError("Just leave me alone :(")
        
    # show all colours 10 times
    for _ in range(10):
        
        for f_img in filtered_imgs:
            # show f_img in one changing window
            cv2.imshow("Filtered Porygon", f_img)
            # show in front of terminal
            cv2.setWindowProperty("Filtered Porygon", cv2.WND_PROP_TOPMOST, 1)
            # delay between imgs
            cv2.waitKey(delay)
                
else:
    # more crying
    raise ValueError("Come on, I couldn't have made it easier for you :(")

# cleanup
cv2.destroyAllWindows()

# ╰(*°▽°*)╯ The program worked! ╰(*°▽°*)╯