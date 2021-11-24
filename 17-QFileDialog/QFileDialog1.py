import sys
from PyQt5.QtWidgets import QPushButton,QLabel,QFileDialog,QVBoxLayout,QWidget,QApplication,QMainWindow
from PyQt5.QtGui import QPixmap

class QFileDialogDemo(QMainWindow):
    def __init__(self):
        super(QFileDialogDemo, self).__init__()

        #设置窗口大小
        self.resize(400, 150)
        self.setWindowTitle("QFileDialogDemo")

        self.label = QLabel('')
        btn = QPushButton("显示图片")
        btn.clicked.connect(self.btnClick)

        #创建水平布局
        layout = QVBoxLayout()
        layout.addWidget(btn)
        layout.addWidget(self.label)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def btnClick(self):
        imageFile, _ = QFileDialog.getOpenFileName(self,'Open file','C:\\','Image files (*.jpg *.png *.jpeg)')
        self.label.setPixmap(QPixmap(imageFile))

if  __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QFileDialogDemo()
    main.show()
    sys.exit(app.exec_())
