import sys

from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow
    window.show()

    app.exec()
    sys.exit(app.exec_())
