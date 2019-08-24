import cv2
import numpy as np

img = cv2.imread('./data/lena.jpg')

low_resolution = cv2.pyrDown(img)
low_resolution2 = cv2.pyrDown(low_resolution)
high_resolution = cv2.pyrUp(low_resolution2)

cv2.imshow("Original image", img)
cv2.imshow("pyrDown image 1", low_resolution)
cv2.imshow("pyrDown image 2", low_resolution2)
cv2.imshow("pyrUp image 1", high_resolution)

cv2.waitKey(0)
cv2.destroyAllWindows()