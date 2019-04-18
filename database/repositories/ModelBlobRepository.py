from azure.storage.blob.baseblobservice import BaseBlobService
from azure.storage.blob.blockblobservice import BlockBlobService
from database.models.Blob import Blob

class ModelBlobRepository:
    def __init__(self):
        self.blockBlobService = BlockBlobService(account_name='stylesblobstorage', account_key='B4qA7PlPtEk+y/zDsn16+0KXjlLJpcmnZb9C/CLDTbU9PzI294Ithc6j3y+jBz6j4KKAe3LcqadtkKe24JhxIw==')
        self.blobService = BaseBlobService(account_name='stylesblobstorage', account_key='B4qA7PlPtEk+y/zDsn16+0KXjlLJpcmnZb9C/CLDTbU9PzI294Ithc6j3y+jBz6j4KKAe3LcqadtkKe24JhxIw==')
        self.containerName = 'models'

    def create(self, modelBytes, userId):
        self.blockBlobService.create_blob_from_text(self.containerName, userId, modelBytes)
        return userId

    def read(self, blobName):
        blob = self.blobService.get_blob_to_text(self.containerName, blobName)
        return Blob(blob)

    def delete(self, blobName):
        return self.blobService.delete_blob(self.containerName, blobName)
