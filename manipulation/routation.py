
import numpy as np
import cv2 as cv

path = "../images/first.jpg"
# to read the image
img = cv.imread(path)
img = cv.resize(img,(960,600))

# store height and width of the image
height, width = img.shape[:2]

# Divee by two rotoate the image around its center
# rotation center x, rotation centery, angle of routation, scale 
rotation_matrix = cv.getRotationMatrix2D((width/2, height/2), 90, 1)
rotate_image = cv.warpAffine(img, rotation_matrix, (width, height))
cv.imshow('rotate_image', rotate_image)


# Remove the black space around the image
transpose = cv.transpose(img)
cv.imshow('transpose', transpose)

cv.waitKey(0)
cv.destroyAllWindows()