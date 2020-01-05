# Useful when scalling images in object detection
import numpy as np
import cv2 as cv

path = "../images/first.jpg"
img = cv.imread(path)

smaller = cv.pyrDown(img)
smaller = cv.pyrDown(smaller)
large = cv.pyrUp(smaller)

cv.imshow('smaller', smaller)
cv.imshow('large', large)
cv.waitKey(0)
# cv.destroyAllWindows()