from azure.cosmosdb.table.models import Entity

class Datum:
	def __init__(self, other):
		self.PartitionKey = other.PartitionKey if hasattr(other, 'PartitionKey') else ''
		self.RowKey = other.RowKey if hasattr(other, 'RowKey') else ''

		self.imageBase64 = other['imageBase64']
		self.contrast = other['contrast']
		self.brightness = other['brightness']
		self.saturation = other['saturation']
		self.temperature = other['temperature']
