
class Datum:
	def __init__(self, entity):
		self.entity = entity
		self.imageBase64 = entity.imageBase64
		self.contrast = entity.contrast
		self.brightness = entity.brightness
		self.saturation = entity.saturation
		self.tempurature = entity.tempurature
		self.highlights = entity.highlights
