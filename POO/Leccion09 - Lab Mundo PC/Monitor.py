class Monitor:
    contador_monitores = 0

    def __init__(self, marca, tamaño):
        self._id_monitor = Monitor.generar_id_monitor()
        self._marca = marca
        self._tamaño = tamaño

    @property
    def marca(self):
        return self._marca
    
    @property
    def tamaño(self):
        return self._tamaño
    
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @tamaño.setter
    def tamaño(self, tamaño):
        self._tamaño = tamaño

    def __str__(self):
        return  f'ID Monitor: {self._id_monitor}\n' \
                f'Marca: {self._marca}\n' \
                f'Tamaño: {self._tamaño} pulgadas\n'

    @classmethod
    def generar_id_monitor(cls):
        cls.contador_monitores += 1
        return cls.contador_monitores
    

if __name__ == '__main__':
    monitor1 = Monitor('Samsung', 50)
    print(monitor1)

    monitor2 = Monitor('Sony', 35)
    print(monitor2)
