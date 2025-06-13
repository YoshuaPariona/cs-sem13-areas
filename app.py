"""
Este módulo es el punto de entrada principal para la aplicación de calculadora de áreas geométricas.
Inicializa y ejecuta la interfaz gráfica de usuario utilizando PyQt6.
"""

import sys
from PyQt6.QtWidgets import QApplication
from src.vista.gui_ui import Dialogo


def main():
    """
    Función principal que inicializa y ejecuta la aplicación PyQt6.
    Crea una instancia de QApplication y muestra la ventana principal de la aplicación.
    """
    app = QApplication(sys.argv)
    ventana = Dialogo()
    ventana.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
