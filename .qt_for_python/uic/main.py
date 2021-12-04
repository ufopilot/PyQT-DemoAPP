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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QTabWidget,
    QToolBox, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

from gui.widgets.animated_check.animated_check import AnimatedCheck
from gui.widgets.label_horizontal.label_horizontal import LabelHorizontal
from gui.widgets.label_vertical.label_vertical import LabelVertical
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1245, 828)
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
        self.horizontalLayout_17.setSpacing(12)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(12, 0, 0, 2)
        self.appLogo = QLabel(self.mainHeader)
        self.appLogo.setObjectName(u"appLogo")
        self.appLogo.setMinimumSize(QSize(24, 24))
        self.appLogo.setMaximumSize(QSize(24, 24))
        self.appLogo.setStyleSheet(u"")
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
"/*\n"
"#contentMainColor1, #headerMainColor1, #footerMainColor1, #controllerMainColor1{ background:     #3ca2d9;}\n"
"#contentMainColor2, #headerMainColor2, #footerMainColor2, #controllerMainColor2{ background:     #6610f2;}\n"
"#contentMainColor3, #headerMainColor3, #footerMainColor3, #controllerMainColor3{ background:     #6f42c1;}\n"
"#contentMainColor4, #headerMainColor4, #footerMainColor4, #controllerMainColor4{ background:     #e83e8c;}\n"
"#contentMainColor5, #headerMainColor5, #footerMainColor5, #controllerMainColor5{ background:     #dc3545;}\n"
""
                        "#contentMainColor6, #headerMainColor6, #footerMainColor6, #controllerMainColor6{ background:     #fd7e14;}\n"
"#contentMainColor7, #headerMainColor7, #footerMainColor7, #controllerMainColor7{ background:     #ffc107;}\n"
"#contentMainColor8, #headerMainColor8, #footerMainColor8, #controllerMainColor8{ background:     #28a745;}\n"
"#contentMainColor9, #headerMainColor9, #footerMainColor9, #controllerMainColor9{ background:     #20c997;}\n"
"#contentMainColor10, #headerMainColor10, #footerMainColor10, #controllerMainColor10{ background: #17a2b8;}\n"
"#contentMainColor11, #headerMainColor11, #footerMainColor11, #controllerMainColor11{ background: #ffffff;}\n"
"#contentMainColor12, #headerMainColor12, #footerMainColor12, #controllerMainColor12{ background: #6c757d;}\n"
"#contentMainColor13, #headerMainColor13, #footerMainColor13, #controllerMainColor13{ background: #343a40;}\n"
"#contentMainColor14, #headerMainColor14, #footerMainColor14, #controllerMainColor14{ background: #5d5e67;}\n"
"#contentMainColor15, #head"
                        "erMainColor15, #footerMainColor15, #controllerMainColor15{ background: #0b0f13;}\n"
"#contentMainColor16, #headerMainColor16, #footerMainColor16, #controllerMainColor16{ background: #1b202c;}\n"
"#contentMainColor17, #headerMainColor17, #footerMainColor17, #controllerMainColor17{ background: #13161f;}\n"
"#contentMainColor18, #headerMainColor18, #footerMainColor18, #controllerMainColor18{ background: #343a40;}\n"
"#contentMainColor19, #headerMainColor19, #footerMainColor19, #controllerMainColor19{ background: #121212;}\n"
"#contentMainColor20, #headerMainColor20, #footerMainColor20, #controllerMainColor20{ background: #313648;}\n"
"#contentMainColor21, #headerMainColor21, #footerMainColor21, #controllerMainColor21{ background: #eceef2;}\n"
"*/\n"
"/*\n"
"#contentFirst_textColor1, #headerFirst_textColor1, #footerFirst_textColor1, #controllerFirst_textColor1{ background:  	#ffffff;}\n"
"#contentFirst_textColor2, #headerFirst_textColor2, #footerFirst_textColor2, #controllerFirst_textColor2{ background:  	#dddddd;"
                        "}\n"
"#contentFirst_textColor3, #headerFirst_textColor3, #footerFirst_textColor3, #controllerFirst_textColor3{ background:  	#111111;}\n"
"#contentFirst_textColor4, #headerFirst_textColor4, #footerFirst_textColor4, #controllerFirst_textColor4{ background:  	#333333;}\n"
"\n"
"#contentSecond_textColor1, #headerSecond_textColor1, #footerSecond_textColor1, #controllerSecond_textColor1{ background:  #ffffff;}\n"
"#contentSecond_textColor2, #headerSecond_textColor2, #footerSecond_textColor2, #controllerSecond_textColor2{ background:  #dddddd;}\n"
"#contentSecond_textColor3, #headerSecond_textColor3, #footerSecond_textColor3, #controllerSecond_textColor3{ background:  #111111;}\n"
"#contentSecond_textColor4, #headerSecond_textColor4, #footerSecond_textColor4, #controllerSecond_textColor4{ background:  #333333;}\n"
"\n"
"#contentThird_textColor1, #headerThird_textColor1, #footerThird_textColor1, #controllerThird_textColor1{ background:  #ffffff;}\n"
"#contentThird_textColor2, #headerThird_textColor2, #footerThird_tex"
                        "tColor2, #controllerThird_textColor2{ background:  #dddddd;}\n"
"#contentThird_textColor3, #headerThird_textColor3, #footerThird_textColor3, #controllerThird_textColor3{ background:  #111111;}\n"
"#contentThird_textColor4, #headerThird_textColor4, #footerThird_textColor4, #controllerThird_textColor4{ background:  #333333;}\n"
"*/\n"
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
"--light: #f8f9fa;\n"
"\n"
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
"#171c26 #1b202c #1f2533\n"
"*/\n"
"\n"
"QToolBox::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
""
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
        self.verticalLayout_22 = QVBoxLayout(self.appTheming)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.toolBox = QToolBox(self.appTheming)
        self.toolBox.setObjectName(u"toolBox")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 252, 600))
        self.widget_7 = QWidget(self.page)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(10, 10, 241, 591))
        self.frame_10 = QFrame(self.widget_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(0, -10, 240, 170))
        self.frame_10.setMinimumSize(QSize(0, 170))
        self.frame_10.setMaximumSize(QSize(16777215, 120))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_10)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, -1, 0)
        self.label_19 = QLabel(self.frame_10)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_25.addWidget(self.label_19)

        self.panelsBackground_17 = QFrame(self.frame_10)
        self.panelsBackground_17.setObjectName(u"panelsBackground_17")
        self.panelsBackground_17.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_17.setStyleSheet(u"")
        self.panelsBackground_17.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.panelsBackground_17)
        self.horizontalLayout_28.setSpacing(14)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, -1, 0)
        self.headerMainColor1 = QPushButton(self.panelsBackground_17)
        self.headerMainColor1.setObjectName(u"headerMainColor1")
        self.headerMainColor1.setMinimumSize(QSize(24, 24))
        self.headerMainColor1.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_28.addWidget(self.headerMainColor1)

        self.headerMainColor2 = QPushButton(self.panelsBackground_17)
        self.headerMainColor2.setObjectName(u"headerMainColor2")
        self.headerMainColor2.setMinimumSize(QSize(24, 24))
        self.headerMainColor2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_28.addWidget(self.headerMainColor2)

        self.headerMainColor3 = QPushButton(self.panelsBackground_17)
        self.headerMainColor3.setObjectName(u"headerMainColor3")
        self.headerMainColor3.setMinimumSize(QSize(24, 24))
        self.headerMainColor3.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_28.addWidget(self.headerMainColor3)

        self.headerMainColor4 = QPushButton(self.panelsBackground_17)
        self.headerMainColor4.setObjectName(u"headerMainColor4")
        self.headerMainColor4.setMinimumSize(QSize(24, 24))
        self.headerMainColor4.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_28.addWidget(self.headerMainColor4)

        self.headerMainColor5 = QPushButton(self.panelsBackground_17)
        self.headerMainColor5.setObjectName(u"headerMainColor5")
        self.headerMainColor5.setMinimumSize(QSize(24, 24))
        self.headerMainColor5.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_28.addWidget(self.headerMainColor5)

        self.headerMainColor6 = QPushButton(self.panelsBackground_17)
        self.headerMainColor6.setObjectName(u"headerMainColor6")
        self.headerMainColor6.setMinimumSize(QSize(24, 24))
        self.headerMainColor6.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_28.addWidget(self.headerMainColor6)

        self.headerMainColor7 = QPushButton(self.panelsBackground_17)
        self.headerMainColor7.setObjectName(u"headerMainColor7")
        self.headerMainColor7.setMinimumSize(QSize(24, 24))
        self.headerMainColor7.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_28.addWidget(self.headerMainColor7)


        self.verticalLayout_25.addWidget(self.panelsBackground_17)

        self.panelsBackground_18 = QFrame(self.frame_10)
        self.panelsBackground_18.setObjectName(u"panelsBackground_18")
        self.panelsBackground_18.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_18.setStyleSheet(u"")
        self.panelsBackground_18.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.panelsBackground_18)
        self.horizontalLayout_29.setSpacing(14)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, -1, 0)
        self.headerMainColor8 = QPushButton(self.panelsBackground_18)
        self.headerMainColor8.setObjectName(u"headerMainColor8")
        self.headerMainColor8.setMinimumSize(QSize(24, 24))
        self.headerMainColor8.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_29.addWidget(self.headerMainColor8)

        self.headerMainColor9 = QPushButton(self.panelsBackground_18)
        self.headerMainColor9.setObjectName(u"headerMainColor9")
        self.headerMainColor9.setMinimumSize(QSize(24, 24))
        self.headerMainColor9.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_29.addWidget(self.headerMainColor9)

        self.headerMainColor10 = QPushButton(self.panelsBackground_18)
        self.headerMainColor10.setObjectName(u"headerMainColor10")
        self.headerMainColor10.setMinimumSize(QSize(24, 24))
        self.headerMainColor10.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_29.addWidget(self.headerMainColor10)

        self.headerMainColor11 = QPushButton(self.panelsBackground_18)
        self.headerMainColor11.setObjectName(u"headerMainColor11")
        self.headerMainColor11.setMinimumSize(QSize(24, 24))
        self.headerMainColor11.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_29.addWidget(self.headerMainColor11)

        self.headerMainColor12 = QPushButton(self.panelsBackground_18)
        self.headerMainColor12.setObjectName(u"headerMainColor12")
        self.headerMainColor12.setMinimumSize(QSize(24, 24))
        self.headerMainColor12.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_29.addWidget(self.headerMainColor12)

        self.headerMainColor13 = QPushButton(self.panelsBackground_18)
        self.headerMainColor13.setObjectName(u"headerMainColor13")
        self.headerMainColor13.setMinimumSize(QSize(24, 24))
        self.headerMainColor13.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_29.addWidget(self.headerMainColor13)

        self.headerMainColor14 = QPushButton(self.panelsBackground_18)
        self.headerMainColor14.setObjectName(u"headerMainColor14")
        self.headerMainColor14.setMinimumSize(QSize(24, 24))
        self.headerMainColor14.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_29.addWidget(self.headerMainColor14)


        self.verticalLayout_25.addWidget(self.panelsBackground_18)

        self.panelsBackground_19 = QFrame(self.frame_10)
        self.panelsBackground_19.setObjectName(u"panelsBackground_19")
        self.panelsBackground_19.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_19.setStyleSheet(u"")
        self.panelsBackground_19.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_80 = QHBoxLayout(self.panelsBackground_19)
        self.horizontalLayout_80.setSpacing(14)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setContentsMargins(0, 0, -1, 0)
        self.headerMainColor15 = QPushButton(self.panelsBackground_19)
        self.headerMainColor15.setObjectName(u"headerMainColor15")
        self.headerMainColor15.setMinimumSize(QSize(24, 24))
        self.headerMainColor15.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_80.addWidget(self.headerMainColor15)

        self.headerMainColor16 = QPushButton(self.panelsBackground_19)
        self.headerMainColor16.setObjectName(u"headerMainColor16")
        self.headerMainColor16.setMinimumSize(QSize(24, 24))
        self.headerMainColor16.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_80.addWidget(self.headerMainColor16)

        self.headerMainColor17 = QPushButton(self.panelsBackground_19)
        self.headerMainColor17.setObjectName(u"headerMainColor17")
        self.headerMainColor17.setMinimumSize(QSize(24, 24))
        self.headerMainColor17.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_80.addWidget(self.headerMainColor17)

        self.headerMainColor18 = QPushButton(self.panelsBackground_19)
        self.headerMainColor18.setObjectName(u"headerMainColor18")
        self.headerMainColor18.setMinimumSize(QSize(24, 24))
        self.headerMainColor18.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_80.addWidget(self.headerMainColor18)

        self.headerMainColor19 = QPushButton(self.panelsBackground_19)
        self.headerMainColor19.setObjectName(u"headerMainColor19")
        self.headerMainColor19.setMinimumSize(QSize(24, 24))
        self.headerMainColor19.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_80.addWidget(self.headerMainColor19)

        self.headerMainColor20 = QPushButton(self.panelsBackground_19)
        self.headerMainColor20.setObjectName(u"headerMainColor20")
        self.headerMainColor20.setMinimumSize(QSize(24, 24))
        self.headerMainColor20.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_80.addWidget(self.headerMainColor20)

        self.headerMainColor21 = QPushButton(self.panelsBackground_19)
        self.headerMainColor21.setObjectName(u"headerMainColor21")
        self.headerMainColor21.setMinimumSize(QSize(24, 24))
        self.headerMainColor21.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_80.addWidget(self.headerMainColor21)


        self.verticalLayout_25.addWidget(self.panelsBackground_19)

        self.frame_32 = QFrame(self.widget_7)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setGeometry(QRect(-10, 160, 252, 48))
        self.frame_32.setMaximumSize(QSize(16777213, 48))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_81.setSpacing(0)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(3, 0, 0, 0)
        self.panelsBackground_36 = QFrame(self.frame_32)
        self.panelsBackground_36.setObjectName(u"panelsBackground_36")
        self.panelsBackground_36.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_36.setStyleSheet(u"")
        self.panelsBackground_36.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_82 = QHBoxLayout(self.panelsBackground_36)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.label_48 = QLabel(self.panelsBackground_36)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_82.addWidget(self.label_48)


        self.horizontalLayout_81.addWidget(self.panelsBackground_36)

        self.frame_11 = QFrame(self.frame_32)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 40))
        self.frame_11.setStyleSheet(u"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_83 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.headerHoverColor1 = QPushButton(self.frame_11)
        self.headerHoverColor1.setObjectName(u"headerHoverColor1")
        self.headerHoverColor1.setMinimumSize(QSize(24, 24))
        self.headerHoverColor1.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_83.addWidget(self.headerHoverColor1)

        self.headerHoverColor2 = QPushButton(self.frame_11)
        self.headerHoverColor2.setObjectName(u"headerHoverColor2")
        self.headerHoverColor2.setMinimumSize(QSize(24, 24))
        self.headerHoverColor2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_83.addWidget(self.headerHoverColor2)

        self.headerHoverColor3 = QPushButton(self.frame_11)
        self.headerHoverColor3.setObjectName(u"headerHoverColor3")
        self.headerHoverColor3.setMinimumSize(QSize(24, 24))
        self.headerHoverColor3.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_83.addWidget(self.headerHoverColor3)

        self.headerHoverColor4 = QPushButton(self.frame_11)
        self.headerHoverColor4.setObjectName(u"headerHoverColor4")
        self.headerHoverColor4.setMinimumSize(QSize(24, 24))
        self.headerHoverColor4.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_83.addWidget(self.headerHoverColor4)


        self.horizontalLayout_81.addWidget(self.frame_11)

        self.frame_33 = QFrame(self.widget_7)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setGeometry(QRect(-10, 210, 252, 48))
        self.frame_33.setMaximumSize(QSize(16777213, 48))
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_84 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_84.setSpacing(0)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(3, 0, 0, 0)
        self.panelsBackground_51 = QFrame(self.frame_33)
        self.panelsBackground_51.setObjectName(u"panelsBackground_51")
        self.panelsBackground_51.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_51.setStyleSheet(u"")
        self.panelsBackground_51.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_85 = QHBoxLayout(self.panelsBackground_51)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.label_49 = QLabel(self.panelsBackground_51)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_85.addWidget(self.label_49)


        self.horizontalLayout_84.addWidget(self.panelsBackground_51)

        self.panelsBackground_52 = QFrame(self.frame_33)
        self.panelsBackground_52.setObjectName(u"panelsBackground_52")
        self.panelsBackground_52.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_52.setStyleSheet(u"")
        self.panelsBackground_52.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_86 = QHBoxLayout(self.panelsBackground_52)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.headerBorderColor1 = QPushButton(self.panelsBackground_52)
        self.headerBorderColor1.setObjectName(u"headerBorderColor1")
        self.headerBorderColor1.setMinimumSize(QSize(24, 24))
        self.headerBorderColor1.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_86.addWidget(self.headerBorderColor1)

        self.headerBorderColor2 = QPushButton(self.panelsBackground_52)
        self.headerBorderColor2.setObjectName(u"headerBorderColor2")
        self.headerBorderColor2.setMinimumSize(QSize(24, 24))
        self.headerBorderColor2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_86.addWidget(self.headerBorderColor2)

        self.headerBorderColor3 = QPushButton(self.panelsBackground_52)
        self.headerBorderColor3.setObjectName(u"headerBorderColor3")
        self.headerBorderColor3.setMinimumSize(QSize(24, 24))
        self.headerBorderColor3.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_86.addWidget(self.headerBorderColor3)

        self.headerBorderColor4 = QPushButton(self.panelsBackground_52)
        self.headerBorderColor4.setObjectName(u"headerBorderColor4")
        self.headerBorderColor4.setMinimumSize(QSize(24, 24))
        self.headerBorderColor4.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_86.addWidget(self.headerBorderColor4)


        self.horizontalLayout_84.addWidget(self.panelsBackground_52)

        self.frame_34 = QFrame(self.widget_7)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setGeometry(QRect(-10, 260, 252, 48))
        self.frame_34.setMaximumSize(QSize(16777213, 48))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_87 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_87.setSpacing(0)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.horizontalLayout_87.setContentsMargins(3, 0, 0, 0)
        self.panelsBackground_53 = QFrame(self.frame_34)
        self.panelsBackground_53.setObjectName(u"panelsBackground_53")
        self.panelsBackground_53.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_53.setStyleSheet(u"")
        self.panelsBackground_53.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_88 = QHBoxLayout(self.panelsBackground_53)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.label_50 = QLabel(self.panelsBackground_53)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_88.addWidget(self.label_50)


        self.horizontalLayout_87.addWidget(self.panelsBackground_53)

        self.panelsBackground_54 = QFrame(self.frame_34)
        self.panelsBackground_54.setObjectName(u"panelsBackground_54")
        self.panelsBackground_54.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_54.setStyleSheet(u"")
        self.panelsBackground_54.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_89 = QHBoxLayout(self.panelsBackground_54)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.headerFirst_textColor1 = QPushButton(self.panelsBackground_54)
        self.headerFirst_textColor1.setObjectName(u"headerFirst_textColor1")
        self.headerFirst_textColor1.setMinimumSize(QSize(24, 24))
        self.headerFirst_textColor1.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_89.addWidget(self.headerFirst_textColor1)

        self.headerFirst_textColor2 = QPushButton(self.panelsBackground_54)
        self.headerFirst_textColor2.setObjectName(u"headerFirst_textColor2")
        self.headerFirst_textColor2.setMinimumSize(QSize(24, 24))
        self.headerFirst_textColor2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_89.addWidget(self.headerFirst_textColor2)

        self.headerFirst_textColor3 = QPushButton(self.panelsBackground_54)
        self.headerFirst_textColor3.setObjectName(u"headerFirst_textColor3")
        self.headerFirst_textColor3.setMinimumSize(QSize(24, 24))
        self.headerFirst_textColor3.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_89.addWidget(self.headerFirst_textColor3)

        self.headerFirst_textColor4 = QPushButton(self.panelsBackground_54)
        self.headerFirst_textColor4.setObjectName(u"headerFirst_textColor4")
        self.headerFirst_textColor4.setMinimumSize(QSize(24, 24))
        self.headerFirst_textColor4.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_89.addWidget(self.headerFirst_textColor4)


        self.horizontalLayout_87.addWidget(self.panelsBackground_54)

        self.frame_35 = QFrame(self.widget_7)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setGeometry(QRect(-10, 310, 252, 48))
        self.frame_35.setMaximumSize(QSize(16777213, 48))
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_90 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_90.setSpacing(0)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalLayout_90.setContentsMargins(3, 0, 0, 0)
        self.panelsBackground_55 = QFrame(self.frame_35)
        self.panelsBackground_55.setObjectName(u"panelsBackground_55")
        self.panelsBackground_55.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_55.setStyleSheet(u"")
        self.panelsBackground_55.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_55.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_91 = QHBoxLayout(self.panelsBackground_55)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.label_51 = QLabel(self.panelsBackground_55)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_91.addWidget(self.label_51)


        self.horizontalLayout_90.addWidget(self.panelsBackground_55)

        self.panelsBackground_56 = QFrame(self.frame_35)
        self.panelsBackground_56.setObjectName(u"panelsBackground_56")
        self.panelsBackground_56.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_56.setStyleSheet(u"")
        self.panelsBackground_56.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_92 = QHBoxLayout(self.panelsBackground_56)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.headerSecond_textColor1 = QPushButton(self.panelsBackground_56)
        self.headerSecond_textColor1.setObjectName(u"headerSecond_textColor1")
        self.headerSecond_textColor1.setMinimumSize(QSize(24, 24))
        self.headerSecond_textColor1.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_92.addWidget(self.headerSecond_textColor1)

        self.headerSecond_textColor2 = QPushButton(self.panelsBackground_56)
        self.headerSecond_textColor2.setObjectName(u"headerSecond_textColor2")
        self.headerSecond_textColor2.setMinimumSize(QSize(24, 24))
        self.headerSecond_textColor2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_92.addWidget(self.headerSecond_textColor2)

        self.headerSecond_textColor3 = QPushButton(self.panelsBackground_56)
        self.headerSecond_textColor3.setObjectName(u"headerSecond_textColor3")
        self.headerSecond_textColor3.setMinimumSize(QSize(24, 24))
        self.headerSecond_textColor3.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_92.addWidget(self.headerSecond_textColor3)

        self.headerSecond_textColor4 = QPushButton(self.panelsBackground_56)
        self.headerSecond_textColor4.setObjectName(u"headerSecond_textColor4")
        self.headerSecond_textColor4.setMinimumSize(QSize(24, 24))
        self.headerSecond_textColor4.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_92.addWidget(self.headerSecond_textColor4)


        self.horizontalLayout_90.addWidget(self.panelsBackground_56)

        self.frame_36 = QFrame(self.widget_7)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setGeometry(QRect(-10, 360, 252, 48))
        self.frame_36.setMaximumSize(QSize(16777213, 48))
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_93 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_93.setSpacing(0)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalLayout_93.setContentsMargins(3, 0, 0, 0)
        self.panelsBackground_57 = QFrame(self.frame_36)
        self.panelsBackground_57.setObjectName(u"panelsBackground_57")
        self.panelsBackground_57.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_57.setStyleSheet(u"")
        self.panelsBackground_57.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_94 = QHBoxLayout(self.panelsBackground_57)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.label_52 = QLabel(self.panelsBackground_57)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_94.addWidget(self.label_52)


        self.horizontalLayout_93.addWidget(self.panelsBackground_57)

        self.panelsBackground_58 = QFrame(self.frame_36)
        self.panelsBackground_58.setObjectName(u"panelsBackground_58")
        self.panelsBackground_58.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_58.setStyleSheet(u"")
        self.panelsBackground_58.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_58.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_95 = QHBoxLayout(self.panelsBackground_58)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.headerThird_textColor1 = QPushButton(self.panelsBackground_58)
        self.headerThird_textColor1.setObjectName(u"headerThird_textColor1")
        self.headerThird_textColor1.setMinimumSize(QSize(24, 24))
        self.headerThird_textColor1.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_95.addWidget(self.headerThird_textColor1)

        self.headerThird_textColor2 = QPushButton(self.panelsBackground_58)
        self.headerThird_textColor2.setObjectName(u"headerThird_textColor2")
        self.headerThird_textColor2.setMinimumSize(QSize(24, 24))
        self.headerThird_textColor2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_95.addWidget(self.headerThird_textColor2)

        self.headerThird_textColor3 = QPushButton(self.panelsBackground_58)
        self.headerThird_textColor3.setObjectName(u"headerThird_textColor3")
        self.headerThird_textColor3.setMinimumSize(QSize(24, 24))
        self.headerThird_textColor3.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_95.addWidget(self.headerThird_textColor3)

        self.headerThird_textColor4 = QPushButton(self.panelsBackground_58)
        self.headerThird_textColor4.setObjectName(u"headerThird_textColor4")
        self.headerThird_textColor4.setMinimumSize(QSize(24, 24))
        self.headerThird_textColor4.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_95.addWidget(self.headerThird_textColor4)


        self.horizontalLayout_93.addWidget(self.panelsBackground_58)

        self.toolBox.addItem(self.page, u"Header")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 252, 600))
        self.scrollArea_2 = QScrollArea(self.page_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(0, 0, 251, 601))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 251, 601))
        self.widget_6 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(9, 9, 241, 591))
        self.frame_8 = QFrame(self.widget_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(0, -10, 240, 170))
        self.frame_8.setMinimumSize(QSize(0, 170))
        self.frame_8.setMaximumSize(QSize(16777215, 120))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_8)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, -1, 0)
        self.label_18 = QLabel(self.frame_8)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_24.addWidget(self.label_18)

        self.panelsBackground_15 = QFrame(self.frame_8)
        self.panelsBackground_15.setObjectName(u"panelsBackground_15")
        self.panelsBackground_15.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_15.setStyleSheet(u"")
        self.panelsBackground_15.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.panelsBackground_15)
        self.horizontalLayout_27.setSpacing(14)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, -1, 0)
        self.contentMainColor1 = QPushButton(self.panelsBackground_15)
        self.contentMainColor1.setObjectName(u"contentMainColor1")
        self.contentMainColor1.setMinimumSize(QSize(24, 24))
        self.contentMainColor1.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_27.addWidget(self.contentMainColor1)

        self.contentMainColor2 = QPushButton(self.panelsBackground_15)
        self.contentMainColor2.setObjectName(u"contentMainColor2")
        self.contentMainColor2.setMinimumSize(QSize(24, 24))
        self.contentMainColor2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_27.addWidget(self.contentMainColor2)

        self.contentMainColor3 = QPushButton(self.panelsBackground_15)
        self.contentMainColor3.setObjectName(u"contentMainColor3")
        self.contentMainColor3.setMinimumSize(QSize(24, 24))
        self.contentMainColor3.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_27.addWidget(self.contentMainColor3)

        self.contentMainColor4 = QPushButton(self.panelsBackground_15)
        self.contentMainColor4.setObjectName(u"contentMainColor4")
        self.contentMainColor4.setMinimumSize(QSize(24, 24))
        self.contentMainColor4.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_27.addWidget(self.contentMainColor4)

        self.contentMainColor5 = QPushButton(self.panelsBackground_15)
        self.contentMainColor5.setObjectName(u"contentMainColor5")
        self.contentMainColor5.setMinimumSize(QSize(24, 24))
        self.contentMainColor5.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_27.addWidget(self.contentMainColor5)

        self.contentMainColor6 = QPushButton(self.panelsBackground_15)
        self.contentMainColor6.setObjectName(u"contentMainColor6")
        self.contentMainColor6.setMinimumSize(QSize(24, 24))
        self.contentMainColor6.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_27.addWidget(self.contentMainColor6)

        self.contentMainColor7 = QPushButton(self.panelsBackground_15)
        self.contentMainColor7.setObjectName(u"contentMainColor7")
        self.contentMainColor7.setMinimumSize(QSize(24, 24))
        self.contentMainColor7.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_27.addWidget(self.contentMainColor7)


        self.verticalLayout_24.addWidget(self.panelsBackground_15)

        self.panelsBackground_14 = QFrame(self.frame_8)
        self.panelsBackground_14.setObjectName(u"panelsBackground_14")
        self.panelsBackground_14.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_14.setStyleSheet(u"")
        self.panelsBackground_14.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.panelsBackground_14)
        self.horizontalLayout_26.setSpacing(14)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, -1, 0)
        self.contentMainColor8 = QPushButton(self.panelsBackground_14)
        self.contentMainColor8.setObjectName(u"contentMainColor8")
        self.contentMainColor8.setMinimumSize(QSize(24, 24))
        self.contentMainColor8.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_26.addWidget(self.contentMainColor8)

        self.contentMainColor9 = QPushButton(self.panelsBackground_14)
        self.contentMainColor9.setObjectName(u"contentMainColor9")
        self.contentMainColor9.setMinimumSize(QSize(24, 24))
        self.contentMainColor9.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_26.addWidget(self.contentMainColor9)

        self.contentMainColor10 = QPushButton(self.panelsBackground_14)
        self.contentMainColor10.setObjectName(u"contentMainColor10")
        self.contentMainColor10.setMinimumSize(QSize(24, 24))
        self.contentMainColor10.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_26.addWidget(self.contentMainColor10)

        self.contentMainColor11 = QPushButton(self.panelsBackground_14)
        self.contentMainColor11.setObjectName(u"contentMainColor11")
        self.contentMainColor11.setMinimumSize(QSize(24, 24))
        self.contentMainColor11.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_26.addWidget(self.contentMainColor11)

        self.contentMainColor12 = QPushButton(self.panelsBackground_14)
        self.contentMainColor12.setObjectName(u"contentMainColor12")
        self.contentMainColor12.setMinimumSize(QSize(24, 24))
        self.contentMainColor12.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_26.addWidget(self.contentMainColor12)

        self.contentMainColor13 = QPushButton(self.panelsBackground_14)
        self.contentMainColor13.setObjectName(u"contentMainColor13")
        self.contentMainColor13.setMinimumSize(QSize(24, 24))
        self.contentMainColor13.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_26.addWidget(self.contentMainColor13)

        self.contentMainColor14 = QPushButton(self.panelsBackground_14)
        self.contentMainColor14.setObjectName(u"contentMainColor14")
        self.contentMainColor14.setMinimumSize(QSize(24, 24))
        self.contentMainColor14.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_26.addWidget(self.contentMainColor14)


        self.verticalLayout_24.addWidget(self.panelsBackground_14)

        self.panelsBackground_16 = QFrame(self.frame_8)
        self.panelsBackground_16.setObjectName(u"panelsBackground_16")
        self.panelsBackground_16.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_16.setStyleSheet(u"")
        self.panelsBackground_16.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.panelsBackground_16)
        self.horizontalLayout_79.setSpacing(14)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(0, 0, -1, 0)
        self.contentMainColor15 = QPushButton(self.panelsBackground_16)
        self.contentMainColor15.setObjectName(u"contentMainColor15")
        self.contentMainColor15.setMinimumSize(QSize(24, 24))
        self.contentMainColor15.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_79.addWidget(self.contentMainColor15)

        self.contentMainColor16 = QPushButton(self.panelsBackground_16)
        self.contentMainColor16.setObjectName(u"contentMainColor16")
        self.contentMainColor16.setMinimumSize(QSize(24, 24))
        self.contentMainColor16.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_79.addWidget(self.contentMainColor16)

        self.contentMainColor17 = QPushButton(self.panelsBackground_16)
        self.contentMainColor17.setObjectName(u"contentMainColor17")
        self.contentMainColor17.setMinimumSize(QSize(24, 24))
        self.contentMainColor17.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_79.addWidget(self.contentMainColor17)

        self.contentMainColor18 = QPushButton(self.panelsBackground_16)
        self.contentMainColor18.setObjectName(u"contentMainColor18")
        self.contentMainColor18.setMinimumSize(QSize(24, 24))
        self.contentMainColor18.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_79.addWidget(self.contentMainColor18)

        self.contentMainColor19 = QPushButton(self.panelsBackground_16)
        self.contentMainColor19.setObjectName(u"contentMainColor19")
        self.contentMainColor19.setMinimumSize(QSize(24, 24))
        self.contentMainColor19.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_79.addWidget(self.contentMainColor19)

        self.contentMainColor20 = QPushButton(self.panelsBackground_16)
        self.contentMainColor20.setObjectName(u"contentMainColor20")
        self.contentMainColor20.setMinimumSize(QSize(24, 24))
        self.contentMainColor20.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_79.addWidget(self.contentMainColor20)

        self.contentMainColor21 = QPushButton(self.panelsBackground_16)
        self.contentMainColor21.setObjectName(u"contentMainColor21")
        self.contentMainColor21.setMinimumSize(QSize(24, 24))
        self.contentMainColor21.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_79.addWidget(self.contentMainColor21)


        self.verticalLayout_24.addWidget(self.panelsBackground_16)

        self.frame_24 = QFrame(self.widget_6)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setGeometry(QRect(-10, 160, 252, 48))
        self.frame_24.setMaximumSize(QSize(16777213, 48))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(3, 0, 0, 0)
        self.panelsBackground_35 = QFrame(self.frame_24)
        self.panelsBackground_35.setObjectName(u"panelsBackground_35")
        self.panelsBackground_35.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_35.setStyleSheet(u"")
        self.panelsBackground_35.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.panelsBackground_35)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.label_40 = QLabel(self.panelsBackground_35)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_56.addWidget(self.label_40)


        self.horizontalLayout_55.addWidget(self.panelsBackground_35)

        self.frame_9 = QFrame(self.frame_24)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 40))
        self.frame_9.setStyleSheet(u"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.contentHeaderColor1 = QPushButton(self.frame_9)
        self.contentHeaderColor1.setObjectName(u"contentHeaderColor1")
        self.contentHeaderColor1.setMinimumSize(QSize(24, 24))
        self.contentHeaderColor1.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_57.addWidget(self.contentHeaderColor1)

        self.contentHeaderColor2 = QPushButton(self.frame_9)
        self.contentHeaderColor2.setObjectName(u"contentHeaderColor2")
        self.contentHeaderColor2.setMinimumSize(QSize(24, 24))
        self.contentHeaderColor2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_57.addWidget(self.contentHeaderColor2)

        self.contentHeaderColor3 = QPushButton(self.frame_9)
        self.contentHeaderColor3.setObjectName(u"contentHeaderColor3")
        self.contentHeaderColor3.setMinimumSize(QSize(24, 24))
        self.contentHeaderColor3.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_57.addWidget(self.contentHeaderColor3)

        self.contentHeaderColor4 = QPushButton(self.frame_9)
        self.contentHeaderColor4.setObjectName(u"contentHeaderColor4")
        self.contentHeaderColor4.setMinimumSize(QSize(24, 24))
        self.contentHeaderColor4.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_57.addWidget(self.contentHeaderColor4)


        self.horizontalLayout_55.addWidget(self.frame_9)

        self.frame_25 = QFrame(self.widget_6)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setGeometry(QRect(-10, 210, 252, 48))
        self.frame_25.setMaximumSize(QSize(16777213, 48))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_58.setSpacing(0)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(3, 0, 0, 0)
        self.panelsBackground_37 = QFrame(self.frame_25)
        self.panelsBackground_37.setObjectName(u"panelsBackground_37")
        self.panelsBackground_37.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_37.setStyleSheet(u"")
        self.panelsBackground_37.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.panelsBackground_37)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.label_41 = QLabel(self.panelsBackground_37)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_59.addWidget(self.label_41)


        self.horizontalLayout_58.addWidget(self.panelsBackground_37)

        self.panelsBackground_38 = QFrame(self.frame_25)
        self.panelsBackground_38.setObjectName(u"panelsBackground_38")
        self.panelsBackground_38.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_38.setStyleSheet(u"")
        self.panelsBackground_38.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.panelsBackground_38)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.contentFooterColor1 = QPushButton(self.panelsBackground_38)
        self.contentFooterColor1.setObjectName(u"contentFooterColor1")
        self.contentFooterColor1.setMinimumSize(QSize(24, 24))
        self.contentFooterColor1.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_60.addWidget(self.contentFooterColor1)

        self.contentFooterColor2 = QPushButton(self.panelsBackground_38)
        self.contentFooterColor2.setObjectName(u"contentFooterColor2")
        self.contentFooterColor2.setMinimumSize(QSize(24, 24))
        self.contentFooterColor2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_60.addWidget(self.contentFooterColor2)

        self.contentFooterColor3 = QPushButton(self.panelsBackground_38)
        self.contentFooterColor3.setObjectName(u"contentFooterColor3")
        self.contentFooterColor3.setMinimumSize(QSize(24, 24))
        self.contentFooterColor3.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_60.addWidget(self.contentFooterColor3)

        self.contentFooterColor4 = QPushButton(self.panelsBackground_38)
        self.contentFooterColor4.setObjectName(u"contentFooterColor4")
        self.contentFooterColor4.setMinimumSize(QSize(24, 24))
        self.contentFooterColor4.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_60.addWidget(self.contentFooterColor4)


        self.horizontalLayout_58.addWidget(self.panelsBackground_38)

        self.frame_26 = QFrame(self.widget_6)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setGeometry(QRect(-10, 260, 252, 48))
        self.frame_26.setMaximumSize(QSize(16777213, 48))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_61.setSpacing(0)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(3, 0, 0, 0)
        self.panelsBackground_39 = QFrame(self.frame_26)
        self.panelsBackground_39.setObjectName(u"panelsBackground_39")
        self.panelsBackground_39.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_39.setStyleSheet(u"")
        self.panelsBackground_39.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.panelsBackground_39)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.label_42 = QLabel(self.panelsBackground_39)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_62.addWidget(self.label_42)


        self.horizontalLayout_61.addWidget(self.panelsBackground_39)

        self.panelsBackground_40 = QFrame(self.frame_26)
        self.panelsBackground_40.setObjectName(u"panelsBackground_40")
        self.panelsBackground_40.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_40.setStyleSheet(u"")
        self.panelsBackground_40.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.panelsBackground_40)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.contentBorderColor1 = QPushButton(self.panelsBackground_40)
        self.contentBorderColor1.setObjectName(u"contentBorderColor1")
        self.contentBorderColor1.setMinimumSize(QSize(24, 24))
        self.contentBorderColor1.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_63.addWidget(self.contentBorderColor1)

        self.contentBorderColor2 = QPushButton(self.panelsBackground_40)
        self.contentBorderColor2.setObjectName(u"contentBorderColor2")
        self.contentBorderColor2.setMinimumSize(QSize(24, 24))
        self.contentBorderColor2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_63.addWidget(self.contentBorderColor2)

        self.contentBorderColor3 = QPushButton(self.panelsBackground_40)
        self.contentBorderColor3.setObjectName(u"contentBorderColor3")
        self.contentBorderColor3.setMinimumSize(QSize(24, 24))
        self.contentBorderColor3.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_63.addWidget(self.contentBorderColor3)

        self.contentBorderColor4 = QPushButton(self.panelsBackground_40)
        self.contentBorderColor4.setObjectName(u"contentBorderColor4")
        self.contentBorderColor4.setMinimumSize(QSize(24, 24))
        self.contentBorderColor4.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_63.addWidget(self.contentBorderColor4)


        self.horizontalLayout_61.addWidget(self.panelsBackground_40)

        self.frame_27 = QFrame(self.widget_6)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setGeometry(QRect(-10, 310, 252, 48))
        self.frame_27.setMaximumSize(QSize(16777213, 48))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_64.setSpacing(0)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(3, 0, 0, 0)
        self.panelsBackground_41 = QFrame(self.frame_27)
        self.panelsBackground_41.setObjectName(u"panelsBackground_41")
        self.panelsBackground_41.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_41.setStyleSheet(u"")
        self.panelsBackground_41.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.panelsBackground_41)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.label_43 = QLabel(self.panelsBackground_41)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_65.addWidget(self.label_43)


        self.horizontalLayout_64.addWidget(self.panelsBackground_41)

        self.panelsBackground_42 = QFrame(self.frame_27)
        self.panelsBackground_42.setObjectName(u"panelsBackground_42")
        self.panelsBackground_42.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_42.setStyleSheet(u"")
        self.panelsBackground_42.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.panelsBackground_42)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.contentHoverColor1 = QPushButton(self.panelsBackground_42)
        self.contentHoverColor1.setObjectName(u"contentHoverColor1")
        self.contentHoverColor1.setMinimumSize(QSize(24, 24))
        self.contentHoverColor1.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_66.addWidget(self.contentHoverColor1)

        self.contentHoverColor2 = QPushButton(self.panelsBackground_42)
        self.contentHoverColor2.setObjectName(u"contentHoverColor2")
        self.contentHoverColor2.setMinimumSize(QSize(24, 24))
        self.contentHoverColor2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_66.addWidget(self.contentHoverColor2)

        self.contentHoverColor3 = QPushButton(self.panelsBackground_42)
        self.contentHoverColor3.setObjectName(u"contentHoverColor3")
        self.contentHoverColor3.setMinimumSize(QSize(24, 24))
        self.contentHoverColor3.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_66.addWidget(self.contentHoverColor3)

        self.contentHoverColor4 = QPushButton(self.panelsBackground_42)
        self.contentHoverColor4.setObjectName(u"contentHoverColor4")
        self.contentHoverColor4.setMinimumSize(QSize(24, 24))
        self.contentHoverColor4.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_66.addWidget(self.contentHoverColor4)


        self.horizontalLayout_64.addWidget(self.panelsBackground_42)

        self.frame_28 = QFrame(self.widget_6)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setGeometry(QRect(-10, 360, 252, 48))
        self.frame_28.setMaximumSize(QSize(16777213, 48))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_67.setSpacing(0)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(3, 0, 0, 0)
        self.panelsBackground_43 = QFrame(self.frame_28)
        self.panelsBackground_43.setObjectName(u"panelsBackground_43")
        self.panelsBackground_43.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_43.setStyleSheet(u"")
        self.panelsBackground_43.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.panelsBackground_43)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.label_44 = QLabel(self.panelsBackground_43)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_68.addWidget(self.label_44)


        self.horizontalLayout_67.addWidget(self.panelsBackground_43)

        self.panelsBackground_44 = QFrame(self.frame_28)
        self.panelsBackground_44.setObjectName(u"panelsBackground_44")
        self.panelsBackground_44.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_44.setStyleSheet(u"")
        self.panelsBackground_44.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.panelsBackground_44)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.contentFirst_textColor1 = QPushButton(self.panelsBackground_44)
        self.contentFirst_textColor1.setObjectName(u"contentFirst_textColor1")
        self.contentFirst_textColor1.setMinimumSize(QSize(24, 24))
        self.contentFirst_textColor1.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_69.addWidget(self.contentFirst_textColor1)

        self.contentFirst_textColor2 = QPushButton(self.panelsBackground_44)
        self.contentFirst_textColor2.setObjectName(u"contentFirst_textColor2")
        self.contentFirst_textColor2.setMinimumSize(QSize(24, 24))
        self.contentFirst_textColor2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_69.addWidget(self.contentFirst_textColor2)

        self.contentFirst_textColor3 = QPushButton(self.panelsBackground_44)
        self.contentFirst_textColor3.setObjectName(u"contentFirst_textColor3")
        self.contentFirst_textColor3.setMinimumSize(QSize(24, 24))
        self.contentFirst_textColor3.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_69.addWidget(self.contentFirst_textColor3)

        self.contentFirst_textColor4 = QPushButton(self.panelsBackground_44)
        self.contentFirst_textColor4.setObjectName(u"contentFirst_textColor4")
        self.contentFirst_textColor4.setMinimumSize(QSize(24, 24))
        self.contentFirst_textColor4.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_69.addWidget(self.contentFirst_textColor4)


        self.horizontalLayout_67.addWidget(self.panelsBackground_44)

        self.frame_29 = QFrame(self.widget_6)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setGeometry(QRect(-10, 410, 252, 48))
        self.frame_29.setMaximumSize(QSize(16777213, 48))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_70.setSpacing(0)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(3, 0, 0, 0)
        self.panelsBackground_45 = QFrame(self.frame_29)
        self.panelsBackground_45.setObjectName(u"panelsBackground_45")
        self.panelsBackground_45.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_45.setStyleSheet(u"")
        self.panelsBackground_45.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.panelsBackground_45)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.label_45 = QLabel(self.panelsBackground_45)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_71.addWidget(self.label_45)


        self.horizontalLayout_70.addWidget(self.panelsBackground_45)

        self.panelsBackground_46 = QFrame(self.frame_29)
        self.panelsBackground_46.setObjectName(u"panelsBackground_46")
        self.panelsBackground_46.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_46.setStyleSheet(u"")
        self.panelsBackground_46.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.panelsBackground_46)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.contentSecond_textColor1 = QPushButton(self.panelsBackground_46)
        self.contentSecond_textColor1.setObjectName(u"contentSecond_textColor1")
        self.contentSecond_textColor1.setMinimumSize(QSize(24, 24))
        self.contentSecond_textColor1.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_72.addWidget(self.contentSecond_textColor1)

        self.contentSecond_textColor2 = QPushButton(self.panelsBackground_46)
        self.contentSecond_textColor2.setObjectName(u"contentSecond_textColor2")
        self.contentSecond_textColor2.setMinimumSize(QSize(24, 24))
        self.contentSecond_textColor2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_72.addWidget(self.contentSecond_textColor2)

        self.contentSecond_textColor3 = QPushButton(self.panelsBackground_46)
        self.contentSecond_textColor3.setObjectName(u"contentSecond_textColor3")
        self.contentSecond_textColor3.setMinimumSize(QSize(24, 24))
        self.contentSecond_textColor3.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_72.addWidget(self.contentSecond_textColor3)

        self.contentSecond_textColor4 = QPushButton(self.panelsBackground_46)
        self.contentSecond_textColor4.setObjectName(u"contentSecond_textColor4")
        self.contentSecond_textColor4.setMinimumSize(QSize(24, 24))
        self.contentSecond_textColor4.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_72.addWidget(self.contentSecond_textColor4)


        self.horizontalLayout_70.addWidget(self.panelsBackground_46)

        self.frame_30 = QFrame(self.widget_6)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setGeometry(QRect(-10, 460, 252, 48))
        self.frame_30.setMaximumSize(QSize(16777213, 48))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_73.setSpacing(0)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(3, 0, 0, 0)
        self.panelsBackground_47 = QFrame(self.frame_30)
        self.panelsBackground_47.setObjectName(u"panelsBackground_47")
        self.panelsBackground_47.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_47.setStyleSheet(u"")
        self.panelsBackground_47.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_74 = QHBoxLayout(self.panelsBackground_47)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.label_46 = QLabel(self.panelsBackground_47)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_74.addWidget(self.label_46)


        self.horizontalLayout_73.addWidget(self.panelsBackground_47)

        self.panelsBackground_48 = QFrame(self.frame_30)
        self.panelsBackground_48.setObjectName(u"panelsBackground_48")
        self.panelsBackground_48.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_48.setStyleSheet(u"")
        self.panelsBackground_48.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_75 = QHBoxLayout(self.panelsBackground_48)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.contentThird_textColor1 = QPushButton(self.panelsBackground_48)
        self.contentThird_textColor1.setObjectName(u"contentThird_textColor1")
        self.contentThird_textColor1.setMinimumSize(QSize(24, 24))
        self.contentThird_textColor1.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_75.addWidget(self.contentThird_textColor1)

        self.contentThird_textColor2 = QPushButton(self.panelsBackground_48)
        self.contentThird_textColor2.setObjectName(u"contentThird_textColor2")
        self.contentThird_textColor2.setMinimumSize(QSize(24, 24))
        self.contentThird_textColor2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_75.addWidget(self.contentThird_textColor2)

        self.contentThird_textColor3 = QPushButton(self.panelsBackground_48)
        self.contentThird_textColor3.setObjectName(u"contentThird_textColor3")
        self.contentThird_textColor3.setMinimumSize(QSize(24, 24))
        self.contentThird_textColor3.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_75.addWidget(self.contentThird_textColor3)

        self.contentThird_textColor4 = QPushButton(self.panelsBackground_48)
        self.contentThird_textColor4.setObjectName(u"contentThird_textColor4")
        self.contentThird_textColor4.setMinimumSize(QSize(24, 24))
        self.contentThird_textColor4.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_75.addWidget(self.contentThird_textColor4)


        self.horizontalLayout_73.addWidget(self.panelsBackground_48)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.toolBox.addItem(self.page_2, u"Content")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 252, 600))
        self.widget_9 = QWidget(self.page_3)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(10, 10, 241, 591))
        self.frame_14 = QFrame(self.widget_9)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(0, -10, 240, 170))
        self.frame_14.setMinimumSize(QSize(0, 170))
        self.frame_14.setMaximumSize(QSize(16777215, 120))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_14)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, -1, 0)
        self.label_21 = QLabel(self.frame_14)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_27.addWidget(self.label_21)

        self.panelsBackground_23 = QFrame(self.frame_14)
        self.panelsBackground_23.setObjectName(u"panelsBackground_23")
        self.panelsBackground_23.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_23.setStyleSheet(u"")
        self.panelsBackground_23.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.panelsBackground_23)
        self.horizontalLayout_32.setSpacing(14)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, -1, 0)
        self.footerMainColor1 = QPushButton(self.panelsBackground_23)
        self.footerMainColor1.setObjectName(u"footerMainColor1")
        self.footerMainColor1.setMinimumSize(QSize(24, 24))
        self.footerMainColor1.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_32.addWidget(self.footerMainColor1)

        self.footerMainColor2 = QPushButton(self.panelsBackground_23)
        self.footerMainColor2.setObjectName(u"footerMainColor2")
        self.footerMainColor2.setMinimumSize(QSize(24, 24))
        self.footerMainColor2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_32.addWidget(self.footerMainColor2)

        self.footerMainColor3 = QPushButton(self.panelsBackground_23)
        self.footerMainColor3.setObjectName(u"footerMainColor3")
        self.footerMainColor3.setMinimumSize(QSize(24, 24))
        self.footerMainColor3.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_32.addWidget(self.footerMainColor3)

        self.footerMainColor4 = QPushButton(self.panelsBackground_23)
        self.footerMainColor4.setObjectName(u"footerMainColor4")
        self.footerMainColor4.setMinimumSize(QSize(24, 24))
        self.footerMainColor4.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_32.addWidget(self.footerMainColor4)

        self.footerMainColor5 = QPushButton(self.panelsBackground_23)
        self.footerMainColor5.setObjectName(u"footerMainColor5")
        self.footerMainColor5.setMinimumSize(QSize(24, 24))
        self.footerMainColor5.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_32.addWidget(self.footerMainColor5)

        self.footerMainColor6 = QPushButton(self.panelsBackground_23)
        self.footerMainColor6.setObjectName(u"footerMainColor6")
        self.footerMainColor6.setMinimumSize(QSize(24, 24))
        self.footerMainColor6.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_32.addWidget(self.footerMainColor6)

        self.footerMainColor7 = QPushButton(self.panelsBackground_23)
        self.footerMainColor7.setObjectName(u"footerMainColor7")
        self.footerMainColor7.setMinimumSize(QSize(24, 24))
        self.footerMainColor7.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_32.addWidget(self.footerMainColor7)


        self.verticalLayout_27.addWidget(self.panelsBackground_23)

        self.panelsBackground_24 = QFrame(self.frame_14)
        self.panelsBackground_24.setObjectName(u"panelsBackground_24")
        self.panelsBackground_24.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_24.setStyleSheet(u"")
        self.panelsBackground_24.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.panelsBackground_24)
        self.horizontalLayout_33.setSpacing(14)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, -1, 0)
        self.footerMainColor8 = QPushButton(self.panelsBackground_24)
        self.footerMainColor8.setObjectName(u"footerMainColor8")
        self.footerMainColor8.setMinimumSize(QSize(24, 24))
        self.footerMainColor8.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_33.addWidget(self.footerMainColor8)

        self.footerMainColor9 = QPushButton(self.panelsBackground_24)
        self.footerMainColor9.setObjectName(u"footerMainColor9")
        self.footerMainColor9.setMinimumSize(QSize(24, 24))
        self.footerMainColor9.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_33.addWidget(self.footerMainColor9)

        self.footerMainColor10 = QPushButton(self.panelsBackground_24)
        self.footerMainColor10.setObjectName(u"footerMainColor10")
        self.footerMainColor10.setMinimumSize(QSize(24, 24))
        self.footerMainColor10.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_33.addWidget(self.footerMainColor10)

        self.footerMainColor11 = QPushButton(self.panelsBackground_24)
        self.footerMainColor11.setObjectName(u"footerMainColor11")
        self.footerMainColor11.setMinimumSize(QSize(24, 24))
        self.footerMainColor11.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_33.addWidget(self.footerMainColor11)

        self.footerMainColor12 = QPushButton(self.panelsBackground_24)
        self.footerMainColor12.setObjectName(u"footerMainColor12")
        self.footerMainColor12.setMinimumSize(QSize(24, 24))
        self.footerMainColor12.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_33.addWidget(self.footerMainColor12)

        self.footerMainColor13 = QPushButton(self.panelsBackground_24)
        self.footerMainColor13.setObjectName(u"footerMainColor13")
        self.footerMainColor13.setMinimumSize(QSize(24, 24))
        self.footerMainColor13.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_33.addWidget(self.footerMainColor13)

        self.footerMainColor14 = QPushButton(self.panelsBackground_24)
        self.footerMainColor14.setObjectName(u"footerMainColor14")
        self.footerMainColor14.setMinimumSize(QSize(24, 24))
        self.footerMainColor14.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_33.addWidget(self.footerMainColor14)


        self.verticalLayout_27.addWidget(self.panelsBackground_24)

        self.panelsBackground_25 = QFrame(self.frame_14)
        self.panelsBackground_25.setObjectName(u"panelsBackground_25")
        self.panelsBackground_25.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_25.setStyleSheet(u"")
        self.panelsBackground_25.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_130 = QHBoxLayout(self.panelsBackground_25)
        self.horizontalLayout_130.setSpacing(14)
        self.horizontalLayout_130.setObjectName(u"horizontalLayout_130")
        self.horizontalLayout_130.setContentsMargins(0, 0, -1, 0)
        self.footerMainColor15 = QPushButton(self.panelsBackground_25)
        self.footerMainColor15.setObjectName(u"footerMainColor15")
        self.footerMainColor15.setMinimumSize(QSize(24, 24))
        self.footerMainColor15.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_130.addWidget(self.footerMainColor15)

        self.footerMainColor16 = QPushButton(self.panelsBackground_25)
        self.footerMainColor16.setObjectName(u"footerMainColor16")
        self.footerMainColor16.setMinimumSize(QSize(24, 24))
        self.footerMainColor16.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_130.addWidget(self.footerMainColor16)

        self.footerMainColor17 = QPushButton(self.panelsBackground_25)
        self.footerMainColor17.setObjectName(u"footerMainColor17")
        self.footerMainColor17.setMinimumSize(QSize(24, 24))
        self.footerMainColor17.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_130.addWidget(self.footerMainColor17)

        self.footerMainColor18 = QPushButton(self.panelsBackground_25)
        self.footerMainColor18.setObjectName(u"footerMainColor18")
        self.footerMainColor18.setMinimumSize(QSize(24, 24))
        self.footerMainColor18.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_130.addWidget(self.footerMainColor18)

        self.footerMainColor19 = QPushButton(self.panelsBackground_25)
        self.footerMainColor19.setObjectName(u"footerMainColor19")
        self.footerMainColor19.setMinimumSize(QSize(24, 24))
        self.footerMainColor19.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_130.addWidget(self.footerMainColor19)

        self.footerMainColor20 = QPushButton(self.panelsBackground_25)
        self.footerMainColor20.setObjectName(u"footerMainColor20")
        self.footerMainColor20.setMinimumSize(QSize(24, 24))
        self.footerMainColor20.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_130.addWidget(self.footerMainColor20)

        self.footerMainColor21 = QPushButton(self.panelsBackground_25)
        self.footerMainColor21.setObjectName(u"footerMainColor21")
        self.footerMainColor21.setMinimumSize(QSize(24, 24))
        self.footerMainColor21.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_130.addWidget(self.footerMainColor21)


        self.verticalLayout_27.addWidget(self.panelsBackground_25)

        self.frame_48 = QFrame(self.widget_9)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setGeometry(QRect(-10, 160, 252, 48))
        self.frame_48.setMaximumSize(QSize(16777213, 48))
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_131 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_131.setSpacing(0)
        self.horizontalLayout_131.setObjectName(u"horizontalLayout_131")
        self.horizontalLayout_131.setContentsMargins(3, 0, 0, 0)
        self.panelsBackground_80 = QFrame(self.frame_48)
        self.panelsBackground_80.setObjectName(u"panelsBackground_80")
        self.panelsBackground_80.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_80.setStyleSheet(u"")
        self.panelsBackground_80.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_80.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_132 = QHBoxLayout(self.panelsBackground_80)
        self.horizontalLayout_132.setObjectName(u"horizontalLayout_132")
        self.label_64 = QLabel(self.panelsBackground_80)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_132.addWidget(self.label_64)


        self.horizontalLayout_131.addWidget(self.panelsBackground_80)

        self.frame_15 = QFrame(self.frame_48)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 40))
        self.frame_15.setStyleSheet(u"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_133 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_133.setObjectName(u"horizontalLayout_133")
        self.footerHoverColor1 = QPushButton(self.frame_15)
        self.footerHoverColor1.setObjectName(u"footerHoverColor1")
        self.footerHoverColor1.setMinimumSize(QSize(24, 24))
        self.footerHoverColor1.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_133.addWidget(self.footerHoverColor1)

        self.footerHoverColor2 = QPushButton(self.frame_15)
        self.footerHoverColor2.setObjectName(u"footerHoverColor2")
        self.footerHoverColor2.setMinimumSize(QSize(24, 24))
        self.footerHoverColor2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_133.addWidget(self.footerHoverColor2)

        self.footerHoverColor3 = QPushButton(self.frame_15)
        self.footerHoverColor3.setObjectName(u"footerHoverColor3")
        self.footerHoverColor3.setMinimumSize(QSize(24, 24))
        self.footerHoverColor3.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_133.addWidget(self.footerHoverColor3)

        self.footerHoverColor4 = QPushButton(self.frame_15)
        self.footerHoverColor4.setObjectName(u"footerHoverColor4")
        self.footerHoverColor4.setMinimumSize(QSize(24, 24))
        self.footerHoverColor4.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_133.addWidget(self.footerHoverColor4)


        self.horizontalLayout_131.addWidget(self.frame_15)

        self.frame_49 = QFrame(self.widget_9)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setGeometry(QRect(-10, 210, 252, 48))
        self.frame_49.setMaximumSize(QSize(16777213, 48))
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_134 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_134.setSpacing(0)
        self.horizontalLayout_134.setObjectName(u"horizontalLayout_134")
        self.horizontalLayout_134.setContentsMargins(3, 0, 0, 0)
        self.panelsBackground_81 = QFrame(self.frame_49)
        self.panelsBackground_81.setObjectName(u"panelsBackground_81")
        self.panelsBackground_81.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_81.setStyleSheet(u"")
        self.panelsBackground_81.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_81.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_135 = QHBoxLayout(self.panelsBackground_81)
        self.horizontalLayout_135.setObjectName(u"horizontalLayout_135")
        self.label_65 = QLabel(self.panelsBackground_81)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_135.addWidget(self.label_65)


        self.horizontalLayout_134.addWidget(self.panelsBackground_81)

        self.panelsBackground_82 = QFrame(self.frame_49)
        self.panelsBackground_82.setObjectName(u"panelsBackground_82")
        self.panelsBackground_82.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_82.setStyleSheet(u"")
        self.panelsBackground_82.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_82.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_136 = QHBoxLayout(self.panelsBackground_82)
        self.horizontalLayout_136.setObjectName(u"horizontalLayout_136")
        self.footerBorderColor1 = QPushButton(self.panelsBackground_82)
        self.footerBorderColor1.setObjectName(u"footerBorderColor1")
        self.footerBorderColor1.setMinimumSize(QSize(24, 24))
        self.footerBorderColor1.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_136.addWidget(self.footerBorderColor1)

        self.footerBorderColor2 = QPushButton(self.panelsBackground_82)
        self.footerBorderColor2.setObjectName(u"footerBorderColor2")
        self.footerBorderColor2.setMinimumSize(QSize(24, 24))
        self.footerBorderColor2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_136.addWidget(self.footerBorderColor2)

        self.footerBorderColor3 = QPushButton(self.panelsBackground_82)
        self.footerBorderColor3.setObjectName(u"footerBorderColor3")
        self.footerBorderColor3.setMinimumSize(QSize(24, 24))
        self.footerBorderColor3.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_136.addWidget(self.footerBorderColor3)

        self.footerBorderColor4 = QPushButton(self.panelsBackground_82)
        self.footerBorderColor4.setObjectName(u"footerBorderColor4")
        self.footerBorderColor4.setMinimumSize(QSize(24, 24))
        self.footerBorderColor4.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_136.addWidget(self.footerBorderColor4)


        self.horizontalLayout_134.addWidget(self.panelsBackground_82)

        self.frame_50 = QFrame(self.widget_9)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setGeometry(QRect(-10, 260, 252, 48))
        self.frame_50.setMaximumSize(QSize(16777213, 48))
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_137 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_137.setSpacing(0)
        self.horizontalLayout_137.setObjectName(u"horizontalLayout_137")
        self.horizontalLayout_137.setContentsMargins(3, 0, 0, 0)
        self.panelsBackground_83 = QFrame(self.frame_50)
        self.panelsBackground_83.setObjectName(u"panelsBackground_83")
        self.panelsBackground_83.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_83.setStyleSheet(u"")
        self.panelsBackground_83.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_83.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_138 = QHBoxLayout(self.panelsBackground_83)
        self.horizontalLayout_138.setObjectName(u"horizontalLayout_138")
        self.label_66 = QLabel(self.panelsBackground_83)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_138.addWidget(self.label_66)


        self.horizontalLayout_137.addWidget(self.panelsBackground_83)

        self.panelsBackground_84 = QFrame(self.frame_50)
        self.panelsBackground_84.setObjectName(u"panelsBackground_84")
        self.panelsBackground_84.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_84.setStyleSheet(u"")
        self.panelsBackground_84.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_84.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_139 = QHBoxLayout(self.panelsBackground_84)
        self.horizontalLayout_139.setObjectName(u"horizontalLayout_139")
        self.footerFirst_textColor1 = QPushButton(self.panelsBackground_84)
        self.footerFirst_textColor1.setObjectName(u"footerFirst_textColor1")
        self.footerFirst_textColor1.setMinimumSize(QSize(24, 24))
        self.footerFirst_textColor1.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_139.addWidget(self.footerFirst_textColor1)

        self.footerFirst_textColor2 = QPushButton(self.panelsBackground_84)
        self.footerFirst_textColor2.setObjectName(u"footerFirst_textColor2")
        self.footerFirst_textColor2.setMinimumSize(QSize(24, 24))
        self.footerFirst_textColor2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_139.addWidget(self.footerFirst_textColor2)

        self.footerFirst_textColor3 = QPushButton(self.panelsBackground_84)
        self.footerFirst_textColor3.setObjectName(u"footerFirst_textColor3")
        self.footerFirst_textColor3.setMinimumSize(QSize(24, 24))
        self.footerFirst_textColor3.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_139.addWidget(self.footerFirst_textColor3)

        self.footerFirst_textColor4 = QPushButton(self.panelsBackground_84)
        self.footerFirst_textColor4.setObjectName(u"footerFirst_textColor4")
        self.footerFirst_textColor4.setMinimumSize(QSize(24, 24))
        self.footerFirst_textColor4.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_139.addWidget(self.footerFirst_textColor4)


        self.horizontalLayout_137.addWidget(self.panelsBackground_84)

        self.frame_51 = QFrame(self.widget_9)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setGeometry(QRect(-10, 310, 252, 48))
        self.frame_51.setMaximumSize(QSize(16777213, 48))
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_140 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_140.setSpacing(0)
        self.horizontalLayout_140.setObjectName(u"horizontalLayout_140")
        self.horizontalLayout_140.setContentsMargins(3, 0, 0, 0)
        self.panelsBackground_85 = QFrame(self.frame_51)
        self.panelsBackground_85.setObjectName(u"panelsBackground_85")
        self.panelsBackground_85.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_85.setStyleSheet(u"")
        self.panelsBackground_85.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_85.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_141 = QHBoxLayout(self.panelsBackground_85)
        self.horizontalLayout_141.setObjectName(u"horizontalLayout_141")
        self.label_67 = QLabel(self.panelsBackground_85)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_141.addWidget(self.label_67)


        self.horizontalLayout_140.addWidget(self.panelsBackground_85)

        self.panelsBackground_86 = QFrame(self.frame_51)
        self.panelsBackground_86.setObjectName(u"panelsBackground_86")
        self.panelsBackground_86.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_86.setStyleSheet(u"")
        self.panelsBackground_86.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_86.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_142 = QHBoxLayout(self.panelsBackground_86)
        self.horizontalLayout_142.setObjectName(u"horizontalLayout_142")
        self.footerSecond_textColor1 = QPushButton(self.panelsBackground_86)
        self.footerSecond_textColor1.setObjectName(u"footerSecond_textColor1")
        self.footerSecond_textColor1.setMinimumSize(QSize(24, 24))
        self.footerSecond_textColor1.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_142.addWidget(self.footerSecond_textColor1)

        self.footerSecond_textColor2 = QPushButton(self.panelsBackground_86)
        self.footerSecond_textColor2.setObjectName(u"footerSecond_textColor2")
        self.footerSecond_textColor2.setMinimumSize(QSize(24, 24))
        self.footerSecond_textColor2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_142.addWidget(self.footerSecond_textColor2)

        self.footerSecond_textColor3 = QPushButton(self.panelsBackground_86)
        self.footerSecond_textColor3.setObjectName(u"footerSecond_textColor3")
        self.footerSecond_textColor3.setMinimumSize(QSize(24, 24))
        self.footerSecond_textColor3.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_142.addWidget(self.footerSecond_textColor3)

        self.footerSecond_textColor4 = QPushButton(self.panelsBackground_86)
        self.footerSecond_textColor4.setObjectName(u"footerSecond_textColor4")
        self.footerSecond_textColor4.setMinimumSize(QSize(24, 24))
        self.footerSecond_textColor4.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_142.addWidget(self.footerSecond_textColor4)


        self.horizontalLayout_140.addWidget(self.panelsBackground_86)

        self.frame_52 = QFrame(self.widget_9)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setGeometry(QRect(-10, 360, 252, 48))
        self.frame_52.setMaximumSize(QSize(16777213, 48))
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_143 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_143.setSpacing(0)
        self.horizontalLayout_143.setObjectName(u"horizontalLayout_143")
        self.horizontalLayout_143.setContentsMargins(3, 0, 0, 0)
        self.panelsBackground_87 = QFrame(self.frame_52)
        self.panelsBackground_87.setObjectName(u"panelsBackground_87")
        self.panelsBackground_87.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_87.setStyleSheet(u"")
        self.panelsBackground_87.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_87.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_144 = QHBoxLayout(self.panelsBackground_87)
        self.horizontalLayout_144.setObjectName(u"horizontalLayout_144")
        self.label_68 = QLabel(self.panelsBackground_87)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_144.addWidget(self.label_68)


        self.horizontalLayout_143.addWidget(self.panelsBackground_87)

        self.panelsBackground_88 = QFrame(self.frame_52)
        self.panelsBackground_88.setObjectName(u"panelsBackground_88")
        self.panelsBackground_88.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_88.setStyleSheet(u"")
        self.panelsBackground_88.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_88.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_145 = QHBoxLayout(self.panelsBackground_88)
        self.horizontalLayout_145.setObjectName(u"horizontalLayout_145")
        self.footerThird_textColor1 = QPushButton(self.panelsBackground_88)
        self.footerThird_textColor1.setObjectName(u"footerThird_textColor1")
        self.footerThird_textColor1.setMinimumSize(QSize(24, 24))
        self.footerThird_textColor1.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_145.addWidget(self.footerThird_textColor1)

        self.footerThird_textColor2 = QPushButton(self.panelsBackground_88)
        self.footerThird_textColor2.setObjectName(u"footerThird_textColor2")
        self.footerThird_textColor2.setMinimumSize(QSize(24, 24))
        self.footerThird_textColor2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_145.addWidget(self.footerThird_textColor2)

        self.footerThird_textColor3 = QPushButton(self.panelsBackground_88)
        self.footerThird_textColor3.setObjectName(u"footerThird_textColor3")
        self.footerThird_textColor3.setMinimumSize(QSize(24, 24))
        self.footerThird_textColor3.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_145.addWidget(self.footerThird_textColor3)

        self.footerThird_textColor4 = QPushButton(self.panelsBackground_88)
        self.footerThird_textColor4.setObjectName(u"footerThird_textColor4")
        self.footerThird_textColor4.setMinimumSize(QSize(24, 24))
        self.footerThird_textColor4.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_145.addWidget(self.footerThird_textColor4)


        self.horizontalLayout_143.addWidget(self.panelsBackground_88)

        self.toolBox.addItem(self.page_3, u"Footer")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 252, 600))
        self.widget_10 = QWidget(self.page_4)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setGeometry(QRect(10, 10, 241, 591))
        self.frame_16 = QFrame(self.widget_10)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(0, -10, 240, 170))
        self.frame_16.setMinimumSize(QSize(0, 170))
        self.frame_16.setMaximumSize(QSize(16777215, 120))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_16)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, -1, 0)
        self.label_22 = QLabel(self.frame_16)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_28.addWidget(self.label_22)

        self.panelsBackground_26 = QFrame(self.frame_16)
        self.panelsBackground_26.setObjectName(u"panelsBackground_26")
        self.panelsBackground_26.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_26.setStyleSheet(u"")
        self.panelsBackground_26.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.panelsBackground_26)
        self.horizontalLayout_34.setSpacing(14)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, -1, 0)
        self.controllerMainColor1 = QPushButton(self.panelsBackground_26)
        self.controllerMainColor1.setObjectName(u"controllerMainColor1")
        self.controllerMainColor1.setMinimumSize(QSize(24, 24))
        self.controllerMainColor1.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_34.addWidget(self.controllerMainColor1)

        self.controllerMainColor2 = QPushButton(self.panelsBackground_26)
        self.controllerMainColor2.setObjectName(u"controllerMainColor2")
        self.controllerMainColor2.setMinimumSize(QSize(24, 24))
        self.controllerMainColor2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_34.addWidget(self.controllerMainColor2)

        self.controllerMainColor3 = QPushButton(self.panelsBackground_26)
        self.controllerMainColor3.setObjectName(u"controllerMainColor3")
        self.controllerMainColor3.setMinimumSize(QSize(24, 24))
        self.controllerMainColor3.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_34.addWidget(self.controllerMainColor3)

        self.controllerMainColor4 = QPushButton(self.panelsBackground_26)
        self.controllerMainColor4.setObjectName(u"controllerMainColor4")
        self.controllerMainColor4.setMinimumSize(QSize(24, 24))
        self.controllerMainColor4.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_34.addWidget(self.controllerMainColor4)

        self.controllerMainColor5 = QPushButton(self.panelsBackground_26)
        self.controllerMainColor5.setObjectName(u"controllerMainColor5")
        self.controllerMainColor5.setMinimumSize(QSize(24, 24))
        self.controllerMainColor5.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_34.addWidget(self.controllerMainColor5)

        self.controllerMainColor6 = QPushButton(self.panelsBackground_26)
        self.controllerMainColor6.setObjectName(u"controllerMainColor6")
        self.controllerMainColor6.setMinimumSize(QSize(24, 24))
        self.controllerMainColor6.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_34.addWidget(self.controllerMainColor6)

        self.controllerMainColor7 = QPushButton(self.panelsBackground_26)
        self.controllerMainColor7.setObjectName(u"controllerMainColor7")
        self.controllerMainColor7.setMinimumSize(QSize(24, 24))
        self.controllerMainColor7.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_34.addWidget(self.controllerMainColor7)


        self.verticalLayout_28.addWidget(self.panelsBackground_26)

        self.panelsBackground_27 = QFrame(self.frame_16)
        self.panelsBackground_27.setObjectName(u"panelsBackground_27")
        self.panelsBackground_27.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_27.setStyleSheet(u"")
        self.panelsBackground_27.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.panelsBackground_27)
        self.horizontalLayout_35.setSpacing(14)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, -1, 0)
        self.controllerMainColor8 = QPushButton(self.panelsBackground_27)
        self.controllerMainColor8.setObjectName(u"controllerMainColor8")
        self.controllerMainColor8.setMinimumSize(QSize(24, 24))
        self.controllerMainColor8.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_35.addWidget(self.controllerMainColor8)

        self.controllerMainColor9 = QPushButton(self.panelsBackground_27)
        self.controllerMainColor9.setObjectName(u"controllerMainColor9")
        self.controllerMainColor9.setMinimumSize(QSize(24, 24))
        self.controllerMainColor9.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_35.addWidget(self.controllerMainColor9)

        self.controllerMainColor10 = QPushButton(self.panelsBackground_27)
        self.controllerMainColor10.setObjectName(u"controllerMainColor10")
        self.controllerMainColor10.setMinimumSize(QSize(24, 24))
        self.controllerMainColor10.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_35.addWidget(self.controllerMainColor10)

        self.controllerMainColor11 = QPushButton(self.panelsBackground_27)
        self.controllerMainColor11.setObjectName(u"controllerMainColor11")
        self.controllerMainColor11.setMinimumSize(QSize(24, 24))
        self.controllerMainColor11.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_35.addWidget(self.controllerMainColor11)

        self.controllerMainColor12 = QPushButton(self.panelsBackground_27)
        self.controllerMainColor12.setObjectName(u"controllerMainColor12")
        self.controllerMainColor12.setMinimumSize(QSize(24, 24))
        self.controllerMainColor12.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_35.addWidget(self.controllerMainColor12)

        self.controllerMainColor13 = QPushButton(self.panelsBackground_27)
        self.controllerMainColor13.setObjectName(u"controllerMainColor13")
        self.controllerMainColor13.setMinimumSize(QSize(24, 24))
        self.controllerMainColor13.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_35.addWidget(self.controllerMainColor13)

        self.controllerMainColor14 = QPushButton(self.panelsBackground_27)
        self.controllerMainColor14.setObjectName(u"controllerMainColor14")
        self.controllerMainColor14.setMinimumSize(QSize(24, 24))
        self.controllerMainColor14.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_35.addWidget(self.controllerMainColor14)


        self.verticalLayout_28.addWidget(self.panelsBackground_27)

        self.panelsBackground_28 = QFrame(self.frame_16)
        self.panelsBackground_28.setObjectName(u"panelsBackground_28")
        self.panelsBackground_28.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_28.setStyleSheet(u"")
        self.panelsBackground_28.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_155 = QHBoxLayout(self.panelsBackground_28)
        self.horizontalLayout_155.setSpacing(14)
        self.horizontalLayout_155.setObjectName(u"horizontalLayout_155")
        self.horizontalLayout_155.setContentsMargins(0, 0, -1, 0)
        self.controllerMainColor15 = QPushButton(self.panelsBackground_28)
        self.controllerMainColor15.setObjectName(u"controllerMainColor15")
        self.controllerMainColor15.setMinimumSize(QSize(24, 24))
        self.controllerMainColor15.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_155.addWidget(self.controllerMainColor15)

        self.controllerMainColor16 = QPushButton(self.panelsBackground_28)
        self.controllerMainColor16.setObjectName(u"controllerMainColor16")
        self.controllerMainColor16.setMinimumSize(QSize(24, 24))
        self.controllerMainColor16.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_155.addWidget(self.controllerMainColor16)

        self.controllerMainColor17 = QPushButton(self.panelsBackground_28)
        self.controllerMainColor17.setObjectName(u"controllerMainColor17")
        self.controllerMainColor17.setMinimumSize(QSize(24, 24))
        self.controllerMainColor17.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_155.addWidget(self.controllerMainColor17)

        self.controllerMainColor18 = QPushButton(self.panelsBackground_28)
        self.controllerMainColor18.setObjectName(u"controllerMainColor18")
        self.controllerMainColor18.setMinimumSize(QSize(24, 24))
        self.controllerMainColor18.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_155.addWidget(self.controllerMainColor18)

        self.controllerMainColor19 = QPushButton(self.panelsBackground_28)
        self.controllerMainColor19.setObjectName(u"controllerMainColor19")
        self.controllerMainColor19.setMinimumSize(QSize(24, 24))
        self.controllerMainColor19.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_155.addWidget(self.controllerMainColor19)

        self.controllerMainColor20 = QPushButton(self.panelsBackground_28)
        self.controllerMainColor20.setObjectName(u"controllerMainColor20")
        self.controllerMainColor20.setMinimumSize(QSize(24, 24))
        self.controllerMainColor20.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_155.addWidget(self.controllerMainColor20)

        self.controllerMainColor21 = QPushButton(self.panelsBackground_28)
        self.controllerMainColor21.setObjectName(u"controllerMainColor21")
        self.controllerMainColor21.setMinimumSize(QSize(24, 24))
        self.controllerMainColor21.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_155.addWidget(self.controllerMainColor21)


        self.verticalLayout_28.addWidget(self.panelsBackground_28)

        self.frame_56 = QFrame(self.widget_10)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setGeometry(QRect(-10, 160, 252, 48))
        self.frame_56.setMaximumSize(QSize(16777213, 48))
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_156 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_156.setSpacing(0)
        self.horizontalLayout_156.setObjectName(u"horizontalLayout_156")
        self.horizontalLayout_156.setContentsMargins(3, 0, 0, 0)
        self.panelsBackground_95 = QFrame(self.frame_56)
        self.panelsBackground_95.setObjectName(u"panelsBackground_95")
        self.panelsBackground_95.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_95.setStyleSheet(u"")
        self.panelsBackground_95.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_95.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_157 = QHBoxLayout(self.panelsBackground_95)
        self.horizontalLayout_157.setObjectName(u"horizontalLayout_157")
        self.label_72 = QLabel(self.panelsBackground_95)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_157.addWidget(self.label_72)


        self.horizontalLayout_156.addWidget(self.panelsBackground_95)

        self.frame_18 = QFrame(self.frame_56)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(16777215, 40))
        self.frame_18.setStyleSheet(u"")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_158 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_158.setObjectName(u"horizontalLayout_158")
        self.controllerHoverColor1 = QPushButton(self.frame_18)
        self.controllerHoverColor1.setObjectName(u"controllerHoverColor1")
        self.controllerHoverColor1.setMinimumSize(QSize(24, 24))
        self.controllerHoverColor1.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_158.addWidget(self.controllerHoverColor1)

        self.controllerHoverColor2 = QPushButton(self.frame_18)
        self.controllerHoverColor2.setObjectName(u"controllerHoverColor2")
        self.controllerHoverColor2.setMinimumSize(QSize(24, 24))
        self.controllerHoverColor2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_158.addWidget(self.controllerHoverColor2)

        self.controllerHoverColor3 = QPushButton(self.frame_18)
        self.controllerHoverColor3.setObjectName(u"controllerHoverColor3")
        self.controllerHoverColor3.setMinimumSize(QSize(24, 24))
        self.controllerHoverColor3.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_158.addWidget(self.controllerHoverColor3)

        self.controllerHoverColor4 = QPushButton(self.frame_18)
        self.controllerHoverColor4.setObjectName(u"controllerHoverColor4")
        self.controllerHoverColor4.setMinimumSize(QSize(24, 24))
        self.controllerHoverColor4.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_158.addWidget(self.controllerHoverColor4)


        self.horizontalLayout_156.addWidget(self.frame_18)

        self.frame_57 = QFrame(self.widget_10)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setGeometry(QRect(-10, 210, 252, 48))
        self.frame_57.setMaximumSize(QSize(16777213, 48))
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_159 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_159.setSpacing(0)
        self.horizontalLayout_159.setObjectName(u"horizontalLayout_159")
        self.horizontalLayout_159.setContentsMargins(3, 0, 0, 0)
        self.panelsBackground_96 = QFrame(self.frame_57)
        self.panelsBackground_96.setObjectName(u"panelsBackground_96")
        self.panelsBackground_96.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_96.setStyleSheet(u"")
        self.panelsBackground_96.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_96.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_160 = QHBoxLayout(self.panelsBackground_96)
        self.horizontalLayout_160.setObjectName(u"horizontalLayout_160")
        self.label_73 = QLabel(self.panelsBackground_96)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_160.addWidget(self.label_73)


        self.horizontalLayout_159.addWidget(self.panelsBackground_96)

        self.panelsBackground_97 = QFrame(self.frame_57)
        self.panelsBackground_97.setObjectName(u"panelsBackground_97")
        self.panelsBackground_97.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_97.setStyleSheet(u"")
        self.panelsBackground_97.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_97.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_161 = QHBoxLayout(self.panelsBackground_97)
        self.horizontalLayout_161.setObjectName(u"horizontalLayout_161")
        self.controllerBorderColor1 = QPushButton(self.panelsBackground_97)
        self.controllerBorderColor1.setObjectName(u"controllerBorderColor1")
        self.controllerBorderColor1.setMinimumSize(QSize(24, 24))
        self.controllerBorderColor1.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_161.addWidget(self.controllerBorderColor1)

        self.controllerBorderColor2 = QPushButton(self.panelsBackground_97)
        self.controllerBorderColor2.setObjectName(u"controllerBorderColor2")
        self.controllerBorderColor2.setMinimumSize(QSize(24, 24))
        self.controllerBorderColor2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_161.addWidget(self.controllerBorderColor2)

        self.controllerBorderColor3 = QPushButton(self.panelsBackground_97)
        self.controllerBorderColor3.setObjectName(u"controllerBorderColor3")
        self.controllerBorderColor3.setMinimumSize(QSize(24, 24))
        self.controllerBorderColor3.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_161.addWidget(self.controllerBorderColor3)

        self.controllerBorderColor4 = QPushButton(self.panelsBackground_97)
        self.controllerBorderColor4.setObjectName(u"controllerBorderColor4")
        self.controllerBorderColor4.setMinimumSize(QSize(24, 24))
        self.controllerBorderColor4.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_161.addWidget(self.controllerBorderColor4)


        self.horizontalLayout_159.addWidget(self.panelsBackground_97)

        self.frame_58 = QFrame(self.widget_10)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setGeometry(QRect(-10, 260, 252, 48))
        self.frame_58.setMaximumSize(QSize(16777213, 48))
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_162 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_162.setSpacing(0)
        self.horizontalLayout_162.setObjectName(u"horizontalLayout_162")
        self.horizontalLayout_162.setContentsMargins(3, 0, 0, 0)
        self.panelsBackground_98 = QFrame(self.frame_58)
        self.panelsBackground_98.setObjectName(u"panelsBackground_98")
        self.panelsBackground_98.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_98.setStyleSheet(u"")
        self.panelsBackground_98.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_98.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_163 = QHBoxLayout(self.panelsBackground_98)
        self.horizontalLayout_163.setObjectName(u"horizontalLayout_163")
        self.label_74 = QLabel(self.panelsBackground_98)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_163.addWidget(self.label_74)


        self.horizontalLayout_162.addWidget(self.panelsBackground_98)

        self.panelsBackground_99 = QFrame(self.frame_58)
        self.panelsBackground_99.setObjectName(u"panelsBackground_99")
        self.panelsBackground_99.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_99.setStyleSheet(u"")
        self.panelsBackground_99.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_99.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_164 = QHBoxLayout(self.panelsBackground_99)
        self.horizontalLayout_164.setObjectName(u"horizontalLayout_164")
        self.controllerFirst_textColor1 = QPushButton(self.panelsBackground_99)
        self.controllerFirst_textColor1.setObjectName(u"controllerFirst_textColor1")
        self.controllerFirst_textColor1.setMinimumSize(QSize(24, 24))
        self.controllerFirst_textColor1.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_164.addWidget(self.controllerFirst_textColor1)

        self.controllerFirst_textColor2 = QPushButton(self.panelsBackground_99)
        self.controllerFirst_textColor2.setObjectName(u"controllerFirst_textColor2")
        self.controllerFirst_textColor2.setMinimumSize(QSize(24, 24))
        self.controllerFirst_textColor2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_164.addWidget(self.controllerFirst_textColor2)

        self.controllerFirst_textColor3 = QPushButton(self.panelsBackground_99)
        self.controllerFirst_textColor3.setObjectName(u"controllerFirst_textColor3")
        self.controllerFirst_textColor3.setMinimumSize(QSize(24, 24))
        self.controllerFirst_textColor3.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_164.addWidget(self.controllerFirst_textColor3)

        self.controllerFirst_textColor4 = QPushButton(self.panelsBackground_99)
        self.controllerFirst_textColor4.setObjectName(u"controllerFirst_textColor4")
        self.controllerFirst_textColor4.setMinimumSize(QSize(24, 24))
        self.controllerFirst_textColor4.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_164.addWidget(self.controllerFirst_textColor4)


        self.horizontalLayout_162.addWidget(self.panelsBackground_99)

        self.frame_59 = QFrame(self.widget_10)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setGeometry(QRect(-10, 310, 252, 48))
        self.frame_59.setMaximumSize(QSize(16777213, 48))
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_165 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_165.setSpacing(0)
        self.horizontalLayout_165.setObjectName(u"horizontalLayout_165")
        self.horizontalLayout_165.setContentsMargins(3, 0, 0, 0)
        self.panelsBackground_100 = QFrame(self.frame_59)
        self.panelsBackground_100.setObjectName(u"panelsBackground_100")
        self.panelsBackground_100.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_100.setStyleSheet(u"")
        self.panelsBackground_100.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_100.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_166 = QHBoxLayout(self.panelsBackground_100)
        self.horizontalLayout_166.setObjectName(u"horizontalLayout_166")
        self.label_75 = QLabel(self.panelsBackground_100)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_166.addWidget(self.label_75)


        self.horizontalLayout_165.addWidget(self.panelsBackground_100)

        self.panelsBackground_101 = QFrame(self.frame_59)
        self.panelsBackground_101.setObjectName(u"panelsBackground_101")
        self.panelsBackground_101.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_101.setStyleSheet(u"")
        self.panelsBackground_101.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_101.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_167 = QHBoxLayout(self.panelsBackground_101)
        self.horizontalLayout_167.setObjectName(u"horizontalLayout_167")
        self.controllerSecond_textColor1 = QPushButton(self.panelsBackground_101)
        self.controllerSecond_textColor1.setObjectName(u"controllerSecond_textColor1")
        self.controllerSecond_textColor1.setMinimumSize(QSize(24, 24))
        self.controllerSecond_textColor1.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_167.addWidget(self.controllerSecond_textColor1)

        self.controllerSecond_textColor2 = QPushButton(self.panelsBackground_101)
        self.controllerSecond_textColor2.setObjectName(u"controllerSecond_textColor2")
        self.controllerSecond_textColor2.setMinimumSize(QSize(24, 24))
        self.controllerSecond_textColor2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_167.addWidget(self.controllerSecond_textColor2)

        self.controllerSecond_textColor3 = QPushButton(self.panelsBackground_101)
        self.controllerSecond_textColor3.setObjectName(u"controllerSecond_textColor3")
        self.controllerSecond_textColor3.setMinimumSize(QSize(24, 24))
        self.controllerSecond_textColor3.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_167.addWidget(self.controllerSecond_textColor3)

        self.controllerSecond_textColor4 = QPushButton(self.panelsBackground_101)
        self.controllerSecond_textColor4.setObjectName(u"controllerSecond_textColor4")
        self.controllerSecond_textColor4.setMinimumSize(QSize(24, 24))
        self.controllerSecond_textColor4.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_167.addWidget(self.controllerSecond_textColor4)


        self.horizontalLayout_165.addWidget(self.panelsBackground_101)

        self.frame_60 = QFrame(self.widget_10)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setGeometry(QRect(-10, 360, 252, 48))
        self.frame_60.setMaximumSize(QSize(16777213, 48))
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_168 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_168.setSpacing(0)
        self.horizontalLayout_168.setObjectName(u"horizontalLayout_168")
        self.horizontalLayout_168.setContentsMargins(3, 0, 0, 0)
        self.panelsBackground_102 = QFrame(self.frame_60)
        self.panelsBackground_102.setObjectName(u"panelsBackground_102")
        self.panelsBackground_102.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_102.setStyleSheet(u"")
        self.panelsBackground_102.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_102.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_169 = QHBoxLayout(self.panelsBackground_102)
        self.horizontalLayout_169.setObjectName(u"horizontalLayout_169")
        self.label_76 = QLabel(self.panelsBackground_102)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_169.addWidget(self.label_76)


        self.horizontalLayout_168.addWidget(self.panelsBackground_102)

        self.panelsBackground_103 = QFrame(self.frame_60)
        self.panelsBackground_103.setObjectName(u"panelsBackground_103")
        self.panelsBackground_103.setMaximumSize(QSize(16777215, 40))
        self.panelsBackground_103.setStyleSheet(u"")
        self.panelsBackground_103.setFrameShape(QFrame.StyledPanel)
        self.panelsBackground_103.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_170 = QHBoxLayout(self.panelsBackground_103)
        self.horizontalLayout_170.setObjectName(u"horizontalLayout_170")
        self.controllerThird_textColor1 = QPushButton(self.panelsBackground_103)
        self.controllerThird_textColor1.setObjectName(u"controllerThird_textColor1")
        self.controllerThird_textColor1.setMinimumSize(QSize(24, 24))
        self.controllerThird_textColor1.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_170.addWidget(self.controllerThird_textColor1)

        self.controllerThird_textColor2 = QPushButton(self.panelsBackground_103)
        self.controllerThird_textColor2.setObjectName(u"controllerThird_textColor2")
        self.controllerThird_textColor2.setMinimumSize(QSize(24, 24))
        self.controllerThird_textColor2.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_170.addWidget(self.controllerThird_textColor2)

        self.controllerThird_textColor3 = QPushButton(self.panelsBackground_103)
        self.controllerThird_textColor3.setObjectName(u"controllerThird_textColor3")
        self.controllerThird_textColor3.setMinimumSize(QSize(24, 24))
        self.controllerThird_textColor3.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_170.addWidget(self.controllerThird_textColor3)

        self.controllerThird_textColor4 = QPushButton(self.panelsBackground_103)
        self.controllerThird_textColor4.setObjectName(u"controllerThird_textColor4")
        self.controllerThird_textColor4.setMinimumSize(QSize(24, 24))
        self.controllerThird_textColor4.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_170.addWidget(self.controllerThird_textColor4)


        self.horizontalLayout_168.addWidget(self.panelsBackground_103)

        self.toolBox.addItem(self.page_4, u"Controllers")

        self.verticalLayout_22.addWidget(self.toolBox)

        self.themingsTabs.addTab(self.appTheming, "")
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
        self.scrollAreaWidgetContents2.setGeometry(QRect(0, 0, 270, 726))
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
        self.footerLabel = QFrame(self.mainFooter)
        self.footerLabel.setObjectName(u"footerLabel")
        self.footerLabel.setFrameShape(QFrame.StyledPanel)
        self.footerLabel.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.footerLabel)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(12, 0, 0, 0)
        self.autor = QLabel(self.footerLabel)
        self.autor.setObjectName(u"autor")

        self.horizontalLayout_11.addWidget(self.autor)


        self.horizontalLayout_7.addWidget(self.footerLabel)

        self.loadingFrame = QFrame(self.mainFooter)
        self.loadingFrame.setObjectName(u"loadingFrame")
        self.loadingFrame.setFrameShape(QFrame.StyledPanel)
        self.loadingFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.loadingFrame)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.loadingLabel = QLabel(self.loadingFrame)
        self.loadingLabel.setObjectName(u"loadingLabel")

        self.horizontalLayout_12.addWidget(self.loadingLabel)


        self.horizontalLayout_7.addWidget(self.loadingFrame)

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
        self.themingsTabs.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        self.panelSettings4.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionvvv.setText(QCoreApplication.translate("MainWindow", u"vvv", None))
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
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Main Background", None))
        self.headerMainColor1.setText("")
        self.headerMainColor2.setText("")
        self.headerMainColor3.setText("")
        self.headerMainColor4.setText("")
        self.headerMainColor5.setText("")
        self.headerMainColor6.setText("")
        self.headerMainColor7.setText("")
        self.headerMainColor8.setText("")
        self.headerMainColor9.setText("")
        self.headerMainColor10.setText("")
        self.headerMainColor11.setText("")
        self.headerMainColor12.setText("")
        self.headerMainColor13.setText("")
        self.headerMainColor14.setText("")
        self.headerMainColor15.setText("")
        self.headerMainColor16.setText("")
        self.headerMainColor17.setText("")
        self.headerMainColor18.setText("")
        self.headerMainColor19.setText("")
        self.headerMainColor20.setText("")
        self.headerMainColor21.setText("")
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Hover", None))
        self.headerHoverColor1.setText("")
        self.headerHoverColor2.setText("")
        self.headerHoverColor3.setText("")
        self.headerHoverColor4.setText("")
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Border", None))
        self.headerBorderColor1.setText("")
        self.headerBorderColor2.setText("")
        self.headerBorderColor3.setText("")
        self.headerBorderColor4.setText("")
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Text1", None))
        self.headerFirst_textColor1.setText("")
        self.headerFirst_textColor2.setText("")
        self.headerFirst_textColor3.setText("")
        self.headerFirst_textColor4.setText("")
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Text2", None))
        self.headerSecond_textColor1.setText("")
        self.headerSecond_textColor2.setText("")
        self.headerSecond_textColor3.setText("")
        self.headerSecond_textColor4.setText("")
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Text3", None))
        self.headerThird_textColor1.setText("")
        self.headerThird_textColor2.setText("")
        self.headerThird_textColor3.setText("")
        self.headerThird_textColor4.setText("")
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Header", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Main Background", None))
        self.contentMainColor1.setText("")
        self.contentMainColor2.setText("")
        self.contentMainColor3.setText("")
        self.contentMainColor4.setText("")
        self.contentMainColor5.setText("")
        self.contentMainColor6.setText("")
        self.contentMainColor7.setText("")
        self.contentMainColor8.setText("")
        self.contentMainColor9.setText("")
        self.contentMainColor10.setText("")
        self.contentMainColor11.setText("")
        self.contentMainColor12.setText("")
        self.contentMainColor13.setText("")
        self.contentMainColor14.setText("")
        self.contentMainColor15.setText("")
        self.contentMainColor16.setText("")
        self.contentMainColor17.setText("")
        self.contentMainColor18.setText("")
        self.contentMainColor19.setText("")
        self.contentMainColor20.setText("")
        self.contentMainColor21.setText("")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Header", None))
        self.contentHeaderColor1.setText("")
        self.contentHeaderColor2.setText("")
        self.contentHeaderColor3.setText("")
        self.contentHeaderColor4.setText("")
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Footer", None))
        self.contentFooterColor1.setText("")
        self.contentFooterColor2.setText("")
        self.contentFooterColor3.setText("")
        self.contentFooterColor4.setText("")
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Border", None))
        self.contentBorderColor1.setText("")
        self.contentBorderColor2.setText("")
        self.contentBorderColor3.setText("")
        self.contentBorderColor4.setText("")
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Hover", None))
        self.contentHoverColor1.setText("")
        self.contentHoverColor2.setText("")
        self.contentHoverColor3.setText("")
        self.contentHoverColor4.setText("")
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Text1", None))
        self.contentFirst_textColor1.setText("")
        self.contentFirst_textColor2.setText("")
        self.contentFirst_textColor3.setText("")
        self.contentFirst_textColor4.setText("")
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Text2", None))
        self.contentSecond_textColor1.setText("")
        self.contentSecond_textColor2.setText("")
        self.contentSecond_textColor3.setText("")
        self.contentSecond_textColor4.setText("")
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Text3", None))
        self.contentThird_textColor1.setText("")
        self.contentThird_textColor2.setText("")
        self.contentThird_textColor3.setText("")
        self.contentThird_textColor4.setText("")
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Content", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Main Background", None))
        self.footerMainColor1.setText("")
        self.footerMainColor2.setText("")
        self.footerMainColor3.setText("")
        self.footerMainColor4.setText("")
        self.footerMainColor5.setText("")
        self.footerMainColor6.setText("")
        self.footerMainColor7.setText("")
        self.footerMainColor8.setText("")
        self.footerMainColor9.setText("")
        self.footerMainColor10.setText("")
        self.footerMainColor11.setText("")
        self.footerMainColor12.setText("")
        self.footerMainColor13.setText("")
        self.footerMainColor14.setText("")
        self.footerMainColor15.setText("")
        self.footerMainColor16.setText("")
        self.footerMainColor17.setText("")
        self.footerMainColor18.setText("")
        self.footerMainColor19.setText("")
        self.footerMainColor20.setText("")
        self.footerMainColor21.setText("")
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Hover", None))
        self.footerHoverColor1.setText("")
        self.footerHoverColor2.setText("")
        self.footerHoverColor3.setText("")
        self.footerHoverColor4.setText("")
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Border", None))
        self.footerBorderColor1.setText("")
        self.footerBorderColor2.setText("")
        self.footerBorderColor3.setText("")
        self.footerBorderColor4.setText("")
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Text1", None))
        self.footerFirst_textColor1.setText("")
        self.footerFirst_textColor2.setText("")
        self.footerFirst_textColor3.setText("")
        self.footerFirst_textColor4.setText("")
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Text2", None))
        self.footerSecond_textColor1.setText("")
        self.footerSecond_textColor2.setText("")
        self.footerSecond_textColor3.setText("")
        self.footerSecond_textColor4.setText("")
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Text3", None))
        self.footerThird_textColor1.setText("")
        self.footerThird_textColor2.setText("")
        self.footerThird_textColor3.setText("")
        self.footerThird_textColor4.setText("")
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"Footer", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Main Background", None))
        self.controllerMainColor1.setText("")
        self.controllerMainColor2.setText("")
        self.controllerMainColor3.setText("")
        self.controllerMainColor4.setText("")
        self.controllerMainColor5.setText("")
        self.controllerMainColor6.setText("")
        self.controllerMainColor7.setText("")
        self.controllerMainColor8.setText("")
        self.controllerMainColor9.setText("")
        self.controllerMainColor10.setText("")
        self.controllerMainColor11.setText("")
        self.controllerMainColor12.setText("")
        self.controllerMainColor13.setText("")
        self.controllerMainColor14.setText("")
        self.controllerMainColor15.setText("")
        self.controllerMainColor16.setText("")
        self.controllerMainColor17.setText("")
        self.controllerMainColor18.setText("")
        self.controllerMainColor19.setText("")
        self.controllerMainColor20.setText("")
        self.controllerMainColor21.setText("")
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Hover", None))
        self.controllerHoverColor1.setText("")
        self.controllerHoverColor2.setText("")
        self.controllerHoverColor3.setText("")
        self.controllerHoverColor4.setText("")
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Border", None))
        self.controllerBorderColor1.setText("")
        self.controllerBorderColor2.setText("")
        self.controllerBorderColor3.setText("")
        self.controllerBorderColor4.setText("")
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Text1", None))
        self.controllerFirst_textColor1.setText("")
        self.controllerFirst_textColor2.setText("")
        self.controllerFirst_textColor3.setText("")
        self.controllerFirst_textColor4.setText("")
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Text2", None))
        self.controllerSecond_textColor1.setText("")
        self.controllerSecond_textColor2.setText("")
        self.controllerSecond_textColor3.setText("")
        self.controllerSecond_textColor4.setText("")
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Text3", None))
        self.controllerThird_textColor1.setText("")
        self.controllerThird_textColor2.setText("")
        self.controllerThird_textColor3.setText("")
        self.controllerThird_textColor4.setText("")
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"Controllers", None))
        self.themingsTabs.setTabText(self.themingsTabs.indexOf(self.appTheming), QCoreApplication.translate("MainWindow", u"Theming", None))
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
        self.autor.setText(QCoreApplication.translate("MainWindow", u"autor", None))
        self.loadingLabel.setText(QCoreApplication.translate("MainWindow", u"Loading ...", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.pushButton_6.setText("")
    # retranslateUi

