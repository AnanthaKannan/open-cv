from keras.models import load_model
from keras.datasets import mnist
from keras.preprocessing import image
from keras import backend as k
import cv2 as cv
import numpy as np
import sys

classifiers = load_model('trainedmode.h5')
# image_path = "number0_.png"
image_path = "4.jpg"
# image_path = "5.jpg"
# image_path = "2.png"

(x_train, y_train), (x_test, y_test) = mnist.load_data()


img_arr = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
resized_image = cv.resize(img_arr, (28, 28))
input_img = resized_image
original_img = input_img
input_img = input_img.reshape(1, 28, 28, 1)
res = str(classifiers.predict_classes(input_img, 1, verbose=0)[0])
window_name = "window" + str(res)
cv.imshow(window_name, original_img)
cv.waitKey(0)
print("result", res)
cv.destroyAllWindows()


sys.exit()

for i in range(0, 3):
    random_num = np.random.randint(0, len(x_train))
    input_img = x_train[random_num]
    original_img = input_img
    input_img = input_img.reshape(1, 28, 28, 1)
    res = str(classifiers.predict_classes(input_img, 1, verbose=0)[0])
    window_name = "window" + str(res)
    cv.imshow(window_name, original_img)
    cv.waitKey(0)
    print("result", res)


cv.destroyAllWindows()