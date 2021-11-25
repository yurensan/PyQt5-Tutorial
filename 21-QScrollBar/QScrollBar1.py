import sys
from PyQt5.QtWidgets import QLabel,QScrollBar,QHBoxLayout,QWidget,QApplication,QMainWindow

class QScrollBarDemo(QMainWindow):
    def __init__(self):
        super(QScrollBarDemo, self).__init__()

        self.resize(400, 150)
        #设置窗口标题
        self.setWindowTitle("QScrollBarDemo")

        self.label = QLabel('滚动条的值')
        self.scrollBar1 = QScrollBar()
        self.scrollBar1.setMaximum(255)
        self.scrollBar1.sliderMoved.connect(self.sliderChange)

        self.scrollBar2 = QScrollBar()
        self.scrollBar2.setMaximum(255)
        self.scrollBar2.sliderMoved.connect(self.sliderChange)

        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.scrollBar1)
        layout.addWidget(self.scrollBar2)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def sliderChange(self):
        self.label.setText("滚动条1的值:"+str(self.scrollBar1.value())+", 滚动条2的值:"+str(self.scrollBar2.value()))

if  __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QScrollBarDemo()
    main.show()
    sys.exit(app.exec_())
