import sys
from PyQt5.QtWidgets import QPushButton,QMessageBox,QVBoxLayout,QWidget,QApplication,QMainWindow

class QMessageBoxDemo(QMainWindow):
    def __init__(self):
        super(QMessageBoxDemo, self).__init__()

        #设置窗口大小
        self.resize(400, 150)
        #设置窗口标题
        self.setWindowTitle("QMessageBoxDemo")
        
        button1 = QPushButton("关于对话框")
        #为button1设置点击事件
        button1.clicked.connect(self.showMessageBox)

        button2 = QPushButton("消息对话框")
        button2.clicked.connect(self.showMessageBox)
        button3 = QPushButton("警告对话框")
        button3.clicked.connect(self.showMessageBox)
        button4 = QPushButton("错误对话框")
        button4.clicked.connect(self.showMessageBox)
        button5 = QPushButton("提问对话框")
        button5.clicked.connect(self.showMessageBox)

        #创建垂直布局
        layout = QVBoxLayout()
        #将各button添加到布局中
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.addWidget(button5)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def showMessageBox(self):
        text = self.sender().text()
        #根据button标题来判断用户点击的是哪个按钮
        if text == "关于对话框":
            QMessageBox.about(self, "关于", "这是一个关于对话框")
        elif text == "消息对话框":
            QMessageBox.information(self, "消息", "这是一个消息对话框",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        elif text == "警告对话框":
            QMessageBox.warning(self, "警告", "这是一个警告对话框",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        elif text == "错误对话框":
            QMessageBox.critical(self, "错误", "这是一个错误对话框",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        elif text == "提问对话框":
            QMessageBox.question(self, "提问", "这是一个提问对话框",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)

if  __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QMessageBoxDemo()
    main.show()
    sys.exit(app.exec_())
