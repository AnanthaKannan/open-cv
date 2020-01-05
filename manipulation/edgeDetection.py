import numpy as np
import cv2 as cv

path = "../images/first.jpg"
img = cv.imread(path, 0)
img = cv.resize(img, None, fx=0.25, fy=0.25)
height, width = img.shape

# Extract sobel edges
sobel_x = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=5)
sobel_y = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=5)
sobel_or = cv.bitwise_or(sobel_x, sobel_y)

# laplacian
laplacian = cv.Laplacian(img, cv.CV_64F)

# canny
canny = cv.Canny(img, 20, 70)

cv.imshow('img', img)
cv.imshow('sobel_y', sobel_y)
cv.imshow('sobel_or', sobel_or)
cv.imshow('laplacian', laplacian)
cv.imshow('canny', canny)

cv.waitKey(0)
cv.destroyAllWindows()