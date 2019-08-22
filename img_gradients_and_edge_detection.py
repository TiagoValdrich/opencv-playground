import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./data/sudoku.png', cv2.IMREAD_GRAYSCALE)
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))

# Vertical
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0)
# Horizontal
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1)

sobel_x = np.uint8(np.absolute(sobel_x))
sobel_y = np.uint8(np.absolute(sobel_y))

sobel_combined = cv2.bitwise_or(sobel_x, sobel_y)

titles = ['image', 'Laplacian', 'Sobel X', 'Sobel Y', 'Sobel Combined']
images = [img, lap, sobel_x, sobel_y, sobel_combined]

for i in range(5):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()