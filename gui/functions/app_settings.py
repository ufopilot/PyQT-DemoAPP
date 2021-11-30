# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import json
import os, sys


# APP SETTINGS
# ///////////////////////////////////////////////////////////////
class Settings(object):
	def __init__(self):
		super(Settings, self).__init__()
		self.json_file = "gui/settings/app_settings.json"
		self.settings_path = self.resource_path(self.json_file)
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
			
	def resource_path(self, relative_path):
		if hasattr(sys, '_MEIPASS'):
			return os.path.join(sys._MEIPASS, relative_path)
		return os.path.join(os.path.abspath("."), relative_path)
			