import sys

from PyQt6.QtWidgets import QApplication
from src.vista.GUI_ui import Dialogo

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogo=Dialogo()
    dialogo.show()
    sys.exit(app.exec())