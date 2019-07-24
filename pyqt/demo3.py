import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSystemTrayIcon, QAction, QMenu,\
    qApp, QMessageBox, QWidgetAction, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit, QGridLayout,\
    QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QCoreApplication, Qt, QSize, QDir
import os
from multiprocessing.managers import BaseManager
import threading
import uuid
from multiprocessing import Queue
import pprint
import time
import os, shutil
import sys



class ServerManager(BaseManager):
    pass


ServerManager.register('get_request_queue')
ServerManager.register('get_response_queue')


def send_request(config, req):
    server = ServerManager(address=(config['address'], config['port']), authkey=config['auth_key'])
    server.connect()
    response_queue = server.get_response_queue()
    uid = response_queue.get()
    request_queue = server.get_request_queue()
    request_queue.put((uid, req))
    return response_queue.get()

def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    import socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


class SystemTray(QSystemTrayIcon):

    def __init__(self, parent = None):
        super(SystemTray, self).__init__(parent)
        self.createActions()
        self.EdgeAction()
        self.UploadAction()
        self.addActions()
        self.setContextMenu(self.menu)

    def showWidget(self):
        if w.isVisible():
            w.hide()
            self.show_action.setIcon(QIcon(QPixmap("./icons/加号.png")))
        else:
            w.showNormal()
            self.show_action.setIcon(QIcon(QPixmap("./icons/减号.png")))

    def exitWidget(self):
        sys.exit(app.exec_())

    def createActions(self):
        self.setIcon(QIcon('./icons/sandbox.png'))
        self.menu = QMenu(QApplication.desktop())
        self.menu.setStyleSheet("QMenu{text-align:center}")
        self.show_action = QWidgetAction(self.menu)
        self.exit_action = QWidgetAction(self.menu)

        self.show_action.triggered.connect(self.showWidget)
        self.exit_action.triggered.connect(self.exitWidget)

        self.show_action.setIcon(QIcon(QPixmap("./icons/减号.png")))
        self.show_action.setIconText("显示主界面")
        self.exit_action.setIcon(QIcon(QPixmap("./icons/关机.png")))
        self.exit_action.setIconText("退出程序")

    def EdgeAction(self):
        edge_widget = QWidget()
        self.edge_action = QWidgetAction(self.menu)
        self.searchLine = QLineEdit()
        self.searchLine.setPlaceholderText('search in sandbox')
        self.searchButton = QPushButton()
        self.searchButton.setIcon(QIcon(QPixmap("./icons/search.png")))
        self.searchButton.setObjectName("searchButton")
        self.searchButton.setIconSize(QSize(18,18))
        self.searchButton.setStyleSheet("QPushButton{border:2px}")
        self.searchButton.clicked.connect(self.searchInSanbox)
        layout = QGridLayout()
        layout.addWidget(self.searchLine, 1, 1)
        layout.addWidget(self.searchButton, 1, 0)
        edge_widget.setLayout(layout)
        self.edge_action.setDefaultWidget(edge_widget)


    def UploadAction(self):
        upload_widget = QWidget()
        self.upload_action = QWidgetAction(self.menu)
        self.upload_action.setIcon(QIcon(QPixmap("./icons/file.png")))
        self.upload_action.setIconText("加载文件")
        self.upload_action.triggered.connect(self.getfile)
        # self.upload_button = QPushButton("加载文件")
        # self.upload_button.setIcon(QIcon(QPixmap("./icons/file.png")))
        # self.upload_button.setIconSize(QSize(15,15))
        # self.upload_button.setStyleSheet("QPushButton{border:2px}")
        # self.upload_button.clicked.connect(self.getfile)
        # layout = QVBoxLayout()
        # layout.addWidget(self.upload_button)
        # upload_widget.setLayout(layout)
        # self.upload_action.setDefaultWidget(upload_widget)

    def searchInSanbox(self):
        print('hello')
        url = self.searchLine.text()
        if url == '':
            url = 'https://www.baidu.com'
        # self.searchLine.setText(None)
        import os
        # cmd = f"start microsoft-edge:{url}"
        # os.popen(cmd)
        # print(url)
        # print('unit test')

        # s = "C:\\Users\\ztp\\Desktop\\Shadowsocks-4.1.6\\Shadowsocks.exe"
        # s = str(sys.argv[1])
        # print(s)
        # ss = s.strip().split("\\")[-1]
        # if os.path.exists(s):
        #     res = shutil.copy(s, f'C:\summer_camp\source\\{ss}')
        # thispath = os.path.abspath('.')
        fip = open("C:\summer_camp\\2019-summer-intern\clientip.txt")
        server_ip = fip.readline().strip()
        fip.close()
        server_config = {'address': server_ip, 'port': 9998, 'auth_key': b'A8rhWNHR2p'}
        ip = get_host_ip()
        while True:
            cmdType = '1'  # 1:open url; 2:run a exe; 3
            exefile = 'microsoft-edge:'
            # url = "https://www.google.com"
            cmd = f"start microsoft-edge:{url}"  # chrome
            # cmd = f"start chrome --new-windows {url}" #chrome
            # exestr="C:\summer_camp\source\\ChromeSetup.exe /silent /install"
            # cmd=ss
            # cmd = "ChromeSetup.exe /silent /install"
            resstr = send_request(server_config, {'cmdType': cmdType, 'request': cmd, 'time': time.time()})
            if resstr:
                pprint.pprint(resstr)
                break

    def getfile(self):
        q_file = QFileDialog()
        q_file.setFileMode(QFileDialog.AnyFile)
        q_file.setFilter(QDir.Files)
        if q_file.exec():
            filenames = q_file.selectedFiles()
            print(filenames[0])

            print('unit test')


            # s = "C:\\Users\\ztp\\Desktop\\Shadowsocks-4.1.6\\Shadowsocks.exe"
            # s = str(sys.argv[1])
            # print(s)
            s=filenames[0]
            ss = s.strip().split("/")[-1]
            if os.path.exists(s):
                try:
                    res = shutil.copy(s, f'C:\\summer_camp\\2019-summer-intern\\source\\{ss}')
                except Exception as e:
                    print(e)
            thispath = os.path.abspath('.')
            fip = open("C:\summer_camp\\2019-summer-intern\\clientip.txt")
            server_ip = fip.readline().strip()
            fip.close()
            server_config = {'address': server_ip, 'port': 9998, 'auth_key': b'A8rhWNHR2p'}
            ip = get_host_ip()
            while True:
                cmdType = '2'  # 1:open url; 2:run a exe; 3
                exefile = 'microsoft-edge:'
                url = "https://www.google.com"
                cmd = f"start microsoft-edge:{url}"  # chrome
                # cmd = f"start chrome --new-windows {url}" #chrome
                # exestr="C:\summer_camp\source\\ChromeSetup.exe /silent /install"
                cmd=ss
                # cmd = "ChromeSetup.exe /silent /install"
                resstr = send_request(server_config, {'cmdType': cmdType, 'request': cmd, 'time': time.time()})
                if resstr:
                    pprint.pprint(resstr)
                    break
                # time.sleep(0.5)

    def addActions(self):
        self.menu.addAction(self.edge_action)
        self.menu.addAction(self.upload_action)
        self.menu.addAction(self.show_action)
        self.menu.addAction(self.exit_action)

class window(QWidget):
    def __init__(self, parent=None):
        super(window, self).__init__(parent)
        ti = SystemTray(self)
        ti.show()

if __name__ == '__main__':
    import sys

    # os.system("C:\\summer_camp\\2019-summer-intern\\sb.wsb")
    os.system("python C:\\summer_camp\\2019-summer-intern\\ipc_server.py")

    print("please wait sandbox running!")
    app = QApplication(sys.argv)
    w = window()
    w.show()
    sys.exit(app.exec_())