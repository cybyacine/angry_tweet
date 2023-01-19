import sys
from PyQt5 import QMainWindow, QApplication
from PyQt5 import uic.loadUi


class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        loadUi('basic.ui', self)
        self.show()


app = QApplication(sys.argv)
window = Ui()
app.exec_()
