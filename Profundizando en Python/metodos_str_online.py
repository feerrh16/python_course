# Leer contenido online
import urllib
from urllib.request import urlopen

# Debido a cambios en la libreria se deben hacer los siguientes cambios:
peticion = urllib.request.Request(
    'http://globalmentoring.com.mx/recursos/GlobalMentoring.txt',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
with urlopen(peticion) as mensaje:
    contenido = mensaje.read().decode('utf-8')

# Contar ocurrencias de una cadena
print('No. veces Universidad: ', contenido.count('Universidad'))

# upper convierte a mayúsculas un str
print(contenido.upper())
print(contenido)

# lower convierte a minúsculas un str
print(contenido.lower())

# buscamos la cadena python en el contenido
print('Existe python?: ','python'.lower() in contenido.lower())
print('Existe Python?: ','Python'.upper() in contenido.upper())

# startswith - inicia con
print('Inicia con: ',contenido.startswith('En GlobalMentoring.com.mx'))

# endswith - termina con
print('Termina con:', contenido.lower().endswith('globalmentoring.com.mx'.lower()))

# Métodos islower() e isupper()
mensaje = 'Hola Mundo'
print(mensaje.lower().islower())
print(mensaje.upper().isupper())

# Alinear cadenas

# Centrar cadenas
titulo = 'Sitio web de GlobalMentoring.com.mx'
print(titulo.center(50, '-'))
print(len(titulo.center(50, '-')))

# Forma dinámica de centrar
print(titulo.center(len(titulo)+15 ,'-'))

# Alinear a la izquierda
print(titulo.ljust(len(titulo)+15, '-'))

# Alinear a la derecha
print(titulo.rjust(len(titulo)+15, '-'))

# Método replace
print(contenido.replace(' ', '-'))

# Método strip (Elimina caracteres)
titulo = ' *** GlobalMentoring.com.mx *** '
print(titulo)
print(len(titulo))
titulo = titulo.strip()
print(titulo)
print(len(titulo))

titulo = '***GlobalMentoring.com.mx***'.strip('*')
print(titulo)
print(len(titulo))

titulo = '***GlobalMentoring.com.mx***'.lstrip('*')
print(titulo)
print(len(titulo))

titulo = '***GlobalMentoring.com.mx***'.rstrip('*')
print(titulo)
print(len(titulo))

titulo = ' *** GlobalMentoring.com.mx *** '.strip().strip('*').strip()
print(titulo)
print(len(titulo))
