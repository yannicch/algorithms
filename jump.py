from PyQt6.QtWidgets import (QGraphicsView, QGraphicsScene,
                             QGraphicsRectItem, QGraphicsTextItem, QVBoxLayout,
                             QWidget, QPushButton, QLabel)
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QBrush, QColor, QFont



class JumpSearchVisualizer(QWidget):
    def __init__(self, progress):
        super().__init__()
        self.progress = progress
        # Данные
        self.data = sorted([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])
        self.target = 15
        self.step = int(len(self.data) ** 0.5)
        self.prev = -1
        self.num = 1


        font = QFont("Arial", 16)
        self.label = QLabel('Поиск 15')
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

            if i == self.prev  and self.data[self.prev] == self.target:
                rect.setBrush(QBrush(QColor("green")))
            elif i == self.prev:
                rect.setBrush(QBrush(QColor("red")))  # Mid
            elif i > self.prev and self.data[self.prev] != self.target:
                rect.setBrush(QBrush(QColor("lightblue")))
            else:
                rect.setBrush(QBrush(QColor("lightgrey")))

            self.scene.addItem(rect)

            text = QGraphicsTextItem(str(val))
            text.setPos(i * (width + 10) + 10, 110)
            self.scene.addItem(text)


    def start_search(self):
        self.prev = 0
        self.num = 1
        self.progress.setValue(self.num * 25)
        self.step = int(len(self.data) ** 0.5)
        self.draw_array()
        self.timer.start(1000)  # Шаг 1 секунда

    def search_step(self):
        self.num += 1
        self.progress.setValue(self.num * 25)
        if self.data[min(self.step, len(self.data) - 1)] <= self.target:
            self.prev = self.step
            self.step += int(len(self.data) ** 0.5)
            self.draw_array()
            if self.data[self.prev] == self.target:
                self.timer.stop()
            elif self.prev >= len(self.data):
                self.timer.stop()
        else:
            self.prev += 1
            if self.prev >= len(self.data) or self.data[self.prev] > self.target:
                self.timer.stop()
            self.draw_array()
            if self.data[self.prev] == self.target:
                self.timer.stop()