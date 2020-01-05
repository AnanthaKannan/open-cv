# Translation means move your image up down left and right
# trans matrix
# T = ([1, 0 tx], [0, 1, ty])
import numpy as np
import cv2 as cv

path = "../images/first.jpg"
# to read the image
img = cv.imread(path)
img = cv.resize(img,(960,600))

# store height and width of the image
height, width = img.shape[:2]
quater_height, quater_width = height/4, width/4
# T is our trasisiton matrix
T = np.float32([[1, 0, quater_width], [0, 1, quater_height]])

# warpAffine function used to transform the image
img_translation = cv.warpAffine(img, T, (width, height))
cv.imshow('translation', img_translation)

cv.waitKey(0)
cv.destroyAllWindows()