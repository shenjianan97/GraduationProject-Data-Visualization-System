# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_DataVisualizationWin.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DataVisualizationWin(object):
    def setupUi(self, DataVisualizationWin):
        DataVisualizationWin.setObjectName("DataVisualizationWin")
        DataVisualizationWin.resize(1024, 768)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DataVisualizationWin.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(DataVisualizationWin)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_win = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_win.setObjectName("horizontalLayout_win")
        self.horizontalLayout_main = QtWidgets.QVBoxLayout()
        self.horizontalLayout_main.setObjectName("horizontalLayout_main")
        self.horizontalLayout_UI = QtWidgets.QHBoxLayout()
        self.horizontalLayout_UI.setObjectName("horizontalLayout_UI")
        self.verticalLayout_parameter = QtWidgets.QVBoxLayout()
        self.verticalLayout_parameter.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_parameter.setObjectName("verticalLayout_parameter")
        self.tableNameLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.tableNameLabel.setFont(font)
        self.tableNameLabel.setObjectName("tableNameLabel")
        self.verticalLayout_parameter.addWidget(self.tableNameLabel, 0, QtCore.Qt.AlignTop)
        self.line = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setBaseSize(QtCore.QSize(0, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_parameter.addWidget(self.line)
        self.verticalLayout_dimension = QtWidgets.QVBoxLayout()
        self.verticalLayout_dimension.setObjectName("verticalLayout_dimension")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_dimension.addWidget(self.label_2, 0, QtCore.Qt.AlignVCenter)
        self.listWidget_dimension = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_dimension.sizePolicy().hasHeightForWidth())
        self.listWidget_dimension.setSizePolicy(sizePolicy)
        self.listWidget_dimension.setMinimumSize(QtCore.QSize(0, 0))
        self.listWidget_dimension.setMaximumSize(QtCore.QSize(225, 16777215))
        self.listWidget_dimension.setBaseSize(QtCore.QSize(0, 0))
        self.listWidget_dimension.setDragEnabled(True)
        self.listWidget_dimension.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.listWidget_dimension.setObjectName("listWidget_dimension")
        self.verticalLayout_dimension.addWidget(self.listWidget_dimension)
        self.verticalLayout_parameter.addLayout(self.verticalLayout_dimension)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_parameter.addWidget(self.line_2)
        self.verticalLayout_indicator = QtWidgets.QVBoxLayout()
        self.verticalLayout_indicator.setObjectName("verticalLayout_indicator")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_indicator.addWidget(self.label_3, 0, QtCore.Qt.AlignVCenter)
        self.listWidget_indicator = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_indicator.sizePolicy().hasHeightForWidth())
        self.listWidget_indicator.setSizePolicy(sizePolicy)
        self.listWidget_indicator.setMaximumSize(QtCore.QSize(225, 16777215))
        self.listWidget_indicator.setDragEnabled(True)
        self.listWidget_indicator.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.listWidget_indicator.setObjectName("listWidget_indicator")
        self.verticalLayout_indicator.addWidget(self.listWidget_indicator)
        self.verticalLayout_parameter.addLayout(self.verticalLayout_indicator)
        self.horizontalLayout_UI.addLayout(self.verticalLayout_parameter)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphTypeLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.graphTypeLabel.setFont(font)
        self.graphTypeLabel.setObjectName("graphTypeLabel")
        self.verticalLayout.addWidget(self.graphTypeLabel, 0, QtCore.Qt.AlignTop)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(250, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(250, 16777215))
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 248, 350))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_graph = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_graph.setMinimumSize(QtCore.QSize(0, 350))
        self.widget_graph.setObjectName("widget_graph")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_graph)
        self.horizontalLayout_2.setContentsMargins(0, 12, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_line_chart = ClickableLabel(self.widget_graph)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_line_chart.sizePolicy().hasHeightForWidth())
        self.label_line_chart.setSizePolicy(sizePolicy)
        self.label_line_chart.setMaximumSize(QtCore.QSize(60, 60))
        self.label_line_chart.setText("")
        self.label_line_chart.setPixmap(QtGui.QPixmap("icon/line_chart.png"))
        self.label_line_chart.setScaledContents(True)
        self.label_line_chart.setObjectName("label_line_chart")
        self.gridLayout.addWidget(self.label_line_chart, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_bar_chart = ClickableLabel(self.widget_graph)
        self.label_bar_chart.setMaximumSize(QtCore.QSize(60, 60))
        self.label_bar_chart.setText("")
        self.label_bar_chart.setPixmap(QtGui.QPixmap("icon/bar_chart.png"))
        self.label_bar_chart.setScaledContents(True)
        self.label_bar_chart.setObjectName("label_bar_chart")
        self.gridLayout.addWidget(self.label_bar_chart, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_18 = ClickableLabel(self.widget_graph)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 2, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_13 = ClickableLabel(self.widget_graph)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_16 = ClickableLabel(self.widget_graph)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_pie_chart = ClickableLabel(self.widget_graph)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_pie_chart.sizePolicy().hasHeightForWidth())
        self.label_pie_chart.setSizePolicy(sizePolicy)
        self.label_pie_chart.setMaximumSize(QtCore.QSize(60, 60))
        self.label_pie_chart.setText("")
        self.label_pie_chart.setPixmap(QtGui.QPixmap("icon/pie_chart.png"))
        self.label_pie_chart.setScaledContents(True)
        self.label_pie_chart.setObjectName("label_pie_chart")
        self.gridLayout.addWidget(self.label_pie_chart, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_7 = ClickableLabel(self.widget_graph)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_histogram = ClickableLabel(self.widget_graph)
        self.label_histogram.setMaximumSize(QtCore.QSize(60, 60))
        self.label_histogram.setText("")
        self.label_histogram.setPixmap(QtGui.QPixmap("icon/histogram.png"))
        self.label_histogram.setScaledContents(True)
        self.label_histogram.setObjectName("label_histogram")
        self.gridLayout.addWidget(self.label_histogram, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_8 = ClickableLabel(self.widget_graph)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_17 = ClickableLabel(self.widget_graph)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 3, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_14 = ClickableLabel(self.widget_graph)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_9 = ClickableLabel(self.widget_graph)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(self.widget_graph)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout_2.addWidget(self.widget_graph, 0, QtCore.Qt.AlignHCenter)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_7.addLayout(self.verticalLayout)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_7.addWidget(self.line_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(250, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.property_tab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.property_tab.sizePolicy().hasHeightForWidth())
        self.property_tab.setSizePolicy(sizePolicy)
        self.property_tab.setObjectName("property_tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.property_tab)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_property = propertyForm(self.property_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_property.sizePolicy().hasHeightForWidth())
        self.widget_property.setSizePolicy(sizePolicy)
        self.widget_property.setMinimumSize(QtCore.QSize(250, 0))
        self.widget_property.setMaximumSize(QtCore.QSize(250, 16777215))
        self.widget_property.setObjectName("widget_property")
        self.verticalLayout_5.addWidget(self.widget_property, 0, QtCore.Qt.AlignHCenter)
        self.tabWidget.addTab(self.property_tab, "")
        self.style_tab = QtWidgets.QWidget()
        self.style_tab.setObjectName("style_tab")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.style_tab)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.widget_style = styleForm(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_style.sizePolicy().hasHeightForWidth())
        self.widget_style.setSizePolicy(sizePolicy)
        self.widget_style.setMinimumSize(QtCore.QSize(250, 0))
        self.widget_style.setMaximumSize(QtCore.QSize(250, 16777215))
        self.widget_style.setObjectName("widget_style")
        self.horizontalLayout_6.addWidget(self.widget_style)
        self.tabWidget.addTab(self.style_tab, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        self.verticalLayout_7.addLayout(self.verticalLayout_4)
        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(2, 1)
        self.horizontalLayout_UI.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, 5, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontal_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontal_label.sizePolicy().hasHeightForWidth())
        self.horizontal_label.setSizePolicy(sizePolicy)
        self.horizontal_label.setMinimumSize(QtCore.QSize(105, 0))
        self.horizontal_label.setMaximumSize(QtCore.QSize(105, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.horizontal_label.setFont(font)
        self.horizontal_label.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontal_label.setObjectName("horizontal_label")
        self.horizontalLayout_4.addWidget(self.horizontal_label, 0, QtCore.Qt.AlignHCenter)
        self.listWidget_horizontal = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_horizontal.sizePolicy().hasHeightForWidth())
        self.listWidget_horizontal.setSizePolicy(sizePolicy)
        self.listWidget_horizontal.setMaximumSize(QtCore.QSize(16777215, 40))
        self.listWidget_horizontal.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_horizontal.setDragDropOverwriteMode(False)
        self.listWidget_horizontal.setDragDropMode(QtWidgets.QAbstractItemView.DropOnly)
        self.listWidget_horizontal.setFlow(QtWidgets.QListView.LeftToRight)
        self.listWidget_horizontal.setObjectName("listWidget_horizontal")
        self.horizontalLayout_4.addWidget(self.listWidget_horizontal)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, 5, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.vertical_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vertical_label.sizePolicy().hasHeightForWidth())
        self.vertical_label.setSizePolicy(sizePolicy)
        self.vertical_label.setMinimumSize(QtCore.QSize(105, 0))
        self.vertical_label.setMaximumSize(QtCore.QSize(105, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.vertical_label.setFont(font)
        self.vertical_label.setAlignment(QtCore.Qt.AlignCenter)
        self.vertical_label.setObjectName("vertical_label")
        self.horizontalLayout_3.addWidget(self.vertical_label, 0, QtCore.Qt.AlignHCenter)
        self.listWidget_vertical = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_vertical.sizePolicy().hasHeightForWidth())
        self.listWidget_vertical.setSizePolicy(sizePolicy)
        self.listWidget_vertical.setMaximumSize(QtCore.QSize(16777215, 40))
        self.listWidget_vertical.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_vertical.setDragDropMode(QtWidgets.QAbstractItemView.DropOnly)
        self.listWidget_vertical.setFlow(QtWidgets.QListView.LeftToRight)
        self.listWidget_vertical.setObjectName("listWidget_vertical")
        self.horizontalLayout_3.addWidget(self.listWidget_vertical)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_6.addWidget(self.line_4)
        self.mplwidget = MplWidget(self.centralwidget)
        self.mplwidget.setObjectName("mplwidget")
        self.verticalLayout_6.addWidget(self.mplwidget)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.generateButton = QtWidgets.QPushButton(self.centralwidget)
        self.generateButton.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.generateButton.setFont(font)
        self.generateButton.setObjectName("generateButton")
        self.horizontalLayout_5.addWidget(self.generateButton)
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.saveButton.setFont(font)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout_5.addWidget(self.saveButton)
        spacerItem1 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_6.setStretch(3, 1)
        self.horizontalLayout_UI.addLayout(self.verticalLayout_6)
        self.horizontalLayout_UI.setStretch(2, 1)
        self.horizontalLayout_main.addLayout(self.horizontalLayout_UI)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")
        self.horizontalLayout.addWidget(self.backButton)
        spacerItem3 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.horizontalLayout_main.addLayout(self.horizontalLayout)
        self.horizontalLayout_win.addLayout(self.horizontalLayout_main)
        DataVisualizationWin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DataVisualizationWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 22))
        self.menubar.setObjectName("menubar")
        DataVisualizationWin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DataVisualizationWin)
        self.statusbar.setStyleSheet("QStatusBar\n"
"{\n"
"    color: rgb(255, 0, 0);\n"
"}")
        self.statusbar.setObjectName("statusbar")
        DataVisualizationWin.setStatusBar(self.statusbar)

        self.retranslateUi(DataVisualizationWin)
        self.tabWidget.setCurrentIndex(0)
        self.backButton.clicked.connect(DataVisualizationWin.backClicked)
        self.listWidget_horizontal.itemDoubleClicked['QListWidgetItem*'].connect(DataVisualizationWin.horizontalParamRemove)
        self.listWidget_vertical.itemDoubleClicked['QListWidgetItem*'].connect(DataVisualizationWin.verticalParamRemove)
        self.label_line_chart.clicked.connect(DataVisualizationWin.graphTypeClicked)
        self.label_pie_chart.clicked.connect(DataVisualizationWin.graphTypeClicked)
        self.label_histogram.clicked.connect(DataVisualizationWin.graphTypeClicked)
        self.label_bar_chart.clicked.connect(DataVisualizationWin.graphTypeClicked)
        self.generateButton.clicked.connect(DataVisualizationWin.generateGraph)
        self.listWidget_horizontal.itemChanged['QListWidgetItem*'].connect(DataVisualizationWin.parameterAddedHorizontal)
        self.listWidget_vertical.itemChanged['QListWidgetItem*'].connect(DataVisualizationWin.parameterAddedVertical)
        self.saveButton.clicked.connect(DataVisualizationWin.saveGraph)
        QtCore.QMetaObject.connectSlotsByName(DataVisualizationWin)

    def retranslateUi(self, DataVisualizationWin):
        _translate = QtCore.QCoreApplication.translate
        DataVisualizationWin.setWindowTitle(_translate("DataVisualizationWin", "Data Visualisation"))
        self.tableNameLabel.setText(_translate("DataVisualizationWin", "Fields"))
        self.label_2.setText(_translate("DataVisualizationWin", "Dimension"))
        self.label_3.setText(_translate("DataVisualizationWin", "Indicator"))
        self.graphTypeLabel.setText(_translate("DataVisualizationWin", "Chart Type"))
        self.label_line_chart.setToolTip(_translate("DataVisualizationWin", "line chart"))
        self.label_bar_chart.setToolTip(_translate("DataVisualizationWin", "bar chart"))
        self.label_18.setText(_translate("DataVisualizationWin", "..."))
        self.label_13.setText(_translate("DataVisualizationWin", "..."))
        self.label_16.setText(_translate("DataVisualizationWin", "..."))
        self.label_pie_chart.setToolTip(_translate("DataVisualizationWin", "pie chart"))
        self.label_7.setText(_translate("DataVisualizationWin", "..."))
        self.label_histogram.setToolTip(_translate("DataVisualizationWin", "histogram"))
        self.label_8.setText(_translate("DataVisualizationWin", "..."))
        self.label_17.setText(_translate("DataVisualizationWin", "..."))
        self.label_14.setText(_translate("DataVisualizationWin", "..."))
        self.label_9.setText(_translate("DataVisualizationWin", "..."))
        self.label.setText(_translate("DataVisualizationWin", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.property_tab), _translate("DataVisualizationWin", "Property"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.style_tab), _translate("DataVisualizationWin", "Style"))
        self.horizontal_label.setText(_translate("DataVisualizationWin", "Horizontal Axes"))
        self.vertical_label.setText(_translate("DataVisualizationWin", "Vertical Axes"))
        self.generateButton.setText(_translate("DataVisualizationWin", "Generate Chart"))
        self.saveButton.setText(_translate("DataVisualizationWin", "Save Picture"))
        self.backButton.setText(_translate("DataVisualizationWin", "Back"))


from .clickablelabel import ClickableLabel
from .mplwidget import MplWidget
from .propertyForm import propertyForm
from .styleForm import styleForm
