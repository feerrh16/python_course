"""
Sergio Fernando Rodríguez Hernández
Curso de Udemy: Universidad de Python - POO, PySide, Tkinter, Django y Flask!
Tema: Operadores

Código → Programa que verifica sí un número dado por el usuario está dentro del rango (Operación AND)
"""

# Rango
Inicio = -10
Final = 69

Dado = int(input("Ingrese un número cualquiera. El programa indicará si está dentro del rango: "))
print()

# Operación Lógica
Comp = Inicio <= Dado <= Final

if Inicio <= Dado <= Final:
    print(f"Esta operación lógica tiene un valor de: {Comp}")
    print(f"Por tanto, el número {Dado} está dentro del rango, cuyo Inicio es {Inicio} y su Final es {Final}")
else:
    print(f"Esta operación lógica tiene un valor de: {Comp}")
    print(f"Por tanto, el número {Dado} no está dentro del rango, cuyo Inicio es {Inicio} y su Final es {Final}")
