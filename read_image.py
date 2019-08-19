import cv2

'''
Flag
1 -> Loads a color image
0 -> Loads a image in grayscale mode
-1 -> Loads a image as such including alpha channel
'''
img = cv2.imread('./data/lena.jpg', 1)

#print(img)

# Show image
cv2.imshow('image', img)
# Set the time to close the window, if is 0 it keep's opened 
key = cv2.waitKey(0)

if key == 27:
    # Close all the windows.
    cv2.destroyAllWindows()
elif key == ord('s'):
    # Create a image copy from a image
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()