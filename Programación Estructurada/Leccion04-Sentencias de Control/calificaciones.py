"""
Sergio Fernando Rodríguez Hernández
Curso de Udemy: Universidad de Python - POO, PySide, Tkinter, Django y Flask!
Tema: Sentencias de Control

Código → Sistema de calificaciones

"""

Grade = float(input("Ingrese su calificación: "))
CharGrade = None

if 0 <= Grade < 6:
    CharGrade = "F"
elif 6 <= Grade < 7:
    CharGrade = "D"
elif 7 <= Grade < 8:
    CharGrade = "C"
elif 8 <= Grade < 9:
    CharGrade = "B"
elif 9 <= Grade < 10:
    CharGrade = "A"
else:
    print("Ingrese un valor entre 0 y 10")

print(f"La calificación asignada para {Grade} dentro del sistema es: {CharGrade}")
print()
