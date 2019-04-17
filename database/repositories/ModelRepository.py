from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity, EntityProperty, EdmType
from string import Template
from database.models.Model import Model

class ModelRepository:
	def __init__(self):
		self.tableService = TableService(connection_string='DefaultEndpointsProtocol=https;AccountName=styles-db;AccountKey=GKnYYUiWGAPVQuu7qjqPDUrfESoMQLrQ2YZmAahqW6WnSkwICAxd8yj3G2OlZMA27VPVmAECrcrBwq8bJfmjXg==;TableEndpoint=https://styles-db.table.cosmos.azure.com:443/;')
		self.tableName = 'models'
		self.PartitionKey = 'models'

	def create(self, model):
		entity = Entity()
		entity.PartitionKey = self.PartitionKey
		entity.RowKey = model.RowKey

		return self.tableService.insert_entity(self.tableName, entity)

	def read(self, RowKey = None):
		if RowKey is None:
			# Get all
			queryTemplate = Template("PartitionKey eq '$PartitionKey'")
			result = self.tableService.query_entities(self.tableName, filter=queryTemplate.substitute(PartitionKey=self.PartitionKey))
			result = [Model(item) for item in result]
			return result

		# Get by id
		result = self.tableService.get_entity(self.tableName, self.PartitionKey, RowKey)
		result = Model(result)
		return result

	def update(self, entity):
		self.tableService.update_entity(self.tableName, entity)

	def delete(self, RowKey):
		self.tableService.delete_entity(self.tableName, self.PartitionKey, RowKey)