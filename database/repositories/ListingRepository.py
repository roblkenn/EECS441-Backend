from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity, EntityProperty, EdmType
from string import Template
from database.models.Listing import Listing

class ListingRepository:
	def __init__(self):
		self.tableService = TableService(connection_string='DefaultEndpointsProtocol=https;AccountName=styles-db;AccountKey=GKnYYUiWGAPVQuu7qjqPDUrfESoMQLrQ2YZmAahqW6WnSkwICAxd8yj3G2OlZMA27VPVmAECrcrBwq8bJfmjXg==;TableEndpoint=https://styles-db.table.cosmos.azure.com:443/;')
		self.tableName = 'listings'
		self.PartitionKey = 'listings'

	def create(self, listing):
		entity = Entity()
		entity.PartitionKey = self.PartitionKey
		entity.RowKey = listing.RowKey
		entity.title = EntityProperty(EdmType.STRING, listing.title)
		entity.price = EntityProperty(EdmType.INT32, listing.price)
		entity.description = EntityProperty(EdmType.STRING, listing.description)
		entity.username = EntityProperty(EdmType.STRING, listing.username)

		return self.tableService.insert_entity(self.tableName, entity)

	def read(self, RowKey = None):
		if RowKey is None:
			# Get all
			queryTemplate = Template("PartitionKey eq '$PartitionKey'")
			result = self.tableService.query_entities(self.tableName, filter=queryTemplate.substitute(PartitionKey=self.PartitionKey))
			result = [Listing(item) for item in result]
			return result

		# Get by id
		result = self.tableService.get_entity(self.tableName, self.PartitionKey, RowKey)
		result = Listing(result)
		return result

	def update(self, entity):
		self.tableService.update_entity(self.tableName, entity)

	def delete(self, RowKey):
		self.tableService.delete_entity(self.tableName, self.PartitionKey, RowKey)