from importlib.metadata import version
from sys import argv, exit as sys_exit

from PySide6.QtWidgets import QApplication

from .ui import MainWindow


APPLICATION_DISPLAY_NAME: str = 'Trading 212 Assistant'
APPLICATION_VERSION: str = version('trading-212-assistant')


def main() -> None:
    application: QApplication = QApplication(argv)

    main_window: MainWindow = MainWindow()
    main_window.setWindowTitle(f"{APPLICATION_DISPLAY_NAME} {APPLICATION_VERSION}")
    main_window.show()

    sys_exit(application.exec())
