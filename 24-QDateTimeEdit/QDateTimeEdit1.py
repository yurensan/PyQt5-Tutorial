import sys
from PyQt5.QtWidgets import QDateTimeEdit,QVBoxLayout,QWidget,QApplication,QMainWindow
from PyQt5.QtCore import QDateTime,QDate,QTime

class QDateTimeEditDemo(QMainWindow):
    def __init__(self):
        super(QDateTimeEditDemo, self).__init__()

        #设置窗口大小
        self.resize(400, 150)
        self.setWindowTitle("QDateTimeEditDemo")

        dateTimeEdit = QDateTimeEdit(QDateTime.currentDateTime(), self)
        dateEdit = QDateTimeEdit(QDate.currentDate(), self)
        timeEdit = QDateTimeEdit(QTime.currentTime(), self)
        dateTimeEdit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        dateEdit.setDisplayFormat("yyyy.MM.dd")
        timeEdit.setDisplayFormat("HH:mm:ss")

        #创建水平布局
        layout = QVBoxLayout()
        layout.addWidget(dateTimeEdit)
        layout.addWidget(dateEdit)
        layout.addWidget(timeEdit)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

if  __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QDateTimeEditDemo()
    main.show()
    sys.exit(app.exec_())
