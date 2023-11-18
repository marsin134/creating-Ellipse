import sys
from PyQt5 import QtCore
from random import randint
from UI import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class Ellipse(QMainWindow):
    def __init__(self):
        super().__init__()
        Ui_MainWindow.setupUi(self, self)
        self.start = False
        self.pushButton.clicked.connect(self.run)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "! ЖМИ !"))

    def run(self):
        self.start = True
        self.update()

    def paintEvent(self, event):
        if self.start:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            x, y = randint(100, 600), randint(100, 450)
            diametr = randint(10, 75)
            qp.drawEllipse(x, y, diametr, diametr)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ellipse()
    ex.show()
    sys.exit(app.exec_())
