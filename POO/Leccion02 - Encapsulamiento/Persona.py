# Clase persona

class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    # Métodos get
    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def edad(self):
        return self._edad

    # Métodos set
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrar_info(self):
        print(f'La información contenida en el objeto Persona es la siguiente:\n'.center(50, '-'),
              f'Nombre: {self._nombre}'.center(50, '-'), f'\n',
              f'Apellido: {self._apellido}'.center(50, '-'), f'\n',
              f'Edad: {self._edad}'.center(50, '-'), f'\n')

    def __del__(self):
        print(f'El Objeto {self._nombre} {self._apellido} ha sido borrado'.center(50, '-'))


if __name__ == 'main':

    print(f'Módulo en ejecución: {__name__}'.center(50, '-'))

    persona1 = Persona('Juan', 'Pérez', 28)
    persona1.mostrar_info()

    persona2 = Persona('Karla', 'Gómez', 30)
    persona2.mostrar_info()

    persona3 = Persona('Sergio', 'Rodríguez', 23)
    persona3.mostrar_info()
