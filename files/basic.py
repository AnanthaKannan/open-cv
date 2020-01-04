import numpy as np
import cv2 as cv

path = "../images/first.jpg"
# to read the image
input = cv.imread(path)
input = cv.resize(input,(960,600))
# print(input)
# find the shape
print(input.shape)
print('Height', int(input.shape[0]), 'px')
print('Height', int(input.shape[1]), 'px')
# to show the image
window_title = "Hello world"
# cv.imshow(window_title, input)

# waitKey used for click any button and the window will destroy
cv.waitKey(0)

# to write the image

cv.imwrite('output.jpg', input)

# Gray scale image (Black and white)
# to change the color
gray_image = cv.cvtColor(input, cv.COLOR_BGR2GRAY)
# cv.imshow(window_title, gray_image)
cv.waitKey(0)

# gray scale imge for another way
img = cv.imread('../images/first.jpg',0)
# print(img)
# cv.imshow('window heading', img)
cv.waitKey(0)


# HSV H: 0-180, S: 0-255, V: 0-255
hsv_img = cv.cvtColor(input, cv.COLOR_RGB2HSV)
# cv.imshow('HSV image', hsv_img)
# cv.imshow('Hue channel', hsv_img[:,:,0])
# cv.imshow('Saturation channel', hsv_img[:,:,1])
# cv.imshow('Value channel', hsv_img[:,:,2])
cv.waitKey(0)

# Individual channels in an RGB image
B, G, R = cv.split(input)
# cv.imshow('B', B)
# cv.imshow('G', G)
# cv.imshow('R', R)
# remark the original image
merge = cv.merge([B, G, R])
# cv.imshow('merge', merge)
# amplify the blue collor
# cv.imshow('ampify', cv.merge([B, G , R]))



cv.waitKey(0)
cv.destroyAllWindows()