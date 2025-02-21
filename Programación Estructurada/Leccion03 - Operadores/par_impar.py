"""
Sergio Fernando Rodríguez Hernández
Curso de Udemy: Universidad de Python - POO, PySide, Tkinter, Django y Flask!
Tema: Operadores

Código → Algoritmo para determinar si un número es par o impar
"""

NumComp = int(input("Ingrese un número para determinar si es par o impar: "))

if (NumComp % 2) == 0:
    print("El número es par.")
else:
    print("El número es impar")
