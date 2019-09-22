import sys
import os
import csv
from PyQt5.QtWidgets import (QFileDialog, QMainWindow, QApplication, QMessageBox, QSpinBox, QGridLayout,QSizePolicy)
from PyQt5 import QtGui

from Ui_DataAnalyze import Ui_DataAnalyze #从自动生成的界面文件导入基础界面
from MyFigure import PlotCanvas #从图表文件中导入图表类
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

class MyWindow(QMainWindow, Ui_DataAnalyze, QFileDialog):
    
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.ui_init()
        self.SetConnect()
        self.show()

    def ui_init(self):
        self.lineEdit_Key.setText("")
        self.progressBar.setValue(0)
        self.comboBox_Type.addItem("int")
        self.comboBox_Type.addItem("float")
        self.plot = PlotCanvas(self, width=5, height=4)
        self.verticalLayout.addWidget(self.plot)
        self.mpl_ntb = NavigationToolbar(self.plot, self)
        self.verticalLayout.addWidget(self.mpl_ntb)

    def SetConnect(self):    
        self.DirButton.clicked.connect(self.OpenDirPath)
        self.pushButton_Process.clicked.connect(self.DataAnalyzeClick)

    def OpenDirPath(self):
        path = QFileDialog.getOpenFileName(self, "选择数据文件","/")
        self.lineEdit_FileDir.setText(path[0])

    def DataAnalyzeClick(self):
        self.content=[]
        self.plot.clear()
        key = self.lineEdit_Key.text() #获取数据名称
        file_path = self.lineEdit_FileDir.text()
        if os.path.exists(file_path):       #检查文件是否存在，若存在则打开读取其中的数据
            file_open = open(file_path,'r')
            # csv_file=csv.reader(file_open) #读取CSV格式文件
            pr = os.popen('find /V "" /C ' + file_path) 
            # print(pr.read())
            range_number = int((pr.read().split(":")[2]))
            pr.close()
            self.progressBar.setRange(0, range_number) #根据文件行数修改range范围
            count = 0
            for line in file_open:
                new = line.split(': ') #非CSV文件 直接按符号分割
                if new[0] == key:  #数据名称
                    if self.comboBox_Type.currentText() == 'float':
                        number = float(new[1]) #浮点型数据
                    if self.comboBox_Type.currentText() == 'int':
                        number = int(new[1]) #整型数据
                    # if number >= 10: #按值筛选
                    # if count >= 60828: #按行数筛选
                        # self.textEdit.insertPlainText('%d'%(count) +'\r\n')  #输出原始数据所在行数
                        # self.textEdit.insertPlainText('%d'%(len(self.content[0])) +'\r\n') #输出数据所在横坐标
                    self.content.append(number)
                    # self.textEdit.insertPlainText(number +'\r\n')
                count = count + 1
                self.progressBar.setValue(count)
        self.plot.plot(data = self.content)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myshow = MyWindow()
    sys.exit(app.exec_())