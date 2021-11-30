from qt_core import *
from gui.functions.ui_functions import UIFunctions
from gui.functions.settings import Settings


Gen_Class, Base_Class = loadUiType(UIFunctions().resource_path("./gui/uis/title_bar.ui"))

class TitleBar(Base_Class, Gen_Class):
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

		if not self.settings['custom_title_bar']:
			self.windowicons.hide()
		
		UIFunctions().setGuiStyle("titlebar", "dark", self)
		#effect = QGraphicsDropShadowEffect(self.frame, enabled=False, blurRadius=5)
		#self.frame.setGraphicsEffect(effect)
		#self.shadow = QGraphicsDropShadowEffect(self)
		#self.shadow.setBlurRadius(15)
		#self.shadow.setXOffset(0)
		#self.shadow.setYOffset(0)
		#self.shadow.setColor(QColor(0, 0, 0, 150))
		## add the shadow object to the frame
		#self.frame.raise_()
		#self.frame.setGraphicsEffect(self.shadow)

		#UIFunctions().setGuiStyle("dialog", "dark", self.frame)

		#self.buttonBox.accepted.connect(self.ok_callback)
		#self.buttonBox.rejected.connect(self.cancel_callback)
		self.restorewindow.hide()
		self.restorewindow.clicked.connect(self.maximisewindow.show)
		self.restorewindow.clicked.connect(self.restorewindow.hide)
		self.restorewindow.clicked.connect(self.window().showNormal)
		
		self.maximisewindow.clicked.connect(self.maximisewindow.hide)   
		self.maximisewindow.clicked.connect(self.restorewindow.show)
		self.maximisewindow.clicked.connect(self.window().showMaximized)
		
		self.minimizewindow.clicked.connect(self.window().showMinimized)
		self.closewindow.clicked.connect(self.window().close)

	def mouseDoubleClickEvent(self, event):
		if self.settings['custom_title_bar']:
			if self.appDescription.underMouse():
				if self.window().isMaximized():
					QTimer.singleShot(0, self.restorewindow.clicked.emit)
				else:
					QTimer.singleShot(0, self.maximisewindow.clicked.emit)