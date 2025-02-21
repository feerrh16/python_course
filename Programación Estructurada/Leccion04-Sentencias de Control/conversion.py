"""
Sergio Fernando Rodríguez Hernández
Curso de Udemy: Universidad de Python - POO, PySide, Tkinter, Django y Flask!
Tema: Sentencias de Control

Código → Conversión de número a texto (limitado a tres números)
"""

Num = int(input("Ingrese un número para su conversión a texto: "))
print()
NumStr = ""

if Num == 1:
    NumStr = "Uno"
elif Num == 2:
    NumStr = "Dos"
elif Num == 3:
    NumStr = "Tres"
else:
    print("Número no contemplado por el sistema.")

print(f"El número ingresado es: {NumStr}")
