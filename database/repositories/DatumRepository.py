from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
from os import environ
from database.models.Datum import Datum
from string import Template
import uuid

def generateRowKey():
	return str(uuid.uuid4())

class DatumRepository:
	
	def __init__(self):
		self.tableService = TableService(connection_string=environ['CUSTOMCONNSTR_DatabaseConnectionString'])
		#self.tableService.create_table('dataset')
		self.tableName = 'dataset'
		self.PartitionKey = 'dataset'

	# Returns the created Entity object
	def create(self, datum):
		entity = Entity()
		entity.PartitionKey = self.PartitionKey
		entity.RowKey = generateRowKey()
		entity.imageBase64 = datum.imageBase64
		entity.contrast = datum.contrast
		entity.brightness = datum.brightness
		entity.highlights = datum.highlights
		entity.tempurature = datum.tempurature
		entity.saturation = datum.saturation

		return self.tableService.insert_entity(self.tableName, entity)

	# Returns either an Entity or a list of Entity objects
	def read(self, RowKey = None):
		if RowKey is None:
			# Get all
			queryTemplate = Template("PartitionKey eq '$PartitionKey'")
			return list(self.tableService.query_entities(self.tableName, filter=queryTemplate.substitute(PartitionKey=self.PartitionKey)))
		else:
			# Get by id
			return self.tableService.get_entity(self.tableName, self.PartitionKey, RowKey)

	# Returns the updated Entity object
	def update(self, entity):
		self.tableService.update_entity(self.tableName, entity)

	# Returns a succeeded bool
	def delete(self, RowKey):
		self.tableService.delete_entity(self.tableName, self.PartitionKey, RowKey)
	
