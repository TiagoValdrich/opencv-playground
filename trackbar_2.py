import cv2 as cv
import numpy as np


def callback(position):
    pass


cv.namedWindow('image')

cv.createTrackbar('Number', 'image', 0, 400, callback)
cv.createTrackbar('Gray / Color', 'image', 1, 1, callback)

while True:
    BLACK_AND_WHITE = cv.getTrackbarPos('Gray / Color', 'image')
    text = 'Number: ' + str(cv.getTrackbarPos('Number', 'image'))
    img = cv.imread('./data/lena.jpg', BLACK_AND_WHITE)
    img_shape = np.shape(img)
    cv.putText(img, text, (img_shape[0] - 120, img_shape[1] - 10), cv.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255), 1)
    cv.imshow('image', img)

    if cv.waitKey(1) == 27 & 0xFF:
        break

cv.destroyAllWindows()