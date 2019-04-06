from keras.models import Sequential,save_model
from keras.layers import Dense, Input, Conv2D, Flatten
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.datasets import make_regression

from database.repositories.DatumRepository import DatumRepository
from database.repositories.ImageRepository import ImageRepository

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

    model.add(Conv2D(64, kernel_size=3, activation=’relu’, input_shape=IMAGE_DIMS))
    model.add(Conv2D(32, kernel_size=3, activation=’relu’))
    model.add(Flatten())

    #################################################################################
    # don't if this is nessecary 

    model.summary()

    contra_out = Dense(1,  activation='linear')
    bri_out = Dense(1,  activation='linear')
    temp_out = Dense(1,  activation='linear')
    satu_out = Dense(1,  activation='linear')
    out5 = Dense(1,  activation='linear')

    model = Model(inputs=inputs, outputs=[contra_out,bri_out,temp_out,satu_out,out5])

    ###################################################################################

    # optimizer adam? loss mse?? metrics??
    # tune parameters
    model.compile(optimizer = "rmsprop", loss = 'binary_crossentropy', metrics=['accuracy'])

    # , validation_split=0.2
    history = model.fit(X, y, epochs=75, batch_size=50,  verbose=1)
    
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
    y = datumRepository.read()
    y = [i.__dict__ for i in y]
    X = ImageRepository.read()
    X = [i.__dict__ for i in X]
    return X,y

if __name__ == "__main__":
    X, y = image_preprocessing()
    dense_layers(X, y)




