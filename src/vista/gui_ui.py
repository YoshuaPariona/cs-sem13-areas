"""
Este módulo define la interfaz gráfica de usuario para una calculadora de áreas geométricas.
Utiliza PyQt6 para cargar la interfaz de usuario desde un archivo .ui y calcular áreas de diferentes
formas geométricas.
"""

import sys
import os
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QApplication
from PyQt6 import uic
from src.logica.calculadora_area import CalculadoraArea


class Dialogo(QMainWindow):
    """
    Clase principal de la interfaz gráfica de usuario para la calculadora de áreas.
    Carga la interfaz desde un archivo .ui y conecta los botones a sus respectivas funciones.
    """

    def __init__(self):
        """
        Inicializa la ventana principal de la aplicación.
        Carga la interfaz de usuario desde un archivo .ui y conecta los botones a sus funciones.
        """
        ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gui-calculadora-area.ui")
        super().__init__()
        uic.loadUi(ruta, self)

        # Conectar botones
        self.calcular_btn.clicked.connect(self.calcular_areas)
        self.salir_btn.clicked.connect(self.close)
        self.actionSalir.triggered.connect(self.close)

    def calcular_areas(self):
        """
        Calcula las áreas de diferentes formas geométricas basadas en las entradas del usuario.
        """
        if not self.validar_campos():
            return

        self.calcular_area_cuadrado()
        self.calcular_area_rectangulo()
        self.calcular_area_triangulo()
        self.calcular_area_circulo()

    def validar_campos(self):
        """
        Valida que ningún campo esté vacío.

        Retorna:
        bool: True si todos los campos tienen valores válidos, False en caso contrario.
        """
        if (not self.lado_input.text() or not self.radio_input.text() or
                not self.altura_input.text() or not self.base_input.text()):
            QMessageBox.warning(self, "Advertencia", "Ningún campo puede estar vacío.")
            return False
        return True

    def calcular_area_cuadrado(self):
        """
        Calcula y muestra el área de un cuadrado.
        """
        lado = float(self.lado_input.text())
        calculadora = CalculadoraArea(lado=lado)
        self.area_de_cuadrado.setText(f"Área del cuadrado: {round(calculadora.area_cuadrado())}")

    def calcular_area_rectangulo(self):
        """
        Calcula y muestra el área de un rectángulo.
        """
        base = float(self.base_input.text())
        altura = float(self.altura_input.text())
        calculadora = CalculadoraArea(base=base, altura=altura)
        self.area_de_rectangulo.setText(
            f"Área del rectángulo: {round(calculadora.area_rectangulo())}"
        )

    def calcular_area_triangulo(self):
        """
        Calcula y muestra el área de un triángulo.
        """
        base = float(self.base_input.text())
        altura = float(self.altura_input.text())
        calculadora = CalculadoraArea(base=base, altura=altura)
        self.area_de_triangulo.setText(f"Área del triángulo: {round(calculadora.area_triangulo())}")

    def calcular_area_circulo(self):
        """
        Calcula y muestra el área de un círculo.
        """
        radio = float(self.radio_input.text())
        calculadora = CalculadoraArea(radio=radio)
        self.area_de_circulo.setText(f"Área del círculo: {round(calculadora.area_circulo())}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Dialogo()
    ventana.show()
    sys.exit(app.exec())
