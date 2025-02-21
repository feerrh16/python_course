"""
Sergio Fernando Rodríguez Hernández
Curso de Udemy: Universidad de Python - POO, PySide, Tkinter, Django y Flask!
Tema: Colecciones

Código → Serie de Fibonacci.
"""

n = int(input(print("Ingrese el número para el cual desee calcular la serie de Fibonacci: ")))


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(f"El resultado de la serie de Fibonacci para {n} es: {fibonacci(n)}")
