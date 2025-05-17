from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel

class CustomDialog(QDialog):
    def __init__(self, title, mess):
        super().__init__()

        self.setWindowTitle(title)

        QBtn = (
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        message = QLabel(mess)
        layout.addWidget(message)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

