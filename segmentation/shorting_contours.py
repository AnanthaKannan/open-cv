
import numpy as np
import cv2 as cv

path = "../images/shapes.png"
img = cv.imread(path)
img = cv.resize(img, None, fx=2, fy=2)
# original_img = img
blank_img = np.zeros(img.shape)
# grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# find canny edges
edged = cv.Canny(img, 60, 200)
# finding contours
contours, hierarchy = cv.findContours(edged, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
print("Number of contours fond : " + str(len(contours)))

# Sort contours Large to Small
sort_contours = sorted(contours, key=cv.contourArea, reverse=True)

for c in sort_contours:
    cv.drawContours(img, [c], -1, (0, 255, 0), 2)
    cv.waitKey()
    cv.imshow('coutes area', img)

# draw all contours in black image
cv.drawContours(blank_img, contours, -1, (0, 255, 0), 2)
# cv.imshow('blank_img', blank_img)

# draw all contorurs in original image
cv.drawContours(img, contours, -1, (0, 255, 0), 2)
# cv.imshow('original', img)

cv.waitKey(0)
cv.destroyAllWindows()