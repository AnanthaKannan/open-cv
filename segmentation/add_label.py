
import numpy as np
import cv2 as cv

def x_cord_contours(contours):
    # return X cordinate for the contours centroid
    if cv.contourArea(contours) > 10:
        M = cv.moments(contours)
        return(int(M['m10']/M['m00']))

def label_contour_center(img, c, i):
    # place a red circle on the center of contours
    M = cv.moments(c)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    # cv.circle(img, (cx, cy), 10, (0, 0, 255), -1)
    cv.putText(img, str(i+1), (cx-10, cy+10), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    return img

path = "../images/shapes.png"
img = cv.imread(path)
img = cv.resize(img, None, fx=2, fy=2)
original_img = img.copy()
blank_img = np.zeros(img.shape)
# grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# find canny edges
edged = cv.Canny(img, 60, 200)
# finding contours
contours, hierarchy = cv.findContours(edged, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
print("Number of contours fond : " + str(len(contours)))

# put dot in the center of the image
# for (i, c) in enumerate(contours):
#     orig = label_contour_center(img, c, i)
#     cv.waitKey()
#     cv.imshow('coutes area', orig)

# Sort contours Large to Small
left_to_right = sorted(contours, key=x_cord_contours, reverse=False)

for (i, c) in enumerate(left_to_right):
    cv.drawContours(img, [c], -1, (0, 255, 0), 2)
    labled_img = label_contour_center(img, c, i)
    cv.waitKey()
    cv.imshow('coutes area', labled_img)

    # cropped the contours
    (x, y, w, h) = cv.boundingRect(c)
    cropped_contours = original_img[y:y + h, x:x + w]
    cv.imshow('croped', cropped_contours)

# draw all contours in black image
cv.drawContours(blank_img, contours, -1, (0, 255, 0), 2)
# cv.imshow('blank_img', blank_img)

# draw all contorurs in original image
cv.drawContours(img, contours, -1, (0, 255, 0), 2)
# cv.imshow('original', img)

cv.waitKey(0)
cv.destroyAllWindows()