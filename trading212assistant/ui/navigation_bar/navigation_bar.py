from PySide6.QtWidgets import QHBoxLayout, QWidget

from .navigation_buttons import NavigationButtons


class NavigationBar(QWidget):
    def __init__(self,
                 parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self._layout: QHBoxLayout = QHBoxLayout(self)

        self._navigation_buttons: NavigationButtons = NavigationButtons(self)
        self._layout.addWidget(self._navigation_buttons)
