import sys
import time
from UI.mainwindows_test import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QLineEdit, QMessageBox

class demo2(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(demo2, self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.showWindows)
        self.pushButton_2.setText("等待分析中")
        self.pushButton_2.show()
        self.pushButton_2.setText("查看分析报告")


    def showWindows(self):
        self.pushButton_2.hide()
        self.textBrowser.hide()
        self.frame.show()
        self.frame_2.show()
        self.frame_2.show()
        self.frame_2.show()
        self.frame_2.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = demo2()
    win.show()
    sys.exit(app.exec_())