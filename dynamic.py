from PyQt6.QtWidgets import (QGraphicsView, QGraphicsScene,
                             QGraphicsRectItem, QGraphicsTextItem, QVBoxLayout,
                             QWidget, QPushButton, QLabel, QLineEdit)
from PyQt6.QtCore import QTimer
from math import ceil
from PyQt6.QtGui import QBrush, QColor, QFont, QRegularExpressionValidator
from PyQt6.QtCore import QRegularExpression



class DynamicVisualizer(QWidget):
    def __init__(self, progress):
        super().__init__()
        self.progress = progress
        self.point = 2
        self.data = [0, 0, 0, 0, 0, 0]
        self.percent = ceil(100 / (len(self.data) - 1))
        self.num = 1


        self.line = QLineEdit(self)
        regex = QRegularExpression(r"[1-9]\d*")
        validator = QRegularExpressionValidator(regex)
        self.line.setValidator(validator)
        self.line.setFixedSize(100, 20)
        self.lab = QLabel('Введите координату n')
        font = QFont("Arial", 12)
        self.lab.setFont(font)
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.lab)
        self.layout.addWidget(self.line)
        self.layout.addWidget(self.view)

        self.btn_start = QPushButton("Начать поиск")
        self.btn_start.clicked.connect(self.start_search)
        self.layout.addWidget(self.btn_start)

        self.setLayout(self.layout)


        self.timer = QTimer()
        self.timer.timeout.connect(self.search_step)
        self.draw_array()

    def draw_array(self):
        self.scene.clear()
        width = 50
        height = 50
        for i, val in enumerate(self.data):
            rect = QGraphicsRectItem(i * (width + 10), 100, width, height)

            if self.point == len(self.data) and i == len(self.data) - 1:
                rect.setBrush(QBrush(QColor("green")))
            elif (i == self.point - 1 or i == self.point - 2) and self.point != len(self.data) and self.data[0] != 0:
                rect.setBrush(QBrush(QColor("lightyellow")))
            elif self.num != 1:
                if i == self.point:
                        rect.setBrush(QBrush(QColor("red")))
                else:
                        rect.setBrush(QBrush(QColor("lightgrey")))

            self.scene.addItem(rect)

            text = QGraphicsTextItem(str(val))
            text.setPos(i * (width + 10) + 10, 110)
            self.scene.addItem(text)



    def start_search(self):
        self.point = 2
        self.num = 1
        self.data = [1, 1, 0, 0, 0, 0]
        if self.line.text() != '':
            textt = int(self.line.text())
            self.data = [0] * (textt + 1)
        self.percent = ceil(100 / (len(self.data) - 1))
        self.data[0] = 1
        self.data[1] = 1
        self.draw_array()
        self.timer.start(1000)

    def search_step(self):
        self.progress.setValue(self.num * self.percent)
        self.num += 1
        if self.point == len(self.data):
            self.draw_array()
            self.timer.stop()
        else:
            self.data[self.point] = self.data[self.point - 1] + self.data[self.point - 2]
            self.draw_array()
            self.point += 1

