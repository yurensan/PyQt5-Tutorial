import sys
from PyQt5.QtWidgets import QAction,QHBoxLayout,QWidget,QApplication,QMainWindow
from PyQt5.QtGui import QIcon

class QToolBarDemo(QMainWindow):
    def __init__(self):
        super(QToolBarDemo, self).__init__()

        #设置窗口大小
        self.resize(400, 150)
        #设置窗口标题
        self.setWindowTitle("QToolBarDemo")

        toolBar = self.addToolBar('File')
        new = QAction(QIcon('u1.ico'), 'new', self)
        toolBar.addAction(new)
        open = QAction(QIcon('u2.ico'), 'open', self)
        toolBar.addAction(open)
        save = QAction(QIcon('u3.ico'), 'save', self)
        toolBar.addAction(save)
        toolBar.actionTriggered[QAction].connect(self.btnClick)

        #创建水平布局
        layout = QHBoxLayout()
        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def btnClick(self, w):
        print("pressed tool button is:", w.text())

if  __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QToolBarDemo()
    main.show()
    sys.exit(app.exec_())
