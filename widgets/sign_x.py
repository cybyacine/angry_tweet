from PyQt5.QtWidgets import QTabWidget

from widgets.sign_in import SignIn
from widgets.sign_up import SignUp


class SignX(QL):
    def __init__(self):
        super().__init__()
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.West)
        tabs.addTab(SignIn, "SignIn")
        tabs.addTab(SignUp, "SignUp")
