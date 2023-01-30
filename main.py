import os
import sys
import time

from PyQt5 import uic
from PyQt5.QtWidgets import QStackedWidget, QApplication, QWidget
from Services.user_service import UserService

sign_in_ui, _ = uic.loadUiType(os.path.join("UIs", "sign-in.ui"))
sign_up_ui, _ = uic.loadUiType(os.path.join("UIs", "sign-up.ui"))
chat_box_ui, _ = uic.loadUiType(os.path.join("UIs", "chat-box.ui"))
userService = UserService()


class SignIn(QWidget, sign_in_ui):
    def __init__(self, parent=None):
        super(SignIn, self).__init__(parent)
        self.setupUi(self)

    def sign_in(self, username, password):
        user = userService.search_user(uid=username)
        if user and user.password == password:
            w.setCurrentIndex(2)
        else:
            sign_in.responseInvalidQLabel.setText(f"{username} is not valid or password invalid")
            time.sleep(4)
            sign_in.responseInvalidQLabel.setText(None)


class SignUp(QWidget, sign_up_ui):
    def __init__(self, parent=None):
        super(SignUp, self).__init__(parent)
        self.setupUi(self)


class ChatBox(QWidget, chat_box_ui):
    def __init__(self, parent=None):
        super(ChatBox, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    sign_in = SignIn()
    sign_up = SignUp()
    chat_box = ChatBox()

    w = QStackedWidget()
    w.addWidget(sign_in)
    w.addWidget(sign_up)
    w.addWidget(chat_box)

    sign_up.signInPushButton.clicked.connect(lambda: w.setCurrentIndex(0))
    sign_in.signUpPushButton.clicked.connect(lambda: w.setCurrentIndex(1))
    sign_in.okPushButton.clicked.connect(lambda: sign_in.signIn(sign_in.usernameLineEdit.text(), sign_in.passwordLineEdit.text()))
    w.show()
    sys.exit(app.exec_())
