from gui.functions.settings import Settings
from gui.functions.ui_functions import UIFunctions
from qt_core import *


class SetStyle(QWidget):
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		#self.setupUi(self)
		self.ui = parent
		settings = Settings('ui')
		self.settings = settings.items

		self.setTheme(self.settings['theme_name'])
		effect = QGraphicsDropShadowEffect(self.ui.mainFrame, enabled=False, blurRadius=5)
		self.ui.mainFrame.setGraphicsEffect(effect)
		self.shadow = QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(15)
		self.shadow.setXOffset(0)
		self.shadow.setYOffset(0)
		self.shadow.setColor(QColor(0, 0, 0, 150))
		# add the shadow object to the frame
		self.ui.mainFrame.raise_()
		self.ui.mainFrame.setGraphicsEffect(self.shadow)

	def setTheme(self, theme):
		template_stylesheet = ""
		with open(UIFunctions().resource_path(f'./gui/assets/style/base2.qss')) as f:
				base_stylesheet = f.read()  
		if theme == "fusion":
			print("set theme", theme)
			self.centralwidget.setStyleSheet(f"{base_stylesheet}")
		else:
			print("set theme", theme)
			with open(UIFunctions().resource_path(f'./gui/assets/style/colors.qss')) as f:
				template_stylesheet = f.read()
			with open(UIFunctions().resource_path(f'./gui/assets/themes/{theme}.json')) as f:
				theme_stylesheet = json.load(f)
				for key, value in theme_stylesheet.items():
					template_stylesheet = template_stylesheet.replace(key, value)
			#\n{template_stylesheet}
			self.ui.centralwidget.setStyleSheet(f"{base_stylesheet}")
