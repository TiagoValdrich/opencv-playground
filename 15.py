import cv2 as cv
import numpy as np

img = cv.imread('./data/gradient.png', 0)
_, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

cv.imshow("Image", img)
cv.imshow("Th1", th1)
cv.imshow("Th2", th2)
cv.imshow("Th3", th3)
cv.imshow("Th4", th4)
cv.imshow("Th5", th5)

cv.waitKey(0)
cv.destroyAllWindows()