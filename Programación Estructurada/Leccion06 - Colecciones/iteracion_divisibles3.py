"""
Sergio Fernando Rodríguez Hernández
Curso de Udemy: Universidad de Python - POO, PySide, Tkinter, Django y Flask!
Tema: Colecciones

Código → Iterar un rango de cero a diez e imprimir los números que son divisibles entre 3
"""

conjunto = [-1]

for i in conjunto:
    i += 1
    conjunto.append(i)

    if i % 3 == 0:
        print(f"Número divisible entre 3: {i}")

    elif i == 10:
        break
else:
    print("No quedan más elementos en la lista")
