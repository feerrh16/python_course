from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        # Validaciones
        if self.validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor no procesable en ancho ({ancho})')
        
        if self.validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f'Valor no procesable en alto ({alto})')

    # Métodos get
        @property
        def ancho(self):
            return self._ancho
        
        @property
        def alto(self):
            return self._alto
        
    # Métodos set
        @ancho.setter
        def ancho(self, ancho):
            if self.validar_valor(ancho):
                self._ancho = ancho
            else:
                print(f'Valor no procesable en ancho ({ancho})')

        @alto.setter
        def alto(self, alto):
            if self.validar_valor(alto):
                self._alto = alto
            else:
                print(f'Valor no procesable en alto ({alto})')

    # Método Abstracto
        @abstractmethod
        def calcular_area(self):
            pass 

    def __str__(self):
        return  f'Objeto: {type(self)}\n' \
                f'Alto: {self._alto}\n' \
                f'Ancho: {self._ancho}'

    def validar_valor(self, valor):
        return True if 0 < valor < 10 else False