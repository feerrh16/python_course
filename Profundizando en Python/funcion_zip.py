# print(dir(__builtins__))
# help(zip)

numeros = [1, 2, 3]
letras = ['a', 'b', 'c', 'd']

# identificadores se convierte en una tupla automáticamente separando con ,
identificadores = 123, 124, 125, 126, 127, 128

# la variable conjunto es un set; toma un orden aleatorio cuando se usa
conjunto = {1, 67, 23, 76, 75, 212}
mezcla = zip(numeros, letras, identificadores, conjunto)
print(f'Objeto zip creado: {mezcla}')
print(f'Tipo de objeto: {type(mezcla)}')
print(f'Conversión en lista del objeto zip: {list(mezcla)}')
print(f'Conversión en una tupla del objeto zip: {tuple(zip(numeros, letras, identificadores, conjunto))}')
