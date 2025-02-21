"""
Sergio Fernando Rodríguez Hernández
Curso de Udemy: Universidad de Python - POO, PySide, Tkinter, Django y Flask!
Tema: Sentencias de Control

Código → Programa que calcula la Estación según el Mes proporcionado por el usuario.
"""

Month = str(input("Este programa indica la estación del año según el mes. Introduzca el mes: "))

# None es utilizado para asignarle un valor nulo a una variable
Station = None

if Month == "Enero" or "enero":
    Station = "Invierno"
elif Month == "Febrero" or "febrero":
    Station = "Invierno"
elif Month == "Marzo" or "marzo":
    Station = "Primavera"
elif Month == "Abril" or "abril":
    Station = "Primavera"
elif Month == "Mayo" or "mayo":
    Station = "Primavera"
elif Month == "Junio" or "junio":
    Station = "Primavera"
elif Month == "Julio" or "julio":
    Station = "Verano"
elif Month == "Agosto" or "agosto":
    Station = "Verano"
elif Month == "Septiembre" or "septiembre":
    Station = "Verano"
elif Month == "Octubre" or "octubre":
    Station = "Otoño"
elif Month == "Noviembre" or "noviembre":
    Station = "Otoño"
elif Month == "Diciembre" or "diciembre":
    Station = "Invierno"
else:
    print("Entrada inválida. Intente de nuevo.")

print(f"La estación es: {Station}")
print()
