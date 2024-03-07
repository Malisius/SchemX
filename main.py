import nbtlib
import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import Qt
from mainwindow_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.actionHorizontal.triggered.connect(self.layout_horizontal)
        self.actionVertical.triggered.connect(self.layout_vertical)

    def layout_horizontal(self):
        self.splitter.setOrientation(Qt.Horizontal)

    def layout_vertical(self):
        self.splitter.setOrientation(Qt.Vertical)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
