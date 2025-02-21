class Persona:
    # Variable de clase
    contador_personas = 0

    def __init__(self, nombre, edad):
        self.id_persona = Persona.generar_siguiente_valor()

        if self.validar_nombre(nombre):
            self._nombre = nombre
        else:
            return False
        
        if self.validar_edad(edad):
            self._edad = edad
        else:
            return False
        
    # Métodos get
    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self): 
        return self._edad

    # Métodos set
    @nombre.setter
    def nombre(self, nombre):
        if self.validar_nombre(nombre):
            self._nombre = nombre
        else:
            print(f'Error: Ingrese un nombre válido')

    @edad.setter
    def edad(self, edad):
        if self.validar_edad(edad):
            self._edad = edad
        else:
            print(f'Error: Ingrese una edad válida')

    # Validaciones
    def validar_nombre(self, nombre):
        return True if nombre != '' else False
    
    def validar_edad(self, edad):
        return True if 1 < edad < 99 else False
    
    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas
    
    def __str__(self):
        return  f'Nombre: {self._nombre}\n' \
                f'Edad: {self._edad}\n' \
                f'ID: {self.id_persona}\n' \

persona1 = Persona('Juan', 23)
print(persona1)

persona2 = Persona('Karla', 29)
print(persona2)
