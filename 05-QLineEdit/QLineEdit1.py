import sys
from PyQt5.QtWidgets import QLabel,QLineEdit,QHBoxLayout,QWidget,QApplication,QMainWindow

class QLineEditDemo(QMainWindow):
    def __init__(self):
        super(QLineEditDemo, self).__init__()

        #设置窗口大小
        self.resize(400, 150)
        #设置窗口标题
        self.setWindowTitle("QLineEditDemo")
        lineEdit = QLineEdit()
        lineEdit.setPlaceholderText("这是单行输入框")
        label = QLabel('单行输入框',self)

        #创建水平布局
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(lineEdit)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

if  __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditDemo()
    main.show()
    sys.exit(app.exec_())
