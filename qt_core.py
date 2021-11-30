import platform
import json
import os
import sys
from functools import partial

if platform.system() == "Windows":
	#try:
	#	from PySide6.QtCore import (QCoreApplication, hhh, QTimer,
	#	QDate, QDateTime, QLocale, Slot, QRectF, QPointF,
	#	QMetaObject, QObject, QPoint, QRect, QEvent, Signal, Property, QSequentialAnimationGroup,
	#	QSize, QTime, QUrl, Qt, QPropertyAnimation, QEasingCurve, QAbstractAnimation, QParallelAnimationGroup, QPropertyAnimation)
	#	from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
	#		QFont, QFontDatabase, QGradient, QIcon, QFontMetrics,
	#		QImage, QKeySequence, QLinearGradient, QPainter, QPen, QPaintEvent,
	#		QPalette, QPixmap, QRadialGradient, QTransform, QStandardItem)
	#	from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy, QGridLayout, QLineEdit, QComboBox, QSpinBox, QDialogButtonBox,
	#		QStatusBar, QWidget, QLabel, QButtonGroup, QAbstractButton, QPushButton, QGraphicsDropShadowEffect, QSizeGrip,
	#    	QVBoxLayout, QFrame, QHBoxLayout, QCheckBox, QTreeWidgetItem, QHeaderView, QAbstractItemView, QTreeWidget, QFileSystemModel, QTreeView)
	#	from PySide6.QtUiTools import loadUiType
	#	print("Windows pyside6")
	#except:
	#	print("Windows pyside6 not found")
	#	try:
	#		from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QLocale, Slot, QRectF, QPointF, hhh, 
	#			QMetaObject, QObject, QPoint, QRect, QEvent, Signal, Property, QSequentialAnimationGroup, QTimer,
	#			QSize, QTime, QUrl, Qt, QPropertyAnimation, QEasingCurve, QAbstractAnimation, QParallelAnimationGroup, QPropertyAnimation)
	#		from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
	#			QFont, QFontDatabase, QGradient, QIcon, QFontMetrics,
	#			QImage, QKeySequence, QLinearGradient, QPainter, QPen, QPaintEvent,
	#			QPalette, QPixmap, QRadialGradient, QTransform, QStandardItem)
	#		from PySide2.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy, QGridLayout, QLineEdit, QComboBox, QSpinBox, QDialogButtonBox,
	#			QStatusBar, QWidget, QLabel, QButtonGroup, QAbstractButton, QPushButton, QGraphicsDropShadowEffect, QSizeGrip,
	#	    	QVBoxLayout, QFrame, QHBoxLayout, QCheckBox, QTreeWidgetItem, QHeaderView, QAbstractItemView, QTreeWidget, QFileSystemModel, QTreeView)
	#		from PySide2.QtUiTools import loadUiType
	#		print("Windows pyside2")
	#	except:
	#		print("Windows pyside2 not found")
	from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QLocale, pyqtSlot as Slot, QRectF, QPointF, QTimer,
		QMetaObject, QObject, QPoint, QRect, QEvent, pyqtSignal as Signal, pyqtProperty as Property, QSequentialAnimationGroup,
		QSize, QTime, QUrl, Qt, QPropertyAnimation, QEasingCurve, QAbstractAnimation, QParallelAnimationGroup, QPropertyAnimation)
	from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
		QFont, QFontDatabase, QGradient, QIcon, QFontMetrics,
		QImage, QKeySequence, QLinearGradient, QPainter, QPen, QPaintEvent,
		QPalette, QPixmap, QRadialGradient, QTransform, QStandardItem)
	from PyQt5.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy, QGridLayout, QLineEdit, QComboBox, QSpinBox, QDialogButtonBox,
		QStatusBar, QWidget, QLabel, QButtonGroup, QAbstractButton, QPushButton, QGraphicsDropShadowEffect, QSizeGrip,
		QVBoxLayout, QFrame, QHBoxLayout, QCheckBox, QTreeWidgetItem, QHeaderView, QAbstractItemView, QTreeWidget, QFileSystemModel, QTreeView)
	from PyQt5.uic import loadUiType
	print("Windows pyqt5")
else:
	from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QLocale, pyqtSlot as Slot, QRectF, QPointF, QTimer,
		QMetaObject, QObject, QPoint, QRect, QEvent, pyqtSignal as Signal, pyqtProperty as Property, QSequentialAnimationGroup,
		QSize, QTime, QUrl, Qt, QPropertyAnimation, QEasingCurve, QAbstractAnimation, QParallelAnimationGroup, QPropertyAnimation)
	from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
		QFont, QFontDatabase, QGradient, QIcon, QFontMetrics,
		QImage, QKeySequence, QLinearGradient, QPainter, QPen, QPaintEvent,
		QPalette, QPixmap, QRadialGradient, QTransform, QStandardItem)
	from PyQt5.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy, QGridLayout, QLineEdit, QComboBox, QSpinBox, QDialogButtonBox,
		QStatusBar, QWidget, QLabel, QButtonGroup, QAbstractButton, QPushButton, QGraphicsDropShadowEffect, QSizeGrip,
		QVBoxLayout, QFrame, QHBoxLayout, QCheckBox, QTreeWidgetItem, QHeaderView, QAbstractItemView, QTreeWidget, QFileSystemModel, QTreeView)
	from PyQt5.uic import loadUiType
	print("Linux pyqt5")
#from PySide6.QtSvg import QSvgWidget


