"""
Sergio Fernando Rodríguez Hernández
Curso de Udemy: Universidad de Python - POO, PySide, Tkinter, Django y Flask!
Tema: Colecciones

Código → Función con argumentos variables para sumar todos los valores recibidos.
"""


def suma_variables(*args):
    resultado = 0
    for valor in args:
        resultado += valor
    return resultado


print(f"El resultado de la suma es: {suma_variables(123, 432, 34, 54, 434)}")
