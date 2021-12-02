from qt_core import *
from gui.content import *

from gui.functions.settings import Settings
from gui.functions.ui_functions import UIFunctions
import re

color_names = {
	'#000000': 'black',
	'#ffffff': 'white',
	'#808080': 'gray',
	'#b0b0b0': 'light gray',
	'#ff0000': 'red',
	'#800000': 'red',
	'#00ff00': 'green',
	'#008000': 'green',
	'#0000ff': 'blue',
	'#000080': 'blue',
	'#ffff00': 'yellow',
	'#808000': 'olive',
	'#00ffff': 'cyan',
	'#ff00ff': 'magenta',
	'#800080': 'purple'
	}

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
				button.setCheckable(True)
				button.clicked.connect(self.changeBg)
				
	def changeBg(self):
		
		button = self.sender()
		parentFrame = button.parent().parent()
		for btn in parentFrame.findChildren(QAbstractButton):
			if btn.isChecked() and btn.objectName() != button.objectName():
				btn.toggle()

		color = button.palette().color(QPalette.Background).name()
		qcolor = QColor(color)
		darker = qcolor.darker(115).name()
		lighter = qcolor.lighter(115).name()
		print(darker, color, lighter)

		typos = re.sub('BgColor.*', '', button.objectName())
		print(typos)
		if typos in ("header", "panel", "footer", "controller"):
			self.theme_settings.items['colors'][typos+'_bg'] = color
			self.theme_settings.items['colors'][typos+'_darker_bg'] = darker
			self.theme_settings.items['colors'][typos+'_lighter_bg'] = lighter
		
			if color.startswith("#f"):
				text_color = "#333"
			else:
				text_color = "#eee"
			qcolor = QColor(text_color)
			darker = qcolor.darker(115).name()
			lighter = qcolor.lighter(115).name()
			self.theme_settings.items['colors'][typos+'_text'] = color
			self.theme_settings.items['colors'][typos+'_darker_text'] = darker
			self.theme_settings.items['colors'][typos+'_lighter_text'] = lighter
		


		#if "header" in button.objectName():
		#	self.theme_settings.items['colors']['header_bg'] = color
		#	self.theme_settings.items['colors']['header_darker_bg'] = darker
		#	self.theme_settings.items['colors']['header_lighter_bg'] = lighter
		#if "panel" in button.objectName():
		#	self.theme_settings.items['colors']['panel_bg'] = color
		#	self.theme_settings.items['colors']['panel_darker_bg'] = darker
		#	self.theme_settings.items['colors']['panel_lighter_bg'] = lighter
		#if "footer" in button.objectName():
		#	self.theme_settings.items['colors']['footer_bg'] = color
		#if "controller" in button.objectName():
		#	self.theme_settings.items['colors']['controller_bg'] = color
			
		if "icon" in button.objectName():
			print(color_names[color])
			self.theme_settings.items['colors']['icon_bg'] = color_names[color]
			self.changeIcons()
		self.theme_settings.serialize()
		self.reloadStyle()
	
	def changeIcons(self):
		print("In Arbeit")
		#self.ui.panel1.deleteLater()
		#self.ui.panel1.repaint()
		#for button in self.ui.findChildren(QAbstractButton):
		#	print(button.icon().name())
			
			#if "BgColor" in button.objectName():
			#	button.setCursor(QCursor(Qt.PointingHandCursor))
			#	button.clicked.connect(self.changeBg)

	def reloadStyle(self):
		stylesheet = UIFunctions().getAppTheme(self.theme_settings.items)
		self.ui.centralwidget.setStyleSheet(stylesheet)
		
		
		
		
	