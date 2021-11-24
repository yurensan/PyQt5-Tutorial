import sys
from PyQt5.QtWidgets import QLabel,QHBoxLayout,QWidget,QApplication,QMainWindow
from PyQt5.QtGui import QPixmap

class QPixmapDemo(QMainWindow):
    def __init__(self):
        super(QPixmapDemo, self).__init__()

        #设置窗口大小
        self.resize(400, 150)
        #设置窗口标题
        self.setWindowTitle("QPixmapDemo")

        pixmap = QPixmap("python.jpg")
        label = QLabel(self)
        label.setPixmap(pixmap)

        #创建水平布局
        layout = QHBoxLayout()
        layout.addWidget(label)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

if  __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QPixmapDemo()
    main.show()
    sys.exit(app.exec_())
