from PyQt6.QtWidgets import QMainWindow, QApplication
from binary import BinarySearchVisualizer
from jump import JumpSearchVisualizer
from dynamic import DynamicVisualizer
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
        icon.addPixmap(QtGui.QPixmap("cor.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
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
        self.comboBox.addItem('Поиск прыжками')
        self.comboBox.addItem('Динамическое программирование')
        self.binary = BinarySearchVisualizer(self.progressBar)
        self.jump = JumpSearchVisualizer(self.progressBar)
        self.dynamic = DynamicVisualizer(self.progressBar)
        self.visualizer_container = QtWidgets.QFrame(self.centralwidget)
        self.visualizer_container.setGeometry(QtCore.QRect(40, 150, 960, 350))
        self.visualizer_container.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.setWindowIcon(QtGui.QIcon('sign.ico'))

        self.layout = QtWidgets.QVBoxLayout(self.visualizer_container)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.progressBar.setValue(0)

        self.visualizer_container.hide()


        self.initUI()

    def initUI(self):
        self.submit.clicked.connect(self.real)

    def real(self):
        if self.comboBox.currentText() == 'Бинарный поиск':
            old = self.layout.takeAt(0)
            if old is not None:
                old.widget().deleteLater()
            self.progressBar.setValue(0)
            self.binary = BinarySearchVisualizer(self.progressBar)
            self.layout.addWidget(self.binary)
            self.visualizer_container.show()
        if self.comboBox.currentText() == 'Поиск прыжками':
            old = self.layout.takeAt(0)
            if old is not None:
                old.widget().deleteLater()
            self.progressBar.setValue(0)
            self.jump = JumpSearchVisualizer(self.progressBar)
            self.layout.addWidget(self.jump)
            self.visualizer_container.show()
        if self.comboBox.currentText() == 'Динамическое программирование':
            old = self.layout.takeAt(0)
            if old is not None:
                old.widget().deleteLater()
            self.progressBar.setValue(0)
            self.dynamic = DynamicVisualizer(self.progressBar)
            self.layout.addWidget(self.dynamic)
            self.visualizer_container.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    ex.show()
    sys.exit(app.exec())
