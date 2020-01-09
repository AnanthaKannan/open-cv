import cv2 as cv
import numpy as np

path = "../images/chess.jpg"
img = cv.imread(path)
img = cv.resize(img, None, fx=0.50, fy=0.50)
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# we specify top 50 corners
corners = cv.goodFeaturesToTrack(img_gray, 10, 0.01, 15)
print(corners)
for corner in corners:
    x,y = corner[0]
    x = int(x)
    y = int(y)
    cv.rectangle(img, (x-10, y-10), (x+10, y+10), (0, 255, 0), 2)
    cv.imshow('haha', img)

# cv.imshow('corner found', img)
cv.waitKey(0)
cv.destroyAllWindows()











# import cv2 as cv
# import numpy as np

# path = ''
# img = cv.imread(path)

# cv.imshow('img', img)
# cv.waitKey(0)
# cv.destroyAllWindows()