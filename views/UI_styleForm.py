# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_styleForm.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_styleForm(object):
    def setupUi(self, styleForm):
        styleForm.setObjectName("styleForm")
        styleForm.resize(256, 300)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(styleForm)
        self.verticalLayout_2.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolBox = QtWidgets.QToolBox(styleForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.toolBox.setMinimumSize(QtCore.QSize(250, 0))
        self.toolBox.setMaximumSize(QtCore.QSize(250, 16777215))
        self.toolBox.setObjectName("toolBox")
        self.page_title = QtWidgets.QWidget()
        self.page_title.setGeometry(QtCore.QRect(0, 0, 250, 184))
        self.page_title.setObjectName("page_title")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.page_title)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.page_title)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.page_title)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.page_title)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.lineEdit_title_content = QtWidgets.QLineEdit(self.page_title)
        self.lineEdit_title_content.setEnabled(False)
        self.lineEdit_title_content.setObjectName("lineEdit_title_content")
        self.gridLayout.addWidget(self.lineEdit_title_content, 1, 1, 1, 1)
        self.pushButton_title_pallet = QtWidgets.QPushButton(self.page_title)
        self.pushButton_title_pallet.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_title_pallet.setObjectName("pushButton_title_pallet")
        self.gridLayout.addWidget(self.pushButton_title_pallet, 0, 2, 1, 1)
        self.lineEdit_title_color = QtWidgets.QLineEdit(self.page_title)
        self.lineEdit_title_color.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_title_color.sizePolicy().hasHeightForWidth())
        self.lineEdit_title_color.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_title_color.setFont(font)
        self.lineEdit_title_color.setObjectName("lineEdit_title_color")
        self.gridLayout.addWidget(self.lineEdit_title_color, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.page_title)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox_title_enable = QtWidgets.QComboBox(self.page_title)
        self.comboBox_title_enable.setObjectName("comboBox_title_enable")
        self.comboBox_title_enable.addItem("")
        self.comboBox_title_enable.addItem("")
        self.gridLayout.addWidget(self.comboBox_title_enable, 2, 1, 1, 2)
        self.gridLayout.setColumnStretch(1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.toolBox.addItem(self.page_title, "")
        self.page_legend = QtWidgets.QWidget()
        self.page_legend.setGeometry(QtCore.QRect(0, 0, 250, 184))
        self.page_legend.setObjectName("page_legend")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page_legend)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.page_legend)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.page_legend)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.comboBox_legend_enable = QtWidgets.QComboBox(self.page_legend)
        self.comboBox_legend_enable.setObjectName("comboBox_legend_enable")
        self.comboBox_legend_enable.addItem("")
        self.comboBox_legend_enable.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_legend_enable, 1, 1, 1, 2)
        self.comboBox_legend_position = QtWidgets.QComboBox(self.page_legend)
        self.comboBox_legend_position.setObjectName("comboBox_legend_position")
        self.comboBox_legend_position.addItem("")
        self.comboBox_legend_position.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_legend_position, 0, 1, 1, 2)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.toolBox.addItem(self.page_legend, "")
        self.page_background = QtWidgets.QWidget()
        self.page_background.setGeometry(QtCore.QRect(0, 0, 250, 184))
        self.page_background.setObjectName("page_background")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.page_background)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.page_background)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.pushButton_background_pallet = QtWidgets.QPushButton(self.page_background)
        self.pushButton_background_pallet.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_background_pallet.setObjectName("pushButton_background_pallet")
        self.gridLayout_3.addWidget(self.pushButton_background_pallet, 0, 2, 1, 1)
        self.lineEdit_background_color = QtWidgets.QLineEdit(self.page_background)
        self.lineEdit_background_color.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_background_color.sizePolicy().hasHeightForWidth())
        self.lineEdit_background_color.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_background_color.setFont(font)
        self.lineEdit_background_color.setObjectName("lineEdit_background_color")
        self.gridLayout_3.addWidget(self.lineEdit_background_color, 0, 1, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_3)
        self.toolBox.addItem(self.page_background, "")
        self.verticalLayout.addWidget(self.toolBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(styleForm)
        self.toolBox.setCurrentIndex(0)
        self.pushButton_2.clicked.connect(styleForm.set_title_content_enable)
        self.lineEdit_title_content.returnPressed.connect(styleForm.title_content_clicked)
        self.pushButton_title_pallet.clicked.connect(styleForm.title_color_pallet)
        self.pushButton_background_pallet.clicked.connect(styleForm.background_color_pallet)
        QtCore.QMetaObject.connectSlotsByName(styleForm)

    def retranslateUi(self, styleForm):
        _translate = QtCore.QCoreApplication.translate
        styleForm.setWindowTitle(_translate("styleForm", "Form"))
        self.label_5.setText(_translate("styleForm", "Content"))
        self.pushButton_2.setText(_translate("styleForm", "Modify"))
        self.label_6.setText(_translate("styleForm", "Display"))
        self.pushButton_title_pallet.setText(_translate("styleForm", "Pallet"))
        self.label.setText(_translate("styleForm", "Color"))
        self.comboBox_title_enable.setItemText(0, _translate("styleForm", "yes"))
        self.comboBox_title_enable.setItemText(1, _translate("styleForm", "no"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_title), _translate("styleForm", "Title"))
        self.label_4.setText(_translate("styleForm", "Display"))
        self.label_2.setText(_translate("styleForm", "Position"))
        self.comboBox_legend_enable.setItemText(0, _translate("styleForm", "yes"))
        self.comboBox_legend_enable.setItemText(1, _translate("styleForm", "no"))
        self.comboBox_legend_position.setItemText(0, _translate("styleForm", "upper right"))
        self.comboBox_legend_position.setItemText(1, _translate("styleForm", "upper left"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_legend), _translate("styleForm", "Legend"))
        self.label_3.setText(_translate("styleForm", "Color"))
        self.pushButton_background_pallet.setText(_translate("styleForm", "Pallet"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_background), _translate("styleForm", "Background"))


