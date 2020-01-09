import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# create a black image
image = np.zeros((512, 512, 3), np.uint8)
# make this as a black and white
# image_bw = np.zeros((512, 512), np.uint8)

# cv.imshow('black', image)
# cv.imshow('image_bw', image_bw)

# draw the line
# image, starting, ending, color(b, g, r), thikness
# if you give the thikness as a negative value then it's background color will added
cv.line(image,(0,0), (511, 511), (255, 127, 0), 5)
cv.rectangle(image,(100,100), (300, 250), (0, 127, 100), 5)
# image, center, radius, color, fill
cv.circle(image,(350,350), 100, (15, 75, 50), -1)

# difine the pointes
points = np.array([[10, 50], [400, 50], [90, 200], [50, 500]], np.int32)
points = points.reshape((-1, 1, 2))
# below True or false is the polygon close or not
cv.polylines(image, [points], True, (0, 0, 255), 3)


# Add text
# image, textDisplay, bottom left starting point, font, font size, color, thickness
cv.putText(image, 'Hello world!', (75, 300), cv.FONT_HERSHEY_COMPLEX, 2, (100, 170, 0), 3)

cv.imshow('line', image)
cv.waitKey(0)
cv.destroyAllWindows()
