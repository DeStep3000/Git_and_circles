import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton
from random import randint


class Circle:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
        self.colors = randint(0, 255), randint(0, 255), randint(0, 255)

    def draw(self, painter):
        painter.setBrush(QColor(self.colors[0], self.colors[1], self.colors[-1]))
        painter.setPen(QColor(self.colors[0], self.colors[1], self.colors[-1]))
        painter.drawEllipse(self.x, self.y, self.d, self.d)


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.objects = []
        button = QPushButton(self)
        button.move(300, 20)
        button.setText('Нажми меня')
        button.clicked.connect(self.run)
        self.loadui()

    def loadui(self):
        k = InitUi()
        k = k.load()
        self.setGeometry(k[0], k[1], k[2], k[3])
        self.setWindowTitle(k[-1])

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        for obj in self.objects:
            obj.draw(painter)
        painter.end()

    def run(self):
        x = randint(50, 600)
        y = randint(20, 600)
        d = randint(20, 50)
        self.objects.append(Circle(x, y, d))
        self.update()


class InitUi:
    def __init__(self):
        self.x = 700
        self.y = 700
        self.label = 'Случайные круги'

    def load(self):
        return 300, 50, self.x, self.y, self.label


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())