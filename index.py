import sys
import urllib.request

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.uic import loadUiType

from os import path

FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "download.ui"))


class MainApp(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.HandelUIChanges()
        self.HandelButtons()

    def HandelUIChanges(self):
        self.setWindowTitle("You-Downloader")
        self.setFixedSize(700, 300)

    def HandelButtons(self):
        self.pushButton.clicked.connect(self.HandelStartDownload)

    def HandelBrowse(self):
        pass

    def HandelProgressBar(self):
        pass

    def HandelStartDownload(self):
        url = self.lineEdit_3.text()
        save_path = self.lineEdit_2.text()
        urllib.request.urlretrieve(url, save_path, self.HandelProgressBar)

        QMessageBox.Information(self, "Download Completed", "Finished Downloading")

        self.progressBar.setvalue(0)
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

