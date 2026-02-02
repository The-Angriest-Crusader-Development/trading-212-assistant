from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QScrollArea, QWidget


class NavigationBar(QWidget):
    def __init__(self,
                 parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self._layout: QHBoxLayout = QHBoxLayout(self)
