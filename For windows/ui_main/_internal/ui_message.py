from PyQt6.QtWidgets import QMessageBox

def warning_window(title, text):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.exec()