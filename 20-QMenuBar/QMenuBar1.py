import sys
from PyQt5.QtWidgets import QAction,QHBoxLayout,QWidget,QApplication,QMainWindow

class QMenuBarDemo(QMainWindow):
    def __init__(self):
        super(QMenuBarDemo, self).__init__()

        self.resize(400, 150)
        #设置窗口标题
        self.setWindowTitle("QMenuBarDemo")

        bar = self.menuBar()
        file = bar.addMenu('File')

        file.addAction('New')
        save = QAction('Save', self)
        save.setShortcut('Ctrl+S')
        file.addAction(save)

        edit = bar.addMenu('Edit')
        edit.addAction('Copy')
        edit.addAction('Paste')

        quit = QAction('Quit', self)
        file.addAction(quit)
        file.triggered[QAction].connect(self.menuClick)

        layout = QHBoxLayout()
        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def menuClick(self, q):
        print(q.text() + " is click")

if  __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QMenuBarDemo()
    main.show()
    sys.exit(app.exec_())
