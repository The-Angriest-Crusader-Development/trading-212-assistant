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

        self.setFixedHeight(self.sizeHint().height())
        self.setWidgetResizable(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self._container: QWidget = QWidget()
        self._layout: QHBoxLayout = QHBoxLayout(self._container)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        # These are just placeholder buttons
        self._buttons: list[QPushButton] = []
        for i in range(20):
            button: QPushButton = QPushButton(f"Button {i}")
            self._layout.addWidget(button)
            self._buttons.append(button)

        self.setWidget(self._container)

        container_height = self._container.sizeHint().height()
        horizontal_scrollbar_height = self.horizontalScrollBar().sizeHint().height()
        self.setFixedHeight(container_height + horizontal_scrollbar_height + self.frameWidth() * 2)
