from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from demo4 import Ui_MainWindow

class window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.setupUi(self)
        #ti = SystemTray(self)
        #ti.show()

    def showOperator(self):
        sender = self.sender()
        self.stackedWidget.setCurrentIndex(1)
        print(sender.text())
        self.textEdit.setText(f"Hello {sender.text()}")

    def showOperator1(self):
        self.stackedWidget.setCurrentIndex(0)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = window()
    w.show()
    sys.exit(app.exec_())