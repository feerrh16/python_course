from FiguraGeometrica import *
from Color import *

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self._alto * self._ancho

    def __str__(self):
        return  f'{FiguraGeometrica.__str__(self)}\n' \
                f'{Color.__str__(self)}' \
                f'Área: {self.calcular_area()}\n'
