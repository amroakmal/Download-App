import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUiType

from os import path

FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "download.ui"))


class mainapp(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(mainapp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    window = mainapp()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()

