from PySide6.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QStackedWidget,
    QVBoxLayout,
    QWidget
)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self._central_widget: QWidget = QWidget()
        self.setCentralWidget(self._central_widget)

        self._central_layout: QVBoxLayout = QVBoxLayout(self._central_widget)

        self._build_ui()

    def _build_ui(self):
        # TODO: Replace these implementations of the main content and navigation bar with QWidget subclasses for better
        #  encapsulation.
        self.main_content: QStackedWidget = QStackedWidget(self._central_widget)
        self._central_layout.addWidget(self.main_content)

        self._navigation_bar_widget: QWidget = QWidget(self._central_widget)
        self._navigation_bar_layout: QHBoxLayout = QHBoxLayout(self._navigation_bar_widget)
        self._central_layout.addWidget(self._navigation_bar_widget)
