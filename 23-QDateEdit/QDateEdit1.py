import sys
from PyQt5.QtWidgets import QPlainTextEdit,QDateEdit,QVBoxLayout,QWidget,QApplication,QMainWindow
from PyQt5.QtCore import QDate,Qt

class QDateEditDemo(QMainWindow):
    def __init__(self):
        super(QDateEditDemo, self).__init__()

        #设置窗口大小
        self.resize(400, 150)
        self.setWindowTitle("QDateEditDemo")

        dateEdit = QDateEdit(QDate.currentDate(), self)
        dateEdit.setDisplayFormat("yyyy-MM-dd")
        #dateEdit.setCalendarPopup(True)
        dateEdit.dateChanged.connect(self.dateChanged)

        self.text = QPlainTextEdit(self)
        self.text.setReadOnly(True)

        #创建水平布局
        layout = QVBoxLayout()
        layout.addWidget(dateEdit)
        layout.addWidget(self.text)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def dateChanged(self, date):
        self.text.appendPlainText(date.toString(Qt.ISODate))
        self.text.appendPlainText(date.toString('yyyy:MM:dd [ddd]'))

if  __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QDateEditDemo()
    main.show()
    sys.exit(app.exec_())
