from importlib.metadata import version
from sys import argv, exit as sys_exit

from PySide6.QtWidgets import QApplication, QMainWindow


def main() -> None:
    application: QApplication = QApplication(argv)
    main_window: QMainWindow = QMainWindow()
    main_window.setWindowTitle(f"Trading 212 Assistant {version('trading-212-assistant')}")
    main_window.show()
    sys_exit(application.exec())
