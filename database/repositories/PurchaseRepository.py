from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity, EntityProperty, EdmType
from string import Template
from database.models.Purchase import Purchase

class PurchaseRepository:
	def __init__(self):
		self.tableService = TableService(connection_string='DefaultEndpointsProtocol=https;AccountName=styles-db;AccountKey=GKnYYUiWGAPVQuu7qjqPDUrfESoMQLrQ2YZmAahqW6WnSkwICAxd8yj3G2OlZMA27VPVmAECrcrBwq8bJfmjXg==;TableEndpoint=https://styles-db.table.cosmos.azure.com:443/;')
		self.tableName = 'purchases'
		self.PartitionKey = 'purchases'

	def create(self, purchase):
		entity = Entity()
		entity.PartitionKey = self.PartitionKey
		entity.RowKey = purchase.RowKey
		entity.transaction_id = EntityProperty(EdmType.INT32, purchase.transaction_id)
		entity.product_id = EntityProperty(EdmType.INT32, purchase.product_id)
		entity.quantity = EntityProperty(EdmType.INT32, purchase.quantity)
		entity.purchased_at = EntityProperty(EdmType.DATETIME, purchase.purchased_at)
		entity.response = EntityProperty(EdmType.STRING, purchase.response)

		return self.tableService.insert_entity(self.tableName, entity)

	def read(self, RowKey = None):
		if RowKey is None:
			# Get all
			queryTemplate = Template("PartitionKey eq '$PartitionKey'")
			result = self.tableService.query_entities(self.tableName, filter=queryTemplate.substitute(PartitionKey=self.PartitionKey))
			result = [Purchase(item) for item in result]
			return result

		# Get by id
		result = self.tableService.get_entity(self.tableName, self.PartitionKey, RowKey)
		result = Purchase(result)
		return result

	def update(self, entity):
		self.tableService.update_entity(self.tableName, entity)

	def delete(self, RowKey):
		self.tableService.delete_entity(self.tableName, self.PartitionKey, RowKey)
