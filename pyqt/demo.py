import sys
from UI.openWindows import Ui_Open
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QLineEdit, QMessageBox
from demo2 import demo2
import time
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from demo3 import window
import os
import multiprocessing
from multiprocessing import Manager

from demoold import *
import threading
import matplotlib.pyplot as plt
import numpy as np
from csv_reader import *


app = None
win = None
win2 = None


class AnalyseThread(QThread):
    _signal = pyqtSignal(str)

    def __init__(self, file):
        self.file = file
        super(AnalyseThread, self).__init__()

    def __del__(self):
        self.wait()

    def run(self):
        print('show_page1')

        print('sendfile')
        with open('C:\\summer_camp\\2019-summer-intern\\lib_self\\filename.txt', 'w') as f:
            f.write(self.file)
        sendfile(self.file)

        with open('C:\\summer_camp\\2019-summer-intern\\lib_self\\doneflag.txt', 'w') as f:
            pass
        while True:
            # print('while true',end='\n')
            with open('C:\\summer_camp\\2019-summer-intern\\lib_self\\doneflag.txt') as f:
                l = f.readline()
                if l.strip() == 'done':
                    break
                time.sleep(3)
        drawCpuLine()
        try:
            print(self.file.split('/')[-1])
            analysis_main('C:\\summer_camp\\2019-summer-intern\\lib_self\\pmc\\', self.file.split('/')[-1])
        except Exception as e:
            print(e)
        self.callback("等待结束")

    def callback(self, msg):
        self._signal.emit(msg)

class democlass(QWidget, Ui_Open):

    def __init__(self):
        super(democlass, self).__init__()
        self.setupUi(self)
        print('init')
        self.ti = SystemTray(self)
        self.ti.show()
        self.stackedWidget.setCurrentIndex(0)
        self.action_Open_Environment_Folders.triggered.connect(self.openFolders)
        self.action_Open_EXE.triggered.connect(self.openExe)
        self.action_Manual_Input.triggered.connect(self.manualInput)
        self.action_Run.triggered.connect(self.check_file)
        self.pushButton.clicked.connect(lambda x: openMainWindows(win, win2))
        self.folders = None
        self.file = None
        self.record_buttons = [self.toolButton_14, self.toolButton_10, self.toolButton_13,
                               self.toolButton_12, self.toolButton_11, self.toolButton_18,
                               self.toolButton_17, self.toolButton_16, self.toolButton_15]
        self.toolButton_14.setVisible(False)
        self.toolButton_10.setVisible(False)
        self.toolButton_13.setVisible(False)
        self.toolButton_12.setVisible(False)
        self.toolButton_11.setVisible(False)
        self.toolButton_18.setVisible(False)
        self.toolButton_17.setVisible(False)
        self.toolButton_16.setVisible(False)
        self.toolButton_15.setVisible(False)
        self.show_records()

    def openFolders(self):
        fileDialog = QFileDialog()
        fileDialog.setFileMode(QFileDialog.Directory)
        if fileDialog.exec_():
            filenames = fileDialog.selectedFiles()
            self.folders = filenames[0]
        print(self.folders)

    def openExe(self):
        if self.folders is not None:
            self.file, ok = QFileDialog.getOpenFileName(self, "打开", self.folders, "All Files (*);; exe(*.exe)")
        else:
            self.file, ok = QFileDialog.getOpenFileName(self, "打开", "C:/", "All Files (*);; exe(*.exe)")
        self.add_record()
        print(self.file)


    def manualInput(self):
        self.file = self.lineEdit.text()
        self.add_record()
        print(self.file)


    def check_file(self):
        self.pushButton.setEnabled(False)
        if self.file is None:
            QMessageBox.critical(self,"","请输入执行程序位置",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        else:
            self.showPage1()

    def showPage1(self):
        self.stackedWidget.setCurrentIndex(1)
        self.analyseThread = AnalyseThread(self.file)
        self.analyseThread._signal.connect(self.callbacklog)
        self.analyseThread.start()

    def callbacklog(self, msg):
        print(msg)
        self.pushButton.setEnabled(True)
        self.pushButton.setText("点击查看分析报告")
        self.label.setText("分析完成 ")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font: 18pt Adobe Devanagari")
        self.pushButton.setStyleSheet("QPushButton{background-color:#1B9AF7;border-color:#1B9AF7;"
                                      "color:#FFFFFF;border-radius:30px;font: 18pt Adobe Devanagari}")
        # self.openMainWindows()




    def show_records(self):
        with open('record.txt', 'r', encoding='utf-8') as f:
            records = f.readlines()
            records = list(set(records))
        for i, record in enumerate(records):
            record = record.rstrip()
            self.record_buttons[i].setVisible(True)
            if len(record) > 30:
                record_long = "..." + r'/'.join(record[-30:].split(r'/')[1:])
                self.record_buttons[i].setText(' '*8+record_long)

            else:
                self.record_buttons[i].setText(' '*8+record)
            self.record_buttons[i].setStyleSheet("QPushButton{text-align : left;border:none;border-style:none}\n"
                                                 "QPushButton:hover{border-style:none;background-color:#4B6EAF}")
            self.record_buttons[i].clicked.connect(lambda x: self.open_record(record))



    def open_record(self, record):
        self.file=record
        self.pushButton.setEnabled(False)
        self.showPage1()


    def add_record(self):
        with open('record.txt', 'r+', encoding='utf-8') as f:
            records = f.readlines()
            records = list(set(records))
            while len(records) > 9:
                records.pop(0)
        with open('record.txt', 'w', encoding='utf-8') as f:
            for record in records:
                f.write(record)
            f.write(self.file)
            f.write('\n')


# app = QApplication(sys.argv)
# win = democlass()
# win2 = window()




def openMainWindows(win, win2):
    win.close()
    win2.show()

def runWindow():
    global app, win, win2
    app = QApplication(sys.argv)
    win = democlass()
    win2 = window()
    win.show()
    sys.exit(app.exec_())

def drawCpuLine(figSize=(6,4)):
    with open('C:\\summer_camp\\2019-summer-intern\\cpu_util.txt') as f:
        ctime=[]
        cpurate=[]
        cmenrate=[]
        line=f.readline()
        fristtime=float(line.strip().split()[0])
        while line:
            temp=list(map(float,line.strip().split()))
            ctime.append(temp[0]-fristtime)
            cpurate.append(temp[1])
            cmenrate.append(temp[2])
            line=f.readline()
    plt.figure(figsize=figSize)
    plt.plot(ctime, cpurate,color='red')
    plt.xlabel("Time(s)")  # x轴上的名字
    plt.ylabel("CPU(%)")  # y轴上的名字
    plt.savefig('C:\\summer_camp\\2019-summer-intern\\lib_self\\cpuUtil.png')
    plt.figure(figsize=figSize)
    plt.plot(ctime, cmenrate,color='green')
    plt.xlabel("Time(s)")  # x轴上的名字
    plt.ylabel("MENORY(%)")  # y轴上的名字
    plt.savefig('C:\\summer_camp\\2019-summer-intern\\lib_self\\menUtil.png')
    # plt.show()


if __name__ == '__main__':
    # drawCpuLine()
    # psub=multiprocessing.Process(target=runSubcmd, args=(cmd,))
    # psub.start()

    # manager=Manager().dict({'win': win, 'win2': win2})
    pswsb=multiprocessing.Process(target=runWindow, args=())
    pswsb.start()
    # os.system("C:\\summer_camp\\2019-summer-intern\\sb.wsb")
    os.system("python C:\\summer_camp\\2019-summer-intern\\ipc_server.py")
