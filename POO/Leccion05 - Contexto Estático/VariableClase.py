class VariableClase:
    # Variable asociada con la clase
    var_clase = 'Valor de la variable de clase'

    def __init__(self, var_instancia):
        # Variable asociada con un objeto creado a partir de la clase
        self._var_instancia = var_instancia

    @staticmethod
    def metodo_estatico():
        # Acceso a la variable de clase de forma indirecta
        print(VariableClase.var_clase)

    @classmethod
    def metodo_clase(cls):
        print(cls.var_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.var_clase)
        print(self._var_instancia)

# Acceso a variable de clase
print(VariableClase.var_clase)

# Acceso a variable de instancia
objeto1 = VariableClase('Valor de la variable de instancia')
print(objeto1._var_instancia)
print(objeto1.var_clase)

objeto2 = VariableClase('Otro valor de la variable de instancia')
print(objeto2._var_instancia)
print(objeto2.var_clase)

# Creación de variables de clase "al vuelo" (al momento)
VariableClase.var_clase2 = 'Nueva variable de clase'
print(VariableClase.var_clase2)
print('Objeto 1 accediendo a variables de instancia y de clase')
print(objeto1._var_instancia)
print(objeto1.var_clase)
print(VariableClase.var_clase2)

print('Objeto 2 accediendo a variables de instancia y de clase')
print(objeto2._var_instancia)
print(objeto2.var_clase)
print(VariableClase.var_clase2)

# Invocando al método estático
VariableClase.metodo_estatico()

# Invocando al método de clase
VariableClase.metodo_clase()

# Invocando al método de Instancia
objeto3 = VariableClase('Variable de instancia')
objeto3.metodo_clase()
objeto3.metodo_instancia()
