from keras.models import Sequential,save_model, Model
from keras.layers import Dense, Input, Conv2D, Flatten
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.datasets import make_regression

from database.repositories.DatumRepository import DatumRepository
from database.repositories.ImageRepository import ImageRepository

import cv2
import os
import numpy as np

imageRepository = ImageRepository()
datumRepository = DatumRepository()

EPOCHS = 75
INIT_LR = 1e-3
BS = 32
IMAGE_DIMS = (100, 100, 3)

def dense_layers(X, y):
    '''
    A 2 dense layes model
    '''

    # y should ve in shape (n,5)

    ################################################################################
    # samples = 100
    # features = 64
    # X, y = make_regression(n_samples=samples, n_features=features, noise=0.1)
    # scalarX, scalarY = MinMaxScaler(), MinMaxScaler()
    # scalarX.fit(X)
    # scalarY.fit(y.reshape(samples,5))
    # X = scalarX.transform(X)
    # y = scalarY.transform(y.reshape(samples,5))
    ################################################################################

    model = Sequential()

    model.add(Conv2D(64, kernel_size=3, activation='relu', input_shape=IMAGE_DIMS))
    model.add(Conv2D(32, kernel_size=3, activation='relu'))
    model.add(Flatten())
    model.add(Dense(5, activation='linear'))

    model.summary()

    ###################################################################################

    # optimizer adam? loss mse?? metrics??
    # tune parameters
    model.compile(optimizer = "rmsprop", loss = 'binary_crossentropy', metrics=['accuracy'])

    # , validation_split=0.2
    history = model.fit(X, y, epochs=75, verbose=1)
    
    save_model(model)


def save_model(model):
    # serialize model to JSON
    model_json = model.to_json()
    with open("model.json", "w") as json_file:
        json_file.write(model_json)
    # serialize weights to HDF5
    model.save_weights("model.h5")

def image_preprocessing():
    # fixme 'float' object has no attribute 'value'

    #FIXME IMPROT FROM DATASET
    # y = datumRepository.read()
    # y = [i.__dict__ for i in y]
    # X = ImageRepository.read()
    # X = [i.__dict__ for i in X]
    # return X,y

    #import from local dir
    dircs = os.listdir('./var/')
    paths = ['./var/'+p for p in dircs]
    for path in paths:
        X = [cv2.resize(cv2.imread(path, 1),(100,100)) for path in paths]
    y = np.random.randint(0, high=100, size=(114,5))
    X = np.array(X)
    print(X.shape, y.shape)
    return X, y

if __name__ == "__main__":
    X, y = image_preprocessing()
    dense_layers(X, y)




