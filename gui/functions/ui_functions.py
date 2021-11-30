
from qt_core import *
from gui.functions.app_settings import Settings

# GET RELATIVE PATH
# ///////////////////////////////////////////////////////////////

class UIFunctions():
	def __init__(self):
		super().__init__()
		
		#self.ui = UI_MainWindow()
		#self.ui.setup_ui(self)
		self.settings = Settings()

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
	
	def start_box_animation(self, left_box_width, right_box_width, direction):
		right_width = 0
		left_width = 0
		time_animation = self.settings["time_animation"]
		minimum_left = self.settings["left_column_size"]["minimum"]
		maximum_left = self.settings["left_column_size"]["maximum"]
		minimum_right = self.settings["right_column_size"]["minimum"]
		maximum_right = self.settings["right_column_size"]["maximum"]

		# Check Left Values        
		if left_box_width == minimum_left and direction == "left":
			left_width = maximum_left
		else:
			left_width = minimum_left

		# Check Right values        
		if right_box_width == minimum_right and direction == "right":
			right_width = maximum_right
		else:
			right_width = minimum_right       

		# ANIMATION LEFT BOX        
		self.left_box = QPropertyAnimation(self.ui.left_column_frame, b"minimumWidth")
		self.left_box.setDuration(time_animation)
		self.left_box.setStartValue(left_box_width)
		self.left_box.setEndValue(left_width)
		self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

		# ANIMATION RIGHT BOX        
		self.right_box = QPropertyAnimation(self.ui.right_column_frame, b"minimumWidth")
		self.right_box.setDuration(time_animation)
		self.right_box.setStartValue(right_box_width)
		self.right_box.setEndValue(right_width)
		self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

		# GROUP ANIMATION
		self.group = QParallelAnimationGroup()
		self.group.stop()
		self.group.addAnimation(self.left_box)
		self.group.addAnimation(self.right_box)
		self.group.start()