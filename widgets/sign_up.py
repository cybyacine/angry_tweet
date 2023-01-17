from PyQt5.QtWidgets import QLineEdit, QFormLayout, QLabel, QGroupBox, QTabWidget
from PyQt5.uic.properties import QtGui


class SignUp(QTabWidget):
    def __init__(self):

        widget_username = QLineEdit()
        widget_username.setPlaceholderText("Enter your fullname")

        widget_email = QLineEdit()
        widget_email.setPlaceholderText("Enter your email")

        widget_password = QLineEdit()
        widget_password.setEchoMode(QtGui.QLineEdit.Password)
        widget_password.setPlaceholderText("Enter your password")

        widget_c_password = QLineEdit()
        widget_c_password.setEchoMode(QtGui.QLineEdit.Password)
        widget_c_password.setPlaceholderText("Enter your confirmation password")

        layout = QFormLayout()
        layout.addRow(QLabel("Username : "), widget_username)
        layout.addRow(QLabel("Email : "), widget_email)
        layout.addRow(QLabel("Password : "), widget_password)
        layout.addRow(QLabel("Confirmation : "), widget_c_password)

        form_group_box = QGroupBox("Sign Up")
        form_group_box.setLayout(layout)
        self.setLayout(form_group_box)
