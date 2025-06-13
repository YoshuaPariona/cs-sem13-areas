# src/logica/GUI-ui.py

class CalculadoraInteresCompuesto:
    """
    Clase para calcular interés compuesto.
    """

    def __init__(self, principal: float, tasa: float, tiempo: float, periodos: int):
        self.principal = principal
        self.tasa = tasa
        self.tiempo = tiempo
        self.periodos = periodos

    def calcular(self) -> float:
        """
        Calcula el monto acumulado con interés compuesto.
        A = P * (1 + r/n)^(nt)
        """
        monto = self.principal * (1 + self.tasa / self.periodos) ** (self.periodos * self.tiempo)
        return round(monto, 2)
