# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QHBoxLayout, QLineEdit,
    QListView, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QSplitter,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(841, 592)
        MainWindow.setTabShape(QTabWidget.Triangular)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionNoRecents = QAction(MainWindow)
        self.actionNoRecents.setObjectName(u"actionNoRecents")
        self.actionHorizontal = QAction(MainWindow)
        self.actionHorizontal.setObjectName(u"actionHorizontal")
        self.actionHorizontal.setCheckable(False)
        self.actionHorizontal.setChecked(False)
        self.actionVertical = QAction(MainWindow)
        self.actionVertical.setObjectName(u"actionVertical")
        self.actionVertical.setCheckable(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(10)
        self.splitter.setChildrenCollapsible(True)
        self.listView = QListView(self.splitter)
        self.listView.setObjectName(u"listView")
        self.splitter.addWidget(self.listView)
        self.verticalLayoutWidget = QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.graphicsView = QGraphicsView(self.verticalLayoutWidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout.addWidget(self.graphicsView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_first_layer = QPushButton(self.verticalLayoutWidget)
        self.pushButton_first_layer.setObjectName(u"pushButton_first_layer")
        self.pushButton_first_layer.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_first_layer)

        self.pushButton_prev_layer = QPushButton(self.verticalLayoutWidget)
        self.pushButton_prev_layer.setObjectName(u"pushButton_prev_layer")
        self.pushButton_prev_layer.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_prev_layer)

        self.lineEdit_layer = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_layer.setObjectName(u"lineEdit_layer")
        self.lineEdit_layer.setEnabled(True)
        self.lineEdit_layer.setMaximumSize(QSize(60, 16777215))
        self.lineEdit_layer.setCursor(QCursor(Qt.ArrowCursor))
        self.lineEdit_layer.setAlignment(Qt.AlignCenter)
        self.lineEdit_layer.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEdit_layer)

        self.pushButton_next_layer = QPushButton(self.verticalLayoutWidget)
        self.pushButton_next_layer.setObjectName(u"pushButton_next_layer")
        self.pushButton_next_layer.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_next_layer)

        self.pushButton_last_layer = QPushButton(self.verticalLayoutWidget)
        self.pushButton_last_layer.setObjectName(u"pushButton_last_layer")
        self.pushButton_last_layer.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_last_layer)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.splitter.addWidget(self.verticalLayoutWidget)

        self.horizontalLayout_2.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 841, 20))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuFile.setTearOffEnabled(False)
        self.menuOpen_Recent = QMenu(self.menuFile)
        self.menuOpen_Recent.setObjectName(u"menuOpen_Recent")
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        self.menuLayout = QMenu(self.menuOptions)
        self.menuLayout.setObjectName(u"menuLayout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.menuOpen_Recent.menuAction())
        self.menuOpen_Recent.addAction(self.actionNoRecents)
        self.menuOptions.addAction(self.menuLayout.menuAction())
        self.menuLayout.addAction(self.actionHorizontal)
        self.menuLayout.addAction(self.actionVertical)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionNoRecents.setText(QCoreApplication.translate("MainWindow", u"No Recent Files", None))
        self.actionHorizontal.setText(QCoreApplication.translate("MainWindow", u"Horizontal", None))
        self.actionVertical.setText(QCoreApplication.translate("MainWindow", u"Vertical", None))
        self.pushButton_first_layer.setText(QCoreApplication.translate("MainWindow", u"|<", None))
        self.pushButton_prev_layer.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.lineEdit_layer.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_next_layer.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.pushButton_last_layer.setText(QCoreApplication.translate("MainWindow", u">|", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuOpen_Recent.setTitle(QCoreApplication.translate("MainWindow", u"Open Recent", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.menuLayout.setTitle(QCoreApplication.translate("MainWindow", u"Layout", None))
    # retranslateUi

