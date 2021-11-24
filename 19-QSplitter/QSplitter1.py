import sys
from PyQt5.QtWidgets import QTextEdit,QSplitter,QFrame,QHBoxLayout,QWidget,QApplication,QMainWindow
from PyQt5.QtCore import Qt

class QSplitterDemo(QMainWindow):
    def __init__(self):
        super(QSplitterDemo, self).__init__()

        self.resize(400, 150)
        self.setWindowTitle("QSplitterDemo")

        topLeft = QFrame()
        topLeft.setFrameShape(QFrame.StyledPanel)
        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)
        splitter1 = QSplitter(Qt.Horizontal)
        textedit = QTextEdit()
        splitter1.addWidget(topLeft)
        splitter1.addWidget(textedit)
        splitter1.setSizes([100,200])
        
        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        #创建水平布局
        layout = QHBoxLayout()
        layout.addWidget(splitter2)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

if  __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSplitterDemo()
    main.show()
    sys.exit(app.exec_())
