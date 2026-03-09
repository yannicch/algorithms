import sys
import time
from PyQt6.QtWidgets import (QApplication, QGraphicsView, QGraphicsScene,
                             QGraphicsRectItem, QGraphicsTextItem, QVBoxLayout,
                             QWidget, QPushButton, QHBoxLayout, QLabel)
from PyQt6.QtCore import Qt, QTimer, QRectF
from PyQt6.QtGui import QBrush, QColor, QFont


class BinarySearchVisualizer(QWidget):
    def __init__(self):
        super().__init__()

        # Данные
        self.data = sorted([10, 50, 20, 80, 30, 90, 40, 70, 60, 100])
        self.target = 70
        self.low = 0
        self.high = len(self.data) - 1
        self.mid = -1

        # UI элементы
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

        # Таймер для анимации
        self.timer = QTimer()
        self.timer.timeout.connect(self.search_step)

        self.draw_array()

    def draw_array(self, color=QColor("blue")):
        self.scene.clear()
        width = 50
        height = 50
        for i, val in enumerate(self.data):
            rect = QGraphicsRectItem(i * (width + 10), 100, width, height)

            # Цветовая индикация границ и середины
            if i == self.mid:
                rect.setBrush(QBrush(QColor("red")))  # Mid
            elif self.low <= i <= self.high:
                rect.setBrush(QBrush(QColor("lightblue")))  # Диапазон поиска
            else:
                rect.setBrush(QBrush(QColor("lightgrey")))  # Вне диапазона

            self.scene.addItem(rect)

            text = QGraphicsTextItem(str(val))
            text.setPos(i * (width + 10) + 10, 110)
            self.scene.addItem(text)


    def start_search(self):
        self.low = 0
        self.high = len(self.data) - 1
        self.timer.start(1000)  # Шаг 1 секунда

    def search_step(self):
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

