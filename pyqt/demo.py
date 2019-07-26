import sys
from UI.openWindows import Ui_Open
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QLineEdit, QMessageBox
from demo2 import demo2
import time
from demo3 import window
import os
import multiprocessing

from demoold import *
import threading


class demo(QWidget, Ui_Open):

    def __init__(self):
        super(demo, self).__init__()
        self.setupUi(self)
        ti = SystemTray(self)
        ti.show()
        self.stackedWidget.setCurrentIndex(0)
        self.action_Open_Environment_Folders.triggered.connect(self.openFolders)
        self.action_Open_EXE.triggered.connect(self.openExe)
        self.action_Manual_Input.triggered.connect(self.manualInput)
        self.action_Run.triggered.connect(self.showPage1)
        self.pushButton.clicked.connect(self.openMainWindows)
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
        self.read_records()

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
        print(self.file)


    def manualInput(self):
        self.file = self.lineEdit.text()
        print(self.file)


    def showPage1(self):
        print('show_page1')
        self.pushButton.setEnabled(False)
        if self.file is None:
            QMessageBox.critical(self,"","请输入执行程序位置",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        else:
            self.stackedWidget.setCurrentIndex(1)
            with open('record.txt', 'w+', encoding='utf-8') as f:
                records = f.readlines()
                while len(records) > 9:
                    records.pop(0)
                for record in records:
                    f.write(record)
                f.write(self.file)
                f.write('\n')

            def sendfilerun(file):
                print('sendfile')
                sendfile(file)
                with open('C:\\summer_camp\\2019-summer-intern\\lib_self\\doneflag.txt', 'w') as f:
                    pass
                while (True):
                    print('while true')
                    with open('C:\\summer_camp\\2019-summer-intern\\lib_self\\doneflag.txt') as f:
                        l = f.readline()
                        if l.strip() == 'done':
                            break
                        time.sleep(3)
                self.openMainWindows()

            thsendfile=threading.Thread(target=sendfilerun, args=(self.file,))
            thsendfile.start()




    def openMainWindows(self):
        win.close()
        win2.show()

    def read_records(self):
        if not os.path.exists('record.txt'):
            with open('record.txt','w') as f:
                pass
        with open('record.txt', 'r', encoding='utf-8') as f:
            records = f.readlines()
        for i, record in enumerate(records):
            record = record.rstrip()
            self.record_buttons[i].setVisible(True)
            self.record_buttons[i].setText(' '*8+record)
            self.record_buttons[i].setStyleSheet("QPushButton{text-align : left;border:none;border-style:none}\n"
                                                 "QPushButton:hover{border-style:none;background-color:#4B6EAF}")
            self.record_buttons[i].clicked.connect(lambda x: self.open_record(record))


    def open_record(self, record):
        self.stackedWidget.setCurrentIndex(1)
        print(record)

def runWindow():
    app = QApplication(sys.argv)
    win = demo()
    win.show()
    win2 = window()
    sys.exit(app.exec_())



if __name__ == '__main__':
    # psub=multiprocessing.Process(target=runSubcmd, args=(cmd,))
    # psub.start()
    pswsb=multiprocessing.Process(target=runWindow, args=())
    pswsb.start()
    os.system("C:\\summer_camp\\2019-summer-intern\\sb.wsb")
    os.system("python C:\\summer_camp\\2019-summer-intern\\ipc_server.py")
