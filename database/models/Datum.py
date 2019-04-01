
class Datum:
	def __init__(self, other):
		self.PartitionKey = other.PartitionKey or ''
		self.RowKey = other.RowKey or ''
		self.imageBase64 = other.imageBase64
		self.contrast = other.contrast
		self.brightness = other.brightness
		self.saturation = other.saturation
		self.tempurature = other.tempurature
		self.highlights = other.highlights
		
