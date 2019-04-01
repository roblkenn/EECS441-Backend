from azure.cosmosdb.table.models import Entity

class Datum:
	def __init__(self, other):
		try:
			self.PartitionKey = other.PartitionKey
		except:
			self.PartitionKey = None
		try:
			self.RowKey = other.RowKey
		except:
			self.RowKey = None

		self.imageBase64 = other.imageBase64
		self.contrast = other.contrast
		self.brightness = other.brightness
		self.saturation = other.saturation
		self.tempurature = other.tempurature

		if isinstance(other, Entity):
			self.contrast = other.contrast.value
			self.brightness = other.brightness.value
			self.saturation = other.saturation.value
			self.tempurature = other.tempurature.value
