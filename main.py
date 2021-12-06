# -*- coding: utf-8 -*-
#https://github.com/sciter-sdk/pysciter#getting-started

from gui.functions.settings import Settings
from gui.functions.ui_functions import UIFunctions
from gui.modules.button_handler.controller_buttons import SetControllerButtons
from gui.modules.navigation.menu import SetMenu as SetLeftMenu
from gui.modules.resizer.sidegrip import SideGrip

from gui.modules.style.style import SetStyle
#from gui.modules.panel_settings.panel_settings import PanelSettings
from gui.modules.theming.theming import Theming
from gui.modules.customizing.customizing import Customizing
from gui.modules.title_bar.titlebar import TitleBar

from gui.widgets.label_vertical.label_vertical import LabelVertical

from qt_core import *

if platform.system() == "Windows":
	Gen_Class, Base_Class = loadUiType(UIFunctions().resource_path("./gui/uis/main.ui"))
else:
	Gen_Class, Base_Class = loadUiType(UIFunctions().resource_path("./gui/uis/main.ui"))


class MainWidget(Base_Class, Gen_Class):
	_gripSize = 8
	def __init__(self, parent=None):
		##########################################################################################
		# Init
		##########################################################################################
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)
		
		
		# LOAD SETTINGS
		# ///////////////////////////////////////////////////////////////
		settings = Settings("ui")
		self.settings = settings.items
		menu_settings = Settings("menu")
		self.menu_data = menu_settings.items

		##########################################################################################
		# show loading Progress
		##########################################################################################
		self.loadingProgressBar.setValue(0)

		##########################################################################################
		# Set Settings
		##########################################################################################
		self.resize(self.settings['startup_size'][0], self.settings['startup_size'][1])
		self.setMinimumSize(QSize(self.settings['minimum_size'][0], self.settings['minimum_size'][1]))
		self.appTitle.setText(self.settings['app_name'])
		self.appDescription.setText(self.settings['description'])
		#self.autor.setText(self.settings['autor'])
		self.autor.setText(f"{self.settings['version']} | {self.settings['year']} | {self.settings['autor']}")
		self.appLogo.setPixmap(QPixmap(UIFunctions().resource_path(self.settings['icon']['png'])))
		##########################################################################################
		# custom_title_bar 
		##########################################################################################
		if self.settings['custom_title_bar']:
			self.setWindowFlag(Qt.FramelessWindowHint)
			TitleBar(self)
		##########################################################################################
		# App-Icon
		##########################################################################################
		self.windowicon = QIcon()
		self.windowicon.addFile(UIFunctions().resource_path(self.settings['icon']['ico']), QSize(48,48))
		self.setWindowIcon(self.windowicon)	
		##########################################################################################
		# MAIN-UI BTNS
		##########################################################################################
		#self.reloadStylesheet.clicked.connect(lambda: SetStyle(self).setTheme(self.settings['theme_name']))
		self.reloadApp.clicked.connect(self.restart)
		#SetControllerButtons(self)
		self.controllerButtons = SetControllerButtons(self)
		self.controllerButtons.handle_ui_btns()
		self.controllerButtons.toggle_all()
		self.controllerButtons.disableToggleButtons()
		####################################################################################
		# SET STYLE AND THEME
		####################################################################################
		self.setAttribute(Qt.WA_TranslucentBackground, True)
		SetStyle(self)
		#####################################################################################
		# Menu - Navigation
		#####################################################################################
		#self.setupMenu()
		SetLeftMenu(self)
		#####################################################################################
		# Content
		#####################################################################################
		
		#####################################################################################
		# Resize Window
		#####################################################################################
		self.sideGrips = [
			SideGrip(self, Qt.LeftEdge), 
			SideGrip(self, Qt.TopEdge), 
			SideGrip(self, Qt.RightEdge), 
			SideGrip(self, Qt.BottomEdge), 
		]
		self.cornerGrips = [QSizeGrip(self) for i in range(4)]
		for i in range(4):
			self.cornerGrips[i].setStyleSheet("background: transparent;")
		#####################################################################################
		# Theming
		#####################################################################################
		Theming(self)
		#####################################################################################
		# Customizing
		#####################################################################################
		Customizing(self)
			
	def mousePressEvent(self, event):
		if event.buttons() == Qt.RightButton:
			self.pressing = False
			event.ignore()
			return

		if event.button() == Qt.LeftButton:
			if not self.mainHeader.underMouse():
				self.pressing = False
				event.ignore()
				return

		self.start = self.mapToGlobal(event.pos())
		self.pressing = True

	def mouseMoveEvent(self, event):
		try:
			if self.pressing:
				self.end = self.mapToGlobal(event.pos())
				self.movement = self.end-self.start
				self.setGeometry(self.mapToGlobal(self.movement).x(),
				self.mapToGlobal(self.movement).y(),
				self.width(),
				self.height())
				self.start = self.end
		except:
			pass			
	
	@property
	def gripSize(self):
		return self._gripSize

	def setGripSize(self, size):
		if size == self._gripSize:
			return
		self._gripSize = max(2, size)
		self.updateGrips()

	def updateGrips(self):
		#self.setContentsMargins(*[self.gripSize] * 4)
		outRect = self.rect()
		
		# an "inner" rect used for reference to set the geometries of size grips
		inRect = outRect.adjusted(self.gripSize, self.gripSize,
			-self.gripSize, -self.gripSize)
		
		# top left
		self.cornerGrips[0].setGeometry(
			QRect(outRect.topLeft(), inRect.topLeft()))
		# top right
		self.cornerGrips[1].setGeometry(
			QRect(outRect.topRight(), inRect.topRight()).normalized())
		# bottom right
		self.cornerGrips[2].setGeometry(
			QRect(inRect.bottomRight(), outRect.bottomRight()))
		# bottom left
		self.cornerGrips[3].setGeometry(
			QRect(outRect.bottomLeft(), inRect.bottomLeft()).normalized())

		# left edge
		self.sideGrips[0].setGeometry(
			0, inRect.top(), self.gripSize, inRect.height())
		
		# top edge
		self.sideGrips[1].setGeometry(
			inRect.left(), 0, inRect.width(), self.gripSize)
		# right edge
		self.sideGrips[2].setGeometry(
			inRect.left() + inRect.width(), 
			inRect.top(), self.gripSize, inRect.height())
		# bottom edge
		self.sideGrips[3].setGeometry(
			self.gripSize, inRect.top() + inRect.height(), 
			inRect.width(), self.gripSize)

		[grip.raise_() for grip in self.sideGrips + self.cornerGrips]

	def resizeEvent(self, event):
		QMainWindow.resizeEvent(self, event)
		self.updateGrips()
	
	@staticmethod
	def restart():
		os.execl(sys.executable, sys.executable, *sys.argv)



if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	window = MainWidget()
	window.show()
	#window.showMaximized()
	sys.exit(app.exec_())

