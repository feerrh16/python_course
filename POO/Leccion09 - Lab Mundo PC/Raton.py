from DispositivoEntrada import *

class Raton(DispositivoEntrada):
    contador_ratones = 0
    
    def __init__(self, tipo_entrada, marca):
        self._id_raton = Raton.generar_id_raton()
        super().__init__(tipo_entrada, marca)

    @classmethod
    def generar_id_raton(cls):
        cls.contador_ratones += 1
        return cls.contador_ratones
    
    def __str__(self):
        return  f'ID Ratón: {self._id_raton}\n' \
                f'{super().__str__()}'
    

if __name__ == '__main__':
    raton1 = Raton('USB', 'Logitech')
    print(raton1)

    raton2 = Raton('Bluetooth', 'Razer')
    print(raton2)
