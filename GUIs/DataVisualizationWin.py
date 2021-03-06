# -*- coding: utf-8 -*-

from views.UI_DataVisualizationWin import Ui_DataVisualizationWin
from PyQt5.QtWidgets import QMainWindow, QInputDialog, QMessageBox, QDesktopWidget
from PyQt5.QtCore import pyqtSignal, Qt
from libs import GL
from pandas.api.types import *
from views.clickablelabel import ClickableLabel
from GUIs.Threads.VisualizationDataThread import VisualizationDataThread


class DataVisualizationWin(QMainWindow, Ui_DataVisualizationWin):
    backSignal = pyqtSignal(dict)

    def __init__(self, conf, table_name, parent=None):
        super(DataVisualizationWin, self).__init__(parent)
        self.setupUi(self)
        self.center()
        self.conf = conf
        self.table_name = table_name
        for index in list(GL.tables_df.dtypes.index):
            data_type = GL.tables_df.dtypes[index]
            if is_object_dtype(data_type) or is_datetime64_any_dtype(data_type):
                self.listWidget_dimension.addItem(index)
            else:
                self.listWidget_indicator.addItem(index)
        self.listWidget_indicator.addItem("count(*)")
        self.clicked_graph_type_label = {}
        self.horizontal_param = {}
        self.vertical_param = {}
        self.graph_conf = None

    def center(self):  # 主窗口居中显示函数
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def backClicked(self):
        self.backSignal.emit(self.conf)

    def horizontalParamRemove(self, clicked_item):
        self.listWidget_horizontal.takeItem(self.listWidget_horizontal.row(clicked_item))
        text = clicked_item.text()
        if self.horizontal_param[text] == 'dimension':
            self.listWidget_dimension.addItem(text)
        else:
            self.listWidget_indicator.addItem(text)
        self.horizontal_param.pop(text)
        self.check_generate_button()

    def verticalParamRemove(self, clicked_item):
        # 删除
        self.listWidget_vertical.takeItem(self.listWidget_vertical.row(clicked_item))
        text = clicked_item.text()
        if self.vertical_param[text] == 'dimension':
            self.listWidget_dimension.addItem(text)
        else:
            self.listWidget_indicator.addItem(text)
        self.vertical_param.pop(text)
        self.check_generate_button()

    def graphTypeClicked(self, clicked_item_name):
        clicked_item = self.widget_graph.findChild(ClickableLabel, clicked_item_name)
        self.clicked_graph_type_label[clicked_item_name] = clicked_item
        for label in self.clicked_graph_type_label.values():
            label.unclick()
        clicked_item.click()
        # check states and enable
        self.check_generate_button()
        if clicked_item_name == 'label_histogram':
            self.horizontal_label.setText('Index')
            self.vertical_label.setText('Group')
        elif clicked_item_name == 'label_line_chart':
            self.horizontal_label.setText('Horizontal Axes')
            self.vertical_label.setText('Vertical Axes')
        elif clicked_item_name == 'label_pie_chart':
            self.horizontal_label.setText('Angle')
            self.vertical_label.setText('Color')
        elif clicked_item_name == 'label_bar_chart':
            self.horizontal_label.setText('Horizontal Axes')
            self.vertical_label.setText('Vertical Axes')

    def get_clicked_graph_name(self):
        clicked_name = None
        for label in self.clicked_graph_type_label.values():
            if label.if_mouse_press:
                clicked_name = label.objectName()
                break
        return clicked_name

    def generateGraph(self):
        # 新建线程获得数据
        self.getDataThread = VisualizationDataThread(conf=self.conf, table_name=self.table_name,
                                                     horizontal_axes=list(
                                                         self.horizontal_param.keys()),
                                                     vertical_axes=list(self.vertical_param.keys()),
                                                     graph_type=self.get_clicked_graph_name())
        self.getDataThread.trigger.connect(self.generateGraphFinish)
        self.getDataThread.fail.connect(self.generateGraphFailed)
        self.getDataThread.start()

    def generateGraphFinish(self):
        self.graph_conf = self.get_custom_dic()
        self.mplwidget.plot(horizontal_axes=list(self.horizontal_param.keys()),
                            vertical_axes=list(self.vertical_param.keys()),
                            graph_type=self.get_clicked_graph_name(), dataframe=GL.visualization_df,
                            graph_conf=self.graph_conf)
        self.saveButton.setEnabled(True)
        self.statusbar.showMessage('')

    def generateGraphFailed(self, exception_message):
        self.statusbar.showMessage(exception_message)

    def parameterAddedHorizontal(self, widget_item):
        list_widget = self.get_parent_widget(widget_item)
        if list_widget == 'dimension':
            self.listWidget_dimension.takeItem(self.listWidget_dimension.row(self.dimension_out[0]))
            self.horizontal_param[self.dimension_out[0].text()] = 'dimension'
        else:
            self.listWidget_indicator.takeItem(self.listWidget_indicator.row(self.indicator_out[0]))
            self.horizontal_param[self.indicator_out[0].text()] = 'indicator'
        self.check_generate_button()

    def parameterAddedVertical(self, widget_item):
        list_widget = self.get_parent_widget(widget_item)
        if list_widget == 'dimension':
            self.listWidget_dimension.takeItem(self.listWidget_dimension.row(self.dimension_out[0]))
            self.vertical_param[self.dimension_out[0].text()] = 'dimension'
        else:
            self.listWidget_indicator.takeItem(self.listWidget_indicator.row(self.indicator_out[0]))
            self.vertical_param[self.indicator_out[0].text()] = 'indicator'
        self.check_generate_button()

    def get_parent_widget(self, widget_item):
        self.dimension_out = self.listWidget_dimension.findItems(widget_item.text(),
                                                                 Qt.MatchExactly)
        self.indicator_out = self.listWidget_indicator.findItems(widget_item.text(),
                                                                 Qt.MatchExactly)
        if len(self.dimension_out) > 0:
            return 'dimension'
        if len(self.indicator_out) > 0:
            return 'indicator'

    def saveGraph(self):
        image_name, ok = QInputDialog.getText(self, 'Save', 'Input Image Name               ')
        if ok:
            self.mplwidget.save(image_name + '.png')
            QMessageBox.information(self, '', 'Save Successfully！')

    def get_custom_dic(self):
        dic = {}
        dic_property = {}
        dic_style = {}
        dic_property['line_color'] = self.widget_property.rgb
        dic_property['line_width'] = self.widget_property.horizontalSlider_thickness.value()
        dic_property['label_content'] = self.widget_property.lineEdit_label_content.text()
        dic_style['title_color'] = self.widget_style.title_color
        dic_style['title_content'] = self.widget_style.lineEdit_title_content.text()
        dic_style['title_enabled'] = self.widget_style.comboBox_title_enable.currentText()
        dic_style['legend_position'] = self.widget_style.comboBox_legend_position.currentText()
        dic_style['legend_enabled'] = self.widget_style.comboBox_legend_enable.currentText()
        dic_style['background_color'] = self.widget_style.background_color
        dic['property'] = dic_property
        dic['style'] = dic_style
        # {'property': {'line_color': <PyQt5.QtGui.QColor object at 0x157d12828>, 'line_width': 1, 'label_content': ''}, 'style': {'title_color': None, 'title_content': '', 'title_enabled': '是', 'legend_position': '右', 'legend_enabled': '是', 'background_color': None}}
        return dic

    def check_generate_button(self):
        enabled = True
        clicked_graph_name = self.get_clicked_graph_name()
        if self.listWidget_horizontal.count() == 0 or clicked_graph_name is None:
            enabled = False
        elif clicked_graph_name != 'label_histogram':
            if self.listWidget_vertical.count() == 0:
                enabled = False
        if enabled:
            self.generateButton.setEnabled(True)
        else:
            self.generateButton.setEnabled(False)
