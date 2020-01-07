# used to draw the outline of the mask

import numpy as np
import cv2 as cv

path = "../images/boxes.jpg"
img = cv.imread(path)

# grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# find canny edges
edged = cv.Canny(img, 30, 200)
cv.imshow('edged', edged)

# finding contours
# use a copy of your image e.g. edged.copy(), since findCountours alters the image
contours, hierarchy = cv.findContours(edged, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

print("Number of contours fond : " + str(len(contours)))
# draw all contours
# the third parameter -1 is used to draw all contours, if you are select 
# the index then that contours only drawed, 
# (0, 255, 0) is the color
# 2 is the depth of the mask 
cv.drawContours(img, contours, -1, (0, 255, 0), 2)
cv.imshow('contours', img)

cv.waitKey(0)
cv.destroyAllWindows()