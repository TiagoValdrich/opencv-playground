import cv2 as cv
import numpy as np


def nothing(position):
    print(position)


img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow('image')

cv.createTrackbar('B', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('R', 'image', 0, 255, nothing)

switch = '0 : OFF\n 1 : ON'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while True:
    cv.imshow('image', img)
    key = cv.waitKey(1) & 0xFF

    blue = cv.getTrackbarPos('B', 'image')
    green = cv.getTrackbarPos('G', 'image')
    red = cv.getTrackbarPos('R', 'image')
    switch_bar = cv.getTrackbarPos(switch, 'image')

    if switch_bar == 0:
        img[:] = 0
    else:
        img[:] = [blue, green, red]

    if key == 27:
        break

cv.destroyAllWindows()