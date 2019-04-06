from keras.models import Sequential,save_model
from keras.layers import Dense, Input
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.pipeline import Pipeline

from database.repositories.DatumRepository import DatumRepository
from database.repositories.ImageRepository import ImageRepository

imageRepository = ImageRepository()
datumRepository = DatumRepository()

EPOCHS = 75
INIT_LR = 1e-3
BS = 32
IMAGE_DIMS = (96, 96, 3)

def machinelearning(X, y):

	samples = X.shape[0]
	features = np.prod(X.shape[1:])

	X, y = make_regression(n_samples=samples, n_features=features, noise=0.1)
	scalarX, scalarY = MinMaxScaler(), MinMaxScaler()
	scalarX.fit(X)
	scalarY.fit(y.reshape(samples,5))
	X = scalarX.transform(X)
	y = scalarY.transform(y.reshape(samples,5))

	model = Sequential()

	model.add(Dense(64, input_dim=features, kernel_initializer='normal', activation='relu'))
	model.add(Dense(64, activation='relu'))

	model.summary()

	contra_out = Dense(1,  activation='linear')
	bri_out = Dense(1,  activation='linear')
	temp_out = Dense(1,  activation='linear')
	satu_out = Dense(1,  activation='linear')
	out5 = Dense(1,  activation='linear')

	model = Model(inputs=inputs, outputs=[contra_out,bri_out,temp_out,satu_out,out5])
	# optimizer adam? loss mse?? metrics??
	model.compile(optimizer = "rmsprop", loss = 'binary_crossentropy', metrics=['accuracy'])

	history = model.fit(X, y, epochs=150, batch_size=50,  verbose=1, validation_split=0.2)
	
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
	machinelearning(X, y)




