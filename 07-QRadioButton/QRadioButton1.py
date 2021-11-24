import sys
from PyQt5.QtWidgets import QRadioButton,QHBoxLayout,QWidget,QApplication,QMainWindow

class QRadioButtonDemo(QMainWindow):
    def __init__(self):
        super(QRadioButtonDemo, self).__init__()

        #设置窗口大小
        self.resize(400, 150)
        #设置窗口标题
        self.setWindowTitle("QRadioButtonDemo")

        btn1 = QRadioButton("男")
        #设置btn1为默认选中
        btn1.setChecked(True)
        #为btn1绑定点击事件
        btn1.toggled.connect(self.btnClick)
        btn2 = QRadioButton("女")
        btn2.toggled.connect(self.btnClick)

        #创建水平布局
        layout = QHBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def btnClick(self, btn):
        if self.sender().text() == "男":
            if self.sender().isChecked() == True:
                print(self.sender().text() + "  is selected")
            else:
                print(self.sender().text() + "  is deselected")

if  __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QRadioButtonDemo()
    main.show()
    sys.exit(app.exec_())
