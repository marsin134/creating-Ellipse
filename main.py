import sys
from PyQt5 import uic
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class Ellipse(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.start = False
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.start = True
        self.update()

    def paintEvent(self, event):
        if self.start:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            x, y = randint(100, 600), randint(100, 450)
            diametr = randint(10, 75)
            qp.drawEllipse(x, y, diametr, diametr)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ellipse()
    ex.show()
    sys.exit(app.exec_())
