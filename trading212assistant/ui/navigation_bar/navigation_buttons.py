from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QPushButton,
    QScrollArea,
    QWidget
)


class NavigationButtons(QScrollArea):
    def __init__(self,
                 parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.setWidgetResizable(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self._container: QWidget = QWidget()
        self._layout: QHBoxLayout = QHBoxLayout(self._container)

        # These are just placeholder buttons
        self._buttons: list[QPushButton] = []
        for i in range(20):
            button: QPushButton = QPushButton(f"Button {i}")
            self._layout.addWidget(button)
            self._buttons.append(button)

        self.setWidget(self._container)
