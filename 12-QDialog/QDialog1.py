import sys
from PyQt5.QtWidgets import QPushButton,QLabel,QDialog,QHBoxLayout,QVBoxLayout,QWidget,QApplication,QMainWindow
from PyQt5.QtCore import *

class QDialogDemo(QMainWindow):
    def __init__(self):
        super(QDialogDemo, self).__init__()

        #设置窗口大小
        self.resize(400, 150)
        self.setWindowTitle("QDialogDemo")

        btn = QPushButton("开始")
        btn.clicked.connect(self.btnClick)

        #创建水平布局
        layout = QHBoxLayout()
        layout.addWidget(btn)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def btnClick(self):
        self.dialog = QDialog()
        self.dialog.resize(100, 100)
        self.dialog.setWindowTitle("提示信息！")

        vbox = QVBoxLayout()
        label = QLabel("这是QDialog测试消息，确定保存信息？")
        okBtn = QPushButton("确定")
        okBtn.clicked.connect(self.okClick)
        vbox.addWidget(label)
        vbox.addWidget(okBtn)
        self.dialog.setLayout(vbox)
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.exec_()
    
    def okClick(self):
        print("确定保存")
        self.dialog.close()

if  __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QDialogDemo()
    main.show()
    sys.exit(app.exec_())
