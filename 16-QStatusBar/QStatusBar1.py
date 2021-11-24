import sys
from PyQt5.QtWidgets import QComboBox,QStatusBar,QHBoxLayout,QWidget,QApplication,QMainWindow
from PyQt5.QtCore import *

class QStatusBarDemo(QMainWindow):
    def __init__(self):
        super(QStatusBarDemo, self).__init__()

        #设置窗口大小
        self.resize(400, 150)
        #设置窗口标题
        self.setWindowTitle("QComboBoxDemo")

        self.comboBox = QComboBox()
        self.comboBox.addItems(['C','C#','C++'])
        self.comboBox.currentIndexChanged.connect(self.itemChange)
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        #创建水平布局
        layout = QHBoxLayout()
        layout.addWidget(self.comboBox)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def itemChange(self):
        self.statusBar.showMessage(self.comboBox.currentText()+'菜单选项被选中了',1000)

if  __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QStatusBarDemo()
    main.show()
    sys.exit(app.exec_())
