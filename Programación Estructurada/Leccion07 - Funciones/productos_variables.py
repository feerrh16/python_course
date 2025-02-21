"""
Sergio Fernando Rodríguez Hernández
Curso de Udemy: Universidad de Python - POO, PySide, Tkinter, Django y Flask!
Tema: Colecciones

Código → Función con argumentos variables para multiplicar todos los valores recibidos.
"""


def producto_variable(*args):
    resultado = 0
    for valor in args:
        resultado *= valor
    return resultado


print(f"El resultado del producto es: {producto_variable(12, 3, 4, 5)}")
