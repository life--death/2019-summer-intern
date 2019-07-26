import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSystemTrayIcon, QAction, QMenu,\
    qApp, QMessageBox, QWidgetAction, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit, QGridLayout,\
    QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QCoreApplication, Qt, QSize, QDir


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
            url = 'http://www.baidu.com'
        self.searchLine.setText(None)
        import os
        cmd = f"start microsoft-edge:{url}"
        os.popen(cmd)
        print(url)

    def getfile(self):
        q_file = QFileDialog()
        q_file.setFileMode(QFileDialog.AnyFile)
        q_file.setFilter(QDir.Files)
        if q_file.exec():
            filenames = q_file.selectedFiles()
            print(filenames[0])
            with open(filenames[0]) as f:
                print(f.readlines())

    def addActions(self):
        self.menu.addAction(self.edge_action)
        self.menu.addAction(self.upload_action)
        self.menu.addAction(self.show_action)
        self.menu.addAction(self.exit_action)


#
# ui->play_button->setStyleSheet("QPushButton{border-image: url(:/new/icons/icons/play-pause.png);}"
#                               "QPushButton:hover{border-image: url(:/new/icons/icons/play-pause-hover.png);}"
#                               "QPushButton:pressed{border-image: url(:/new/icons/icons/play-pause-pressed.png);}");