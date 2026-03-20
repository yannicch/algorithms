from PyQt6.QtWidgets import (QGraphicsView, QGraphicsScene,
                             QGraphicsRectItem, QGraphicsTextItem, QVBoxLayout,
                             QWidget, QPushButton, QLabel)
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QBrush, QColor, QFont


class BinarySearchVisualizer(QWidget):
    def __init__(self, progress):
        super().__init__()

        self.progress = progress
        self.num = 1
        self.data = sorted([10, 50, 20, 80, 30, 90, 40, 70, 60, 100])
        self.target = 70
        self.low = 0
        self.high = len(self.data) - 1
        self.mid = -1

        font = QFont("Arial", 16)
        self.label = QLabel('Поиск 70')
        self.label.setFont(font)
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
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


            if i == self.mid and self.data[self.mid] == self.target:
                rect.setBrush(QBrush(QColor("green")))
            elif i == self.mid:
                rect.setBrush(QBrush(QColor("red")))
            elif self.low <= i <= self.high:
                rect.setBrush(QBrush(QColor("lightblue")))
            else:
                rect.setBrush(QBrush(QColor("lightgrey")))

            self.scene.addItem(rect)

            text = QGraphicsTextItem(str(val))
            text.setPos(i * (width + 10) + 10, 110)
            self.scene.addItem(text)



    def start_search(self):
        self.num = 1
        self.low = 0
        self.high = len(self.data) - 1
        self.timer.start(1000)

    def search_step(self):
        self.progress.setValue(self.num * 25)
        self.num += 1
        if self.low <= self.high:
            self.mid = (self.low + self.high) // 2
            self.draw_array()

            if self.data[self.mid] == self.target:
                self.timer.stop()
            elif self.data[self.mid] < self.target:
                self.low = self.mid + 1
            else:
                self.high = self.mid - 1
        else:
            self.timer.stop()

