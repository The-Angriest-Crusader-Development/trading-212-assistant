from PySide6.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QWidget
)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        central_widget: QWidget = QWidget()
        self.setCentralWidget(central_widget)

        self._central_layout: QVBoxLayout = QVBoxLayout(central_widget)

        self._build_ui()

    def _build_ui(self):
        pass
