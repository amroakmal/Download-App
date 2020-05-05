from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi, loadUiType

from os import path

FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "download.ui"))
