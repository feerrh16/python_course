class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, ID: {hex(id(self)).upper()}'
    
persona1 = Persona('Juan', 'Pérez')
print(persona1)
