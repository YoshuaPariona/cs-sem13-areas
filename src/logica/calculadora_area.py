"""
Este módulo define una calculadora de áreas para diferentes formas geométricas.
Incluye métodos para calcular el área de un círculo, cuadrado, rectángulo y triángulo.
"""

import math

class CalculadoraArea:
    """
    Clase para calcular áreas de diferentes formas geométricas.
    Proporciona métodos para calcular áreas basados en las dimensiones proporcionadas.
    """

    def __init__(self, base=None, altura=None, radio=None, lado=None):
        """
        Inicializa la calculadora de áreas con las dimensiones proporcionadas.

        Parámetros:
        base (float, opcional): La base de la figura. Usada para rectángulos y triángulos.
        altura (float, opcional): La altura de la figura. Usada para rectángulos y triángulos.
        radio (float, opcional): El radio del círculo.
        lado (float, opcional): La longitud del lado del cuadrado.
        """
        self.base = base
        self.altura = altura
        self.radio = radio
        self.lado = lado

    def area_circulo(self):
        """
        Calcula el área de un círculo.

        Retorna:
        float: El área del círculo redondeada a dos decimales.
        """
        return round(math.pi * self.radio ** 2, 2)

    def area_cuadrado(self):
        """
        Calcula el área de un cuadrado.

        Retorna:
        float: El área del cuadrado redondeada a dos decimales.
        """
        return round(self.lado ** 2, 2)

    def area_rectangulo(self):
        """
        Calcula el área de un rectángulo.

        Retorna:
        float: El área del rectángulo redondeada a dos decimales.
        """
        return round(self.base * self.altura, 2)

    def area_triangulo(self):
        """
        Calcula el área de un triángulo.

        Retorna:
        float: El área del triángulo redondeada a dos decimales.
        """
        return round((self.base * self.altura) / 2, 2)
