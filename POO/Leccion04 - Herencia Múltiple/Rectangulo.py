from FiguraGeometrica import *
from Color import *

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, ancho, alto, color):
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)

    def calcular_area(self):
        return self._ancho * self._alto
    
    def __str__(self):
        return  f'{FiguraGeometrica.__str__(self)}\n' \
                f'{Color.__str__(self)}' \
                f'Área: {self.calcular_area()}\n'
    