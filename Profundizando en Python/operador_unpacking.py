# * sirve para desempaquetar
numeros = [1, 2, 3]
print(f'Se imprime la lista "numeros":')
print(numeros)

# Para imprimir cada valor de la lista utilizamos un packing
print(f'Se imprimen los valores de la lista numeros:')
print(*numeros)

#Utilizando el separador personalizado:
print(f'Se imprimen los valores de la lista numeros, con separador personalizado:')
print(*numeros, sep=' - ')

# Definimos la función Suma para pasarle argumentos variables
def Suma(a, b, c):
    print(f'Resultado de la suma: {a + b + c}')

# Suma(*numeros)

# Uso de funciones para unpacking de Argumentos
def sumar(a, b, c):
    print(f'Resultado de la suma: {a + b + c}')

# Al utilizar el operador unpacking se desempaqueta el contenido de la lista
# como agumentos de la función.
sumar(*numeros)

# Extraer elementos de cualquier iterable
mi_lista=[1, 2, 3, 4, 5, 6]
# La variable con el operador unpacking toma el resto de valores de la lista
a, *b, c, d = mi_lista
print(a, b, c, d)

# Recordemos que el uso de *_ es para elementos que se descartarán

# Unir lista
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [lista1, lista2]
print(f'Lista de listas / Matriz: {lista3}')

lista3 = [*lista1, *lista2]
print(f'Unión de listas (uso de unpacking): {lista3}')


# Puede ser utilizado para unir diccionarios, pero con **
dic1 = {'A':1, 'B':2, 'C':3}
dic2 = {'D':4, 'E':5}
dic3 = {**dic1, **dic2}
print(f'Unión de diccionarios con unpacking: {dic3}')

# Construcción de una lista a partir de un string
lista = [*'Hola mundo']
print(lista)
# Desempaquetado de la lista; imprimir elemento a elemento
print(*lista, sep=' ')
