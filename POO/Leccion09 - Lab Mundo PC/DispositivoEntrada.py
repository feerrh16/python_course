class DispositivoEntrada:
    def __init__(self, tipo_entrada, marca):
        self._tipo_entrada = tipo_entrada
        self._marca = marca
    
    @property
    def tipo_entrada(self):
        return self._tipo_entrada
    
    @property
    def marca(self):
        return self._marca
    
    @tipo_entrada.setter
    def tipo_entrada(self, tipo_entrada):
        self._tipo_entrada = tipo_entrada
        
    @marca.setter
    def marca(self, marca):
        self._marca = marca 
    
    def __str__(self):
        return  f'Tipo de entrada: {self._tipo_entrada}\n' \
                f'Marca del dispositivo: {self._marca}\n'
    