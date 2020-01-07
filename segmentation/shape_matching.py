import numpy as np
import cv2 as cv

template = cv.imread('../images/circle.jpg', 0)
cv.imshow('template', template)
cv.waitKey()

# Load the target image with the shape we're trying to match 
target = cv.imread('../images/shapes.png')
target_gray = cv.cvtColor(target, cv.COLOR_BGR2GRAY)

# threshold both images first before using cv.findContours
ret, thresh1 = cv.threshold(template, 127, 255, 0)
ret, thresh2 = cv.threshold(target_gray, 127, 255, 0)

# find contours from template 
contours, hierarcy = cv.findContours(thresh1, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)

# we need to sort the contours by area so that we can remove the largest
# contours which is the image outline
sort_contours = sorted(contours, key=cv.contourArea, reverse=True)

# We extract the secound largest contours which is will be our  template contours
template_contours = contours[1]

# find contours from target image
contours, hierarcy = cv.findContours(thresh2, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)

for c in contours:
    match = cv.matchShapes(template_contours, c, 1, 0.0)
    print(match)
    if match < 0.15:
        closest_contours = c
    else:
        closest_contours = []


cv.drawContours(target, [closest_contours], -1, (0, 255, 0), 2)
cv.imshow('contours', target)

cv.waitKey(0)
cv.destroyAllWindows()