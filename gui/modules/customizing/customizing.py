from qt_core import *
from gui.content import *

from gui.functions.settings import Settings
from gui.functions.ui_functions import UIFunctions
import re

class Customizing(QWidget):
	_init = True
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		self.ui = parent
		self.settings = Settings('ui')
		self.loadCustomValues()
		for checkox in self.ui.findChildren(QAbstractButton):
			if "customize" in checkox.objectName():
				checkox.setCursor(QCursor(Qt.PointingHandCursor))
				checkox.stateChanged.connect(self.state_changed)

	def loadCustomValues(self):
		for panel in ("panel1", "panel2", "panel4", "panel5"):
			toggle = self.settings.items[panel]['toggle']
			show_onstart = self.settings.items[panel]['show_onstart']
			print(panel, toggle, show_onstart)

	def state_changed(self, int):
		checkbox = self.sender()
		print(checkbox.objectName())
		if checkbox.isChecked():
			print("CHECKED!")
		else:
			print("UNCHECKED!")