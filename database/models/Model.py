from azure.cosmosdb.table.models import Entity

class Model():
	def __init__(self, other):
		self.PartitionKey = other.PartitionKey if hasattr(other, 'PartitionKey') else ''

		if isinstance(other, Entity):
			self.RowKey = other.RowKey
		else:
			self.RowKey = other['RowKey']