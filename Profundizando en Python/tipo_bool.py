"""
bool contiene los valores de True y False
Tipos numéricos: False para 0 y True para los demás valores
Tipo str: False para '' y True para los demás valores
Tipo colecciones: False para colecciones vacías, True para los demás valores
"""

valor = 0
resultado = bool(valor)
print(f'Tipo de dato: {type(valor)}')
print(f'Valor: {valor}')
print(f'Resultado: {resultado}')
print('\n')

valor = 15
resultado = bool(valor)
print(f'Tipo de dato: {type(valor)}')
print(f'Valor: {valor}')
print(f'Resultado: {resultado}')
print('\n')

valor = ''
resultado = bool(valor)
print(f'Tipo de dato: {type(valor)}')
print(f'Valor: {valor}')
print(f'Resultado: {resultado}')
print('\n')

valor = 'Hola, Mundo!'
resultado = bool(valor)
print(f'Tipo de dato: {type(valor)}')
print(f'Valor: {valor}')
print(f'Resultado: {resultado}')
print('\n')

# Listas
valor = []
resultado = bool(valor)
print(f'Tipo de dato: {type(valor)}')
print(f'Valor: {valor}')
print(f'Resultado: {resultado}')
print('\n')

valor = ['Carlos', 'José', 'Rodrigo']
resultado = bool(valor)
print(f'Tipo de dato: {type(valor)}')
print(f'Valor: {valor}')
print(f'Resultado: {resultado}')
print('\n')

# Tuplas
valor = ()
resultado = bool(valor)
print(f'Tipo de dato: {type(valor)}')
print(f'Valor: {valor}')
print(f'Resultado: {resultado}')
print('\n')

valor = ('Carlos', 'José', 'Rodrigo')
resultado = bool(valor)
print(f'Tipo de dato: {type(valor)}')
print(f'Valor: {valor}')
print(f'Resultado: {resultado}')
print('\n')

# Diccionarios
valor = {}
resultado = bool(valor)
print(f'Tipo de dato: {type(valor)}')
print(f'Valor: {valor}')
print(f'Resultado: {resultado}')
print('\n')

valor = {'nombre':'Carlos', 'apellido':'Pérez'}
resultado = bool(valor)
print(f'Tipo de dato: {type(valor)}')
print(f'Valor: {valor}')
print(f'Resultado: {resultado}')
print('\n')

if bool(''):
    print('Regresa True\n')
else:
    print('Regresa False\n')

# Se hace da manera implícita la conversión a bool en las sentencias de control
if 'Hola, Mundo!':
    print('Regresa True\n')
else:
    print('Regresa False\n')
# Recordemos que podemos pasarle cualquier tipo de dato visto anteriormente a una sentencia de control
    
while '':
    print('Ejecución del ciclo While: True\n')
else:
    print('Fin del ciclo While: False\n')

while '1':
    print('Ejecución del ciclo While: True\n')
    break
else:
    print('Fin del ciclo While: False\n')
