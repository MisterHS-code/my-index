from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(100, 100, 480, 360)
    win.setWindowTitle("Testing the window")

    win.show()
    sys.exit(app.exec_())

window()
