import sys
import os
import csv
from PyQt5.QtWidgets import (QFileDialog, QMainWindow, QApplication, QMessageBox, QSpinBox, QGridLayout,QSizePolicy)
from PyQt5 import QtGui

from Ui_DataAnalyze import Ui_DataAnalyze #从自动生成的界面文件导入基础界面
from MyFigure import PlotCanvas #从图表文件中导入图表类
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

def is_number(s):
    try:  # 如果能运行float(s)语句，返回True（字符串s是浮点数）
        float(s)
        return True
    except ValueError:  # ValueError为Python的一种标准异常，表示"传入无效的参数"
        pass  # 如果引发了ValueError这种异常，不做任何事情（pass：不做任何事情，一般用做占位语句）
    try:
        import unicodedata  # 处理ASCii码的包
        unicodedata.numeric(s)  # 把一个表示数字的字符串转换为浮点数返回的函数
        return True
    except (TypeError, ValueError):
        pass
    return False

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
        self.comboBox_Type.addItem("")
        self.comboBox_Type.addItem("int")
        self.comboBox_Type.addItem("float")
        self.lineEdit_value.setText("0")
        self.lineEdit_value2.setText("0")
        self.plot = PlotCanvas(self, width=5, height=4)
        self.verticalLayout.addWidget(self.plot)
        self.mpl_ntb = NavigationToolbar(self.plot, self)
        self.verticalLayout.addWidget(self.mpl_ntb)

    def SetConnect(self):    
        self.DirButton.clicked.connect(self.OpenDirPath)
        self.pushButton_Process.clicked.connect(self.DataAnalyzeClick)
        self.listWidget_KeyName.clicked.connect(self.ClickListWiget)
    
    def OpenDirPath(self):
        path = QFileDialog.getOpenFileName(self, "选择数据文件","/")
        self.lineEdit_FileDir.setText(path[0])

    def ClickListWiget(self):
        row = self.listWidget_KeyName.currentItem()
        self.lineEdit_Key.setText(row.text())

    def DataAnalyzeClick(self):
        self.content=[]
        self.key_list=[]
        self.plot.clear()
        self.textEdit.clear()
        self.textEdit2.clear()
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
                count = count + 1
                self.progressBar.setValue(count)
                new = line.split(':') #非CSV文件 直接按符号分割
                info_count = len(new)
                if(info_count == 4):    #key:value1:value2:value3类型
                    value_index = 3  #取值value3
                elif(info_count == 2): #key:value1类型
                    value_index = 1  #取值value3
                else:
                    continue
                name = new[0].strip().replace("\n","") #去掉keyName前后空格和换行
                value = new[value_index].strip().replace("\n","") 
                value = new[value_index].strip().replace("\"","") #去掉value的换行、引号等字符
                if (is_number(value)): #判断值是否为数字
                    self.key_list.append(name) #记录所有的KeyName
                    if name == key:  #数据名称
                        if(type(eval(value)) == int):
                            number = int(value) #整型数据
                            self.comboBox_Type.setCurrentIndex(1)
                        elif(type(eval(value)) == float):
                            number = float(value) #浮点型数据
                            self.comboBox_Type.setCurrentIndex(2)
                        else:
                            self.comboBox_Type.setCurrentIndex(0)
                            print("data type erro")
                        editvalue = int(self.lineEdit_value.text())
                        if (number >= editvalue) and (editvalue > 0): #按值筛选
                            # self.textEdit.insertPlainText('%d'%(len(self.content)) +'\r\n') #输出数据所在横坐标
                            self.textEdit.insertPlainText('%d'%(count) +'\r\n')  #输出原始数据所在行数
                        self.content.append(number)
                        # self.textEdit.insertPlainText(number +'\r\n')
                editvalue2 = int(self.lineEdit_value2.text())
                if (len(self.content) >= editvalue2) and (editvalue2 > 0): #按横坐标筛选
                    self.textEdit2.insertPlainText('%d'%(count) +'\r\n')  #输出原始数据所在行数
            self.key_list = list(set(self.key_list))    #去掉KeyName中所有重复项
            self.key_list.sort()                        #排序KeyName
            self.listWidget_KeyName.clear()
            self.listWidget_KeyName.addItems(self.key_list)
        self.plot.plot(data = self.content)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myshow = MyWindow()
    sys.exit(app.exec_())