from qt_core import *
from gui.functions.ui_functions import UIFunctions
from gui.functions.settings import Settings


Gen_Class, Base_Class = loadUiType(UIFunctions().resource_path("./gui/uis/theming.ui"))

class Theming(Base_Class, Gen_Class):
	def __init__(self, parent=None):
		##########################################################################################
		# Init
		##########################################################################################
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)
		# LOAD SETTINGS
		# ///////////////////////////////////////////////////////////////
		settings = Settings('ui')
		self.settings = settings.items
		self.frame.setStyleSheet("border:none")

		#UIFunctions().setGuiStyle("titlebar", "dark", self)
		