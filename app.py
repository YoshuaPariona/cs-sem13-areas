import sys
from PyQt6.QtWidgets import QApplication
from src.vista.GUI_ui import Dialogo

def main():
    app = QApplication(sys.argv)
    ventana = Dialogo()
    ventana.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()