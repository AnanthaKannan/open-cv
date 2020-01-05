# Useful when scalling images in object detection
import numpy as np
import cv2 as cv

path = "../images/first.jpg"
img = cv.imread(path)
img = cv.resize(img, None, fx=0.25, fy=0.25)

# create a matrix with a same dimension of our image with all value
M = np.ones(img.shape, dtype="uint8") * 175

# add the M value to original image
added = cv.add(img, M)

# subtrap the M value to original image
subtrap = cv.subtract(img, M)
cv.imshow('added', added)
cv.imshow('subtrap', subtrap)
cv.waitKey(0)
cv.destroyAllWindows()