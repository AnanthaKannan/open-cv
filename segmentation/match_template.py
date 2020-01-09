import cv2 as cv
import numpy as np

path = ''
template_path = ''
# load the image and convert into gray scale

img = cv.imread(path)
img = cv.resize(img, None, fx=0.25, fy=0.25)
cv.imshow('original', img)
cv.waitKey(0)
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# load template
template = cv.imread(template_path, 0)

result = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

# create a bounding box
top_left = max_loc
bottom_right = (top_left[0] + 50, top_left[1] + 50)
cv.rectangle(img, top_left, bottom_right, (0, 0, 255), 5)

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()