import pandas as pd
import tensorflow as tf

def prepare_data(val_size):
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0

    X_valid, X_train = x_train[:val_size] , x_train[val_size:] 
    y_valid, y_train = y_train[:val_size], y_train[val_size:]

    return X_train, y_train, X_valid, y_valid, x_test, y_test
