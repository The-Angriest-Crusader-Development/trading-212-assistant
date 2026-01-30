from importlib.metadata import version
from sys import argv, exit as sys_exit

from PySide6.QtWidgets import QApplication, QMainWindow


APPLICATION_DISPLAY_NAME: str = 'Trading 212 Assistant'
APPLICATION_VERSION: str = version('trading-212-assistant')


def main() -> None:
    application: QApplication = QApplication(argv)
    main_window: QMainWindow = QMainWindow()
    main_window.setWindowTitle(f"{APPLICATION_DISPLAY_NAME} {APPLICATION_VERSION}")
    main_window.show()
    sys_exit(application.exec())
