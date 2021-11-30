from qt_core import *
from gui.functions.ui_functions import UIFunctions
from gui.functions.settings import Settings
#from main import Ui_MainWindow

Gen_Class, Base_Class = loadUiType(UIFunctions().resource_path("./gui/uis/theming.ui"))

class Theming(Base_Class, Gen_Class):
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		#self.ui = Ui_MainWindow()
		self.setupUi(self)
		settings = Settings('ui')
		self.settings = settings.items
		self.frame.setStyleSheet("border:none")
		#self.ui.panel1.setStyleSheet("border:none")
		#UIFunctions().setGuiStyle("titlebar", "dark", self)
		