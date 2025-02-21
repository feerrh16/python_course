"""
Sergio Fernando Rodríguez Hernández
Curso de Udemy: Universidad de Python - POO, PySide, Tkinter, Django y Flask!
Tema: Sentencias de Control

Código → Etapas de vida según edad proporcionada por el usuario
"""

print("Programa que identifica la etapa de su vida según la edad ingresada.")
print()

Edad = int(input("Ingrese su edad: "))
Etapa = None

if 0 < Edad <= 11:
    Etapa = "Infancia"
elif 12 <= Edad <= 18:
    Etapa = "Adolescencia"
elif 19 <= Edad <= 26:
    Etapa = "Juventud"
elif 27 <= Edad <= 59:
    Etapa = "Adultez"
elif 60 <= Edad <= 120:
    Etapa = "Vejez"
else:
    print("Edad fuera de rango.")

print(f"La etapa a la que corresponde su edad ({Edad}) es: {Etapa}")
print()
