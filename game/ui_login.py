import sys
from PyQt6.QtWidgets import (
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QDialog,
    QGridLayout,
)


import users
import ui_message


class LoginWindow(QDialog):
    """
    This "window" is a QDialog.
    It blocks main window.
    """
    def __init__(self, user_box):
        super().__init__()
        self.setWindowTitle("Логин")
        self.login_label = QLabel(f"Логин:")
        self.login_edit = QLineEdit()
        self.login_edit.setPlaceholderText('Введите логин...')
        self.pass_label = QLabel(f"Пароль:")
        self.pass_edit = QLineEdit()
        self.pass_edit.setPlaceholderText('Введите пароль...')

        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Отмена")

        login_layout = QGridLayout()
        buttons_layout = QHBoxLayout()

        login_layout.addWidget(self.login_label, 0, 0)
        login_layout.addWidget(self.login_edit, 0, 1)
        login_layout.addWidget(self.pass_label, 1, 0)
        login_layout.addWidget(self.pass_edit, 1, 1)

        buttons_layout.addWidget(self.ok_button)
        buttons_layout.addWidget(self.cancel_button)

        layout = QVBoxLayout()
        layout.addLayout(login_layout)
        layout.addLayout(buttons_layout)

        self.cancel_button.clicked.connect(self.cancel_login)
        self.ok_button.clicked.connect(self.user_login)

        self.user_box = user_box

        self.setLayout(layout)

    def cancel_login(self):
        self.close()

    def user_login(self):
        login = self.login_edit.text()
        password = self.pass_edit.text()
        result = users.auth_user(login, password)
        if result == "err":
            ui_message.warning_window("Ошибка входа", "Неправильный пароль")
        else:
            self.user_box.append(result)
            self.close()


