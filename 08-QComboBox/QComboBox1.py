import sys
from PyQt5.QtWidgets import QComboBox,QHBoxLayout,QWidget,QApplication,QMainWindow

class QComboBoxDemo(QMainWindow):
    def __init__(self):
        super(QComboBoxDemo, self).__init__()

        #设置窗口大小
        self.resize(400, 150)
        #设置窗口标题
        self.setWindowTitle("QComboBoxDemo")

        self.comboBox = QComboBox()
        self.comboBox.addItems(['C','C#','C++'])
        self.comboBox.currentIndexChanged.connect(self.itemChange)

        #创建水平布局
        layout = QHBoxLayout()
        layout.addWidget(self.comboBox)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def itemChange(self, i):
        print(self.comboBox.currentText() + "  is selected")

if  __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QComboBoxDemo()
    main.show()
    sys.exit(app.exec_())
