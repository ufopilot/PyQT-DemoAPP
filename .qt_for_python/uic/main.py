# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFontComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QTabWidget, QToolBox, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

from gui.widgets.animated_check.animated_check import AnimatedCheck
from gui.widgets.label_horizontal.label_horizontal import LabelHorizontal
from gui.widgets.label_vertical.label_vertical import LabelVertical
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1855, 838)
        MainWindow.setStyleSheet(u"")
        self.actionvvv = QAction(MainWindow)
        self.actionvvv.setObjectName(u"actionvvv")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Sunken)
        self.mainFrame.setLineWidth(10)
        self.gridLayout = QGridLayout(self.mainFrame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.mainHeader = QWidget(self.mainFrame)
        self.mainHeader.setObjectName(u"mainHeader")
        self.mainHeader.setMinimumSize(QSize(0, 40))
        self.mainHeader.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_17 = QHBoxLayout(self.mainHeader)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.dummy = QLabel(self.mainHeader)
        self.dummy.setObjectName(u"dummy")
        self.dummy.setMaximumSize(QSize(14, 16777215))

        self.horizontalLayout_17.addWidget(self.dummy)

        self.appLogo = QLabel(self.mainHeader)
        self.appLogo.setObjectName(u"appLogo")
        self.appLogo.setMinimumSize(QSize(24, 24))
        self.appLogo.setMaximumSize(QSize(24, 24))
        self.appLogo.setStyleSheet(u"")
        self.appLogo.setPixmap(QPixmap(u":/images/gui/resources/imgs/kisspng-python-programming-basics-for-absolute-beginners-michigan-python-user-group-5-jul-2-18-5bfef9220f00d6.4973377615434365780615.png"))
        self.appLogo.setScaledContents(True)
        self.appLogo.setAlignment(Qt.AlignCenter)
        self.appLogo.setWordWrap(False)

        self.horizontalLayout_17.addWidget(self.appLogo)

        self.appTitle = QLabel(self.mainHeader)
        self.appTitle.setObjectName(u"appTitle")
        self.appTitle.setMinimumSize(QSize(0, 0))
        self.appTitle.setMaximumSize(QSize(80, 16777215))
        self.appTitle.setStyleSheet(u"")
        self.appTitle.setScaledContents(True)

        self.horizontalLayout_17.addWidget(self.appTitle)

        self.appDescription = QLabel(self.mainHeader)
        self.appDescription.setObjectName(u"appDescription")

        self.horizontalLayout_17.addWidget(self.appDescription)

        self.windowicons = QFrame(self.mainHeader)
        self.windowicons.setObjectName(u"windowicons")
        self.windowicons.setMaximumSize(QSize(150, 16777215))
        self.windowicons.setFrameShape(QFrame.StyledPanel)
        self.windowicons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.windowicons)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.minimizewindow = QPushButton(self.windowicons)
        self.minimizewindow.setObjectName(u"minimizewindow")
        self.minimizewindow.setMaximumSize(QSize(50, 50))
        icon = QIcon()
        icon.addFile(u":/white-icons-smaller/gui/resources/icons/white/icon_minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizewindow.setIcon(icon)
        self.minimizewindow.setFlat(True)

        self.horizontalLayout_10.addWidget(self.minimizewindow)

        self.restorewindow = QPushButton(self.windowicons)
        self.restorewindow.setObjectName(u"restorewindow")
        self.restorewindow.setMaximumSize(QSize(50, 50))
        icon1 = QIcon()
        icon1.addFile(u":/white-icons-smaller/gui/resources/icons/white/icon_restore.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restorewindow.setIcon(icon1)
        self.restorewindow.setFlat(True)

        self.horizontalLayout_10.addWidget(self.restorewindow)

        self.maximizewindow = QPushButton(self.windowicons)
        self.maximizewindow.setObjectName(u"maximizewindow")
        self.maximizewindow.setMaximumSize(QSize(50, 50))
        icon2 = QIcon()
        icon2.addFile(u":/white-icons-smaller/gui/resources/icons/white/icon_maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizewindow.setIcon(icon2)
        self.maximizewindow.setFlat(True)

        self.horizontalLayout_10.addWidget(self.maximizewindow)

        self.closewindow = QPushButton(self.windowicons)
        self.closewindow.setObjectName(u"closewindow")
        self.closewindow.setMaximumSize(QSize(50, 50))
        icon3 = QIcon()
        icon3.addFile(u":/white-icons-smaller/gui/resources/icons/white/icon_close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closewindow.setIcon(icon3)
        self.closewindow.setFlat(True)

        self.horizontalLayout_10.addWidget(self.closewindow)


        self.horizontalLayout_17.addWidget(self.windowicons)


        self.gridLayout.addWidget(self.mainHeader, 0, 0, 1, 2)

        self.panelContainer = QWidget(self.mainFrame)
        self.panelContainer.setObjectName(u"panelContainer")
        self.panelContainer.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(self.panelContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topPanels = QWidget(self.panelContainer)
        self.topPanels.setObjectName(u"topPanels")
        self.horizontalLayout_2 = QHBoxLayout(self.topPanels)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.parentPanel1 = QWidget(self.topPanels)
        self.parentPanel1.setObjectName(u"parentPanel1")
        self.parentPanel1.setMinimumSize(QSize(300, 0))
        self.parentPanel1.setMaximumSize(QSize(300, 16777215))
        self.horizontalLayout_3 = QHBoxLayout(self.parentPanel1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.panel1 = QWidget(self.parentPanel1)
        self.panel1.setObjectName(u"panel1")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.panel1.sizePolicy().hasHeightForWidth())
        self.panel1.setSizePolicy(sizePolicy)
        self.verticalLayout_7 = QVBoxLayout(self.panel1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.contentMenu = QWidget(self.panel1)
        self.contentMenu.setObjectName(u"contentMenu")
        sizePolicy.setHeightForWidth(self.contentMenu.sizePolicy().hasHeightForWidth())
        self.contentMenu.setSizePolicy(sizePolicy)
        self.verticalLayout_11 = QVBoxLayout(self.contentMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 20, 0, 0)
        self.menuTree = QTreeWidget(self.contentMenu)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.menuTree.setHeaderItem(__qtreewidgetitem)
        self.menuTree.setObjectName(u"menuTree")
        sizePolicy.setHeightForWidth(self.menuTree.sizePolicy().hasHeightForWidth())
        self.menuTree.setSizePolicy(sizePolicy)

        self.verticalLayout_11.addWidget(self.menuTree)


        self.verticalLayout_7.addWidget(self.contentMenu)


        self.horizontalLayout_3.addWidget(self.panel1)

        self.controllerPanel1 = QWidget(self.parentPanel1)
        self.controllerPanel1.setObjectName(u"controllerPanel1")
        self.controllerPanel1.setMinimumSize(QSize(30, 0))
        self.controllerPanel1.setMaximumSize(QSize(30, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.controllerPanel1)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.controllerIcons1 = QFrame(self.controllerPanel1)
        self.controllerIcons1.setObjectName(u"controllerIcons1")
        self.controllerIcons1.setFrameShape(QFrame.StyledPanel)
        self.controllerIcons1.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.controllerIcons1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, -1)
        self.togglePanel1 = QPushButton(self.controllerIcons1)
        self.togglePanel1.setObjectName(u"togglePanel1")
        self.togglePanel1.setMinimumSize(QSize(28, 28))
        self.togglePanel1.setMaximumSize(QSize(28, 28))
        self.togglePanel1.setSizeIncrement(QSize(0, 0))
        self.togglePanel1.setBaseSize(QSize(0, 0))
#if QT_CONFIG(tooltip)
        self.togglePanel1.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.togglePanel1.setAutoFillBackground(False)
        icon4 = QIcon()
        icon4.addFile(u":/gray-icons/gui/resources/icons/gray/chevron-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.togglePanel1.setIcon(icon4)
        self.togglePanel1.setFlat(True)

        self.gridLayout_3.addWidget(self.togglePanel1, 0, 0, 1, 1)

        self.panelSettings1 = QPushButton(self.controllerIcons1)
        self.panelSettings1.setObjectName(u"panelSettings1")
        self.panelSettings1.setMinimumSize(QSize(28, 28))
        self.panelSettings1.setMaximumSize(QSize(28, 28))
        self.panelSettings1.setSizeIncrement(QSize(0, 0))
        self.panelSettings1.setBaseSize(QSize(0, 0))
#if QT_CONFIG(tooltip)
        self.panelSettings1.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        icon5 = QIcon()
        icon5.addFile(u":/gray-icons/gui/resources/icons/gray/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.panelSettings1.setIcon(icon5)
        self.panelSettings1.setIconSize(QSize(12, 12))
        self.panelSettings1.setAutoDefault(False)
        self.panelSettings1.setFlat(True)

        self.gridLayout_3.addWidget(self.panelSettings1, 1, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.controllerIcons1, 0, Qt.AlignTop)

        self.headerPanel1 = LabelVertical(self.controllerPanel1)
        self.headerPanel1.setObjectName(u"headerPanel1")
        self.headerPanel1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.headerPanel1, 0, Qt.AlignBottom)


        self.horizontalLayout_3.addWidget(self.controllerPanel1)


        self.horizontalLayout_2.addWidget(self.parentPanel1)

        self.parentPanel2 = QWidget(self.topPanels)
        self.parentPanel2.setObjectName(u"parentPanel2")
        self.parentPanel2.setMinimumSize(QSize(300, 0))
        self.parentPanel2.setMaximumSize(QSize(300, 16777215))
        self.parentPanel2.setAutoFillBackground(False)
        self.horizontalLayout_5 = QHBoxLayout(self.parentPanel2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.panel2 = QWidget(self.parentPanel2)
        self.panel2.setObjectName(u"panel2")
        self.verticalLayout_8 = QVBoxLayout(self.panel2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.panel2)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_10 = QVBoxLayout(self.widget)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)

        self.verticalLayout_10.addWidget(self.widget_2)


        self.verticalLayout_8.addWidget(self.widget)


        self.horizontalLayout_5.addWidget(self.panel2)

        self.controllerPanel2 = QWidget(self.parentPanel2)
        self.controllerPanel2.setObjectName(u"controllerPanel2")
        self.controllerPanel2.setMinimumSize(QSize(30, 0))
        self.controllerPanel2.setMaximumSize(QSize(30, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.controllerPanel2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.controllerIcons2 = QFrame(self.controllerPanel2)
        self.controllerIcons2.setObjectName(u"controllerIcons2")
        self.controllerIcons2.setFrameShape(QFrame.StyledPanel)
        self.controllerIcons2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.controllerIcons2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setContentsMargins(0, 0, 0, -1)
        self.togglePanel2 = QPushButton(self.controllerIcons2)
        self.togglePanel2.setObjectName(u"togglePanel2")
        self.togglePanel2.setMinimumSize(QSize(28, 28))
        self.togglePanel2.setMaximumSize(QSize(28, 28))
        self.togglePanel2.setSizeIncrement(QSize(0, 0))
        self.togglePanel2.setBaseSize(QSize(0, 0))
#if QT_CONFIG(tooltip)
        self.togglePanel2.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.togglePanel2.setAutoFillBackground(False)
        self.togglePanel2.setIcon(icon4)
        self.togglePanel2.setFlat(True)

        self.gridLayout_4.addWidget(self.togglePanel2, 0, 0, 1, 1)

        self.panelSettings2 = QPushButton(self.controllerIcons2)
        self.panelSettings2.setObjectName(u"panelSettings2")
        self.panelSettings2.setMinimumSize(QSize(28, 28))
        self.panelSettings2.setMaximumSize(QSize(28, 28))
        self.panelSettings2.setSizeIncrement(QSize(0, 0))
        self.panelSettings2.setBaseSize(QSize(0, 0))
#if QT_CONFIG(tooltip)
        self.panelSettings2.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.panelSettings2.setIcon(icon5)
        self.panelSettings2.setIconSize(QSize(12, 12))
        self.panelSettings2.setAutoDefault(False)
        self.panelSettings2.setFlat(True)

        self.gridLayout_4.addWidget(self.panelSettings2, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.controllerIcons2, 0, Qt.AlignTop)

        self.headerPanel2 = LabelVertical(self.controllerPanel2)
        self.headerPanel2.setObjectName(u"headerPanel2")
        self.headerPanel2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.headerPanel2, 0, Qt.AlignBottom)


        self.horizontalLayout_5.addWidget(self.controllerPanel2)


        self.horizontalLayout_2.addWidget(self.parentPanel2)

        self.parentPanel3 = QWidget(self.topPanels)
        self.parentPanel3.setObjectName(u"parentPanel3")
        self.parentPanel3.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_6 = QHBoxLayout(self.parentPanel3)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.panel3 = QWidget(self.parentPanel3)
        self.panel3.setObjectName(u"panel3")
        self.panel3.setLayoutDirection(Qt.LeftToRight)
        self.contentLayout = QVBoxLayout(self.panel3)
        self.contentLayout.setSpacing(0)
        self.contentLayout.setObjectName(u"contentLayout")
        self.contentLayout.setContentsMargins(0, 0, 0, 0)
        self.contentWidget = QWidget(self.panel3)
        self.contentWidget.setObjectName(u"contentWidget")
        sizePolicy.setHeightForWidth(self.contentWidget.sizePolicy().hasHeightForWidth())
        self.contentWidget.setSizePolicy(sizePolicy)
        self.contentWidget.setLayoutDirection(Qt.LeftToRight)

        self.contentLayout.addWidget(self.contentWidget)


        self.horizontalLayout_6.addWidget(self.panel3)

        self.controllerPanel3 = QWidget(self.parentPanel3)
        self.controllerPanel3.setObjectName(u"controllerPanel3")
        self.controllerPanel3.setMinimumSize(QSize(30, 0))
        self.controllerPanel3.setMaximumSize(QSize(30, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.controllerPanel3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.controllerIcons3 = QFrame(self.controllerPanel3)
        self.controllerIcons3.setObjectName(u"controllerIcons3")
        self.controllerIcons3.setFrameShape(QFrame.StyledPanel)
        self.controllerIcons3.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.controllerIcons3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setVerticalSpacing(0)
        self.gridLayout_5.setContentsMargins(0, 0, 0, -1)
        self.closeOtherPanels = QPushButton(self.controllerIcons3)
        self.closeOtherPanels.setObjectName(u"closeOtherPanels")
        self.closeOtherPanels.setMinimumSize(QSize(28, 28))
        self.closeOtherPanels.setMaximumSize(QSize(28, 28))
        self.closeOtherPanels.setSizeIncrement(QSize(0, 0))
        self.closeOtherPanels.setBaseSize(QSize(0, 0))
#if QT_CONFIG(tooltip)
        self.closeOtherPanels.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.closeOtherPanels.setAutoFillBackground(False)
        icon6 = QIcon()
        icon6.addFile(u":/gray-icons/gui/resources/icons/gray/crop.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeOtherPanels.setIcon(icon6)
        self.closeOtherPanels.setFlat(True)

        self.gridLayout_5.addWidget(self.closeOtherPanels, 0, 0, 1, 1)

        self.panelSettings3 = QPushButton(self.controllerIcons3)
        self.panelSettings3.setObjectName(u"panelSettings3")
        self.panelSettings3.setMinimumSize(QSize(28, 28))
        self.panelSettings3.setMaximumSize(QSize(28, 28))
        self.panelSettings3.setSizeIncrement(QSize(0, 0))
        self.panelSettings3.setBaseSize(QSize(0, 0))
#if QT_CONFIG(tooltip)
        self.panelSettings3.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.panelSettings3.setIcon(icon5)
        self.panelSettings3.setIconSize(QSize(12, 12))
        self.panelSettings3.setAutoDefault(False)
        self.panelSettings3.setFlat(True)

        self.gridLayout_5.addWidget(self.panelSettings3, 1, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.controllerIcons3, 0, Qt.AlignTop)

        self.headerPanel3 = LabelVertical(self.controllerPanel3)
        self.headerPanel3.setObjectName(u"headerPanel3")
        self.headerPanel3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.headerPanel3, 0, Qt.AlignBottom)


        self.horizontalLayout_6.addWidget(self.controllerPanel3)


        self.horizontalLayout_2.addWidget(self.parentPanel3)


        self.verticalLayout.addWidget(self.topPanels)

        self.parentPanel5 = QWidget(self.panelContainer)
        self.parentPanel5.setObjectName(u"parentPanel5")
        self.parentPanel5.setMinimumSize(QSize(0, 200))
        self.parentPanel5.setMaximumSize(QSize(16777215, 200))
        self.gridLayout_2 = QGridLayout(self.parentPanel5)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.panel6 = QWidget(self.parentPanel5)
        self.panel6.setObjectName(u"panel6")
        sizePolicy.setHeightForWidth(self.panel6.sizePolicy().hasHeightForWidth())
        self.panel6.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.panel6, 1, 0, 1, 1)

        self.controllerPanel5 = QWidget(self.parentPanel5)
        self.controllerPanel5.setObjectName(u"controllerPanel5")
        self.controllerPanel5.setMinimumSize(QSize(0, 30))
        self.controllerPanel5.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_9 = QHBoxLayout(self.controllerPanel5)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.headerPanel5 = LabelHorizontal(self.controllerPanel5)
        self.headerPanel5.setObjectName(u"headerPanel5")
        self.headerPanel5.setMargin(0)

        self.horizontalLayout_9.addWidget(self.headerPanel5)

        self.controllerIcons5 = QFrame(self.controllerPanel5)
        self.controllerIcons5.setObjectName(u"controllerIcons5")
        self.controllerIcons5.setMinimumSize(QSize(60, 0))
        self.controllerIcons5.setMaximumSize(QSize(60, 16777215))
        self.controllerIcons5.setFrameShape(QFrame.StyledPanel)
        self.controllerIcons5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.controllerIcons5)
        self.horizontalLayout_8.setSpacing(3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.panelSettings5 = QPushButton(self.controllerIcons5)
        self.panelSettings5.setObjectName(u"panelSettings5")
        self.panelSettings5.setMinimumSize(QSize(28, 28))
        self.panelSettings5.setMaximumSize(QSize(28, 28))
        self.panelSettings5.setSizeIncrement(QSize(0, 0))
        self.panelSettings5.setBaseSize(QSize(0, 0))
#if QT_CONFIG(tooltip)
        self.panelSettings5.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.panelSettings5.setIcon(icon5)
        self.panelSettings5.setIconSize(QSize(12, 12))
        self.panelSettings5.setAutoDefault(False)
        self.panelSettings5.setFlat(True)

        self.horizontalLayout_8.addWidget(self.panelSettings5, 0, Qt.AlignRight)

        self.togglePanel5 = QPushButton(self.controllerIcons5)
        self.togglePanel5.setObjectName(u"togglePanel5")
        self.togglePanel5.setMinimumSize(QSize(28, 28))
        self.togglePanel5.setMaximumSize(QSize(28, 28))
        self.togglePanel5.setSizeIncrement(QSize(0, 0))
        self.togglePanel5.setBaseSize(QSize(0, 0))
#if QT_CONFIG(tooltip)
        self.togglePanel5.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.togglePanel5.setAutoFillBackground(False)
        icon7 = QIcon()
        icon7.addFile(u":/gray-icons/gui/resources/icons/gray/chevron-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.togglePanel5.setIcon(icon7)
        self.togglePanel5.setFlat(True)

        self.horizontalLayout_8.addWidget(self.togglePanel5, 0, Qt.AlignRight)


        self.horizontalLayout_9.addWidget(self.controllerIcons5)


        self.gridLayout_2.addWidget(self.controllerPanel5, 0, 0, 1, 3)

        self.panel5 = QWidget(self.parentPanel5)
        self.panel5.setObjectName(u"panel5")
        self.label_5 = QLabel(self.panel5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(690, 90, 49, 16))

        self.gridLayout_2.addWidget(self.panel5, 1, 1, 1, 1)

        self.controllerPanel6 = QWidget(self.parentPanel5)
        self.controllerPanel6.setObjectName(u"controllerPanel6")
        self.controllerPanel6.setMinimumSize(QSize(30, 0))
        self.controllerPanel6.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_2.addWidget(self.controllerPanel6, 1, 2, 1, 1)


        self.verticalLayout.addWidget(self.parentPanel5)


        self.gridLayout.addWidget(self.panelContainer, 1, 0, 1, 1)

        self.parentPanel4 = QWidget(self.mainFrame)
        self.parentPanel4.setObjectName(u"parentPanel4")
        self.parentPanel4.setMinimumSize(QSize(300, 0))
        self.parentPanel4.setMaximumSize(QSize(300, 16777215))
        self.horizontalLayout_4 = QHBoxLayout(self.parentPanel4)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.panel4 = QWidget(self.parentPanel4)
        self.panel4.setObjectName(u"panel4")
        self.panel4.setMaximumSize(QSize(300, 16777215))
        self.panel4.setStyleSheet(u"border: 0px solid;")
        self.verticalLayout_9 = QVBoxLayout(self.panel4)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.themingsTabs = QTabWidget(self.panel4)
        self.themingsTabs.setObjectName(u"themingsTabs")
        sizePolicy.setHeightForWidth(self.themingsTabs.sizePolicy().hasHeightForWidth())
        self.themingsTabs.setSizePolicy(sizePolicy)
        self.themingsTabs.setStyleSheet(u"\n"
"*{\n"
"	background: #1b202c;\n"
"	color: #fff;\n"
"}\n"
"\n"
"\n"
"QTabWidget::pane {\n"
"    border: 0px solid #1b202c;\n"
"	top:-1px;\n"
"}\n"
"\n"
"/*\n"
"QTabWidget::tab-bar {\n"
"    background: #1b202c;\n"
"	border: 1px solid #1b202c;\n"
"	padding: 8px;\n"
"	color: #37c886;\n"
"	font-weight: bold;\n"
"	width: 117px;\n"
"}\n"
"*/\n"
"\n"
"QTabBar::tab {\n"
"	background: #1b202c;\n"
"	border: 1px solid #13161f;\n"
"	padding: 8px;\n"
"	color: #37c886;\n"
"	font-weight: bold;\n"
"	width: 117px;\n"
"  }\n"
"\n"
"QTabBar::scroller {width: 0px;}\n"
"\n"
"QTabBar::tab:selected {\n"
"	background: #1b202c;\n"
"	margin-bottom: -1px;\n"
"	color: #dce1ec;\n"
"	border-bottom: 2px solid #37c886;;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QTabBar::tab {\n"
"	background: #1b202c;\n"
"	border: 1px solid #1b202c;\n"
"	padding: 8px;\n"
"	color: #37c886;\n"
"	font-weight: bold;\n"
"	width: 117px;\n"
"}\n"
"\n"
"\n"
"QFrame{ \n"
"    border: 0px solid;\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"	border: 2px solid teal;\n"
"	border-radius:"
                        " 12px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border: 3px solid cyan;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	border: 4px solid cyan;\n"
"}\n"
"\n"
"#headerBgColor1,#footerBgColor1,#controllerBgColor1,#panelBgColor1{background: #0b0f13;}\n"
"#headerBgColor2,#footerBgColor2,#controllerBgColor2,#panelBgColor2{background: #1b202c;}\n"
"#headerBgColor3,#footerBgColor3,#controllerBgColor3,#panelBgColor3{background: #13161f;}\n"
"#headerBgColor4,#footerBgColor4,#controllerBgColor4,#panelBgColor4{background: #343a40;}\n"
"#headerBgColor5,#footerBgColor5,#controllerBgColor5,#panelBgColor5{background: #6c757d;}\n"
"#headerBgColor6,#footerBgColor6,#controllerBgColor6,#panelBgColor6{background: #007bff;}\n"
"#headerBgColor7,#footerBgColor7,#controllerBgColor7,#panelBgColor7{background: #20c997;}\n"
"#headerBgColor8,#footerBgColor8,#controllerBgColor8,#panelBgColor8{background: #ff8f00;}\n"
"#headerBgColor9,#footerBgColor9,#controllerBgColor9,#panelBgColor9{background: #f8f9fa;}\n"
"#headerBgColor10,#footerBgColor10,#con"
                        "trollerBgColor10,#panelBgColor10{background: #6f42c1;}\n"
"\n"
"#iconBgColor1{ background: aqua; }\n"
"#iconBgColor2{ background: black; }\n"
"#iconBgColor3{ background: blue; }\n"
"#iconBgColor4{ background: yellow; }\n"
"#iconBgColor5{ background: gray; }\n"
"#iconBgColor6{ background: green; }\n"
"#iconBgColor7{ background: magenta; }\n"
"#iconBgColor8{ background: white; }\n"
"#iconBgColor9{ background: purple; }\n"
"#iconBgColor10{ background: red; }\n"
"\n"
"/*\n"
"--blue: #007bff;\n"
"--indigo: #6610f2;\n"
"--purple: #6f42c1;\n"
"--pink: #e83e8c;\n"
"--red: #dc3545;\n"
"--orange: #fd7e14;\n"
"--yellow: #ffc107;\n"
"--green: #28a745;\n"
"--teal: #20c997;\n"
"--cyan: #17a2b8;\n"
"--white: #ffffff;\n"
"--gray: #6c757d;\n"
"--gray-dark: #343a40;\n"
"--primary: #007bff;\n"
"--secondary: #6c757d;\n"
"--success: #28a745;\n"
"--info: #17a2b8;\n"
"--warning: #ffc107;\n"
"--danger: #dc3545;\n"
"--light: #f8f9fa;\n"
"--dark: #343a40;\n"
"*/\n"
"\n"
"\n"
"/*\n"
"#11131b #13161f #161924\n"
"panel\n"
"#171c26 #1b202c"
                        " #1f2533\n"
"*/\n"
"\n"
"QToolBox::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #13161f, stop: 0.4 #161924,\n"
"                                stop: 0.5 #171c26, stop: 1.0 #1b202c);\n"
"    border-radius: 5px;\n"
"    color: darkgray;\n"
"}\n"
"\n"
"QToolBox::tab:selected { \n"
"    font: italic;\n"
"    color: #37c886;\n"
"}\n"
"")
        self.themingsTabs.setTabShape(QTabWidget.Rounded)
        self.appTheming = QWidget()
        self.appTheming.setObjectName(u"appTheming")
        self.appTheming.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.appTheming)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.appTheming)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_12 = QVBoxLayout(self.widget_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.widget_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 253, 765))
        self.verticalLayout_19 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.widget_4 = QWidget(self.scrollAreaWidgetContents)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_18 = QVBoxLayout(self.widget_4)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.widget_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_13.addWidget(self.label_10)

        self.panelsBackground = QFrame(self.frame_2)
        self.panelsBackground.setObjectName(u"panelsBackground")
        self.panelsBackground.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground.setStyleSheet(u"")
        self.panelsBackground.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.panelsBackground)
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, -1, 0, -1)
        self.headerBgColor1 = QPushButton(self.panelsBackground)
        self.headerBgColor1.setObjectName(u"headerBgColor1")
        self.headerBgColor1.setMinimumSize(QSize(24, 24))
        self.headerBgColor1.setMaximumSize(QSize(24, 24))
        self.headerBgColor1.setCheckable(True)

        self.horizontalLayout_11.addWidget(self.headerBgColor1)

        self.headerBgColor2 = QPushButton(self.panelsBackground)
        self.headerBgColor2.setObjectName(u"headerBgColor2")
        self.headerBgColor2.setMinimumSize(QSize(24, 24))
        self.headerBgColor2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_11.addWidget(self.headerBgColor2)

        self.headerBgColor3 = QPushButton(self.panelsBackground)
        self.headerBgColor3.setObjectName(u"headerBgColor3")
        self.headerBgColor3.setMinimumSize(QSize(24, 24))
        self.headerBgColor3.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_11.addWidget(self.headerBgColor3)

        self.headerBgColor4 = QPushButton(self.panelsBackground)
        self.headerBgColor4.setObjectName(u"headerBgColor4")
        self.headerBgColor4.setMinimumSize(QSize(24, 24))
        self.headerBgColor4.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_11.addWidget(self.headerBgColor4)

        self.headerBgColor5 = QPushButton(self.panelsBackground)
        self.headerBgColor5.setObjectName(u"headerBgColor5")
        self.headerBgColor5.setMinimumSize(QSize(24, 24))
        self.headerBgColor5.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_11.addWidget(self.headerBgColor5)


        self.verticalLayout_13.addWidget(self.panelsBackground)

        self.panelsBackground_2 = QFrame(self.frame_2)
        self.panelsBackground_2.setObjectName(u"panelsBackground_2")
        self.panelsBackground_2.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_2.setStyleSheet(u"")
        self.panelsBackground_2.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.panelsBackground_2)
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, -1, 0, -1)
        self.headerBgColor6 = QPushButton(self.panelsBackground_2)
        self.headerBgColor6.setObjectName(u"headerBgColor6")
        self.headerBgColor6.setMinimumSize(QSize(24, 24))
        self.headerBgColor6.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_12.addWidget(self.headerBgColor6)

        self.headerBgColor7 = QPushButton(self.panelsBackground_2)
        self.headerBgColor7.setObjectName(u"headerBgColor7")
        self.headerBgColor7.setMinimumSize(QSize(24, 24))
        self.headerBgColor7.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_12.addWidget(self.headerBgColor7)

        self.headerBgColor8 = QPushButton(self.panelsBackground_2)
        self.headerBgColor8.setObjectName(u"headerBgColor8")
        self.headerBgColor8.setMinimumSize(QSize(24, 24))
        self.headerBgColor8.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_12.addWidget(self.headerBgColor8)

        self.headerBgColor9 = QPushButton(self.panelsBackground_2)
        self.headerBgColor9.setObjectName(u"headerBgColor9")
        self.headerBgColor9.setMinimumSize(QSize(24, 24))
        self.headerBgColor9.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_12.addWidget(self.headerBgColor9)

        self.headerBgColor10 = QPushButton(self.panelsBackground_2)
        self.headerBgColor10.setObjectName(u"headerBgColor10")
        self.headerBgColor10.setMinimumSize(QSize(24, 24))
        self.headerBgColor10.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_12.addWidget(self.headerBgColor10)


        self.verticalLayout_13.addWidget(self.panelsBackground_2)


        self.verticalLayout_18.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.widget_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_11 = QLabel(self.frame_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_15.addWidget(self.label_11)

        self.panelsBackground_3 = QFrame(self.frame_3)
        self.panelsBackground_3.setObjectName(u"panelsBackground_3")
        self.panelsBackground_3.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_3.setStyleSheet(u"")
        self.panelsBackground_3.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.panelsBackground_3)
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, -1, 0, -1)
        self.panelBgColor1 = QPushButton(self.panelsBackground_3)
        self.panelBgColor1.setObjectName(u"panelBgColor1")
        self.panelBgColor1.setMinimumSize(QSize(24, 24))
        self.panelBgColor1.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_13.addWidget(self.panelBgColor1)

        self.panelBgColor2 = QPushButton(self.panelsBackground_3)
        self.panelBgColor2.setObjectName(u"panelBgColor2")
        self.panelBgColor2.setMinimumSize(QSize(24, 24))
        self.panelBgColor2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_13.addWidget(self.panelBgColor2)

        self.panelBgColor3 = QPushButton(self.panelsBackground_3)
        self.panelBgColor3.setObjectName(u"panelBgColor3")
        self.panelBgColor3.setMinimumSize(QSize(24, 24))
        self.panelBgColor3.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_13.addWidget(self.panelBgColor3)

        self.panelBgColor4 = QPushButton(self.panelsBackground_3)
        self.panelBgColor4.setObjectName(u"panelBgColor4")
        self.panelBgColor4.setMinimumSize(QSize(24, 24))
        self.panelBgColor4.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_13.addWidget(self.panelBgColor4)

        self.panelBgColor5 = QPushButton(self.panelsBackground_3)
        self.panelBgColor5.setObjectName(u"panelBgColor5")
        self.panelBgColor5.setMinimumSize(QSize(24, 24))
        self.panelBgColor5.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_13.addWidget(self.panelBgColor5)


        self.verticalLayout_15.addWidget(self.panelsBackground_3)

        self.panelsBackground_4 = QFrame(self.frame_3)
        self.panelsBackground_4.setObjectName(u"panelsBackground_4")
        self.panelsBackground_4.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_4.setStyleSheet(u"")
        self.panelsBackground_4.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.panelsBackground_4)
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, -1, 0, -1)
        self.panelBgColor6 = QPushButton(self.panelsBackground_4)
        self.panelBgColor6.setObjectName(u"panelBgColor6")
        self.panelBgColor6.setMinimumSize(QSize(24, 24))
        self.panelBgColor6.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_14.addWidget(self.panelBgColor6)

        self.panelBgColor7 = QPushButton(self.panelsBackground_4)
        self.panelBgColor7.setObjectName(u"panelBgColor7")
        self.panelBgColor7.setMinimumSize(QSize(24, 24))
        self.panelBgColor7.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_14.addWidget(self.panelBgColor7)

        self.panelBgColor8 = QPushButton(self.panelsBackground_4)
        self.panelBgColor8.setObjectName(u"panelBgColor8")
        self.panelBgColor8.setMinimumSize(QSize(24, 24))
        self.panelBgColor8.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_14.addWidget(self.panelBgColor8)

        self.panelBgColor9 = QPushButton(self.panelsBackground_4)
        self.panelBgColor9.setObjectName(u"panelBgColor9")
        self.panelBgColor9.setMinimumSize(QSize(24, 24))
        self.panelBgColor9.setMaximumSize(QSize(24, 24))
        self.panelBgColor9.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.panelBgColor9)

        self.panelBgColor10 = QPushButton(self.panelsBackground_4)
        self.panelBgColor10.setObjectName(u"panelBgColor10")
        self.panelBgColor10.setMinimumSize(QSize(24, 24))
        self.panelBgColor10.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_14.addWidget(self.panelBgColor10)


        self.verticalLayout_15.addWidget(self.panelsBackground_4)


        self.verticalLayout_18.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.widget_4)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_4)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_12 = QLabel(self.frame_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_17.addWidget(self.label_12)

        self.panelsBackground_5 = QFrame(self.frame_4)
        self.panelsBackground_5.setObjectName(u"panelsBackground_5")
        self.panelsBackground_5.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_5.setStyleSheet(u"")
        self.panelsBackground_5.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.panelsBackground_5)
        self.horizontalLayout_15.setSpacing(6)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, -1, 0, -1)
        self.footerBgColor1 = QPushButton(self.panelsBackground_5)
        self.footerBgColor1.setObjectName(u"footerBgColor1")
        self.footerBgColor1.setMinimumSize(QSize(24, 24))
        self.footerBgColor1.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_15.addWidget(self.footerBgColor1)

        self.footerBgColor2 = QPushButton(self.panelsBackground_5)
        self.footerBgColor2.setObjectName(u"footerBgColor2")
        self.footerBgColor2.setMinimumSize(QSize(24, 24))
        self.footerBgColor2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_15.addWidget(self.footerBgColor2)

        self.footerBgColor3 = QPushButton(self.panelsBackground_5)
        self.footerBgColor3.setObjectName(u"footerBgColor3")
        self.footerBgColor3.setMinimumSize(QSize(24, 24))
        self.footerBgColor3.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_15.addWidget(self.footerBgColor3)

        self.footerBgColor4 = QPushButton(self.panelsBackground_5)
        self.footerBgColor4.setObjectName(u"footerBgColor4")
        self.footerBgColor4.setMinimumSize(QSize(24, 24))
        self.footerBgColor4.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_15.addWidget(self.footerBgColor4)

        self.footerBgColor5 = QPushButton(self.panelsBackground_5)
        self.footerBgColor5.setObjectName(u"footerBgColor5")
        self.footerBgColor5.setMinimumSize(QSize(24, 24))
        self.footerBgColor5.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_15.addWidget(self.footerBgColor5)


        self.verticalLayout_17.addWidget(self.panelsBackground_5)

        self.panelsBackground_6 = QFrame(self.frame_4)
        self.panelsBackground_6.setObjectName(u"panelsBackground_6")
        self.panelsBackground_6.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_6.setStyleSheet(u"")
        self.panelsBackground_6.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.panelsBackground_6)
        self.horizontalLayout_16.setSpacing(6)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, -1, 0, -1)
        self.footerBgColor6 = QPushButton(self.panelsBackground_6)
        self.footerBgColor6.setObjectName(u"footerBgColor6")
        self.footerBgColor6.setMinimumSize(QSize(24, 24))
        self.footerBgColor6.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_16.addWidget(self.footerBgColor6)

        self.footerBgColor7 = QPushButton(self.panelsBackground_6)
        self.footerBgColor7.setObjectName(u"footerBgColor7")
        self.footerBgColor7.setMinimumSize(QSize(24, 24))
        self.footerBgColor7.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_16.addWidget(self.footerBgColor7)

        self.footerBgColor8 = QPushButton(self.panelsBackground_6)
        self.footerBgColor8.setObjectName(u"footerBgColor8")
        self.footerBgColor8.setMinimumSize(QSize(24, 24))
        self.footerBgColor8.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_16.addWidget(self.footerBgColor8)

        self.footerBgColor9 = QPushButton(self.panelsBackground_6)
        self.footerBgColor9.setObjectName(u"footerBgColor9")
        self.footerBgColor9.setMinimumSize(QSize(24, 24))
        self.footerBgColor9.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_16.addWidget(self.footerBgColor9)

        self.footerBgColor10 = QPushButton(self.panelsBackground_6)
        self.footerBgColor10.setObjectName(u"footerBgColor10")
        self.footerBgColor10.setMinimumSize(QSize(24, 24))
        self.footerBgColor10.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_16.addWidget(self.footerBgColor10)


        self.verticalLayout_17.addWidget(self.panelsBackground_6)


        self.verticalLayout_18.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.widget_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_14.addWidget(self.label_13)

        self.panelsBackground_7 = QFrame(self.frame_5)
        self.panelsBackground_7.setObjectName(u"panelsBackground_7")
        self.panelsBackground_7.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_7.setStyleSheet(u"")
        self.panelsBackground_7.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.panelsBackground_7)
        self.horizontalLayout_18.setSpacing(6)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, -1, 0, -1)
        self.controllerBgColor1 = QPushButton(self.panelsBackground_7)
        self.controllerBgColor1.setObjectName(u"controllerBgColor1")
        self.controllerBgColor1.setMinimumSize(QSize(24, 24))
        self.controllerBgColor1.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_18.addWidget(self.controllerBgColor1)

        self.controllerBgColor2 = QPushButton(self.panelsBackground_7)
        self.controllerBgColor2.setObjectName(u"controllerBgColor2")
        self.controllerBgColor2.setMinimumSize(QSize(24, 24))
        self.controllerBgColor2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_18.addWidget(self.controllerBgColor2)

        self.controllerBgColor3 = QPushButton(self.panelsBackground_7)
        self.controllerBgColor3.setObjectName(u"controllerBgColor3")
        self.controllerBgColor3.setMinimumSize(QSize(24, 24))
        self.controllerBgColor3.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_18.addWidget(self.controllerBgColor3)

        self.controllerBgColor4 = QPushButton(self.panelsBackground_7)
        self.controllerBgColor4.setObjectName(u"controllerBgColor4")
        self.controllerBgColor4.setMinimumSize(QSize(24, 24))
        self.controllerBgColor4.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_18.addWidget(self.controllerBgColor4)

        self.controllerBgColor5 = QPushButton(self.panelsBackground_7)
        self.controllerBgColor5.setObjectName(u"controllerBgColor5")
        self.controllerBgColor5.setMinimumSize(QSize(24, 24))
        self.controllerBgColor5.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_18.addWidget(self.controllerBgColor5)


        self.verticalLayout_14.addWidget(self.panelsBackground_7)

        self.panelsBackground_8 = QFrame(self.frame_5)
        self.panelsBackground_8.setObjectName(u"panelsBackground_8")
        self.panelsBackground_8.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_8.setStyleSheet(u"")
        self.panelsBackground_8.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.panelsBackground_8)
        self.horizontalLayout_19.setSpacing(6)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, -1, 0, -1)
        self.controllerBgColor6 = QPushButton(self.panelsBackground_8)
        self.controllerBgColor6.setObjectName(u"controllerBgColor6")
        self.controllerBgColor6.setMinimumSize(QSize(24, 24))
        self.controllerBgColor6.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_19.addWidget(self.controllerBgColor6)

        self.controllerBgColor7 = QPushButton(self.panelsBackground_8)
        self.controllerBgColor7.setObjectName(u"controllerBgColor7")
        self.controllerBgColor7.setMinimumSize(QSize(24, 24))
        self.controllerBgColor7.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_19.addWidget(self.controllerBgColor7)

        self.controllerBgColor8 = QPushButton(self.panelsBackground_8)
        self.controllerBgColor8.setObjectName(u"controllerBgColor8")
        self.controllerBgColor8.setMinimumSize(QSize(24, 24))
        self.controllerBgColor8.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_19.addWidget(self.controllerBgColor8)

        self.controllerBgColor9 = QPushButton(self.panelsBackground_8)
        self.controllerBgColor9.setObjectName(u"controllerBgColor9")
        self.controllerBgColor9.setMinimumSize(QSize(24, 24))
        self.controllerBgColor9.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_19.addWidget(self.controllerBgColor9)

        self.controllerBgColor10 = QPushButton(self.panelsBackground_8)
        self.controllerBgColor10.setObjectName(u"controllerBgColor10")
        self.controllerBgColor10.setMinimumSize(QSize(24, 24))
        self.controllerBgColor10.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_19.addWidget(self.controllerBgColor10)


        self.verticalLayout_14.addWidget(self.panelsBackground_8)


        self.verticalLayout_18.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.widget_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_14 = QLabel(self.frame_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_16.addWidget(self.label_14)

        self.panelsBackground_9 = QFrame(self.frame_6)
        self.panelsBackground_9.setObjectName(u"panelsBackground_9")
        self.panelsBackground_9.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_9.setStyleSheet(u"")
        self.panelsBackground_9.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.panelsBackground_9)
        self.horizontalLayout_20.setSpacing(6)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, -1, 0, -1)
        self.iconBgColor1 = QPushButton(self.panelsBackground_9)
        self.iconBgColor1.setObjectName(u"iconBgColor1")
        self.iconBgColor1.setMinimumSize(QSize(24, 24))
        self.iconBgColor1.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_20.addWidget(self.iconBgColor1)

        self.iconBgColor2 = QPushButton(self.panelsBackground_9)
        self.iconBgColor2.setObjectName(u"iconBgColor2")
        self.iconBgColor2.setMinimumSize(QSize(24, 24))
        self.iconBgColor2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_20.addWidget(self.iconBgColor2)

        self.iconBgColor3 = QPushButton(self.panelsBackground_9)
        self.iconBgColor3.setObjectName(u"iconBgColor3")
        self.iconBgColor3.setMinimumSize(QSize(24, 24))
        self.iconBgColor3.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_20.addWidget(self.iconBgColor3)

        self.iconBgColor4 = QPushButton(self.panelsBackground_9)
        self.iconBgColor4.setObjectName(u"iconBgColor4")
        self.iconBgColor4.setMinimumSize(QSize(24, 24))
        self.iconBgColor4.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_20.addWidget(self.iconBgColor4)

        self.iconBgColor5 = QPushButton(self.panelsBackground_9)
        self.iconBgColor5.setObjectName(u"iconBgColor5")
        self.iconBgColor5.setMinimumSize(QSize(24, 24))
        self.iconBgColor5.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_20.addWidget(self.iconBgColor5)


        self.verticalLayout_16.addWidget(self.panelsBackground_9)

        self.panelsBackground_10 = QFrame(self.frame_6)
        self.panelsBackground_10.setObjectName(u"panelsBackground_10")
        self.panelsBackground_10.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_10.setStyleSheet(u"")
        self.panelsBackground_10.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.panelsBackground_10)
        self.horizontalLayout_21.setSpacing(6)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, -1, 0, -1)
        self.iconBgColor6 = QPushButton(self.panelsBackground_10)
        self.iconBgColor6.setObjectName(u"iconBgColor6")
        self.iconBgColor6.setMinimumSize(QSize(24, 24))
        self.iconBgColor6.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_21.addWidget(self.iconBgColor6)

        self.iconBgColor7 = QPushButton(self.panelsBackground_10)
        self.iconBgColor7.setObjectName(u"iconBgColor7")
        self.iconBgColor7.setMinimumSize(QSize(24, 24))
        self.iconBgColor7.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_21.addWidget(self.iconBgColor7)

        self.iconBgColor8 = QPushButton(self.panelsBackground_10)
        self.iconBgColor8.setObjectName(u"iconBgColor8")
        self.iconBgColor8.setMinimumSize(QSize(24, 24))
        self.iconBgColor8.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_21.addWidget(self.iconBgColor8)

        self.iconBgColor9 = QPushButton(self.panelsBackground_10)
        self.iconBgColor9.setObjectName(u"iconBgColor9")
        self.iconBgColor9.setMinimumSize(QSize(24, 24))
        self.iconBgColor9.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_21.addWidget(self.iconBgColor9)

        self.iconBgColor10 = QPushButton(self.panelsBackground_10)
        self.iconBgColor10.setObjectName(u"iconBgColor10")
        self.iconBgColor10.setMinimumSize(QSize(24, 24))
        self.iconBgColor10.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_21.addWidget(self.iconBgColor10)


        self.verticalLayout_16.addWidget(self.panelsBackground_10)

        self.fontComboBox = QFontComboBox(self.frame_6)
        self.fontComboBox.setObjectName(u"fontComboBox")

        self.verticalLayout_16.addWidget(self.fontComboBox)

        self.themeColors = QComboBox(self.frame_6)
        self.themeColors.addItem("")
        self.themeColors.addItem("")
        self.themeColors.addItem("")
        self.themeColors.setObjectName(u"themeColors")

        self.verticalLayout_16.addWidget(self.themeColors)


        self.verticalLayout_18.addWidget(self.frame_6)

        self.frame = QFrame(self.widget_4)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_8.addWidget(self.label_6, 0, 0, 1, 1)

        self.checkBox_5 = AnimatedCheck(self.frame)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.gridLayout_8.addWidget(self.checkBox_5, 0, 1, 1, 1)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_8.addWidget(self.label_7, 1, 0, 1, 1)

        self.checkBox_6 = AnimatedCheck(self.frame)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.gridLayout_8.addWidget(self.checkBox_6, 1, 1, 1, 1)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_8.addWidget(self.label_8, 2, 0, 1, 1)

        self.checkBox_7 = AnimatedCheck(self.frame)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.gridLayout_8.addWidget(self.checkBox_7, 2, 1, 1, 1)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_8.addWidget(self.label_9, 3, 0, 1, 1)

        self.checkBox_8 = AnimatedCheck(self.frame)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.gridLayout_8.addWidget(self.checkBox_8, 3, 1, 1, 1)


        self.verticalLayout_18.addWidget(self.frame)


        self.verticalLayout_19.addWidget(self.widget_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_12.addWidget(self.scrollArea)


        self.verticalLayout_6.addWidget(self.widget_3)

        self.themingsTabs.addTab(self.appTheming, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_22 = QVBoxLayout(self.tab)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.toolBox = QToolBox(self.tab)
        self.toolBox.setObjectName(u"toolBox")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 252, 610))
        self.frame_7 = QFrame(self.page)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(10, 10, 235, 123))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_7)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_17 = QLabel(self.frame_7)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_23.addWidget(self.label_17)

        self.panelsBackground_11 = QFrame(self.frame_7)
        self.panelsBackground_11.setObjectName(u"panelsBackground_11")
        self.panelsBackground_11.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_11.setStyleSheet(u"")
        self.panelsBackground_11.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.panelsBackground_11)
        self.horizontalLayout_23.setSpacing(6)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, -1, 0, -1)
        self.headerBgColor1_2 = QPushButton(self.panelsBackground_11)
        self.headerBgColor1_2.setObjectName(u"headerBgColor1_2")
        self.headerBgColor1_2.setMinimumSize(QSize(24, 24))
        self.headerBgColor1_2.setMaximumSize(QSize(24, 24))
        self.headerBgColor1_2.setCheckable(True)

        self.horizontalLayout_23.addWidget(self.headerBgColor1_2)

        self.headerBgColor2_2 = QPushButton(self.panelsBackground_11)
        self.headerBgColor2_2.setObjectName(u"headerBgColor2_2")
        self.headerBgColor2_2.setMinimumSize(QSize(24, 24))
        self.headerBgColor2_2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_23.addWidget(self.headerBgColor2_2)

        self.headerBgColor3_2 = QPushButton(self.panelsBackground_11)
        self.headerBgColor3_2.setObjectName(u"headerBgColor3_2")
        self.headerBgColor3_2.setMinimumSize(QSize(24, 24))
        self.headerBgColor3_2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_23.addWidget(self.headerBgColor3_2)

        self.headerBgColor4_2 = QPushButton(self.panelsBackground_11)
        self.headerBgColor4_2.setObjectName(u"headerBgColor4_2")
        self.headerBgColor4_2.setMinimumSize(QSize(24, 24))
        self.headerBgColor4_2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_23.addWidget(self.headerBgColor4_2)

        self.headerBgColor5_2 = QPushButton(self.panelsBackground_11)
        self.headerBgColor5_2.setObjectName(u"headerBgColor5_2")
        self.headerBgColor5_2.setMinimumSize(QSize(24, 24))
        self.headerBgColor5_2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_23.addWidget(self.headerBgColor5_2)


        self.verticalLayout_23.addWidget(self.panelsBackground_11)

        self.panelsBackground_12 = QFrame(self.frame_7)
        self.panelsBackground_12.setObjectName(u"panelsBackground_12")
        self.panelsBackground_12.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_12.setStyleSheet(u"")
        self.panelsBackground_12.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.panelsBackground_12)
        self.horizontalLayout_24.setSpacing(6)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, -1, 0, -1)
        self.headerBgColor6_2 = QPushButton(self.panelsBackground_12)
        self.headerBgColor6_2.setObjectName(u"headerBgColor6_2")
        self.headerBgColor6_2.setMinimumSize(QSize(24, 24))
        self.headerBgColor6_2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_24.addWidget(self.headerBgColor6_2)

        self.headerBgColor7_2 = QPushButton(self.panelsBackground_12)
        self.headerBgColor7_2.setObjectName(u"headerBgColor7_2")
        self.headerBgColor7_2.setMinimumSize(QSize(24, 24))
        self.headerBgColor7_2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_24.addWidget(self.headerBgColor7_2)

        self.headerBgColor8_2 = QPushButton(self.panelsBackground_12)
        self.headerBgColor8_2.setObjectName(u"headerBgColor8_2")
        self.headerBgColor8_2.setMinimumSize(QSize(24, 24))
        self.headerBgColor8_2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_24.addWidget(self.headerBgColor8_2)

        self.headerBgColor9_2 = QPushButton(self.panelsBackground_12)
        self.headerBgColor9_2.setObjectName(u"headerBgColor9_2")
        self.headerBgColor9_2.setMinimumSize(QSize(24, 24))
        self.headerBgColor9_2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_24.addWidget(self.headerBgColor9_2)

        self.headerBgColor10_2 = QPushButton(self.panelsBackground_12)
        self.headerBgColor10_2.setObjectName(u"headerBgColor10_2")
        self.headerBgColor10_2.setMinimumSize(QSize(24, 24))
        self.headerBgColor10_2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_24.addWidget(self.headerBgColor10_2)


        self.verticalLayout_23.addWidget(self.panelsBackground_12)

        self.frame_8 = QFrame(self.page)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(10, 150, 235, 51))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_8)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.panelsBackground_13 = QFrame(self.frame_8)
        self.panelsBackground_13.setObjectName(u"panelsBackground_13")
        self.panelsBackground_13.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_13.setStyleSheet(u"")
        self.panelsBackground_13.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.panelsBackground_13)
        self.horizontalLayout_25.setSpacing(6)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, -1, 0, -1)
        self.label_18 = QLabel(self.panelsBackground_13)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_25.addWidget(self.label_18)

        self.headerBgColor3_3 = QPushButton(self.panelsBackground_13)
        self.headerBgColor3_3.setObjectName(u"headerBgColor3_3")
        self.headerBgColor3_3.setMinimumSize(QSize(24, 24))
        self.headerBgColor3_3.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_25.addWidget(self.headerBgColor3_3)

        self.headerBgColor4_3 = QPushButton(self.panelsBackground_13)
        self.headerBgColor4_3.setObjectName(u"headerBgColor4_3")
        self.headerBgColor4_3.setMinimumSize(QSize(24, 24))
        self.headerBgColor4_3.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_25.addWidget(self.headerBgColor4_3)

        self.headerBgColor5_3 = QPushButton(self.panelsBackground_13)
        self.headerBgColor5_3.setObjectName(u"headerBgColor5_3")
        self.headerBgColor5_3.setMinimumSize(QSize(24, 24))
        self.headerBgColor5_3.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_25.addWidget(self.headerBgColor5_3)


        self.verticalLayout_24.addWidget(self.panelsBackground_13)

        self.frame_11 = QFrame(self.page)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(10, 220, 235, 51))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_11)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.panelsBackground_14 = QFrame(self.frame_11)
        self.panelsBackground_14.setObjectName(u"panelsBackground_14")
        self.panelsBackground_14.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_14.setStyleSheet(u"")
        self.panelsBackground_14.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.panelsBackground_14)
        self.horizontalLayout_26.setSpacing(6)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, -1, 0, -1)
        self.label_21 = QLabel(self.panelsBackground_14)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_26.addWidget(self.label_21)

        self.headerBgColor3_6 = QPushButton(self.panelsBackground_14)
        self.headerBgColor3_6.setObjectName(u"headerBgColor3_6")
        self.headerBgColor3_6.setMinimumSize(QSize(24, 24))
        self.headerBgColor3_6.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_26.addWidget(self.headerBgColor3_6)

        self.headerBgColor4_6 = QPushButton(self.panelsBackground_14)
        self.headerBgColor4_6.setObjectName(u"headerBgColor4_6")
        self.headerBgColor4_6.setMinimumSize(QSize(24, 24))
        self.headerBgColor4_6.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_26.addWidget(self.headerBgColor4_6)

        self.headerBgColor5_6 = QPushButton(self.panelsBackground_14)
        self.headerBgColor5_6.setObjectName(u"headerBgColor5_6")
        self.headerBgColor5_6.setMinimumSize(QSize(24, 24))
        self.headerBgColor5_6.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_26.addWidget(self.headerBgColor5_6)


        self.verticalLayout_27.addWidget(self.panelsBackground_14)

        self.frame_12 = QFrame(self.page)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(10, 290, 235, 51))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_12)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.panelsBackground_15 = QFrame(self.frame_12)
        self.panelsBackground_15.setObjectName(u"panelsBackground_15")
        self.panelsBackground_15.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_15.setStyleSheet(u"")
        self.panelsBackground_15.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.panelsBackground_15)
        self.horizontalLayout_27.setSpacing(6)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, -1, 0, -1)
        self.label_22 = QLabel(self.panelsBackground_15)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_27.addWidget(self.label_22)

        self.headerBgColor3_7 = QPushButton(self.panelsBackground_15)
        self.headerBgColor3_7.setObjectName(u"headerBgColor3_7")
        self.headerBgColor3_7.setMinimumSize(QSize(24, 24))
        self.headerBgColor3_7.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_27.addWidget(self.headerBgColor3_7)

        self.headerBgColor4_7 = QPushButton(self.panelsBackground_15)
        self.headerBgColor4_7.setObjectName(u"headerBgColor4_7")
        self.headerBgColor4_7.setMinimumSize(QSize(24, 24))
        self.headerBgColor4_7.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_27.addWidget(self.headerBgColor4_7)

        self.headerBgColor5_7 = QPushButton(self.panelsBackground_15)
        self.headerBgColor5_7.setObjectName(u"headerBgColor5_7")
        self.headerBgColor5_7.setMinimumSize(QSize(24, 24))
        self.headerBgColor5_7.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_27.addWidget(self.headerBgColor5_7)


        self.verticalLayout_28.addWidget(self.panelsBackground_15)

        self.frame_13 = QFrame(self.page)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(10, 360, 235, 51))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_13)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.panelsBackground_16 = QFrame(self.frame_13)
        self.panelsBackground_16.setObjectName(u"panelsBackground_16")
        self.panelsBackground_16.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_16.setStyleSheet(u"")
        self.panelsBackground_16.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.panelsBackground_16)
        self.horizontalLayout_28.setSpacing(6)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, -1, 0, -1)
        self.label_23 = QLabel(self.panelsBackground_16)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_28.addWidget(self.label_23)

        self.headerBgColor3_8 = QPushButton(self.panelsBackground_16)
        self.headerBgColor3_8.setObjectName(u"headerBgColor3_8")
        self.headerBgColor3_8.setMinimumSize(QSize(24, 24))
        self.headerBgColor3_8.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_28.addWidget(self.headerBgColor3_8)

        self.headerBgColor4_8 = QPushButton(self.panelsBackground_16)
        self.headerBgColor4_8.setObjectName(u"headerBgColor4_8")
        self.headerBgColor4_8.setMinimumSize(QSize(24, 24))
        self.headerBgColor4_8.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_28.addWidget(self.headerBgColor4_8)

        self.headerBgColor5_8 = QPushButton(self.panelsBackground_16)
        self.headerBgColor5_8.setObjectName(u"headerBgColor5_8")
        self.headerBgColor5_8.setMinimumSize(QSize(24, 24))
        self.headerBgColor5_8.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_28.addWidget(self.headerBgColor5_8)


        self.verticalLayout_29.addWidget(self.panelsBackground_16)

        self.toolBox.addItem(self.page, u"Header")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 252, 637))
        self.toolBox.addItem(self.page_2, u"Content")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.toolBox.addItem(self.page_3, u"Footer")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.toolBox.addItem(self.page_4, u"Controllers")

        self.verticalLayout_22.addWidget(self.toolBox)

        self.themingsTabs.addTab(self.tab, "")
        self.appCustomizing = QWidget()
        self.appCustomizing.setObjectName(u"appCustomizing")
        self.verticalLayout_21 = QVBoxLayout(self.appCustomizing)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.appCustomizing)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_30 = QVBoxLayout(self.widget_5)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.scrollArea2 = QScrollArea(self.widget_5)
        self.scrollArea2.setObjectName(u"scrollArea2")
        self.scrollArea2.setStyleSheet(u"")
        self.scrollArea2.setWidgetResizable(True)
        self.scrollAreaWidgetContents2 = QWidget()
        self.scrollAreaWidgetContents2.setObjectName(u"scrollAreaWidgetContents2")
        self.scrollAreaWidgetContents2.setGeometry(QRect(0, 0, 270, 736))
        self.scrollAreaWidgetContents2.setStyleSheet(u"")
        self.verticalLayout_20 = QVBoxLayout(self.scrollAreaWidgetContents2)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.widget_8 = QWidget(self.scrollAreaWidgetContents2)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_32 = QVBoxLayout(self.widget_8)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.widget_8)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_17)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_15 = QLabel(self.frame_17)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_7.addWidget(self.label_15, 0, 0, 1, 1)

        self.label_27 = QLabel(self.frame_17)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_7.addWidget(self.label_27, 1, 0, 1, 1)

        self.checkBox_24 = AnimatedCheck(self.frame_17)
        self.checkBox_24.setObjectName(u"checkBox_24")

        self.gridLayout_7.addWidget(self.checkBox_24, 1, 1, 1, 1)

        self.label_28 = QLabel(self.frame_17)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_7.addWidget(self.label_28, 2, 0, 1, 1)

        self.checkBox_25 = AnimatedCheck(self.frame_17)
        self.checkBox_25.setObjectName(u"checkBox_25")

        self.gridLayout_7.addWidget(self.checkBox_25, 2, 1, 1, 1)

        self.label_29 = QLabel(self.frame_17)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_7.addWidget(self.label_29, 3, 0, 1, 1)

        self.checkBox_26 = AnimatedCheck(self.frame_17)
        self.checkBox_26.setObjectName(u"checkBox_26")

        self.gridLayout_7.addWidget(self.checkBox_26, 3, 1, 1, 1)

        self.label_30 = QLabel(self.frame_17)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_7.addWidget(self.label_30, 4, 0, 1, 1)

        self.checkBox_27 = AnimatedCheck(self.frame_17)
        self.checkBox_27.setObjectName(u"checkBox_27")

        self.gridLayout_7.addWidget(self.checkBox_27, 4, 1, 1, 1)

        self.label_16 = QLabel(self.frame_17)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_7.addWidget(self.label_16, 5, 0, 1, 1)

        self.label_31 = QLabel(self.frame_17)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_7.addWidget(self.label_31, 6, 0, 1, 1)

        self.checkBox_29 = AnimatedCheck(self.frame_17)
        self.checkBox_29.setObjectName(u"checkBox_29")

        self.gridLayout_7.addWidget(self.checkBox_29, 6, 1, 1, 1)

        self.label_32 = QLabel(self.frame_17)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_7.addWidget(self.label_32, 7, 0, 1, 1)

        self.checkBox_30 = AnimatedCheck(self.frame_17)
        self.checkBox_30.setObjectName(u"checkBox_30")

        self.gridLayout_7.addWidget(self.checkBox_30, 7, 1, 1, 1)

        self.label_33 = QLabel(self.frame_17)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_7.addWidget(self.label_33, 8, 0, 1, 1)


        self.verticalLayout_32.addWidget(self.frame_17)


        self.verticalLayout_20.addWidget(self.widget_8)

        self.scrollArea2.setWidget(self.scrollAreaWidgetContents2)

        self.verticalLayout_30.addWidget(self.scrollArea2)


        self.verticalLayout_21.addWidget(self.widget_5)

        self.themingsTabs.addTab(self.appCustomizing, "")

        self.verticalLayout_9.addWidget(self.themingsTabs)


        self.horizontalLayout_4.addWidget(self.panel4)

        self.controllerPanel4 = QWidget(self.parentPanel4)
        self.controllerPanel4.setObjectName(u"controllerPanel4")
        self.controllerPanel4.setMinimumSize(QSize(30, 0))
        self.controllerPanel4.setMaximumSize(QSize(30, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.controllerPanel4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.controllerIcons4 = QFrame(self.controllerPanel4)
        self.controllerIcons4.setObjectName(u"controllerIcons4")
        self.controllerIcons4.setFrameShape(QFrame.StyledPanel)
        self.controllerIcons4.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.controllerIcons4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setVerticalSpacing(0)
        self.gridLayout_6.setContentsMargins(0, 0, 0, -1)
        self.togglePanel4 = QPushButton(self.controllerIcons4)
        self.togglePanel4.setObjectName(u"togglePanel4")
        self.togglePanel4.setMinimumSize(QSize(28, 28))
        self.togglePanel4.setMaximumSize(QSize(28, 28))
        self.togglePanel4.setSizeIncrement(QSize(0, 0))
        self.togglePanel4.setBaseSize(QSize(0, 0))
#if QT_CONFIG(tooltip)
        self.togglePanel4.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.togglePanel4.setAutoFillBackground(False)
        self.togglePanel4.setIcon(icon7)
        self.togglePanel4.setFlat(True)

        self.gridLayout_6.addWidget(self.togglePanel4, 0, 0, 1, 1)

        self.panelSettings4 = QPushButton(self.controllerIcons4)
        self.panelSettings4.setObjectName(u"panelSettings4")
        self.panelSettings4.setMinimumSize(QSize(28, 28))
        self.panelSettings4.setMaximumSize(QSize(28, 28))
        self.panelSettings4.setSizeIncrement(QSize(0, 0))
        self.panelSettings4.setBaseSize(QSize(0, 0))
#if QT_CONFIG(tooltip)
        self.panelSettings4.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.panelSettings4.setIcon(icon5)
        self.panelSettings4.setIconSize(QSize(12, 12))
        self.panelSettings4.setAutoDefault(False)
        self.panelSettings4.setFlat(True)

        self.gridLayout_6.addWidget(self.panelSettings4, 1, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.controllerIcons4, 0, Qt.AlignTop)

        self.headerPanel4 = LabelVertical(self.controllerPanel4)
        self.headerPanel4.setObjectName(u"headerPanel4")
        self.headerPanel4.setAlignment(Qt.AlignCenter)
        self.headerPanel4.setWordWrap(False)

        self.verticalLayout_4.addWidget(self.headerPanel4, 0, Qt.AlignBottom)


        self.horizontalLayout_4.addWidget(self.controllerPanel4)


        self.gridLayout.addWidget(self.parentPanel4, 1, 1, 1, 1)

        self.mainFooter = QWidget(self.mainFrame)
        self.mainFooter.setObjectName(u"mainFooter")
        self.mainFooter.setMinimumSize(QSize(0, 30))
        self.mainFooter.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_7 = QHBoxLayout(self.mainFooter)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.footerframe1 = QFrame(self.mainFooter)
        self.footerframe1.setObjectName(u"footerframe1")
        self.footerframe1.setFrameShape(QFrame.StyledPanel)
        self.footerframe1.setFrameShadow(QFrame.Raised)
        self.autor = QLabel(self.footerframe1)
        self.autor.setObjectName(u"autor")
        self.autor.setGeometry(QRect(10, 10, 47, 13))
        self.version = QLabel(self.footerframe1)
        self.version.setObjectName(u"version")
        self.version.setGeometry(QRect(90, 10, 47, 13))

        self.horizontalLayout_7.addWidget(self.footerframe1)

        self.footerframe2 = QFrame(self.mainFooter)
        self.footerframe2.setObjectName(u"footerframe2")
        self.footerframe2.setFrameShape(QFrame.StyledPanel)
        self.footerframe2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.footerframe2)

        self.footerActions = QFrame(self.mainFooter)
        self.footerActions.setObjectName(u"footerActions")
        self.footerActions.setStyleSheet(u"")
        self.footerActions.setFrameShape(QFrame.StyledPanel)
        self.footerActions.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.footerActions)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.footerActions)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(40, 30))
        self.pushButton.setSizeIncrement(QSize(30, 30))
        icon8 = QIcon()
        icon8.addFile(u":/vscode-icons-dark/gui/resources/vscode-icons/icons/dark/github-inverted.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon8)
        self.pushButton.setFlat(True)

        self.horizontalLayout_22.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.footerActions)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(40, 30))
        icon9 = QIcon()
        icon9.addFile(u":/vscode-icons-dark/gui/resources/vscode-icons/icons/dark/settings-gear.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon9)
        self.pushButton_2.setFlat(True)

        self.horizontalLayout_22.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.footerActions)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(40, 30))
        icon10 = QIcon()
        icon10.addFile(u":/vscode-icons-dark/gui/resources/vscode-icons/icons/dark/code.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon10)
        self.pushButton_3.setFlat(True)

        self.horizontalLayout_22.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.footerActions)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(40, 30))
        icon11 = QIcon()
        icon11.addFile(u":/vscode-icons-dark/gui/resources/vscode-icons/icons/dark/clear-all.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon11)
        self.pushButton_4.setFlat(True)

        self.horizontalLayout_22.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.footerActions)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(40, 30))
        icon12 = QIcon()
        icon12.addFile(u":/vscode-icons-dark/gui/resources/vscode-icons/icons/dark/account.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon12)
        self.pushButton_5.setFlat(True)

        self.horizontalLayout_22.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.footerActions)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(40, 30))
        icon13 = QIcon()
        icon13.addFile(u":/vscode-icons-dark/gui/resources/vscode-icons/icons/dark/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon13)
        self.pushButton_6.setFlat(True)

        self.horizontalLayout_22.addWidget(self.pushButton_6)


        self.horizontalLayout_7.addWidget(self.footerActions, 0, Qt.AlignRight)


        self.gridLayout.addWidget(self.mainFooter, 2, 0, 1, 2)


        self.horizontalLayout.addWidget(self.mainFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.panelSettings1.setDefault(False)
        self.panelSettings2.setDefault(False)
        self.panelSettings3.setDefault(False)
        self.panelSettings5.setDefault(False)
        self.themingsTabs.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(0)
        self.panelSettings4.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionvvv.setText(QCoreApplication.translate("MainWindow", u"vvv", None))
        self.dummy.setText("")
        self.appLogo.setText("")
        self.appTitle.setText(QCoreApplication.translate("MainWindow", u" DemoApp", None))
        self.appDescription.setText(QCoreApplication.translate("MainWindow", u"App Skeleton: responsive | configurable | extendable", None))
        self.minimizewindow.setText("")
        self.restorewindow.setText("")
        self.maximizewindow.setText("")
        self.closewindow.setText("")
        self.togglePanel1.setText("")
        self.panelSettings1.setText("")
        self.headerPanel1.setText(QCoreApplication.translate("MainWindow", u"Navigation", None))
        self.togglePanel2.setText("")
        self.panelSettings2.setText("")
        self.headerPanel2.setText(QCoreApplication.translate("MainWindow", u"Options", None))
        self.closeOtherPanels.setText("")
        self.panelSettings3.setText("")
        self.headerPanel3.setText(QCoreApplication.translate("MainWindow", u"Content", None))
        self.headerPanel5.setText(QCoreApplication.translate("MainWindow", u"Messages", None))
        self.panelSettings5.setText("")
        self.togglePanel5.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Header", None))
        self.headerBgColor1.setText("")
        self.headerBgColor2.setText("")
        self.headerBgColor3.setText("")
        self.headerBgColor4.setText("")
        self.headerBgColor5.setText("")
        self.headerBgColor6.setText("")
        self.headerBgColor7.setText("")
        self.headerBgColor8.setText("")
        self.headerBgColor9.setText("")
        self.headerBgColor10.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Panels", None))
        self.panelBgColor1.setText("")
        self.panelBgColor2.setText("")
        self.panelBgColor3.setText("")
        self.panelBgColor4.setText("")
        self.panelBgColor5.setText("")
        self.panelBgColor6.setText("")
        self.panelBgColor7.setText("")
        self.panelBgColor8.setText("")
        self.panelBgColor9.setText("")
        self.panelBgColor10.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Footer", None))
        self.footerBgColor1.setText("")
        self.footerBgColor2.setText("")
        self.footerBgColor3.setText("")
        self.footerBgColor4.setText("")
        self.footerBgColor5.setText("")
        self.footerBgColor6.setText("")
        self.footerBgColor7.setText("")
        self.footerBgColor8.setText("")
        self.footerBgColor9.setText("")
        self.footerBgColor10.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Controllers", None))
        self.controllerBgColor1.setText("")
        self.controllerBgColor2.setText("")
        self.controllerBgColor3.setText("")
        self.controllerBgColor4.setText("")
        self.controllerBgColor5.setText("")
        self.controllerBgColor6.setText("")
        self.controllerBgColor7.setText("")
        self.controllerBgColor8.setText("")
        self.controllerBgColor9.setText("")
        self.controllerBgColor10.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Icons", None))
        self.iconBgColor1.setText("")
        self.iconBgColor2.setText("")
        self.iconBgColor3.setText("")
        self.iconBgColor4.setText("")
        self.iconBgColor5.setText("")
        self.iconBgColor6.setText("")
        self.iconBgColor7.setText("")
        self.iconBgColor8.setText("")
        self.iconBgColor9.setText("")
        self.iconBgColor10.setText("")
        self.themeColors.setItemText(0, QCoreApplication.translate("MainWindow", u"blue", None))
        self.themeColors.setItemText(1, QCoreApplication.translate("MainWindow", u"red", None))
        self.themeColors.setItemText(2, QCoreApplication.translate("MainWindow", u"#fff", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.themingsTabs.setTabText(self.themingsTabs.indexOf(self.appTheming), QCoreApplication.translate("MainWindow", u"Theming", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"bgColors", None))
        self.headerBgColor1_2.setText("")
        self.headerBgColor2_2.setText("")
        self.headerBgColor3_2.setText("")
        self.headerBgColor4_2.setText("")
        self.headerBgColor5_2.setText("")
        self.headerBgColor6_2.setText("")
        self.headerBgColor7_2.setText("")
        self.headerBgColor8_2.setText("")
        self.headerBgColor9_2.setText("")
        self.headerBgColor10_2.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"textColors", None))
        self.headerBgColor3_3.setText("")
        self.headerBgColor4_3.setText("")
        self.headerBgColor5_3.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"bgColors", None))
        self.headerBgColor3_6.setText("")
        self.headerBgColor4_6.setText("")
        self.headerBgColor5_6.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"bgColors", None))
        self.headerBgColor3_7.setText("")
        self.headerBgColor4_7.setText("")
        self.headerBgColor5_7.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"bgColors", None))
        self.headerBgColor3_8.setText("")
        self.headerBgColor4_8.setText("")
        self.headerBgColor5_8.setText("")
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Header", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Content", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"Footer", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"Controllers", None))
        self.themingsTabs.setTabText(self.themingsTabs.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Theming2", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"GENERAL SETTINGS", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.checkBox_24.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Show your emails", None))
        self.checkBox_25.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Show recent activity", None))
        self.checkBox_26.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Show Task statistics", None))
        self.checkBox_27.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"SYSTEM SETTINGS", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"System Logs", None))
        self.checkBox_29.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Error Reporting", None))
        self.checkBox_30.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Applications Logs", None))
        self.themingsTabs.setTabText(self.themingsTabs.indexOf(self.appCustomizing), QCoreApplication.translate("MainWindow", u"Customizing", None))
        self.togglePanel4.setText("")
        self.panelSettings4.setText("")
        self.headerPanel4.setText(QCoreApplication.translate("MainWindow", u"Theming & Customizing", None))
        self.autor.setText(QCoreApplication.translate("MainWindow", u"Footer", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.pushButton_6.setText("")
    # retranslateUi

