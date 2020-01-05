# Useful when scalling images in object detection
import numpy as np
import cv2 as cv

path = "../images/first.jpg"
img = cv.imread(path)
img = cv.resize(img, None, fx=0.25, fy=0.25)

height, width = img.shape[:2]
# let's get the starting pixel coordinates (top left of cropping rectangle)
start_row, start_col = int(height * .25), int(width * .25)

# let's ending pixel coordinates ( bottom right)
end_row, end_col = int(height * .75), int(width * .75)

# simply use indexing to crop out the rectangle we desigre
cropped_img = img[start_row: end_row, start_col: end_col]

cv.imshow('cropped_img', cropped_img)
cv.waitKey(0)
# cv.destroyAllWindows()