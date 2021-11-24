import sys
from PyQt5.QtWidgets import QCheckBox,QPushButton,QHBoxLayout,QWidget,QApplication,QMainWindow

class QCheckBoxDemo(QMainWindow):
    def __init__(self):
        super(QCheckBoxDemo, self).__init__()

        #设置窗口大小
        self.resize(400, 150)
        #设置窗口标题
        self.setWindowTitle("QCheckBoxDemo")

        self.checkBox = QCheckBox("同意隐私协议")
        self.checkBox.setChecked(True)
        self.checkBox.stateChanged.connect(self.stateChanged)

        #创建水平布局
        layout = QHBoxLayout()
        layout.addWidget(self.checkBox)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def stateChanged(self,btn):
        print(self.checkBox.text() + ", isChecked = " + str(self.checkBox.isChecked()))

if  __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QCheckBoxDemo()
    main.show()
    sys.exit(app.exec_())
