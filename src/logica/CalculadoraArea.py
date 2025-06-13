import math

class CalculadoraArea:
    def __init__(self, base=None, altura=None, radio=None, lado=None):
        self.base = base
        self.altura = altura
        self.radio = radio
        self.lado = lado

    def area_circulo(self):
        return round(math.pi * self.radio ** 2, 2)

    def area_cuadrado(self):
        return round(self.lado ** 2, 2)

    def area_rectangulo(self):
        return round(self.base * self.altura, 2)

    def area_triangulo(self):
        return round((self.base * self.altura) / 2, 2)