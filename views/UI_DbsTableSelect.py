# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_DbsTableSelect.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DbsTableSelect(object):
    def setupUi(self, DbsTableSelect):
        DbsTableSelect.setObjectName("DbsTableSelect")
        DbsTableSelect.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DbsTableSelect.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(DbsTableSelect)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(DbsTableSelect)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.tableNamesWidget = QtWidgets.QListWidget(DbsTableSelect)
        self.tableNamesWidget.setDragEnabled(True)
        self.tableNamesWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.tableNamesWidget.setObjectName("tableNamesWidget")
        self.verticalLayout_6.addWidget(self.tableNamesWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.refreshButton = QtWidgets.QPushButton(DbsTableSelect)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.refreshButton.setFont(font)
        self.refreshButton.setObjectName("refreshButton")
        self.horizontalLayout_2.addWidget(self.refreshButton)
        self.chooseButton = QtWidgets.QPushButton(DbsTableSelect)
        self.chooseButton.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.chooseButton.setFont(font)
        self.chooseButton.setObjectName("chooseButton")
        self.horizontalLayout_2.addWidget(self.chooseButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.Add_Excel_Button = QtWidgets.QPushButton(DbsTableSelect)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.Add_Excel_Button.setFont(font)
        self.Add_Excel_Button.setObjectName("Add_Excel_Button")
        self.horizontalLayout_5.addWidget(self.Add_Excel_Button)
        self.Add_JSON_Button = QtWidgets.QPushButton(DbsTableSelect)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.Add_JSON_Button.setFont(font)
        self.Add_JSON_Button.setObjectName("Add_JSON_Button")
        self.horizontalLayout_5.addWidget(self.Add_JSON_Button)
        self.Add_CSV_Button = QtWidgets.QPushButton(DbsTableSelect)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.Add_CSV_Button.setFont(font)
        self.Add_CSV_Button.setObjectName("Add_CSV_Button")
        self.horizontalLayout_5.addWidget(self.Add_CSV_Button)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.line = QtWidgets.QFrame(DbsTableSelect)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_6.addWidget(self.line)
        self.verticalLayout_6.setStretch(1, 1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(DbsTableSelect)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.tableView = QtWidgets.QTableView(DbsTableSelect)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setVisible(True)
        self.tableView.horizontalHeader().setSortIndicatorShown(False)
        self.tableView.verticalHeader().setVisible(False)
        self.verticalLayout_5.addWidget(self.tableView)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButton = QtWidgets.QPushButton(DbsTableSelect)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignBottom)
        spacerItem5 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(DbsTableSelect)
        self.pushButton.clicked.connect(DbsTableSelect.backClicked)
        self.tableNamesWidget.itemClicked['QListWidgetItem*'].connect(DbsTableSelect.tableSelected)
        self.refreshButton.clicked.connect(DbsTableSelect.refreshClicked)
        self.chooseButton.clicked.connect(DbsTableSelect.chooseClicked)
        self.Add_Excel_Button.clicked.connect(DbsTableSelect.addExcel)
        self.Add_JSON_Button.clicked.connect(DbsTableSelect.addJSON)
        self.Add_CSV_Button.clicked.connect(DbsTableSelect.addCSV)
        QtCore.QMetaObject.connectSlotsByName(DbsTableSelect)

    def retranslateUi(self, DbsTableSelect):
        _translate = QtCore.QCoreApplication.translate
        DbsTableSelect.setWindowTitle(_translate("DbsTableSelect", "Choose Tables"))
        self.label.setText(_translate("DbsTableSelect", "Select Tables"))
        self.refreshButton.setText(_translate("DbsTableSelect", "Refresh"))
        self.chooseButton.setText(_translate("DbsTableSelect", "Choose"))
        self.Add_Excel_Button.setText(_translate("DbsTableSelect", "Add Excel"))
        self.Add_JSON_Button.setText(_translate("DbsTableSelect", "Add JSON"))
        self.Add_CSV_Button.setText(_translate("DbsTableSelect", "Add CSV"))
        self.label_2.setText(_translate("DbsTableSelect", "Table Content Preview"))
        self.pushButton.setText(_translate("DbsTableSelect", "Back"))


