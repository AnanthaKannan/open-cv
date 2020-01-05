import numpy as np
import cv2 as cv

path = "../images/first.jpg"
img = cv.imread(path)
img = cv.resize(img, None, fx=0.25, fy=0.25)

# creating our 3X3 kernal
kernal_3x3 = np.ones((3,3), np.float32)/9

# we using the filter2D method to convolve the kernal with the image
blurred = cv.filter2D(img, -1, kernal_3x3)

cv.imshow('blurred', blurred)



# other comman filter method
blur = cv.blur(img, (3,3))
GaussionBlur = cv.GaussianBlur(img, (7,7), 0)
median = cv.medianBlur(img, 5)
biLateral = cv.bilateralFilter(img, 9, 75, 75)

cv.imshow('blur', blur)
cv.imshow('GaussionBlur', GaussionBlur)
cv.imshow('median', median)
cv.imshow('biLateral', biLateral)

# Image de-nosing-non-local means Denoising
dst = cv.fastNlMeansDenoisingColored(img, None, 6, 6, 7, 21)
cv.imshow('dst', dst)



cv.waitKey(0)
cv.destroyAllWindows()