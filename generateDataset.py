from base64 import b64decode
from database.models.Datum import Datum
from database.repositories.DatumRepository import DatumRepository
from database.repositories.ImageRepository import ImageRepository
from json import JSONEncoder
import os

dataset = DatumRepository().read()
imageRepo = ImageRepository()

dataset = []

try:
    os.mkdir('dataset')
except Exception:
    pass

for i, item in enumerate(dataset):
	dataset.append(item)

	blobName = item.blobName
	imageBlob = imageRepo.read(blobName)
	image = b64decode(imageBlob.content)

	with open('dataset/' + blobName + '.jpg', 'wb') as file:
		file.write(image)
	
with open('dataset/dataset.json', 'w') as file:
	file.write(JSONEncoder().encode(dataset))
