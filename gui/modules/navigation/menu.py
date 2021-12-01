
from qt_core import *
from gui.content import *

from gui.functions.settings import Settings
from gui.functions.ui_functions import UIFunctions

class SetMenu(QWidget):
	_lastcontent = None
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		#self.setupUi(self)
		self.ui = parent
		settings = Settings('ui')
		self.settings = settings.items
		menu_settings = Settings('menu')
		self.menu_data = menu_settings.items
		self.setupMenu()
		
	def setupMenu(self):
		#self.tree.setSelectionMode(QAbstractItemView.NoSelection)
		#self.ui.menuTree.verticalHeader().setVisible(False)
		#.verticalHeader().hide()
		self.ui.menuTree.setFocusPolicy(Qt.NoFocus)
		sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.ui.menuTree.sizePolicy().hasHeightForWidth())
		self.ui.menuTree.setSizePolicy(sizePolicy)
		self.ui.menuTree.setHeaderLabels(['Navigation', 'target'])
		self.ui.menuTree.setHeaderHidden(True);
		self.ui.menuTree.setAnimated(True)
		self.ui.menuTree.setColumnHidden(1, True)
		
		#self.tree.setColumnWidth(0,400)
		#self.ui.menuTree.header().setDefaultSectionSize(0)
	  	#self.tree.expandAll()
		self.build_menu(data=self.menu_data, parent=self.ui.menuTree)
		self.ui.menuTree.itemClicked.connect(self.onItemClicked)

	@Slot(QTreeWidgetItem, int)	
	def onItemClicked(self, item, col):
		if item.text(1) != None and item.text(1) != "":	
			# open menu link in content panel
			# call target class
			targetPageClass = item.text(1)
			
			# test if widgetClass exists 
			try:
				var = eval(targetPageClass)()
			except NameError:
				print(targetPageClass, "is not defined")
				return
			# change remove widget to hide und show
			#while self.contentLayout.count():
			#	child = self.contentLayout.takeAt(0)
			#	if child.widget():
	  		#		child.widget().deleteLater()

			#self.contentLayout.takeAt(0).widget().hide()
			
			if self._lastcontent != None:
				self.ui.panel3.findChild(QWidget, self._lastcontent).hide()
			
			cachedWidget = self.ui.panel3.findChild(QWidget, targetPageClass)
			if cachedWidget:
				cachedWidget.show()
			else:
				self.ui.contentWidget  = eval(targetPageClass)(self.ui.panel3)
				self.ui.contentWidget .setObjectName(f"{targetPageClass}")
				sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
				sizePolicy.setHorizontalStretch(0)
				sizePolicy.setVerticalStretch(0)
				sizePolicy.setHeightForWidth(self.ui.contentWidget .sizePolicy().hasHeightForWidth())
				self.ui.contentWidget .setSizePolicy(sizePolicy)
				self.ui.contentWidget .setLayoutDirection(Qt.LeftToRight)
				self.ui.contentLayout.addWidget(self.ui.contentWidget )
			self._lastcontent = targetPageClass
		else:
			# collapse/expand
			if item.isExpanded():
				if item.text(2) != "":
					item.setIcon(0, QIcon(UIFunctions().set_svg_icon(item.text(2))))
				self.ui.menuTree.collapseItem(item)
			else:
				#self.ui.menuTree.collapseAll()
				if item.text(3) != "":
					item.setIcon(0, QIcon(UIFunctions().set_svg_icon(item.text(3))))
				self.ui.menuTree.expandItem(item)
				
	def build_menu(self, data=None, parent=None):
		for menu_item in data:
			tree_item = QTreeWidgetItem(parent)
			tree_item.setText(0, menu_item['name'])
			if type(menu_item['icon']) == dict:
				tree_item.setIcon(0, QIcon(UIFunctions().set_svg_icon(menu_item['icon']['collapsed'])))
				tree_item.setText(2, menu_item['icon']['collapsed'])
				tree_item.setText(3, menu_item['icon']['expanded'])
			else:
				tree_item.setIcon(0, QIcon(UIFunctions().set_svg_icon(menu_item['icon'])))

			if "children" in menu_item:
				self.build_menu(data=menu_item['children'], parent=tree_item)
			else:
				tree_item.setText(1, menu_item['widget'])
				if "start" in menu_item:
					self.onItemClicked(tree_item, 0)

	