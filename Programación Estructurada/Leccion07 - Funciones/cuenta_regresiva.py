"""
Sergio Fernando Rodríguez Hernández
Curso de Udemy: Universidad de Python - POO, PySide, Tkinter, Django y Flask!
Tema: Colecciones

Código → Imprimir números de 5 a 1 de manera descendente usando funciones recursivas.
"""

n = int(input("Ingrese un número para su cuenta regresiva: "))


def cuenta_regresiva(n):

    print(n)
    n -= 1

    if n <= 0:
        return 1
    else:
        cuenta_regresiva(n)


cuenta_regresiva(n)
