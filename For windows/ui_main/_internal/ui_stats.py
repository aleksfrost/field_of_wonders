
from PyQt6.QtWidgets import (
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QDialog,
    QGridLayout,
    QTableWidget,
    QTableWidgetItem,
)

from PyQt6.QtGui import QColor

from ui_message import warning_window
import users


class StatisticsWindow(QDialog):
    """
    This "window" is a QDialog.
    It blocks main window.
    """
    def __init__(self, stats: list, user: users.User = None):
        super().__init__()
        self.lines = len(stats)
        self.rows = len(stats[0])
        self.setWindowTitle("Statistics")
        self.stats = QTableWidget(self.lines, self.rows)

        self.stats.setHorizontalHeaderLabels(("Игрок", "Очки", "Победы"))
        self.stats.setSortingEnabled(True)
        for line in range(self.lines):
            if stats[line][0] == user.user_name:
                for item in range(self.rows):
                    cellifo = QTableWidgetItem(str(stats[line][item]))
                    cellifo.setBackground(QColor(0, 255, 0))
                    self.stats.setItem(line, item, cellifo)
            else:
                for item in range(self.rows):
                    cellifo = QTableWidgetItem(str(stats[line][item]))
                    self.stats.setItem(line, item, cellifo)

        self.stats.show()

        # prises = get_prises_to_buy()
        # prises_lines = len(prises)
        # prises_rows = len(prises[0])
        # self.prises = QTableWidget(prises_lines, prises_rows)
        # self.prises.setHorizontalHeaderLabels(("Приз", "Скидка", "Стоимость скидки", "Категория"))
        # self.prises.setSortingEnabled(True)
        # for line in range(prises_lines):
        #     for item in range(prises_rows):
        #         cellifo = QTableWidgetItem(str(prises[line][item]))
        #         self.prises.setItem(line, item, cellifo)

        # self.prises.show()

        self.spend_button = QPushButton("Потратить")
        self.exit_button = QPushButton("Выход")

        stats_layout = QGridLayout()
        buttons_layout = QHBoxLayout()

        stats_layout.addWidget(self.stats)
        buttons_layout.addWidget(self.exit_button)
        buttons_layout.addWidget(self.spend_button)

        layout = QVBoxLayout()
        layout.addLayout(stats_layout)
        layout.addLayout(buttons_layout)

        self.exit_button.clicked.connect(self.ok_exit)
        self.spend_button.clicked.connect(self.spend_scores)

        self.setLayout(layout)

    def ok_exit(self):
        self.close()

    def spend_scores(self):
        warning_window("В разработке", "Для приобретения купонов\nвоспользуйтесь web версией приложения")


