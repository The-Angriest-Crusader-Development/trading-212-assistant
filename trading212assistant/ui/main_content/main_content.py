from PySide6.QtWidgets import QStackedWidget, QWidget


class MainContent(QStackedWidget):
    def __init__(self,
                 parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._page_registry: dict[str, QWidget] = {}

    def _register_page(self,
                       key: str,
                       widget: QWidget) -> None:
        self.addWidget(widget)
        self._page_registry[key] = widget

    def show_page(self,
                  page_key: str) -> None:
        widget: QWidget = self._page_registry[page_key]
        index: int = self.indexOf(widget)

        if index == -1:
            self.setCurrentIndex(index)
