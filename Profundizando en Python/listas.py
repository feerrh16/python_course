'''
Profundizando en listas
Recordemos que las listas son mutables, es decir, modificables
'''

# Creación clásica de una lista
nombres1 = ['Juan', 'Karla', 'Pedro']

# Creación de una lista con el método split()
nombres2 = 'Laura María Gonzalo Ernesto'.split()

# Sumar listas (No se modifican las listas originales)
print(f'Suma de listas: {nombres1 + nombres2}')

# Extender una lista sobre otra (Se modifica la lista asignada)
nombres1.extend(nombres2)
print(f'Extensión de la lista 1 con la lista 2: {nombres1}')

# Obtención de un índice de un elemento de la lista
numeros1 = [10, 40, 15, 4, 20, 90, 4]
print(f'Lista original: {numeros1}')
print(f'Índice número 4: {numeros1.index(4)}')

# Invertir orden de los elementos de una lista
numeros1.reverse()
print(f'Lista invertida: {numeros1}')

# Ordenar los elementos de una lista (orden ascendente)
numeros1.sort()
print(f'Lista ordenada ascendentemente: {numeros1}')

# Ordenar los elementos de una lista (orden descendente)
numeros1.sort(reverse = True)
print(f'Lista ordenada descendentemente: {numeros1}')

# Obtención de los valores máximo y mínimo de una lista
print(f'Valor mínimo: {min(numeros1)}')
print(f'Valor máximo: {max(numeros1)}')

# Copiar los elementos de una lista
# copy() realiza una copia de las referencias de los objetos contenidos en la lista a copiar
numeros2 = numeros1.copy()
print('Método copy()')
print(f'¿Es la misma referencia? {numeros1 is numeros2}')
print(f'¿Tienen el mismo contenido? {numeros1 == numeros2}')

# Podemos utilizar el constructor de la lista
numeros2 = list(numeros1)
print('Constructor de lista')
print(f'¿Es la misma referencia? {numeros1 is numeros2}')
print(f'¿Tienen el mismo contenido? {numeros1 == numeros2}')

# Slicing
numeros2 = numeros1[:]
print('Método slicing')
print(f'¿Es la misma referencia? {numeros1 is numeros2}')
print(f'¿Tienen el mismo contenido? {numeros1 == numeros2}')

# Lista de listas
# Multiplicación de listas
multiplicacion_lista = 5*[[2, 5]]
print(multiplicacion_lista)
print(f'¿Es la misma referencia? {multiplicacion_lista[0] is multiplicacion_lista[1]}')
print(f'¿Tienen el mismo contenido? {multiplicacion_lista[0] == multiplicacion_lista[1]}')
multiplicacion_lista[2].append(10)
print(multiplicacion_lista)

# Matrices
matriz = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
print(f'Matriz original: {matriz}')
print(f'Renglón 0, Columna 0: {matriz[0][0]}')
print(f'Renglón 2, Columna 3: {matriz[2][3]}')

# Modificar un valor (60)
matriz[2][0] = 65
print(f'Matriz modificada: {matriz}')

# Ordenanmiento de funciones de tipo built-in
lista_listas = [[10, 14, 87, 90, 71], [4, 5, 6, 7], [9, 0, 11, 15, 45, 61, 70]]
print(f'Lista de listas original: {lista_listas}')
lista_listas.sort(key=len)
print(f'Lista de listas ordenada: {lista_listas}')

# sorted built-in
nombres1 = ['Juan Carlos', 'Karla', 'Pedro', 'Esperanza']
print(f'Lista de nombres original: {nombres1}')
nombres1 = sorted(nombres1)
print(f'Lista de nombres ordenada alfabéticamente: {nombres1}')
nombres1 = sorted(nombres1, reverse = True)
print(f'Lista de nombres ordenada inversamente: {nombres1}')

# Ordenar por cantidad de caracteres
nombres1 = sorted(nombres1, key=len)
print(f'Lista de nombres ordenada por cantidad de caracteres: {nombres1}')

# Función reversed built-in
nombres1 = reversed(nombres1)
print(f'Lista de nombres ordenada inversamente con método built-in: {list(nombres1)}')
