from collections.abc import Sequence
from dataclasses import dataclass

from PySide6.QtWidgets import QWidget


@dataclass(frozen=True)
class PageDefinition:
    display_name: str
    factory: type[QWidget]
    key: str


# TODO: Create real pages for these PageDefinition factories.
PAGE_DEFINITIONS: Sequence[PageDefinition] = (
    PageDefinition(display_name='Home', factory=QWidget, key='home'),
    PageDefinition(display_name='S&S ISA', factory=QWidget, key='s&s isa'),
    PageDefinition(display_name='CFD', factory=QWidget, key='cfd')
)
