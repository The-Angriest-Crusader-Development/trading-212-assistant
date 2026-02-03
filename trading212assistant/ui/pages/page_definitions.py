from collections.abc import Sequence
from dataclasses import dataclass

from PySide6.QtWidgets import QWidget

from .cfd_page import CfdPage
from .home_page import HomePage
from .s_and_s_isa_page import SAndSIsaPage


@dataclass(frozen=True)
class PageDefinition:
    display_name: str
    factory: type[QWidget]
    key: str


# TODO: Create real pages for these PageDefinition factories.
PAGE_DEFINITIONS: Sequence[PageDefinition] = (
    PageDefinition(display_name='Home', factory=HomePage, key='home'),
    PageDefinition(display_name='S&S ISA', factory=SAndSIsaPage, key='s and s isa'),
    PageDefinition(display_name='CFD', factory=CfdPage, key='cfd')
)
