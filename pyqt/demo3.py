from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTreeWidgetItem
from PyQt5.QtGui import QPixmap
from mainUI import MainUI
from csv_reader import *

def DFS(father: node, son: node, father_node: QTreeWidgetItem,node_set:dict):
    if len(son.child) != 0:
        for element in son.child:
            print(element.name)
            if node_set.get(son.pid) == None:
                son_node = QTreeWidgetItem()
                son_node.setText(0, son.name)
                son_node.setText(1, son.pid)
                node_set[son.pid] = son_node
                DFS(son,element,son_node,node_set)
                father_node.addChild(son_node)
            else:
                temp_node = node_set.get(son.pid)
                DFS(son, element, temp_node,node_set)
    else:
        son_node = QTreeWidgetItem()
        son_node.setText(0, son.name)
        son_node.setText(1, son.pid)
        node_set[son.pid] = son_node
        father_node.addChild(son_node)

class window(QMainWindow, MainUI):
    def __init__(self):
        super(window, self).__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(2)
        self.showInit()
        #ti = SystemTray(self)
        #ti.show()

    def showInit(self):
        pass
        # self.textBrowser.setText('Init')

    def readpmc(self,c):
        self.textBrowser.clear()
        try:
            with open(f'C:\\summer_camp\\2019-summer-intern\\lib_self\\pmc\\{c}_report.txt',
                      encoding='utf-8') as f:
                line = f.readline()
                while line:
                    self.textBrowser.append(line)
                    line = f.readline()
            self.textBrowser.moveCursor(self.textBrowser.textCursor().Start)
        except Exception as e:
            print(e)

    def showOperator(self):
        print('op')
        sender = self.sender()
        self.stackedWidget.setCurrentIndex(2)
        print(sender.text())
        with open('C:\\summer_camp\\2019-summer-intern\\lib_self\\filename.txt') as f:
            filename=f.readline().split('/')[-1]
        cla=sender.text().strip()
        if cla=='分析':
            self.textBrowser.clear()
            for n in {'write_action','write_reg','tcp_report'}:
                with open(f'C:\\summer_camp\\2019-summer-intern\\lib_self\\pmc\\{n}_report.txt',
                          encoding='UTF-8') as f:
                    line = f.readline()
                    self.textBrowser.append(line)
        elif cla=='文件读写监控':
            self.readpmc('write_action')
        elif cla=='注册表监控':
            self.readpmc('write_reg')
        elif cla=='网络监控':
            self.readpmc('tcp_report')
        else:
            pass

        # self.textBrowser.setText(f"Hello {sender.text()}")


    def showPidTree(self):
        print('pid')
        self.stackedWidget.setCurrentIndex(1)
        temp = process_analysis_main('C:\\summer_camp\\2019-summer-intern\\lib_self\\pmc\\process-create.pmc.csv')
        root = QTreeWidgetItem(self.treeWidget)
        total = node("total", "-1")
        root.setText(0, "total")
        root.setText(1, "-1")
        node_dict = dict()
        node_dict["-1"] = root
        for element in temp:
            DFS(total, element, root, node_dict)

    def showCpuorMen(self):
        sender = self.sender()
        if sender.text()=='CPU':
            self.label.setPixmap(QPixmap(r'..\lib_self\cpuUtil.png'))
        else:
            self.label.setPixmap(QPixmap(r'..\lib_self\menUtil.png'))
        print(sender.text())


    def showPerformance(self):
        self.stackedWidget.setCurrentIndex(0)
        print('per')
        self.label.setPixmap(QPixmap(r'..\lib_self\cpuUtil.png'))

class treeNode():
    def __init__(self,process_name,pid):
        self.name = process_name
        self.pid = str(pid)
        self.child = []

def createTree():
    root = treeNode('cmd.exe', 5008)
    thirdDeep = treeNode('regsvr.exe', 3368)
    secondDeep = treeNode('netease.exe', 4876)
    secondDeep.child = [thirdDeep]
    root.child = [secondDeep ,treeNode('Procmon.exe', 4976)]
    return root


if __name__ == "__main__":
    import sys
    tree = createTree()
    app = QtWidgets.QApplication(sys.argv)
    w = window()
    w.show()
    sys.exit(app.exec_())