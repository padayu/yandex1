import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QColor
from random import randint


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        qp.setPen(QColor("yellow"))
        for i in range(randint(1, 7)):
            d = randint(2, 250)
            qp.drawEllipse(randint(0, 700), randint(0, 500), d, d)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
