from qt_core import *
#from main import MainWidget
from gui.functions.ui_functions import UIFunctions
from gui.modules.filesystemview.filesystemview import FileSystemView

MENU_DATA = {
		'Dashboard':{
			'Modern': 'ModenDashboard',
			'eCommerce': 'EcommerceDashboard',
			'Analytics': 'AnalyticsDashboard',
		},
		'Tables':{
			'Basic Table': 'BasicTable',
			'Data Table': 'DataTable',
			'System File Tree': 'FileSystemView',
		}
	}

class ContentMenu(QWidget):
	def __init__(self, *args):
		QWidget.__init__(self, *args)
		super(ContentMenu, self).__init__()
		self.tree = QTreeWidget(self)
		#topPanels = self.parent().parent().parent()
		#print(topPanels.objectName())
		#self.content_panel = topPanels.findChild(QWidget, "panel3")
		#print(self.content_panel)
		
		#self.tree.setSelectionMode(QAbstractItemView.NoSelection)
		self.tree.setFocusPolicy(Qt.NoFocus)
		layout = QVBoxLayout(self)
		layout.addWidget(self.tree)
		layout.setSpacing(0)
		layout.setObjectName(u"layout")
		sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.tree.sizePolicy().hasHeightForWidth())
		self.tree.setSizePolicy(sizePolicy)
		
		layout.setContentsMargins(0, 0, 0, 0)

		self.tree.setHeaderLabels(['Navigation2', 'target'])
		self.tree.setAnimated(True)
		self.tree.setColumnHidden(1, True)
		#self.tree.setExpandsClick(True)
		#self.tree.setColumnWidth(0,400)
		
		#self.tree.header().setDefaultSectionSize(180)
	   # self.tree.setModel(self.model)
		#self.importData(data)
		#self.tree.expandAll()
		self.build_tree(data=MENU_DATA, parent=self.tree)
		self.tree.itemClicked.connect(self.onItemClicked)

	@Slot(QTreeWidgetItem, int)
	def onItemClicked(self, item, col):
		if item.text(1) != None and item.text(1) != "":	
			# open menu link in content panel
			# call target class
			targetText = item.text(1)
			self.filesystemview = eval(targetText)(self.panel3)
        		
			try:
				#contentWidget = eval(targetText)()
				self.filesystemview = eval(targetText)(self.panel3)
        		#self.filesystemview.setObjectName(u"filesystemview")
			except:
				print(targetText, "is not defined")
				pass	
		else:
			# collapse/expand
			if item.isExpanded():
				self.tree.collapseItem(item)
			else:
				self.tree.collapseAll()
				self.tree.expandItem(item)
				
	def build_tree(self, data=None, parent=None, icon="chevron-right.svg"):
		for key, value in data.items():
			item = QTreeWidgetItem(parent)
			item.setText(0, key)
			item.setIcon(0, QIcon(UIFunctions().set_svg_icon(icon)))
			
			if isinstance(value, dict):
				self.build_tree(data=value, parent=item, icon="circle.svg")
			else:
				item.setText(1, value)
				

