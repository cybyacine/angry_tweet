from PyQt5.QtWidgets import QLineEdit, QFormLayout, QLabel, QGroupBox, QTabWidget
from PyQt5.uic.properties import QtGui


class SignIn(QTabWidget):
    def __init__(self):
        widget_username = QLineEdit()
        widget_username.setPlaceholderText("Enter your username")

        widget_password = QLineEdit()
        widget_password.setEchoMode(QtGui.QLineEdit.Password)
        widget_password.setPlaceholderText("Enter your password")

        layout = QFormLayout()
        layout.addRow(QLabel("Username : "), widget_username)
        layout.addRow(QLabel("Password : "), widget_password)

        form_group_box = QGroupBox("Sign In")
        form_group_box.setLayout(layout)
