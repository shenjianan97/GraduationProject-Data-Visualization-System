# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_DataVisualizationWin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DataVisualizationWin(object):
    def setupUi(self, DataVisualizationWin):
        DataVisualizationWin.setObjectName("DataVisualizationWin")
        DataVisualizationWin.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(DataVisualizationWin)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 220, 71, 51))
        self.label.setObjectName("label")
        DataVisualizationWin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DataVisualizationWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        DataVisualizationWin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DataVisualizationWin)
        self.statusbar.setObjectName("statusbar")
        DataVisualizationWin.setStatusBar(self.statusbar)

        self.retranslateUi(DataVisualizationWin)
        QtCore.QMetaObject.connectSlotsByName(DataVisualizationWin)

    def retranslateUi(self, DataVisualizationWin):
        _translate = QtCore.QCoreApplication.translate
        DataVisualizationWin.setWindowTitle(_translate("DataVisualizationWin", "数据可视化"))
        self.label.setText(_translate("DataVisualizationWin", "数据可视化"))

