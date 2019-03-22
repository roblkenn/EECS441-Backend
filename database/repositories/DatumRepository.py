from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
from os import environ
from database.models.Datum import Datum

class DatumRepository:
	
	def __init__(self):
		self.tableService = TableService(connection_string=environ['CUSTOMCONNSTR_DatabaseConnectionString'])

	# Returns the created Entity object
	def create(self, entity):
		pass

	# Returns either an Entity or a list of Entity objects
	def read(self, id = None):
		if id is None:
			# Get all
			pass
		else:
			# Get by id
			pass

	# Returns the updated Entity object
	def update(self, entity):
		pass

	# Returns a succeeded bool
	def delete(self, entity):
		pass
	
