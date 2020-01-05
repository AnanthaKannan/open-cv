import numpy as np
import cv2 as cv

path = "../images/first.jpg"
img = cv.imread(path)
img = cv.resize(img, None, fx=0.25, fy=0.25)

kernal_sharpening = np.array([[-1, -1, -1],
                              [-1,  9, -1],
                              [-1, -1, -1]])
sharpened = cv.filter2D(img, -1, kernal_sharpening)
cv.imshow('sharpened', sharpened) 
cv.waitKey(0)
cv.destroyAllWindows()