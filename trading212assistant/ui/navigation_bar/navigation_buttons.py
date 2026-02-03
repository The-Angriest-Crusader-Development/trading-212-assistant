from PySide6.QtCore import Qt, QSize, Signal
from PySide6.QtWidgets import (
    QHBoxLayout,
    QPushButton,
    QScrollArea,
    QWidget
)

from ..pages import PAGE_DEFINITIONS


class NavigationButtons(QScrollArea):
    page_requested: Signal = Signal(str)

    def __init__(self,
                 parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.setWidgetResizable(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        self._container: QWidget = QWidget()
        self._layout: QHBoxLayout = QHBoxLayout(self._container)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        self._buttons: list[QPushButton] = []
        for page_definition in PAGE_DEFINITIONS:
            button: QPushButton = QPushButton(page_definition.display_name.replace('&', '&&'))
            button.clicked.connect(lambda _, page_key=page_definition.key: self.page_requested.emit(page_key))
            self._layout.addWidget(button)
            self._buttons.append(button)

        self.setWidget(self._container)

        self.setFixedHeight(self.sizeHint().height())

    def sizeHint(self) -> QSize:
        if not hasattr(self, '_container'):
            return super().sizeHint()

        container_height = self._container.sizeHint().height()
        horizontal_scrollbar_height = self.horizontalScrollBar().sizeHint().height()
        return QSize(super().sizeHint().width(), container_height + horizontal_scrollbar_height + self.frameWidth() * 2)
