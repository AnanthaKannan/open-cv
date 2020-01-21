from keras.datasets import mnist

# load the minist data set
(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(x_train.shape)