from PySide6.QtWidgets import QStackedWidget, QWidget

from ..pages import PAGE_DEFINITIONS


class MainContent(QStackedWidget):
    def __init__(self,
                 parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._page_registry: dict[str, QWidget] = {}
        self._register_default_pages()

    def _register_default_pages(self) -> None:
        for page_definition in PAGE_DEFINITIONS:
            self._register_page(
                page_definition.key,
                page_definition.factory()
            )

    def _register_page(self,
                       key: str,
                       widget: QWidget) -> None:
        self.addWidget(widget)
        self._page_registry[key] = widget

    def show_page(self,
                  page_key: str) -> None:
        widget: QWidget = self._page_registry.get(page_key)

        if not widget:
            return

        index: int = self.indexOf(widget)

        if index == -1:
            return

        self.setCurrentIndex(index)
