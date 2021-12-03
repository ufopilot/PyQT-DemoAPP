
from qt_core import *
import re

class UIFunctions():
	def __init__(self):
		super().__init__()
		
	def resource_path(self, relative_path):
		if hasattr(sys, '_MEIPASS'):
			return os.path.join(sys._MEIPASS, relative_path)
		return os.path.join(os.path.abspath("."), relative_path)
	# SET SVG ICON
	# ///////////////////////////////////////////////////////////////
	def set_svg_icon(self, icon_name, color="white"):
		app_path = os.path.abspath(os.getcwd())
		folder = self.resource_path(f"gui/resources/icons/{color}/")
		path = os.path.join(app_path, folder)
		icon = os.path.normpath(os.path.join(path, icon_name))
		return icon
	# SET SVG IMAGE
	# ///////////////////////////////////////////////////////////////
	def set_svg_image(self, icon_name):
		app_path = os.path.abspath(os.getcwd())
		folder = self.resource_path("gui/resources/images/svg")
		path = os.path.join(app_path, folder)
		icon = os.path.normpath(os.path.join(path, icon_name))
		return icon
	# SET IMAGE
	# ///////////////////////////////////////////////////////////////
	def set_image(self, image_name):
		app_path = os.path.abspath(os.getcwd())
		folder = self.resource_path("gui/resources/images/png/")
		path = os.path.join(app_path, folder)
		image = os.path.normpath(os.path.join(path, image_name))
		return image
	
	def QIcon_from_svg(self, icon, color='white'):
		img = QPixmap(self.set_svg_icon(icon))
		qp = QPainter(img)
		qp.setCompositionMode(QPainter.CompositionMode_SourceIn)
		qp.fillRect( img.rect(), QColor(color) )
		qp.end()
		return QIcon(img)

	def getAppTheme(self, theme_settings):
		regex = r"\w+\(([^\)]+)\)"
		with open(UIFunctions().resource_path(f'./gui/assets/style/base.qss'), "r", encoding='utf-8') as reader:
			base_stylesheet = reader.read().replace("{","{{").replace("}","}}")
			base_stylesheet = re.sub(regex, '{\\1}', base_stylesheet)
			theme = theme_settings['theme']
			formated_stylesheet = base_stylesheet.format(**theme)
			#formated_stylesheet = base_stylesheet.format(
			#	panel_bg = colors['panel_bg'],
			#	panel_darker_bg = colors['panel_darker_bg'],
			#	panel_lighter_bg = colors['panel_lighter_bg'],
			#	panel_text = colors['panel_text'],
			#	panel_darker_text = colors['panel_darker_text'],
			#	panel_lighter_text = colors['panel_lighter_text'],
			#	header_bg = colors['header_bg'],
			#	header_darker_bg = colors['header_darker_bg'],
			#	header_lighter_bg = colors['header_lighter_bg'],
			#	header_text = colors['header_text'],
			#	header_darker_text = colors['header_darker_text'],
			#	header_lighter_text = colors['header_lighter_text'],
			#	
			#	footer_bg = colors['footer_bg'],
			#	footer_darker_bg = colors['footer_darker_bg'],
			#	footer_lighter_bg = colors['footer_lighter_bg'],
			#	footer_text = colors['footer_text'],
			#	footer_darker_text = colors['footer_darker_text'],
			#	footer_lighter_text = colors['footer_lighter_text'],
			#	
			#	controller_bg = colors['controller_bg'],
			#	controller_darker_bg = colors['controller_darker_bg'],
			#	controller_lighter_bg = colors['controller_lighter_bg'],
			#	controller_text = colors['controller_text'],
			#	controller_darker_text = colors['controller_darker_text'],
			#	controller_lighter_text = colors['controller_lighter_text'],
			#	
			#	scrollbar_bg = colors['scrollbar_bg'],
			#	scrollbar_handle_bg = colors['scrollbar_handle_bg'],
			#	scrollbar_hover_bg = colors['scrollbar_hover_bg'],
			#	table_alternate = colors['table_alternate'],
			#	tab_pane_bg = colors['tab_pane_bg'],
			#	page_header_bg = colors['page_header_bg'],
			#	table_header_bg = colors['table_header_bg'],
			#	lineedit_radius = colors['lineedit_radius'],
        	#	lineedit_border_size = colors['lineedit_border_size'],
        	#	lineedit_color = colors['lineedit_color'],
        	#	lineedit_selection_color = colors['lineedit_selection_color'],
        	#	lineedit_bg_color = colors['lineedit_bg_color'],
        	#	lineedit_bg_color_active = colors['lineedit_bg_color_active'],
        	#	lineedit_context_color = colors['lineedit_context_color']
			#)

			return formated_stylesheet
			

	def setGuiStyle(self, base_style, theme, target):
		template_stylesheet = ""
		with open(UIFunctions().resource_path(f'./gui/assets/style/{base_style}.qss')) as f:
				base_stylesheet = f.read()  
		if theme == "fusion":
			print("set theme", theme)
			target.setStyleSheet(f"{base_stylesheet}")
		else:
			print("set theme", theme)
			with open(UIFunctions().resource_path(f'./gui/assets/style/colors.qss')) as f:
				template_stylesheet = f.read()
			with open(UIFunctions().resource_path(f'./gui/assets/themes/{theme}.json')) as f:
				theme_stylesheet = json.load(f)
				for key, value in theme_stylesheet.items():
					template_stylesheet = template_stylesheet.replace(key, value)
			#\n{template_stylesheet}
			target.setStyleSheet(f"{base_stylesheet}")
	
	