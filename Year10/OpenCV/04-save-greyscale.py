import cv2
from pathlib import Path
from sys import argv, exit

try:
    assert len(argv) == 2
except AssertionError:
    print("DID NOT PROVIDE IMAGE TO CHANGE")
    exit(1)

OPENVC_DIR_PATH = Path(__file__).parent.resolve()
IMGS_PATH = OPENVC_DIR_PATH / "imgs"

# load img
src = cv2.imread(f"{IMGS_PATH}/{argv[1]}")

# convert to geyscale
img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# save img
cv2.imwrite(f"grey-{argv[1]}", img)