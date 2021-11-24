import sys
from PyQt5.QtWidgets import QPushButton,QHBoxLayout,QWidget,QApplication,QMainWindow

class QPushButtonDemo(QMainWindow):
    def __init__(self):
        super(QPushButtonDemo, self).__init__()

        #设置窗口大小
        self.resize(400, 150)
        #设置窗口标题
        self.setWindowTitle("QPushButtonDemo")

        button1 = QPushButton("我是按钮")

        #创建水平布局
        layout = QHBoxLayout()
        layout.addWidget(button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

if  __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QPushButtonDemo()
    main.show()
    sys.exit(app.exec_())
