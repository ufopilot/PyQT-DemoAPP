import time
from threading import Timer
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
	'#008000': 'dark green',
	'#0000ff': 'blue',
	'#000080': 'dark blue',
	'#ffff00': 'yellow',
	'#808000': 'olive',
	'#00ffff': 'cyan',
	'#ff00ff': 'magenta',
	'#800080': 'purple'
	}

class Theming(QWidget):
	_init = True
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		self.ui = parent
		self.theme_settings = Settings('theme')
		self.selectColors()
		
		for button in self.ui.findChildren(QAbstractButton):
			if "MainColor" in button.objectName():
				button.setCursor(QCursor(Qt.PointingHandCursor))
				button.setCheckable(True)
				button.clicked.connect(self.getColorPalette)
		
		List = ("HeaderColor", "FooterColor", "BorderColor", "HoverColor")
		for button in self.ui.findChildren(QAbstractButton):
			if any(comp in button.objectName() for comp in List):
				button.setCursor(QCursor(Qt.PointingHandCursor))
				button.setCheckable(True)
				button.clicked.connect(self.changeColor)

		List = ("First_textColor", "Second_textColor", "Third_textColor")
		for button in self.ui.findChildren(QAbstractButton):
			if any(comp in button.objectName() for comp in List):
				button.setCursor(QCursor(Qt.PointingHandCursor))
				button.setCheckable(True)
				button.clicked.connect(self.changeTextColor)
				
	def selectColors(self):
		T = 0
		D=1000
		for comp in ("header", "footer", "controller", "content"):	
			compString = comp+"MainColor"
			color = self.theme_settings.items['theme'][comp]['background']
			
			for button in self.ui.findChildren(QAbstractButton):
				if compString in button.objectName():
					if color == button.palette().color(QPalette.Background).name():	
						QTimer.singleShot(T, button.clicked.emit)
						QTimer.singleShot(T, button.toggle)
						QTimer.singleShot(D, partial(self.selectSubColors, comp))
						
						T += 100
						D += 100
		
		QTimer.singleShot(D, self.setInitFalse)

	def setInitFalse(self):
		self._init = False

	def selectSubColors(self, comp):
		T = 0
		if comp == "content":
			subcomps = ("Header", "Footer", "Hover", "Border")
		else:
			subcomps = ("Hover", "Border")

		for subcomp in subcomps:
			color = self.theme_settings.items['theme'][comp][subcomp.lower()]
			for i in range(1,5):
				#item = comp+subcomp+"Color"+str(i)
				#btn = eval(self.ui.comp+subcomp+"Color"+str(i))
				btn = self.ui.findChild(QPushButton, f"{comp}{subcomp}Color{i}")
				if color == btn.palette().color(QPalette.Background).name():
					QTimer.singleShot(T, btn.clicked.emit)
					QTimer.singleShot(T, btn.toggle)
			T += 100		

	#def setSelected(self, item):
		#QTimer.singleShot(3000, lambda: item.toggle())
		#self.getColorPaletteinit = True, button = item)
		#QTimer.singleShot(5000, item.clicked.emit)
	#	print(item.objectName())

	def getColorPalette(self):

		button = self.sender()
		name = button.objectName()
		parentFrame = button.parent().parent()
		for btn in parentFrame.findChildren(QAbstractButton):
			if btn.isChecked() and btn.objectName() != button.objectName():
				btn.toggle()

		colorList = [] 
		color = button.palette().color(QPalette.Background).name()
		qcolor = QColor(color)

		colorList.append(color)
		colorList.append(qcolor.darker(110).name())
		colorList.append(qcolor.darker(120).name())
		colorList.append(qcolor.darker(130).name())
		
		i = 0
		if self.typos(name) == "content":
			buttons = {"Header": [], "Footer": [], "Border": [], "Hover": []}
		else:
			buttons = {"Border": [], "Hover": []}
		
		for x in range (1,5):
			for tg, value in buttons.items():
				try:
					buttons[tg].append(eval(f"self.ui.{self.typos(name)}{tg}Color{x}"))
					#print(f"self.ui.{self.typos(name)}{tg}Color{x}")
				except:
					pass
		
		for item, btns in buttons.items():
			i = 0
			for btn in btns:
				try:
					btn.setStyleSheet(f'background: {colorList[i]}')
				except:
					pass	
				i += 1
		# on changing main background -> click first subcolor
		#####################################################
		if not self._init:
			for tg, value in buttons.items():
				T=100
				sub_btn = eval(f"self.ui.{self.typos(name)}{tg}Color1")
				#for sub_btn in (self.ui.headerHoverColor1, self.ui.headerBorderColor1):
				QTimer.singleShot(T, partial(self.toggleSelected, sub_btn))
				QTimer.singleShot(T, sub_btn.clicked.emit)
				T += 100
		# write theme-settings
		# ###################################################		
		self.theme_settings.items['theme'][self.typos(name)]['background'] = color
		self.theme_settings.items['theme'][self.typos(name)]['background_alternate'] = colorList[1]
		self.theme_settings.serialize()
		
		# reload stylesheet
		#####################################################
		self.reloadStyle()
		

	def changeColor(self):
		button = self.sender()
		name = button.objectName()
		parentFrame = button.parent()
		for btn in parentFrame.findChildren(QAbstractButton):
			_name = btn.objectName()
			if btn.isChecked() and _name != name:
				btn.toggle()
		color = button.palette().color(QPalette.Background).name()
		self.theme_settings.items['theme'][self.typos(name)][self.component(name)] = color
		
		self.theme_settings.serialize()
		self.reloadStyle()

	def changeTextColor(self):
		button = self.sender()
		name = button.objectName()
		parentFrame = button.parent()
		for btn in parentFrame.findChildren(QAbstractButton):
			_name = btn.objectName()
			if btn.isChecked() and _name != name:
				btn.toggle()
		color = button.palette().color(QPalette.Background).name()
		self.theme_settings.items['theme'][self.typos(name)][self.component(name)] = color
		
		self.theme_settings.serialize()
		self.reloadStyle()

	def clickSubSelected(self, button, T):
		QTimer.singleShot(T, button.clicked.emit)

	def toggleSelected(self, button):
		name = button.objectName()
		parentFrame = button.parent()
		
		for btn in parentFrame.findChildren(QAbstractButton):
			if btn.isChecked():
				btn.toggle()
		button.toggle()
		

		

	def component(self, name):
		strings = re.sub( r"([A-Z])", r" \1", name).split()
		return  strings[1].lower()
		
	def typos(self, name):
		strings = re.sub( r"([A-Z])", r" \1", name).split()
		return strings[0].lower()
		
	def changeBg(self):
		
		button = self.sender()
		parentFrame = button.parent().parent()
		for btn in parentFrame.findChildren(QAbstractButton):
			if btn.isChecked() and btn.objectName() != button.objectName():
				btn.toggle()

		color = button.palette().color(QPalette.Background).name()
		qcolor = QColor(color)
		middle = qcolor.darker(300).name()
		darker = qcolor.darker(150).name()
		lighter = qcolor.lighter(50).name()
		
		typos = re.sub('MainColor.*', '', button.objectName())
		
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
		
		
		
		
	