import numpy as np
import cv2 as cv

path = "../images/first.jpg"
# to read the image
input = cv.imread(path)
# find the shape
print(input.shape)
print('Height', int(input.shape[0]), 'px')
print('Height', int(input.shape[1]), 'px')
# to show the image
window_title = "Hello world"
cv.imshow(window_title, input)
# waitKey used for click any button and the window will destroy
cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite('output.jpg', input)