import cv2
import matplotlib.pyplot as plt

path = "../images/first.jpg"
img = cv2.imread(path)

cv2.imshow('as', img)
# print(img)
plt.imshow(img)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

print('plot showed')