import sys
import os

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QApplication
from src.logica.CalculadoraInteresCompuesto import CalculadoraInteresCompuesto


class Dialogo (QMainWindow):
    def __init__(self):
        ruta = os.path.dirname ( os.path.abspath ( __file__ ) ) + r"\gui-interes-compuesto.ui"
        QMainWindow.__init__(self)
        uic.loadUi(ruta,self)

        self.calcular_btn.clicked.connect(self.calcular_interes)
        self.salir_btn.clicked.connect(self.close)
        self.actionSalir.triggered.connect(self.close)

    def calcular_interes( self ):
        try:
            P = float(self.principal_input.text())
            r = float(self.tasa_input.text())
            t = float(self.tiempo_input.text())
            n = int(self.periodo_input.text())

            calculadora = CalculadoraInteresCompuesto(P, r, t, n)
            resultado = calculadora.calcular()
            self.resultado_label.setText(f"Resultado: ${resultado}")
        except ValueError:
            QMessageBox.critical(self, "Error", "Por favor, introduce valores numéricos válidos.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogo=Dialogo()
    dialogo.show()
    sys.exit(app.exec())
