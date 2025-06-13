import sys
import os
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QApplication
from src.logica.CalculadoraArea import CalculadoraArea

class Dialogo(QMainWindow):
    def __init__(self):
        ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gui-calculadora-area.ui")
        super().__init__()
        uic.loadUi(ruta, self)

        # Conectar botones
        self.calcular_btn.clicked.connect(self.calcular_areas)
        self.salir_btn.clicked.connect(self.close)
        self.actionSalir.triggered.connect(self.close)

    def calcular_areas(self):
        try:
            # Validar que ningún campo esté vacío
            if not self.lado_input.text() or not self.radio_input.text() or not self.altura_input.text() or not self.base_input.text():
                QMessageBox.warning(self, "Advertencia", "Ningún campo puede estar vacío.")
                return

            # Obtener valores
            lado = float(self.lado_input.text())
            radio = float(self.radio_input.text())
            altura = float(self.altura_input.text())
            base = float(self.base_input.text())

            calculadora = CalculadoraArea(base=base, altura=altura, radio=radio, lado=lado)

            # Mostrar resultados redondeados
            self.lb_resultado.setText("Resultado")
            self.lb_area_de_cuadrado.setText(f"Área del cuadrado: {round(calculadora.area_cuadrado())}")
            self.lb_area_de_rectangulo.setText(f"Área del rectángulo: {round(calculadora.area_rectangulo())}")
            self.lb_area_de_triangulo.setText(f"Área del triángulo: {round(calculadora.area_triangulo())}")
            self.lb_area_de_circulo.setText(f"Área del círculo: {round(calculadora.area_circulo())}")

        except ValueError:
            QMessageBox.critical(self, "Error", "Por favor, introduce valores numéricos válidos.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Dialogo()
    ventana.show()
    sys.exit(app.exec())
