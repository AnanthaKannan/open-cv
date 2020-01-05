import numpy as np
import cv2 as cv

path = "../images/marker.jpg"
img = cv.imread(path)
img = cv.resize(img, None, fx=0.25, fy=0.25)

cv.imshow('img', img)

# define our kernal size
kernal = np.ones((5,5), np.uint8)

# now we erode
erosion = cv.erode(img, kernal, iterations=1)
# now we dialate
dilation = cv.dilate(img, kernal, iterations=1)
# opening - good for remove noise
opening = cv.morphologyEx(img, cv.MORPH_OPEN ,kernal)
# Closing - good for remove noise
closing = cv.morphologyEx(img, cv.MORPH_CLOSE ,kernal)

cv.imshow('img', img)
cv.imshow('erosion', erosion)
cv.imshow('dilation', dilation)
cv.imshow('opening', opening)
cv.imshow('closing', closing)


cv.waitKey(0)
cv.destroyAllWindows()