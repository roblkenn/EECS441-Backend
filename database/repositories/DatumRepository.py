from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity, EntityProperty, EdmType
from os import environ
from database.models.Datum import Datum
from string import Template
import uuid

def generateRowKey():
	return str(uuid.uuid4())

class DatumRepository:
	
	def __init__(self):
		self.tableService = TableService(connection_string='DefaultEndpointsProtocol=https;AccountName=styles-db;AccountKey=GKnYYUiWGAPVQuu7qjqPDUrfESoMQLrQ2YZmAahqW6WnSkwICAxd8yj3G2OlZMA27VPVmAECrcrBwq8bJfmjXg==;TableEndpoint=https://styles-db.table.cosmos.azure.com:443/;')
		self.tableName = 'dataset'
		self.PartitionKey = 'dataset'

	# Returns the created Entity object
	def create(self, datum):
		entity = Entity()
		entity.PartitionKey = self.PartitionKey
		entity.RowKey = generateRowKey()
		entity.blobName = EntityProperty(EdmType.STRING, datum.blobName)
		entity.contrast = EntityProperty(EdmType.DOUBLE, datum.contrast)
		entity.brightness = EntityProperty(EdmType.DOUBLE, datum.brightness)
		entity.temperature = EntityProperty(EdmType.DOUBLE, datum.temperature)
		entity.saturation = EntityProperty(EdmType.DOUBLE, datum.saturation)

		return self.tableService.insert_entity(self.tableName, entity)

	# Returns either an Entity or a list of Entity objects
	def read(self, RowKey = None):
		if RowKey is None:
			# Get all
			queryTemplate = Template("PartitionKey eq '$PartitionKey'")
			result = self.tableService.query_entities(self.tableName, filter=queryTemplate.substitute(PartitionKey=self.PartitionKey))
			result = [Datum(item) for item in result]
			return result
		else:
			# Get by id
			result = self.tableService.get_entity(self.tableName, self.PartitionKey, RowKey)
			result = Datum(result)
			return result

	# Returns the updated Entity object
	def update(self, entity):
		self.tableService.update_entity(self.tableName, entity)

	# Returns a succeeded bool
	def delete(self, RowKey):
		self.tableService.delete_entity(self.tableName, self.PartitionKey, RowKey)
	
