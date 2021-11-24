import sys
from PyQt5.QtWidgets import QProgressBar,QPushButton,QHBoxLayout,QWidget,QApplication,QMainWindow
from PyQt5.QtCore import QTimer

class QProgressBarDemo(QMainWindow):
    def __init__(self):
        super(QProgressBarDemo, self).__init__()

        #设置窗口大小
        self.resize(400, 150)
        #设置窗口标题
        self.setWindowTitle("QProgressBarDemo")

        btn = QPushButton("开始")
        btn.clicked.connect(self.btnClick)
        self.progressBar = QProgressBar(self)
        self.progressBar.setValue(0)

        #创建水平布局
        layout = QHBoxLayout()
        layout.addWidget(btn)
        layout.addWidget(self.progressBar)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def btnClick(self):
        timer = QTimer(self.progressBar)
        def timerFunc():
            if self.progressBar.value() >= self.progressBar.maximum():
                timer.stop()
            self.progressBar.setValue(self.progressBar.value() + 2)
        timer.timeout.connect(timerFunc)
        timer.start(100) #每隔100ms
        self.progressBar.valueChanged.connect(lambda val:print(val))

if  __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QProgressBarDemo()
    main.show()
    sys.exit(app.exec_())
