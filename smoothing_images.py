import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./data/opencv-logo.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img2 = cv2.imread('./data/Noise_salt_and_pepper.png')
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

img3 = cv2.imread('./data/lena.jpg')
img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32) / 25
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5, 5))
g_blur = cv2.GaussianBlur(img2, (5, 5), 0)
# Median is recommended to Salt-and-pepper noise images
# Kenel size needs to be odd, and except the number 1.
median = cv2.medianBlur(img2, 5)
bilateral_filter = cv2.bilateralFilter(img3, 9, 75, 75)

titles = ['image', '2D Convolution', 'Blur', 'Gaussian Blur', 'Median', 'Bilateral Filter']
images = [img, dst, blur, g_blur, median, bilateral_filter]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()