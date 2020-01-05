import numpy as np
import cv2 as cv

# if you're wondering why only two dimensions, well this is a grayscale image
# if we doing a color image, we'd use
# square = np.zeros((300, 300, 3), np.uint8)
 
#  make a square
square = np.zeros((300, 300), np.uint8)
cv.rectangle(square, (50, 50), (250, 250), 255, -2)
cv.imshow('square', square)

# making a ellipse
ellipse = np.zeros((300, 300), np.uint8)
cv.ellipse(ellipse, (150, 150), (150, 150), 30, 0, 180, 255, -1)
cv.imshow('ellipse', ellipse)


# Bitwise
And = cv.bitwise_and(square, ellipse)
cv.imshow('And', And)
Or = cv.bitwise_or(square, ellipse)
cv.imshow('Or', Or)
Not = cv.bitwise_not(square)
cv.imshow('Not', Not)
Xor = cv.bitwise_xor(square, ellipse)
cv.imshow('Xor', Xor)

cv.waitKey(0)
cv.destroyAllWindows()