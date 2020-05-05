import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUiType

from os import path

FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "download.ui"))


class MainApp(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)

    def Handle_Buttons(self):
        pass

    def HandleBrowse(self):
        pass

    def HandleProgressBar(self):
        pass

    def HandleStartDownload(self):
        pass


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

