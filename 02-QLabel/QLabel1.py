import sys
from PyQt5.QtWidgets import QLabel,QHBoxLayout,QWidget,QApplication,QMainWindow

class QLabelDemo(QMainWindow):
    def __init__(self):
        super(QLabelDemo, self).__init__()

        #设置窗口大小
        self.resize(400, 150)
        #设置窗口标题
        self.setWindowTitle("QLabelDemo")
        label1 = QLabel(self)
        label2 = QLabel('第二个标签',self)

        label1.setText("<font color = red>第一个标签</font>")

        #创建水平布局
        layout = QHBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

if  __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelDemo()
    main.show()
    sys.exit(app.exec_())
