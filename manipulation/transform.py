
import numpy as np
import cv2 as cv

path = "../images/first.jpg"
# to read the image
img = cv.imread(path)
img = cv.resize(img,(960,600))

# cordinate of the foure corners of the original immage
point_a = np.float32([[320, 15], [700, 215], [85, 610], [530, 780]])

# cordinate of the foure corners of the desired output
# we use a ratio of an A4 paper 1: 1.41
point_b = np.float32([[0,0], [420, 0], [0, 594], [420, 594]])

M = cv.getPerspectiveTransform(point_a, point_b)
wraped = cv.warpPerspective(img, M, (420, 594))
cv.imshow('wraped', wraped)
cv.waitKey(0)
cv.destroyAllWindows()