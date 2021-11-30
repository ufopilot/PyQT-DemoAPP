import json
from gui.functions.ui_functions import UIFunctions


# APP SETTINGS
# ///////////////////////////////////////////////////////////////
class Settings(object):
	def __init__(self, type=None):
		super(Settings, self).__init__()
		self.json_file = f"gui/settings/{type}_settings.json"
		self.settings_path = UIFunctions().resource_path(self.json_file)
		# DICTIONARY WITH SETTINGS
		# Just to have objects references
		self.items = {}

		# DESERIALIZE
		self.deserialize()
	# SERIALIZE JSON
	# ///////////////////////////////////////////////////////////////
	def serialize(self):
		# WRITE JSON FILE
		with open(self.settings_path, "w", encoding='utf-8') as write:
			json.dump(self.items, write, indent=4)

	# DESERIALIZE JSON
	# ///////////////////////////////////////////////////////////////
	def deserialize(self):
		# READ JSON FILE
		with open(self.settings_path, "r", encoding='utf-8') as reader:
			settings = json.loads(reader.read())
			self.items = settings
	
