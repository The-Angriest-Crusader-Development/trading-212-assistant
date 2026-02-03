from PySide6.QtWidgets import QStackedWidget, QWidget


class MainContent(QStackedWidget):
    def __init__(self,
                 parent: QWidget | None = None) -> None:
        super().__init__(parent)
