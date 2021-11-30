from qt_core import *
from gui.functions.ui_functions import UIFunctions
from gui.functions.app_settings import Settings


Gen_Class, Base_Class = loadUiType(UIFunctions().resource_path("./gui/uis/footer_bar.ui"))

class FooterBar(Base_Class, Gen_Class):
	def __init__(self, parent=None):
		##########################################################################################
		# Init
		##########################################################################################
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)
		# LOAD SETTINGS
		# ///////////////////////////////////////////////////////////////
		settings = Settings()
		self.settings = settings.items

		

	