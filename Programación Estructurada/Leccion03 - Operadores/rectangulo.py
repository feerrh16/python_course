"""
Sergio Fernando Rodríguez Hernández
Curso de Udemy: Universidad de Python - POO, PySide, Tkinter, Django y Flask!
Tema: Operadores

Código de la tarea 3 → Calcula el área y el perímetro de un rectángulo a partir del ancho y la altura
"""

Altura = input("Ingrese la medida de la altura del rectángulo: ")
Base = input("Ingrese la medida de la base del rectángulo: ")
print()

# Cálculo de perímetro
P = (int(Altura) + int(Base)) * 2

# Cálculo del área
A = int(Altura) * int(Base)

print(f"El perímetro del rectángulo es: {P} u")
print(f"El área del rectángulo es: {A} u^2")
