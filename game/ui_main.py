import sys
from time import sleep
from games import get_stats
from make_path import resource_path
from ui_stats import StatisticsWindow
from ui_yes_no_message import CustomDialog
from ui_message import warning_window
import users
from main_game import (create_game,
                       guess_a_letter,
                       guess_the_word,
                       turn_the_drum
                       )
import ui_message
import ui_login
import os

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QHBoxLayout,
    QWidget,
    QLabel,
    QLineEdit,
    QGridLayout,
)

from PyQt6 import QtGui, QtCore
from PyQt6.QtCore import Qt, QBuffer, QByteArray


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Поле чудес")

        #main store
        self.user_box: list[users.User] = []
        self.game_data = None

        cyrillic_lower_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        cyrillic_letters = cyrillic_lower_letters + cyrillic_lower_letters.upper()
        self.letters = cyrillic_letters

        #Lyaouts
        main_layout = QGridLayout()
        main_layout.setColumnStretch(0, 1)
        main_layout.setRowStretch(0, 1)
        main_layout.setRowStretch(1, 1)
        main_layout.setRowStretch(2, 1)
        main_layout.setRowStretch(3, 1)
        main_layout.setRowStretch(4, 1)

        header_layout = QGridLayout()
        central_layout = QGridLayout()
        bottom_layout = QHBoxLayout()

        main_layout.addLayout(header_layout, 0, 0, 1, 1)
        main_layout.addLayout(central_layout, 1, 0, 3, 1, Qt.AlignmentFlag.AlignHCenter)
        main_layout.addLayout(bottom_layout, 4, 0, 1, 1)

        #Start header

        #Quiz task
        self.description_label = QLabel("  ")
        self.description_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.description_label.setFont(QtGui.QFont('Arial', 12))
        self.description_label.setWordWrap(True)
        header_layout.addWidget(self.description_label, 1, 0, 1, 3)

        #Login, NewGame fields
        self.login_label = QLabel("  ")
        self.game_button = QPushButton("Новая игра")
        self.login_button = QPushButton("Логин")

        header_layout.addWidget(self.login_label, 0, 3, 1, 1)
        header_layout.addWidget(self.game_button, 1, 3, 1, 1)
        header_layout.addWidget(self.login_button, 2, 3, 1, 1)

        self.login_button.clicked.connect(self.login_window)
        self.game_button.clicked.connect(self.new_game)

        #Central layout
        self.the_drum = QLabel()
        self.the_drum.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.the_drum.setMinimumSize(QtCore.QSize(275, 120))
        self.the_drum.setMaximumSize(QtCore.QSize(275, 120))
        self.drum = QLabel("  ")
        self.drum.setMinimumSize(QtCore.QSize(150, 25))
        self.drum.setMaximumSize(QtCore.QSize(150, 25))
        self.word = QLabel("  ")
        self.word.setMinimumSize(QtCore.QSize(450, 25))
        self.word.setMaximumSize(QtCore.QSize(450, 25))
        self.drum.setFont(QtGui.QFont('Arial', 14))
        self.word.setFont(QtGui.QFont('Arial', 18))
        self.word.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.drum.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.gues_w_edit = QLineEdit()
        self.gues_w_edit.setMinimumSize(QtCore.QSize(150, 25))
        self.gues_w_edit.setMaximumSize(QtCore.QSize(150, 25))
        self.gues_w_edit.setPlaceholderText('Введите слово...')
        self.gues_l_edit = QLineEdit()
        self.gues_l_edit.setMinimumSize(QtCore.QSize(150, 25))
        self.gues_l_edit.setMaximumSize(QtCore.QSize(150, 25))
        self.gues_l_edit.setPlaceholderText('Введите букву...')
        self.gues_w_button = QPushButton("Проверить слово")
        self.gues_w_button.setMinimumSize(QtCore.QSize(150, 25))
        self.gues_w_button.setMaximumSize(QtCore.QSize(150, 25))
        self.gues_l_button = QPushButton("Проверить букву")
        self.gues_l_button.setMinimumSize(QtCore.QSize(150, 25))
        self.gues_l_button.setMaximumSize(QtCore.QSize(150, 25))
        self.turn_button = QPushButton("Вращать барабан")
        #self.turn_button.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.turn_button.setMinimumSize(QtCore.QSize(150, 25))
        self.turn_button.setMaximumSize(QtCore.QSize(150, 25))
        self.turn_button.clicked.connect(self.make_a_turn)
        self.gues_l_button.clicked.connect(self.guess_a_letter)
        self.gues_w_button.clicked.connect(self.guess_the_word)
        self.letters_label = QLabel("")
        self.letters_label.setWordWrap(True)
        self.letters_label.setFont(QtGui.QFont('Arial', 14))
        self.letters_label.setMinimumSize(QtCore.QSize(150, 25))
        self.letters_label.setMaximumSize(QtCore.QSize(150, 75))

        central_layout.addWidget(self.word, 0, 0, 1, 5, Qt.AlignmentFlag.AlignHCenter)
        central_layout.addWidget(self.the_drum, 1, 0, 3, 3, Qt.AlignmentFlag.AlignHCenter)
        central_layout.addWidget(self.turn_button, 4, 0, 1, 3, Qt.AlignmentFlag.AlignHCenter)
        central_layout.addWidget(self.drum, 5, 0, 1, 3, Qt.AlignmentFlag.AlignHCenter)
        central_layout.addWidget(self.gues_l_edit, 1, 4, 1, 2, Qt.AlignmentFlag.AlignHCenter)
        central_layout.addWidget(self.gues_l_button, 2, 4, 1, 2, Qt.AlignmentFlag.AlignHCenter)
        central_layout.addWidget(self.gues_w_edit, 3, 4, 1, 2, Qt.AlignmentFlag.AlignHCenter)
        central_layout.addWidget(self.gues_w_button, 4, 4, 1, 2, Qt.AlignmentFlag.AlignHCenter)
        central_layout.addWidget(self.letters_label, 5, 4, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        central_layout.setColumnMinimumWidth(0, 150)
        central_layout.setColumnMinimumWidth(1, 150)
        central_layout.setColumnMinimumWidth(2, 150)
        central_layout.setColumnMinimumWidth(3, 150)
        central_layout.setColumnMinimumWidth(4, 150)
        central_layout.setColumnMinimumWidth(5, 150)
        central_layout.setRowMinimumHeight(0, 25)
        central_layout.setRowMinimumHeight(1, 25)
        central_layout.setRowMinimumHeight(2, 25)
        central_layout.setRowMinimumHeight(3, 25)
        central_layout.setRowMinimumHeight(4, 25)
        central_layout.setRowMinimumHeight(5, 25)
        central_layout.setColumnStretch(0, 1)
        central_layout.setColumnStretch(1, 1)
        central_layout.setColumnStretch(2, 1)
        central_layout.setColumnStretch(3, 1)
        central_layout.setColumnStretch(4, 1)
        central_layout.setColumnStretch(5, 1)
        central_layout.setRowStretch(0, 1)
        central_layout.setRowStretch(1, 1)
        central_layout.setRowStretch(2, 1)
        central_layout.setRowStretch(3, 1)
        central_layout.setRowStretch(4, 1)
        central_layout.setRowStretch(5, 1)


        #Bottom layout

        self.bottom_label = QLabel("Реитинг, очки, и пр.")
        self.rating_button = QPushButton("Рейтнг")
        self.rating_button.clicked.connect(self.ratings_game)
        bottom_layout.addWidget(self.bottom_label)
        bottom_layout.addWidget(self.rating_button)

        #main widqet
        widget = QWidget()
        widget.setFixedSize(500, 500)
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

        file = open(resource_path('drum.gif'), "rb")
        ba = file.read()
        self.buffer = QBuffer()
        self.buffer.setData(ba)
        self.movie = QtGui.QMovie(self.buffer, QByteArray())
        self.the_drum.setMovie(self.movie)
        self.the_drum.setMargin(1)

    def login_window(self):
        login = ui_login.LoginWindow(self.user_box)
        login.exec()
        self.login_label.setText(f"Привет, {self.user_box[0].user_name}!")
        self.game_button.show()
        self.rating_button.show()
        self.bottom_label.show()

    def new_game(self):
        self.turn_button.show()
        self.the_drum.show()
        self.guess_hide()
        self.game_data = create_game(self.user_box[0])
        self.description_label.setText(self.game_data.word.description.capitalize())
        self.word.setText(self.game_data.word_to_show)
        self.turn_button.show()
        self.the_drum.show()
        self.guess_hide()


    def make_a_turn(self):
        self.game_data = turn_the_drum(self.game_data)
        self.the_drum.show()
        self.movie.start()
        self.turn_button.hide()
        self.guess_show()
        if self.game_data.ground.round_score:
            self.drum.setText(f"{self.game_data.ground.round_score} очка(-ов)")
        else:
            self.drum.setText(self.game_data.ground.round_prise)
            dlg = CustomDialog("Приз!", f"{self.game_data.ground.round_prise}\nЗабрать и закончить игру?")
            dlg.exec()
            if dlg.accepted == 1:
                self.guess_hide()
                self.turn_button.hide()
            else:
                self.turn_button.show()
                self.guess_hide()
                self.make_a_turn()


    def guess_a_letter(self):
        self.letters_label.show()
        letter = self.gues_l_edit.text()
        if letter:
            if len(letter) == 1:
                if letter in self.letters:
                    self.game_data.letters.add(letter.upper())
                    self.game_data = guess_a_letter(letter, self.game_data)
                    self.word.setText(self.game_data.word_to_show)
                    self.letters_label.setText(', '.join(self.game_data.letters))
                    if self.game_data.ground.is_word_guessed:
                        self.word.setText(f'Загаданное слово:{self.game_data.word.word.upper()}')
                        self.the_drum.hide()
                        self.drum.hide()
                    else:
                        self.turn_button.show()
                    self.guess_hide()
                else:
                    warning_window(f"Упсс!", "Для ввода доступны только\nбуквы русского алфавита")
            else:
                warning_window("Упсс!", "Введи ОДНУ букву")
        else:
            warning_window("Упсс!", "Введи букву")



    def guess_the_word(self):
        word = self.gues_w_edit.text()
        if word:
            if all(map(lambda x: x in self.letters, word)):
                self.game_data = guess_the_word(word, self.game_data)
                if self.game_data.ground.is_word_guessed:
                    self.word.setText(f'Загаданное слово:{self.game_data.word.word.upper()}')
                    self.the_drum.hide()
                    self.drum.hide()
                else:
                    ui_message.warning_window("Внимание", "Не верно, еще раз")
                    self.turn_button.show()
                self.guess_hide()
            else:
                warning_window("Упсс!", "Все еще по-русски говорим?")
        else:
            warning_window("Упсс!", "Введи слово")



    def ratings_game(self):
        #ui_message.warning_window("Ratings", "Coming soon!")
        stats = get_stats()
        rates = StatisticsWindow(stats, self.user_box[0])
        rates.exec()



    def startAnimation(self):
        self.movie.start()
        self.movie.setSpeed(400)
        sleep(0.5)
        self.movie.setSpeed(300)
        sleep(0.5)
        self.movie.setSpeed(200)
        sleep(0.5)

    # Stop Animation(According to need)
    def stopAnimation(self):
        self.movie.stop()

    def guess_show(self):
        self.gues_l_edit.show()
        self.gues_l_button.show()
        self.gues_w_edit.show()
        self.gues_w_button.show()

    def guess_hide(self):
        self.gues_l_edit.hide()
        self.gues_l_edit.clear()
        self.gues_l_button.hide()
        self.gues_w_edit.hide()
        self.gues_w_edit.clear()
        self.gues_w_button.hide()



app = QApplication(sys.argv)
ico = QtGui.QIcon(resource_path('fow.ico'))
app.setWindowIcon(ico)
w = MainWindow()
w.show()
if not w.user_box:
    w.game_button.hide()
    w.rating_button.hide()
    w.bottom_label.hide()
    w.letters_label.hide()
    w.stopAnimation()
if not w.game_data:
    w.gues_l_edit.hide()
    w.gues_l_button.hide()
    w.gues_w_edit.hide()
    w.gues_w_button.hide()
    w.turn_button.hide()
app.exec()