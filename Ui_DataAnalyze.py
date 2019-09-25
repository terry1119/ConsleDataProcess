# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\hf_work\python_work\ConsleDataProcess\DataAnalyze.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DataAnalyze(object):
    def setupUi(self, DataAnalyze):
        DataAnalyze.setObjectName("DataAnalyze")
        DataAnalyze.resize(1282, 693)
        self.centralwidget = QtWidgets.QWidget(DataAnalyze)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_FileDir = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_FileDir.setGeometry(QtCore.QRect(162, 20, 361, 21))
        self.lineEdit_FileDir.setReadOnly(True)
        self.lineEdit_FileDir.setObjectName("lineEdit_FileDir")
        self.DirButton = QtWidgets.QPushButton(self.centralwidget)
        self.DirButton.setGeometry(QtCore.QRect(530, 17, 31, 28))
        self.DirButton.setObjectName("DirButton")
        self.label_FileDir = QtWidgets.QLabel(self.centralwidget)
        self.label_FileDir.setGeometry(QtCore.QRect(20, 20, 131, 16))
        self.label_FileDir.setObjectName("label_FileDir")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(800, 70, 281, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_CanID = QtWidgets.QLabel(self.centralwidget)
        self.label_CanID.setGeometry(QtCore.QRect(20, 70, 51, 16))
        self.label_CanID.setTextFormat(QtCore.Qt.AutoText)
        self.label_CanID.setObjectName("label_CanID")
        self.lineEdit_Key = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Key.setGeometry(QtCore.QRect(70, 70, 121, 21))
        self.lineEdit_Key.setObjectName("lineEdit_Key")
        self.pushButton_Process = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Process.setGeometry(QtCore.QRect(700, 70, 93, 28))
        self.pushButton_Process.setObjectName("pushButton_Process")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(200, 100, 1071, 571))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1041, 521))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 1061, 531))
        self.textEdit.setObjectName("textEdit")
        self.tabWidget.addTab(self.tab_2, "")
        self.comboBox_Type = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Type.setGeometry(QtCore.QRect(240, 70, 87, 22))
        self.comboBox_Type.setObjectName("comboBox_Type")
        self.listWidget_KeyName = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_KeyName.setGeometry(QtCore.QRect(10, 100, 181, 571))
        self.listWidget_KeyName.setObjectName("listWidget_KeyName")
        DataAnalyze.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DataAnalyze)
        self.statusbar.setObjectName("statusbar")
        DataAnalyze.setStatusBar(self.statusbar)

        self.retranslateUi(DataAnalyze)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DataAnalyze)

    def retranslateUi(self, DataAnalyze):
        _translate = QtCore.QCoreApplication.translate
        DataAnalyze.setWindowTitle(_translate("DataAnalyze", "DataAnalyze"))
        self.DirButton.setText(_translate("DataAnalyze", "..."))
        self.label_FileDir.setText(_translate("DataAnalyze", "选择数据文件路径"))
        self.label_CanID.setText(_translate("DataAnalyze", "KEY："))
        self.pushButton_Process.setText(_translate("DataAnalyze", "分析"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("DataAnalyze", "Plot"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("DataAnalyze", "Info"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DataAnalyze = QtWidgets.QMainWindow()
    ui = Ui_DataAnalyze()
    ui.setupUi(DataAnalyze)
    DataAnalyze.show()
    sys.exit(app.exec_())
