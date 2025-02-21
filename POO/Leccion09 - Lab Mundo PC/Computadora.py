from DispositivoEntrada import *
from Raton import *
from Teclado import *
from Monitor import *

class Computadora:
    contador_computadoras = 0

    def __init__(self, nombre_pc, raton, teclado, monitor):
        self._id_computadora = Computadora.generar_id_computadora()
        self._nombre_pc = nombre_pc
        self._raton = raton
        self._teclado = teclado
        self._monitor = monitor

    @classmethod
    def generar_id_computadora(cls):
        cls.contador_computadoras += 1
        return cls.contador_computadoras
    
    def __str__(self):
        return  f'{self._nombre_pc}: {self._id_computadora}\n' \
                f'Ratón:\n{self._raton}\n' \
                f'Teclado:\n{self._teclado}\n' \
                f'Monitor:\n{self._monitor}\n' \
                
    
if __name__ == '__main__':
    raton1 = Raton('USB', 'Logitech')
    teclado1 = Teclado('USB', 'Razer')
    monitor1 = Monitor('Samsung', 60)
    computadora1 = Computadora('PC Ofimática', raton1, teclado1, monitor1)
    print(computadora1)    
