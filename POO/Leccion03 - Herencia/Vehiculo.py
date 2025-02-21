class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'Objeto de tipo: {type(self)}\n' \
               f'Color: {self.color}\n' \
               f'Número de ruedas: {self.ruedas}\n'


class Bicicleta(Vehiculo):
    def __init__(self, tipo, color, ruedas):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'{super().__str__()}' \
               f'Tipo de bicicleta: {self.tipo}\n'


class Coche(Vehiculo):
    def __init__(self, velocidad, color, ruedas):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f'{super().__str__()}' \
               f'Velocidad del Vehículo: {self.velocidad} km/h\n'


vehiculo1 = Vehiculo('negro', 3)
print(vehiculo1)

bici1 = Bicicleta('bmx', 'azul', 2)
print(bici1)

coche1 = Coche(210, 'rojo', 4)
print(coche1)
