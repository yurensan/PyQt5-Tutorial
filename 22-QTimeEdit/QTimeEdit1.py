import sys
from PyQt5.QtWidgets import QTimeEdit,QPlainTextEdit,QVBoxLayout,QWidget,QApplication,QMainWindow
from PyQt5.QtCore import QTime,Qt

class QTimeEditDemo(QMainWindow):
    def __init__(self):
        super(QTimeEditDemo, self).__init__()

        #设置窗口大小
        self.resize(400, 150)
        self.setWindowTitle("QTimeEditDemo")

        timeEdit = QTimeEdit(self)
        timeEdit.setDisplayFormat('HH:mm:ss')
        timeEdit.setTime(QTime.currentTime())

        timeEdit.timeChanged.connect(self.timeChanged)
        self.plainTextEdit = QPlainTextEdit(self)
        self.plainTextEdit.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(timeEdit)
        layout.addWidget(self.plainTextEdit)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def timeChanged(self, time):
        self.plainTextEdit.appendPlainText(time.toString('hh:mm:ss'))

if  __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QTimeEditDemo()
    main.show()
    sys.exit(app.exec_())
