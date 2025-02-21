from DispositivoEntrada import *

class Teclado(DispositivoEntrada):
    contador_teclados = 0

    def __init__(self, tipo_entrada, marca):
        self._id_teclado = Teclado.generar_id_teclado()
        super().__init__(tipo_entrada, marca)

    @classmethod
    def generar_id_teclado(cls):
        cls.contador_teclados += 1
        return cls.contador_teclados
    
    def __str__(self):
        return  f'ID Teclado: {self._id_teclado}\n' \
                f'{super().__str__()}'
    

if __name__ == '__main__':
    teclado1 = Teclado('USB', 'Custom')
    print(teclado1)

    teclado2 = Teclado('Bluetooth', 'Nuphy')
    print(teclado2)
