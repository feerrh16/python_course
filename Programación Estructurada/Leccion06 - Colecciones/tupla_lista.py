"""
Sergio Fernando Rodríguez Hernández
Curso de Udemy: Universidad de Python - POO, PySide, Tkinter, Django y Flask!
Tema: Colecciones

Código → Dada una tupla, crear una lista que solo incluya los números menores que 5
"""

tupla = (13, 1, 8, 3, 2, 5, 8)

for i in tupla:
    FiltroTupla = list(tupla)
    if i < 5:
        print(f"Elementos menores a 5 en la lista: {i}")
else:
    print("No quedan más elementos menores a 5 en la lista")
