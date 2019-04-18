from tensorflow.keras.models import Sequential, Model, load_model
from tensorflow.keras.layers import Dense, Input, Conv2D, Flatten, Dropout
from tensorflow.keras.wrappers.scikit_learn import KerasRegressor
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import cross_val_score, KFold, train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.datasets import make_regression
from json import JSONDecoder
from database.repositories.ModelBlobRepository import ModelBlobRepository
from database.models.Blob import Blob
from base64 import b64decode

import matplotlib.pyplot as plt
import pandas as pd
import cv2
import numpy as np
import uuid
import os

modelBlobRepo = ModelBlobRepository()

def create_user_model(userId):
	model = load_model('pretrained.h5')

	x = model.output
	x = Dense(256, activation='relu')(x)
	x = Dropout(0.5)(x)
	x = Dense(256, activation='relu')(x)
	predictions = Dense(4, activation='linear')(x)

	transfer_model = Model(inputs = model.input, outputs = predictions)
	transfer_model.compile(optimizer = "adam", loss = 'mse', metrics=['mean_absolute_error', 'mean_squared_error'])

	return transfer_model

def train_user_model(userId, imageBase64, contrast, brightness, temperature, saturation):
	image = b64decode(imageBase64)
	imageName = str(uuid.uuid4()) + '.jpg'

	with open(imageName, 'wb') as file:
		file.write(image)

	X = [cv2.resize(cv2.imread(imageName, 1), (100,100))]
	os.remove(imageName)
	y = [contrast, brightness, temperature, saturation]

	datagen = ImageDataGenerator(
		rotation_range=360,
		zoom_range=[0.5, 1.5],
		horizontal_flip=True,
		vertical_flip=True,
		validation_split=0.2,
		shear_range=30
	)

	model = get_user_model(userId)
	model.fit_generator(datagen.flow(X, y, batch_size=32), epochs=2, verbose=1)
	save_user_model(model, userId)

def run_user_model(userId, imageBase64):
	imageBytes = b64decode(imageBase64)
	imageName = str(uuid.uuid4()) + '.jpg'

	with open(imageName, 'wb') as file:
		file.write(imageBytes)

	image = cv2.resize(cv2.imread(imageName, 1), (100,100))
	os.remove(imageName)
	model = get_user_model(userId)

	return model(image)


def get_user_model(userId):
	try:
		modelBlob = modelBlobRepo.read(userId)
	except:
		return create_user_model(userId)
	
	with open(userId + '.h5', 'wb') as file:
		file.write(modelBlob.content)

	model = load_model(userId + '.h5')
	os.remove(userId + '.h5')

	return model

def save_user_model(model, userId):
	model.save(userId + '.h5')

	with open(userId + '.h5', 'rb') as file:
		modelBytes = file.read()

	modelBlobRepo.create(modelBytes, userId)

	os.remove(userId + '.h5')