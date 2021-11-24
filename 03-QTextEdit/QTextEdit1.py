import sys
from PyQt5.QtWidgets import QTextEdit,QHBoxLayout,QWidget,QApplication,QMainWindow

class QTextEditDemo(QMainWindow):
    def __init__(self):
        super(QTextEditDemo, self).__init__()

        #设置窗口大小
        self.resize(400, 150)
        #设置窗口标题
        self.setWindowTitle("QTextEditDemo")
        textEdit = QTextEdit()
        # textEdit.setReadOnly(True)

        #创建水平布局
        layout = QHBoxLayout()
        layout.addWidget(textEdit)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

if  __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QTextEditDemo()
    main.show()
    sys.exit(app.exec_())
