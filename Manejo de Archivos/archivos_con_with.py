from ManejoArchivos import ManejoArchivos

# with open('prueba.txt','r', encoding='utf8') as archivo:
with ManejoArchivos('c:\\CURSOS\\Python\\Manejo de Archivos\\prueba.txt') as archivo:
    print(archivo.read())
