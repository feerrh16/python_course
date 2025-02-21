"""
Sergio Fernando Rodríguez Hernández
Curso de Udemy: Universidad de Python - POO, PySide, Tkinter, Django y Flask!
Tema: Operadores

Código → Programa que realiza las operaciones lógicas AND, OR y NOT
"""

a = (input("Ingrese un valor Booleano (True/False) para la variable a: "))
b = (input("Ingrese un valor Booleano (True/False) para la variable b: "))
print()

if a == "True" and b == "True":
    a = True
    b = True
elif a == "True" and b == "False":
    a = True
    b = False
elif a == "False" and b == "True":
    a = False
    b = True
elif a == "False" and b == "False":
    a = False
    b = False

else:
    print("Ingrese un valor Booleano válido.")

# Operaciones Lógicas
AND = a and b
OR = a or b
NOT_A = not a
NOT_B = not b

# Resultados
print("Resultados de las operaciones lógicas.")
print()

print(f"La operación lógica a y b (a and b) tiene un valor: {AND}")
print(f"La operación lógica a o b (a or b) tiene un valor: {OR}")
print(f"La operación lógica negación de a (not a) tiene un valor: {NOT_A}")
print(f"La operación lógica negación de b (not b) tiene un valor: {NOT_B}")
