import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QColor
from random import randint

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(756, 580)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(340, 260, 93, 28))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Git и желтые окружности"))
        self.pushButton.setText(_translate("Form", "Кнопка"))


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        for i in range(randint(1, 7)):
            qp.setPen(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
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
