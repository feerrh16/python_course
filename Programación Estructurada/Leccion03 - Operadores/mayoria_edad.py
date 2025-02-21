"""
Sergio Fernando Rodríguez Hernández
Curso de Udemy: Universidad de Python - POO, PySide, Tkinter, Django y Flask!
Tema: Operadores

Código → Algoritmo que verifica la mayoría de edad del usuario
"""

MayorEdad = 18
Edad = int(input("Ingrese su edad: "))

if Edad >= MayorEdad:
    print("Usuario mayor de edad.")
else:
    print("Usuario menor de edad.")
