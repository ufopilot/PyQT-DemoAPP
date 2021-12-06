from gui.functions.settings import Settings
from gui.functions.ui_functions import UIFunctions
#from gui.modules.panel_settings.panel_settings import PanelSettings
from qt_core import *
import webbrowser

class SetControllerButtons(QWidget):
	_panels_closed = []
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		#self.setupUi(self)
		self.ui = parent
		settings = Settings('ui')
		self.settings = settings.items
		theme_settings = Settings('theme')
		self.theme_settings = theme_settings.items
		
	def handle_ui_btns(self):
		self.ui.closeOtherPanels.clicked.connect(self.close_all_panels)
		self.ui.closeOtherPanels.setToolTip("Close all other Panels")
		self.ui.buttonGroup = QButtonGroup(self)
		for button in self.ui.findChildren(QAbstractButton):
			#self.ui.buttonGroup.addButton(button)
			button.setCursor(QCursor(Qt.PointingHandCursor))
			#if isinstance(button, QPushButton):
			#	button.setFlat(True)
			
			if button.objectName().startswith("togglePanel"):
				button.clicked.connect(self.toggle_panel)
				button.setToolTip("Toggle Panel")
			if button.objectName().startswith("panelSettings"):
				button.setToolTip("Settings")
				button.clicked.connect(self.panel_settings)
			if button.objectName() == "goToGitHub":
				button.clicked.connect(self.openGithub)
				
	def openGithub(self):
		webbrowser.open("https://github.com/ufopilot/PyQT-DemoAPP/")

	def panel_settings(self):
		button = self.sender()
		panel_name = button.objectName().lower().replace('settings', '')
		#self.dialog = PanelSettings()
		#self.dialog.setWindowFlag(Qt.FramelessWindowHint)
		#self.dialog.show()

	def disableToggleButtons(self):
		togglebuttons = (self.ui.closeOtherPanels, self.ui.togglePanel1, self.ui.togglePanel2, self.ui.togglePanel4, self.ui.togglePanel5)
		for i, button in enumerate(togglebuttons):
			button.setEnabled(False)
	
	def EnableToggleButtons(self):
		togglebuttons = (self.ui.closeOtherPanels, self.ui.togglePanel1, self.ui.togglePanel2, self.ui.togglePanel4, self.ui.togglePanel5)
		for i, button in enumerate(togglebuttons):
			button.setEnabled(True)
	
	def close_all_panels(self):
		togglebuttons = (self.ui.togglePanel1, self.ui.togglePanel2, self.ui.togglePanel4, self.ui.togglePanel5)
		for i, button in enumerate(togglebuttons):
			panel_name = button.objectName().replace('toggle', '').lower()
			if panel_name not in self._panels_closed:
				self.toggle_panel(button, 0)	
				#QTimer.singleShot(self.settings['time_animation'], lambda: self.toggle_panel(button))
		
	def toggle_all(self):
		self.ui.buttonGroup = QButtonGroup(self)
		for button in self.ui.findChildren(QAbstractButton):
			if button.objectName().startswith("togglePanel"):
				panel_name = button.objectName().replace("toggle", "").lower()
				if not self.settings[panel_name]['show_onstart']:
					self.toggle_panel(button, 0)
	
	def toggle_panel(self, button=False, timeAnimation=-1):
		if not button:
			button = self.sender()
		if not button.isEnabled():
			return
		panel = button.parent().parent().parent()
		panel_name = button.objectName().replace('toggle', '').lower()
		panel_index = panel_name.replace("panel", '')
		enable = self.settings[panel_name]['toggle']
		if enable:
			width = panel.width()
			height = panel.height()
			maximum = self.settings[panel_name]['maximum']
			minimum = self.settings[panel_name]['minimum']
			if timeAnimation == -1:
				timeAnimation = self.settings['time_animation']
			
			icon = QIcon()
			# ANIMATION
			direction = self.settings[panel_name]['direction']
			if direction == "rtl":
				icon_svg_close = "chevron-left.svg"
				icon_svg_expand = "chevron-right.svg"
				size_option = "minimumWidth"
				startValue = width

			if direction == "ltr":
				icon_svg_close = "chevron-right.svg"
				icon_svg_expand = "chevron-left.svg"
				size_option = "minimumWidth"
				startValue = width

			if direction == "btt":
				icon_svg_close = "chevron-down.svg"
				icon_svg_expand = "chevron-up.svg"
				size_option = "minimumHeight"
				startValue = height

			if direction == "ttb": 
				icon_svg_close = "chevron-down.svg"
				icon_svg_expand = "chevron-up.svg"
				size_option = "minimumHeight"
				startValue = height
			

			panel_title = panel.findChild(QLabel, f"headerPanel{panel_index}")
			
			if startValue == minimum:
				self._panels_closed.remove(panel_name)
				endValue = maximum
				panel_title_style = ""
				#panel_title.setStyleSheet("")
				icon.addPixmap(QPixmap(UIFunctions().set_svg_icon(icon_svg_close, self.theme_settings['colors']['icon_bg'])))
			else:
				self._panels_closed.append(panel_name)
				endValue = minimum
				panel_title_style = "color: #333"	
				#panel_title.setStyleSheet("color: #333")
				icon.addPixmap(QPixmap(UIFunctions().set_svg_icon(icon_svg_expand, self.theme_settings['colors']['icon_bg'])))
			button.setIcon(icon)
			
			self.animation = QPropertyAnimation(panel, bytes(size_option, encoding='utf-8'))
			self.animation.setDuration(timeAnimation)
			self.animation.setStartValue(startValue)
			self.animation.setEndValue(endValue)
			self.animation.setEasingCurve(QEasingCurve.InOutQuart)
			self.animation.start()
			QTimer.singleShot(timeAnimation, lambda: panel_title.setStyleSheet(panel_title_style))
	