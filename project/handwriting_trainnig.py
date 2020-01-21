from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D
from keras.optimizers import SGD
from keras.utils import np_utils
import cv2 as cv
import numpy as np
import sys

# load the minist data set
(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(x_train.shape)

# set the shape
# let store number or rows and columns
img_rows = x_train[0].shape[0]
img_cols = x_train[1].shape[0]

# Our original image shape of (60000, 28, 28) to (60000, 28, 28)
x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)

# store the shape of single image
input_shape = (img_rows, img_cols, 1)

# change our image type to float32 data type
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

# Normailze our data  by changing range from (0 to 255) to (0 to 1)
x_train /= 255
x_test /= 255


# Hot one encoding
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

num_classes = y_test.shape[1]
num_pixels = x_train.shape[1] * x_train.shape[2]

sys.exit()

# create model
model = Sequential()
model.add(Conv2D(32, kernel_size=(3,3), activation='relu', input_shape = input_shape))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer=SGD(0.01), metrics=['accuracy'])
print('summary', model.summary)


# Train our model
batch_size = 32
epochs = 1

history = model.fit(x_train, y_train, batch_size=batch_size, 
            epochs=epochs, verbose=1, validation_data=(x_test, y_test))

score = model.evaluate(x_test, y_test, verbose=0)
print(score)

# Load your model
model.save('trainedmode.h5')
print('model saved')


# for i in range(0,6):
#     random_num = np.random.randint(0, len(x_train))
#     img = x_train[random_num]
#     window_name = 'randow' + str(i)
#     cv.imshow(window_name, img)
#     cv.waitKey(0)

# cv.destroyAllWindows()