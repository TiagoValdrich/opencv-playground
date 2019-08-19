import cv2 as cv
import numpy as np


def nothing(x):
    pass


cap = cv.VideoCapture(0)

cv.namedWindow('Tracking')
cv.createTrackbar('LH', 'Tracking', 0, 255, nothing)
cv.createTrackbar('LS', 'Tracking', 0, 255, nothing)
cv.createTrackbar('LV', 'Tracking', 0, 255, nothing)
cv.createTrackbar('UH', 'Tracking', 255, 255, nothing)
cv.createTrackbar('US', 'Tracking', 255, 255, nothing)
cv.createTrackbar('UV', 'Tracking', 255, 255, nothing)

while True:
    _, frame = cap.read()
    frame = cv.flip(frame, 1)

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_hue = cv.getTrackbarPos('LH', 'Tracking')
    lower_saturation = cv.getTrackbarPos('LS', 'Tracking')
    lower_value = cv.getTrackbarPos('LV', 'Tracking')

    upper_hue = cv.getTrackbarPos('UH', 'Tracking')
    upper_saturation = cv.getTrackbarPos('US', 'Tracking')
    upper_value = cv.getTrackbarPos('UV', 'Tracking')

    l_b = np.array([lower_hue, lower_saturation, lower_value])
    u_b = np.array([upper_hue, upper_saturation, upper_value])

    mask = cv.inRange(hsv, l_b, u_b)

    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)

    if cv.waitKey(1) == 27 & 0xFF:
        break

cap.release()
cv.destroyAllWindows()