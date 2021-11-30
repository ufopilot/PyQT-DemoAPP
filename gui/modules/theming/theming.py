
from qt_core import *
from gui.content import *

from gui.functions.settings import Settings
from gui.functions.ui_functions import UIFunctions

class Theming(QWidget):
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		#self.setupUi(self)
		self.ui = parent
		#settings = Settings('ui')
		#self.settings = settings.items
		self.theme_settings = Settings('theme')
		#self.theme_settings = settings.items 

		for button in self.ui.findChildren(QAbstractButton):
			if "BgColor" in button.objectName():
				button.setCursor(QCursor(Qt.PointingHandCursor))
				button.clicked.connect(self.changeBg)
				
	def changeBg(self):
		button = self.sender()
		color = button.palette().color(QPalette.Background).name()
		if "header" in button.objectName():
			self.theme_settings.items['colors']['header_bg'] = color
		if "panel" in button.objectName():
			self.theme_settings.items['colors']['main_bg'] = color
		if "footer" in button.objectName():
			self.theme_settings.items['colors']['footer_bg'] = color
		if "controller" in button.objectName():
			self.theme_settings.items['colors']['controller_bg'] = color
		
		self.theme_settings.serialize()
		self.reloadStyle()
	
	def reloadStyle(self):
		stylesheet = UIFunctions().getAppTheme(self.theme_settings.items)
		self.ui.centralwidget.setStyleSheet(stylesheet)
		
		
		
		
	