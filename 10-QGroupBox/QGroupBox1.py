import sys
from PyQt5.QtWidgets import QRadioButton,QGroupBox,QHBoxLayout,QWidget,QApplication,QMainWindow

class QGroupBoxDemo(QMainWindow):
    def __init__(self):
        super(QGroupBoxDemo, self).__init__()

        #设置窗口大小
        self.resize(400, 150)
        #设置窗口标题
        self.setWindowTitle("QGroupBoxDemo")

        groupBox = QGroupBox('性别')
        radio1 = QRadioButton('男')
        radio2 = QRadioButton('女')
        radio1.setChecked(True)
        hlayout = QHBoxLayout()
        groupBox.setLayout(hlayout)
        hlayout.addWidget(radio1)
        hlayout.addWidget(radio2)

        #创建水平布局
        layout = QHBoxLayout()
        layout.addWidget(groupBox)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

if  __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QGroupBoxDemo()
    main.show()
    sys.exit(app.exec_())
