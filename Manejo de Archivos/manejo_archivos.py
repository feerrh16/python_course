try:
    archivo = open('c:\\CURSOS\\Python\\Manejo de Archivos\\prueba.txt', 'w', encoding='utf8')
    archivo.write('¡Hola Mundo! Desde un archivo de pruebas en Python\n')
    archivo.write('Adiós')
except Exception as e:
    print(e)
finally:
    archivo.close()
    print('Archivo cerrado')