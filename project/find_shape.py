import numpy as np
import cv2 as cv

template = cv.imread('../images/circle.jpg', 0)
cv.imshow('template', template)
cv.waitKey()


cv.destroyAllWindows()