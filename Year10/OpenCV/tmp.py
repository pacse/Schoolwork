import cv2
import numpy as np

# function to edge detect img (converted cs50x ps 4 solution)
# too slow for video feed processing
def cs50x_edge_detect(img: cv2.typing.MatLike) -> cv2.typing.MatLike:
    # blank img
    filtered = np.zeros(img.shape, dtype=np.uint8)

    # convert img to signed ints - thanks ChatGPT
    img = img.astype(np.int16)

    def _cal_channel_val(x: int, y: int) -> int:
        '''
        returns:
        round(sqrt(x^2 + y^2))
        with a maximum value of 255
        '''
        return min(round(((x ** 2) + (y ** 2)) ** 0.5), 255)

    # Gx & Gy
    Gx = [
        [-1,0,1],
        [-2,0,2],
        [-1,0,1]
    ]

    Gy = [
        [-1,-2,-1],
        [0,0,0],
        [1,2,1]
    ]


    # now filter
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            
            # Gx & Gy counters
            Gx_counter = [0,0,0]
            Gy_counter = [0,0,0]

            # filter local pixels
            for local_x in range(x-1, x+2):
                for local_y in range(y-1, y+2):

                    # if pixel in image bounds
                    if (local_x >= 0 and local_y >= 0) and (local_x < img.shape[1] and local_y < img.shape[0]):

                        pixel = img[local_y, local_x]

                        for i in range(3):
                            # update counters
                            Gx_counter[i] += pixel[i] * Gx[local_y - (y - 1)][local_x - (x - 1)]
                            Gy_counter[i] += pixel[i] * Gy[local_y - (y - 1)][local_x - (x - 1)]
                
            # calculate rgb channel values for each pixel
            # and insert into filtered
            filtered[y,x] = [
                _cal_channel_val(int(Gx_counter[i]), int(Gy_counter[i]))
                for i in range(3)
                ]
    
    return filtered