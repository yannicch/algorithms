from time import sleep

from PyQt6.QtWidgets import QGraphicsTextItem, QMainWindow, QApplication, QLabel, QFrame, QGraphicsView, QGraphicsScene, QVBoxLayout, QGraphicsRectItem
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QBrush, QColor
from PyQt6 import QtCore, QtGui, QtWidgets
from binary import BinarySearchVisualizer
import math
import sys



from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1044, 618)
        MainWindow.setMinimumSize(QtCore.QSize(1044, 618))
        MainWindow.setMaximumSize(QtCore.QSize(1044, 618))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(169, 173, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(169, 173, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(169, 173, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(169, 173, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(620, 100, 391, 31))
        self.comboBox.setEditable(False)
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 961, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.label.setObjectName("label")
        self.submit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(560, 90, 51, 51))
        self.submit.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Desktop/5290109.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.submit.setIcon(icon)
        self.submit.setIconSize(QtCore.QSize(50, 50))
        self.submit.setObjectName("submit")
        self.progressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(70, 510, 971, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1044, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ГРАФИЧЕСКАЯ РЕАЛИЗАЦИЯ АЛГОРИТМОВ"))


class Menu(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Главное меню")
        self.comboBox.addItem('Бинарный поиск')
        self.binary = BinarySearchVisualizer()
        self.visualizer_container = QtWidgets.QFrame(self.centralwidget)
        self.visualizer_container.setGeometry(QtCore.QRect(40, 150, 960, 350))  # Размещаем под кнопками
        self.visualizer_container.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)

        # Используем Layout, чтобы визуализатор растянулся внутри контейнера
        self.layout = QtWidgets.QVBoxLayout(self.visualizer_container)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.binary)
        self.progressBar.setValue(0)

        # Скрываем его изначально (по желанию)
        self.visualizer_container.hide()


        self.initUI()

    def initUI(self):
        self.submit.clicked.connect(self.real)

    def real(self):
        if self.comboBox.currentText() == 'Бинарный поиск':
            self.visualizer_container.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    ex.show()
    sys.exit(app.exec())
