from mi_clase import *
import math

# Profundizando en el tipo str

# Concatenación "clásica" con el operador +
# mensaje = 'Hola' + 'Mundo!'

# Concatenación automática en Python (no se requiere el operador +, excepto para variables)
variable = 'Adiós'
mensaje = 'Hola' 'Mundo!' + variable
mensaje += 'Universidad' 'Python'
print(mensaje)

# Acceso a la ayuda de Python
help(str)
help(str.capitalize)
help(math)
help(str)
help(MiClase)

# LLamada de documentación de la clase (sólo la documentación):
print(MiClase.__doc__)

# Llamada de documentación del método inicializador de la clase
print(MiClase.__init__.__doc__)

# Llamada de documentación del método creado por nosotros
print(MiClase.mi_metodo.__doc__)

# Inmutabilidad de los datos de tipo str
mensaje1 = 'hola, mundo!'
mensaje2 = mensaje1.capitalize()
print(f'Mensaje 1: {mensaje1}, ID: {hex(id(mensaje1))}')
print(f'Mensaje 2: {mensaje2}, ID: {hex(id(mensaje2))}')
mensaje1 += 'Adiós'
print(f'Mensaje 1: {mensaje1}, ID: {hex(id(mensaje1))}')

# Método join
tupla_str = ('Hola', 'Mundo', 'Universidad', 'Python')
mensaje = ' '.join(tupla_str)
print(f'Mensaje: {mensaje}')

lista_cursos = ['Java', 'Python' 'Angular', 'Spring']
mensaje = ', '.join(lista_cursos)
print(f'Mensaje: {mensaje}')

cadena = 'Hola, Mundo!'
mensaje = '.'.join(cadena)
print(f'Mensaje: {mensaje}')

diccionario = {'nombre':'Juan', 'apellido':'Pérez', 'edad':'18'}
llaves = '|'.join(diccionario.keys())
valores = '|'.join(diccionario.values())
print(f'Llaves: {llaves}, Tipo de dato: {type(llaves)}')
print(f'Valores: {valores}, Tipo de dato: {type(llaves)}')

# Método split
cursos = 'Java Python JavaScript Angular Spring Excel'
lista_cursos = cursos.split()
print(f'Lista de cursos: {lista_cursos}')

# Parámetros opcionales del método split (seárador)
cursos_separados_coma = 'Java,Python,JavaScript,Angular,Spring,Excel'
lista_cursos = cursos_separados_coma.split(',')
print(f'Lista de cursos: {lista_cursos}')

# Parámetro maxsplit (Número de palabras a separar)
lista_cursos = cursos_separados_coma.split(',', 2)
print(f'Lista de cursos: {lista_cursos}')

# Dar formato a un str
nombre = 'Juan'
edad = 28
mensaje_con_formato = 'Mi nombre es %s y tengo %d años' %(nombre, edad)
print(mensaje_con_formato)

persona = ('Karla', 'Gómez', 10000.00)
mensaje_con_formato = 'Hola %s %s. Tu sueldo es $%.2f'%persona
print(mensaje_con_formato)

persona = ('Karla', 'Gómez', 10000.00)
mensaje_con_formato = 'Hola %s %s. Tu sueldo es $%.2f'
print(mensaje_con_formato%persona)

# Método format()
nombre = 'Juan'
edad = 28
sueldo = 10000
mensaje = 'Nombre: {}, Edad: {}, Sueldo: ${:.2f}'.format(nombre, edad, sueldo)
print(mensaje)

mensaje = 'Nombre: {0}, Edad: {1}, Sueldo: ${2:.2f}'.format(nombre, edad, sueldo)
print(mensaje)

mensaje = 'Sueldo: ${2:.2f}, Nombre: {0}, Edad: {1}'.format(nombre, edad, sueldo)
print(mensaje)

nombre = 'Juan'
edad = 28
sueldo = 10000
mensaje = 'Nombre: {n}, Edad: {e}, Sueldo: ${s:.2f}'.format(n=nombre, e=edad, s=sueldo)
print(mensaje)

diccionario = {'nombre':'Ivan', 'edad':35, 'sueldo':11000.00}
mensaje = 'Nombre: {dic[nombre]}, Edad: {dic[edad]}, Sueldo: ${dic[sueldo]:.2f}'.format(dic=diccionario)
print(mensaje)


# Uso de f-string
nombre = 'Juan'
edad = 28
sueldo = 10000
mensaje = f'Nombre: {nombre}, Edad: {edad}, Sueldo: ${sueldo:.2f}'
print(mensaje)

# Método print
print(nombre, edad, sueldo, sep=', ')

# Multiplicación de cadenas
resultado = 5*'Hola'
print(f'Resultado: {resultado}')

# Multiplicación de tuplas
resultado = 5*('Hola', 10)
print(f'Resultado: {resultado}')

# Multiplicación de listas
resultado = 10*[0]
print(f'Resultado: {resultado}. Cantidad de elementos en la lista: {len(resultado)}')

# Caracteres de escape
resultado = 'Hola \' mundo\b'
print(f'Resultado: {resultado}')

# \b No siempre funciona, no tengo idea del motivo ni se menciona
resultado = 'Eliminación de un\b caracter'
print(f'Resultado: {resultado}')

resultado = 'C:\\CURSOS\\Python'
print(f'Resultado = {resultado}')

# raw string
resultado = r'Cadena con \n salto de línea'
print(f'Resultado = {resultado}')

# Caracteres UNICODE - Buscar en Google para encontrar valores de caracteres especiales
# \u0020 = espacio
print('Hola\u0020Mundo')
# \u0041 = A
print('Notación simple: ', '\u0041')
# \U00000041 = B
print('Notación extendida: ', '\U00000042')
# \x43 = C
print('Notación hexadecimal: ', '\x43')
# \u2665 = Corazón
print('Corazon: ', '\u2665')
# \U0001f600 = Cara sonriendo
print('Cara sonriendo: ', '\U0001f600')

# Caracteres ASCII
caracter = chr(65)
print(caracter)

caracter = chr(60)
print(caracter)

# Literales de tipo Byte
caracteres_en_bytes = b'Hola Mundo'
print(caracteres_en_bytes)

mensaje = b'Universidad Python'
print(f'Valor en byte del caracter en el índice 0: {mensaje[0]}')
print(f'Caracter asociado al valor anterior: {chr(mensaje[0])}')

lista_caracteres = mensaje.split()
print(lista_caracteres)

# Conversión de str a byte y viceversa
string = 'Programación con Python'
print(f'String original: {string}')

# Conversión a bytes (codificación)
bytes = string.encode('UTF-8')
print(f'Cadena codificada: {bytes}')

# Conversión a string (decodificación)
string2 = bytes.decode('UTF-8')
print(f'Cadena decodificada: {string2}')

# Comprobación de que ambas cadenas son iguales
print(string == string2)
