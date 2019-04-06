from azure.cosmosdb.table.models import Entity

class Listing:
	def __init__(self, other):
		self.PartitionKey = other.PartitionKey if hasattr(other, 'PartitionKey') else ''

		if isinstance(other, Entity):
			self.RowKey = other.RowKey
			self.title = other.title
			self.price = other.price.value
			self.description = other.description
			self.username = other.username
		else:
			self.RowKey = other['RowKey']
			self.title = other['title']
			self.price = other['price']
			self.description = other['description']
			self.username = other['username']
		

		