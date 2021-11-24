import sys
from PyQt5.QtWidgets import QLabel,QSlider,QHBoxLayout,QWidget,QApplication,QMainWindow
from PyQt5.QtCore import *

class QSliderDemo(QMainWindow):
    def __init__(self):
        super(QSliderDemo, self).__init__()

        #设置窗口大小
        self.resize(400, 150)
        #设置窗口标题
        self.setWindowTitle("QSliderDemo")

        self.label = QLabel('当前值：10')
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(10)
        self.slider.setMaximum(50)
        self.slider.setSingleStep(3)
        self.slider.valueChanged.connect(self.valueChange)

        #创建水平布局
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.slider)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def valueChange(self):
        self.label.setText('当前值：%s'%self.slider.value())

if  __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSliderDemo()
    main.show()
    sys.exit(app.exec_())
