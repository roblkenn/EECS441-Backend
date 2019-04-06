from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity, EntityProperty, EdmType
from string import Template
from database.models.User import User

class UserRepository:
	def __init__(self):
		self.tableService = TableService(connection_string='DefaultEndpointsProtocol=https;AccountName=styles-db;AccountKey=GKnYYUiWGAPVQuu7qjqPDUrfESoMQLrQ2YZmAahqW6WnSkwICAxd8yj3G2OlZMA27VPVmAECrcrBwq8bJfmjXg==;TableEndpoint=https://styles-db.table.cosmos.azure.com:443/;')
		self.tableName = 'users'
		self.PartitionKey = 'users'

	def create(self, user):
		entity = Entity()
		entity.PartitionKey = self.PartitionKey
		entity.RowKey = user.RowKey

		return self.tableService.insert_entity(self.tableName, entity)

	def read(self, RowKey = None):
		if RowKey is None:
			# Get all
			queryTemplate = Template("PartitionKey eq '$PartitionKey'")
			result = self.tableService.query_entities(self.tableName, filter=queryTemplate.substitute(PartitionKey=self.PartitionKey))
			result = [User(item) for item in result]
			return result

		# Get by id
		result = self.tableService.get_entity(self.tableName, self.PartitionKey, RowKey)
		result = User(result)
		return result

	def update(self, entity):
		self.tableService.update_entity(self.tableName, entity)

	def delete(self, RowKey):
		self.tableService.delete_entity(self.tableName, self.PartitionKey, RowKey)