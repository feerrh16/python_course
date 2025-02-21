"""
Sergio Fernando Rodríguez Hernández
Curso de Udemy: Universidad de Python - POO, PySide, Tkinter, Django y Flask!
Tema: Operadores

Código → # Programa que compara dos números dados por el usuario e imprime el mayor
"""

No1 = int(input("Ingresa el primer número: "))
No2 = int(input("Ingresa el segundo número: "))

Mayor1 = No1 > No2
Iguales = No1 == No2
Mayor2 = No1 < No2

if Mayor1:
    print(f"El primer número introducido ({No1}) es mayor que el segundo ({No2})")
elif Mayor2:
    print(f"El primer número introducido ({No1}) es menor que el segundo ({No2})")
elif Iguales:
    print("Ambos números son iguales")
