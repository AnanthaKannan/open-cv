import numpy as np
import cv2 as cv

path = "../images/hand.jpg"
img = cv.imread(path)
img = cv.resize(img, None, fx=0.50, fy=0.50)
orignial_img = img.copy()
img_original = img.copy()

# gray scale and binarize
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY_INV)

# find contours
contours, hierarchy = cv.findContours(thresh.copy(), cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

# Iterate through each contours and contours the bounding rectangle
for c in contours:
    x,y,w,h = cv.boundingRect(c)
    cv.rectangle(orignial_img, (x,y),(x+w, y+h), (0,0,255), 2)
    cv.imshow('orignial_img', orignial_img)

cv.waitKey(0)

# Iterate through each contours and compute the approx contours
for c in contours:
    accuracy = 0.001 * cv.arcLength(c, True)
    approx = cv.approxPolyDP(c, accuracy, True)
    cv.drawContours(img, [approx], 0, (0,255,0), 2)
    cv.imshow('apprxply', img)

cv.waitKey(0)


# CONVEX HELL
# sort contours by area and then remove the largest frame contour
n = len(contours) - 1
sort_contours = sorted(contours, key=cv.contourArea, reverse=False)[:n]

# Iteration through contours and draw the convex hull
for c in contours:
    hull = cv.convexHull(c)
    cv.drawContours(img_original, [hull], 0, (0, 255, 0), 2)
    cv.imshow('hull', img_original)

cv.waitKey(0)
cv.destroyAllWindows()

