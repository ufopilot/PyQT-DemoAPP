
from qt_core import *
from gui.content import *

from gui.functions.settings import Settings
from gui.functions.ui_functions import UIFunctions

class TitleBar(QWidget):
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		#self.setupUi(self)
		self.ui = parent
		settings = Settings('ui')
		self.settings = settings.items
		if not self.settings['custom_title_bar']:
			self.windowicons.hide()
			
		self.ui.restorewindow.hide()
		
		self.ui.restorewindow.clicked.connect(self.ui.maximizewindow.show)
		self.ui.restorewindow.clicked.connect(self.ui.restorewindow.hide)
		self.ui.restorewindow.clicked.connect(self.ui.window().showNormal)
		
		self.ui.maximizewindow.clicked.connect(self.ui.maximizewindow.hide)   
		self.ui.maximizewindow.clicked.connect(self.ui.restorewindow.show)
		self.ui.maximizewindow.clicked.connect(self.ui.window().showMaximized)
		
		self.ui.minimizewindow.clicked.connect(self.ui.window().showMinimized)
		self.ui.closewindow.clicked.connect(self.ui.window().close)
		self.ui.appDescription.mouseDoubleClickEvent = self.maximize_restore

	def maximize_restore(self, event=None):
		if self.settings['custom_title_bar']:
			if self.ui.window().isMaximized():
				QTimer.singleShot(0, self.ui.restorewindow.clicked.emit)
			else:
				QTimer.singleShot(0, self.ui.maximizewindow.clicked.emit)