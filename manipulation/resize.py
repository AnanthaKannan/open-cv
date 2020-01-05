# cv.resize(image, dsize(output image size), x scale, y scale, interpolation)

import numpy as np
import cv2 as cv

path = "../images/first.jpg"
# to read the image
img = cv.imread(path)

# Let's make our image quater size of original image
image_scaled = cv.resize(img, None, fx=0.25, fy=0.25)
cv.imshow('image_scaled', image_scaled)

# Let's the doube size of image
double_size = cv.resize(img, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)
cv.imshow('double_size', double_size)

skew_img = cv.resize(img, (900, 400), interpolation=cv.INTER_AREA)
cv.imshow('skew_img', skew_img)


cv.waitKey(0)
cv.destroyAllWindows()