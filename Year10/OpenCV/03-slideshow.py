import cv2
import os

def set_dims(size: int, x: int, y: int) -> tuple[int, int]:
    '''
    Scales the dimensions of an image so that one
    is equal to size, and the other is less than size\n
    made with ChatGPT
    '''
    # how to change dims
    scale = min((size / x), (size / y))

    # change dims
    new_x = x * scale
    new_y = y * scale
    
    # return rounded dims
    return (round(new_x),round(new_y))

imgs = []

# load imgs
for name in os.listdir("./imgs"):
    img = cv2.imread(f"./imgs/{name}")
    s = img.shape
    resized = set_dims(600, s[1],s[0])

    img = cv2.resize(img,resized)
    imgs.append(img)

# show
for _ in range(5):
    for img in imgs:
        cv2.imshow("test",img)
        key = cv2.waitKey(2000)