"""
Sergio Fernando Rodríguez Hernández
Curso de Udemy: Universidad de Python - POO, PySide, Tkinter, Django y Flask!
Tema: Sentencias de Control

Archivo de pruebas para ejercicios y tareas de Udemy. Hacer un archivo individual para cada código después.
Ruta de archivo (para ejecutar desde cmd):
    C:\CURSOS\Python\Leccion04-Sentencias de Control\

Tarea - Sistema de calificaciones

Se le pregunta al usuario un valor entre 0 y 10 (su calificación) y se le asigna una letra según el valor numérico:

    0 - 6 → F
    6 - 7 → D
    7 - 8 → C
    8 - 9 → B
    9 - 10 → A

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
