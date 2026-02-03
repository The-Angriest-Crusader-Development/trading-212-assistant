from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class HomePage(QWidget):
    def __init__(
        self,
        parent: QWidget | None = None
    ) -> None:
        super().__init__(parent)
        self._layout = QVBoxLayout(self)
        self._layout.addWidget(QLabel('Home'))
