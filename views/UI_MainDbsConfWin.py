# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_MainDbsConfWin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainDbsConfWin(object):
    def setupUi(self, MainDbsConfWin):
        MainDbsConfWin.setObjectName("MainDbsConfWin")
        MainDbsConfWin.resize(664, 570)
        self.centralwidget = QtWidgets.QWidget(MainDbsConfWin)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(10, -1, 10, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 1, 6, 1)
        self.editButton = QtWidgets.QPushButton(self.centralwidget)
        self.editButton.setEnabled(False)
        self.editButton.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.editButton.setFont(font)
        self.editButton.setObjectName("editButton")
        self.gridLayout.addWidget(self.editButton, 4, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 6, 2, 1, 1)
        self.title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setEnabled(False)
        self.deleteButton.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.deleteButton.setFont(font)
        self.deleteButton.setObjectName("deleteButton")
        self.gridLayout.addWidget(self.deleteButton, 5, 2, 1, 1)
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setEnabled(False)
        self.connectButton.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.connectButton.setFont(font)
        self.connectButton.setObjectName("connectButton")
        self.gridLayout.addWidget(self.connectButton, 2, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 7, 2, 1, 1)
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 3, 2, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 1, 0, 6, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setMinimumSize(QtCore.QSize(0, 0))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.databaseNameLine = QtWidgets.QLineEdit(self.centralwidget)
        self.databaseNameLine.setEnabled(False)
        self.databaseNameLine.setObjectName("databaseNameLine")
        self.gridLayout_2.addWidget(self.databaseNameLine, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 4, 0, 1, 1, QtCore.Qt.AlignRight)
        self.userLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.userLabel.setFont(font)
        self.userLabel.setObjectName("userLabel")
        self.gridLayout_2.addWidget(self.userLabel, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        self.hostLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.hostLabel.setFont(font)
        self.hostLabel.setObjectName("hostLabel")
        self.gridLayout_2.addWidget(self.hostLabel, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.gridLayout_2.addWidget(self.passwordLabel, 3, 0, 1, 1, QtCore.Qt.AlignRight)
        self.userLine = QtWidgets.QLineEdit(self.centralwidget)
        self.userLine.setEnabled(False)
        self.userLine.setReadOnly(False)
        self.userLine.setObjectName("userLine")
        self.gridLayout_2.addWidget(self.userLine, 2, 1, 1, 1)
        self.portLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.portLabel.setFont(font)
        self.portLabel.setObjectName("portLabel")
        self.gridLayout_2.addWidget(self.portLabel, 1, 0, 1, 1, QtCore.Qt.AlignRight)
        self.passwordLine = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordLine.setEnabled(False)
        self.passwordLine.setReadOnly(False)
        self.passwordLine.setObjectName("passwordLine")
        self.gridLayout_2.addWidget(self.passwordLine, 3, 1, 1, 1)
        self.hostLine = QtWidgets.QLineEdit(self.centralwidget)
        self.hostLine.setEnabled(False)
        self.hostLine.setReadOnly(False)
        self.hostLine.setObjectName("hostLine")
        self.gridLayout_2.addWidget(self.hostLine, 0, 1, 1, 1)
        self.portLine = QtWidgets.QLineEdit(self.centralwidget)
        self.portLine.setEnabled(False)
        self.portLine.setReadOnly(False)
        self.portLine.setObjectName("portLine")
        self.gridLayout_2.addWidget(self.portLine, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 5, 0, 1, 1, QtCore.Qt.AlignRight)
        self.typeComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.typeComboBox.setEnabled(False)
        self.typeComboBox.setObjectName("typeComboBox")
        self.gridLayout_2.addWidget(self.typeComboBox, 5, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 0, 2, 6, 1)
        self.gridLayout_2.setColumnStretch(0, 4)
        self.gridLayout_2.setColumnStretch(1, 16)
        self.gridLayout_2.setColumnStretch(2, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainDbsConfWin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainDbsConfWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 664, 22))
        self.menubar.setObjectName("menubar")
        MainDbsConfWin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainDbsConfWin)
        self.statusbar.setObjectName("statusbar")
        MainDbsConfWin.setStatusBar(self.statusbar)

        self.retranslateUi(MainDbsConfWin)
        self.connectButton.clicked.connect(MainDbsConfWin.connectClicked)
        self.editButton.clicked.connect(MainDbsConfWin.editClicked)
        self.deleteButton.clicked.connect(MainDbsConfWin.deleteClicked)
        self.hostLine.returnPressed.connect(MainDbsConfWin.saveDatabaseConf)
        self.portLine.returnPressed.connect(MainDbsConfWin.saveDatabaseConf)
        self.userLine.returnPressed.connect(MainDbsConfWin.saveDatabaseConf)
        self.passwordLine.returnPressed.connect(MainDbsConfWin.saveDatabaseConf)
        self.addButton.clicked.connect(MainDbsConfWin.addClicked)
        self.listWidget.itemClicked['QListWidgetItem*'].connect(MainDbsConfWin.listClicked)
        self.listWidget.itemDoubleClicked['QListWidgetItem*'].connect(MainDbsConfWin.listDoubleClicked)
        self.databaseNameLine.returnPressed.connect(MainDbsConfWin.saveDatabaseConf)
        self.typeComboBox.activated['int'].connect(MainDbsConfWin.saveDatabaseConf)
        QtCore.QMetaObject.connectSlotsByName(MainDbsConfWin)

    def retranslateUi(self, MainDbsConfWin):
        _translate = QtCore.QCoreApplication.translate
        MainDbsConfWin.setWindowTitle(_translate("MainDbsConfWin", "数据库配置"))
        self.editButton.setText(_translate("MainDbsConfWin", "EDIT"))
        self.title.setText(_translate("MainDbsConfWin", "数据库"))
        self.deleteButton.setText(_translate("MainDbsConfWin", "DELETE"))
        self.connectButton.setText(_translate("MainDbsConfWin", "CONNECT"))
        self.addButton.setText(_translate("MainDbsConfWin", "ADD"))
        self.label.setText(_translate("MainDbsConfWin", "DatabaseName"))
        self.userLabel.setText(_translate("MainDbsConfWin", "User"))
        self.hostLabel.setText(_translate("MainDbsConfWin", "Host"))
        self.passwordLabel.setText(_translate("MainDbsConfWin", "Password"))
        self.portLabel.setText(_translate("MainDbsConfWin", "Port"))
        self.label_2.setText(_translate("MainDbsConfWin", "DatabaseType"))

