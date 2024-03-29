from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Input, Conv2D, Flatten
from tensorflow.keras.wrappers.scikit_learn import KerasRegressor
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import cross_val_score, KFold, train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.datasets import make_regression
from json import JSONDecoder

import tensorflowjs as tfjs
import matplotlib.pyplot as plt
import pandas as pd
import cv2
import numpy as np

EPOCHS = 75
INIT_LR = 1e-3
BS = 32
IMAGE_DIMS = (100, 100, 3)

def train_model(X_train, y_train, X_test, y_test):

    datagen = ImageDataGenerator(
    	rotation_range=360,
    	zoom_range=[0.5, 1.5],
    	horizontal_flip=True,
    	vertical_flip=True,
    	validation_split=0.2,
    	shear_range=30
    )

    model = Sequential()

    model.add(Conv2D(64, kernel_size=3, activation='relu', input_shape=IMAGE_DIMS))
    model.add(Conv2D(32, kernel_size=3, activation='relu'))
    model.add(Flatten())
    model.add(Dense(4, activation='linear'))

    model.summary()

    # optimizer = "rmsprop" 
    model.compile(optimizer = "adam", loss = 'mse', metrics=['mean_absolute_error', 'mean_squared_error'])

    # , validation_split=0.2
    history = model.fit_generator(datagen.flow(X_train, y_train, batch_size=32), validation_data=datagen.flow(X_test, y_test), epochs=16, verbose=1)
    # history = model.fit(X_train, y_train, epochs=10, verbose=1)

    # model.evaluate(X_test, y_test)

    return model, history

def plot_history(history):
	hist = pd.DataFrame(history.history)
	hist['epoch'] = history.epoch

	plt.figure()
	plt.xlabel('Epoch')
	plt.ylabel('Mean Abs Error [MPG]')
	plt.plot(hist['epoch'], hist['mean_absolute_error'],
			label='Train Error')
	plt.plot(hist['epoch'], hist['val_mean_absolute_error'],
			label = 'Val Error')
	plt.ylim([0,5])
	plt.legend()

	plt.figure()
	plt.xlabel('Epoch')
	plt.ylabel('Mean Square Error [$MPG^2$]')
	plt.plot(hist['epoch'], hist['mean_squared_error'],
			label='Train Error')
	plt.plot(hist['epoch'], hist['val_mean_squared_error'],
			label = 'Val Error')
	plt.ylim([0,20])
	plt.legend()
	plt.show()


def save_model(model):
    # Serialize to tensorflowjs model
    tfjs.converters.save_keras_model(model, 'export')

def load_dataset():
    with open('./dataset/dataset.json', 'r') as file:
        dataset = JSONDecoder().decode(file.read())
	
    X = [cv2.resize(cv2.imread('./dataset/' + item['blobName'] + '.jpg', 1), (100, 100)) for item in dataset]
    X = np.array(X)
    y = [[item['contrast'], item['brightness'], item['saturation'], item['temperature']] for item in dataset]
    y = np.array(y)

    print(X.shape, y.shape)
    return X, y

if __name__ == "__main__":
    X, y = load_dataset()
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    trained_model, history = train_model(X_train, y_train, X_test, y_test)
    plot_history(history)
    save_model(trained_model)
