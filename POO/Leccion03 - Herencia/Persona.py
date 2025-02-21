class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def __str__(self):
        return f'Objeto: {type(self)}\n' \
               f'Nombre: {self._nombre}\n' \
               f'Edad: {self._edad}\n'


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self._sueldo = sueldo

    def __str__(self):
        return f'{super().__str__()}\n' \
               f'Sueldo: {self._sueldo}\n'
