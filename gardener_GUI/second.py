from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class gardenLogger(QMainWindow):
    def __init__(self):
        super(gardenLogger,self).__init__()
        self.initUI()

    def button_clicked(self):
        self.label.setText("And fruities!")
        self.update()

    def initUI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Anna's garden")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Here be veggies")
        self.label.move(50,50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("click me!")
        self.b1.clicked.connect(self.button_clicked)

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = gardenLogger()
    win.show()
    sys.exit(app.exec_())

window()
