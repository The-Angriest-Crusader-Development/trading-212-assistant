from PySide6.QtWidgets import (
    QMainWindow,
    QStackedWidget,
    QVBoxLayout,
    QWidget
)

from .navigation_bar import NavigationBar


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self._central_widget: QWidget = QWidget()
        self.setCentralWidget(self._central_widget)

        self._central_layout: QVBoxLayout = QVBoxLayout(self._central_widget)
        self._central_layout.setContentsMargins(0, 0, 0, 0)
        self._central_layout.setSpacing(0)

        self._build_ui()

    def _build_ui(self):
        self.main_content: QStackedWidget = QStackedWidget(self._central_widget)
        self._central_layout.addWidget(self.main_content, 1)

        self._navigation_bar: NavigationBar = NavigationBar()
        self._central_layout.addWidget(self._navigation_bar, 0)
