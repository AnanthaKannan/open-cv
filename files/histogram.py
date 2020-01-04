import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

path = "../images/first.jpg"
input = cv.imread(path)
input = cv.resize(input,(960,600))
histogram = cv.calcHist([input], [0], None, [256], [0,256])
# ravel used to flatern our image array
# print(input.ravel())
plt.hist(input.ravel(), 256, [0, 256])
# plt.hist(histogram)
plt.show()

# viewing seperate color channal
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histogram2 = cv.calcHist([input], [i], None, [256], [0,256])
    plt.plot(histogram2, color=col)
    plt.xlim([0, 256])

plt.show()