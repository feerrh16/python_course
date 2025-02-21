archivo = open('c:\\CURSOS\\Python\\Manejo de Archivos\\prueba.txt', 'r', encoding='utf8')

# Imprimir en consola el contenido del archivo:
# print(archivo.read())

# Leer cierto número de caracteres:
# print(archivo.read(10))

# Leer líneas completas
# print(archivo.readline())
# print(archivo.readline())

# iterar el archivo
# for linea in archivo:
#     print(linea)

# leer lineas
# print(archivo.readlines())

# acceder a una linea de la lista
# print(archivo.readlines()[2])

# abrimos un nuevo archivo
# a - anexar informacion
archivo2 = open('copia.txt', 'a', encoding='utf8')
archivo2.write(archivo.read())

archivo.close()
archivo2.close()
print('se ha terminado el proceso de leer y copiar archivos')