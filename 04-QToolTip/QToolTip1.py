import sys
from PyQt5.QtWidgets import QToolTip,QPushButton,QHBoxLayout,QWidget,QApplication,QMainWindow
from PyQt5.QtGui import QFont

class QToolTipDemo(QMainWindow):
    def __init__(self):
        super(QToolTipDemo, self).__init__()

        #设置窗口大小
        self.resize(400, 150)
        #设置窗口标题
        self.setWindowTitle("QToolTipDemo")

        button1 = QPushButton("我是按钮")
        #设置ToolTip显示的字体与大小
        QToolTip.setFont(QFont("SanSerif",16))
        button1.setToolTip("Tip:我是一个有理想的按钮")

        #创建水平布局
        layout = QHBoxLayout()
        layout.addWidget(button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

if  __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QToolTipDemo()
    main.show()
    sys.exit(app.exec_())
