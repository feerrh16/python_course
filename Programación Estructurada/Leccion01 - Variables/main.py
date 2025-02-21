"""
Sergio Fernando Rodríguez Hernández
Curso de Udemy: Universidad de Python - POO, PySide, Tkinter, Django y Flask!
Tema: Variables

Nota: Los comentarios en Python se hacen utilizando # para una sola línea de comentario y triples
comillas para comentarios multilínea, como se puede ver en este encabezado.
"""

# Declaración de variables
x = 420
y = 69
z = x * (-y)
R = "El resultado de la operación es: "

"""" id nos muestra la dirección de memoria en la que está guardado el valor al que apunte una cierta variable"""

print("Valor de x: ", x)
print("La dirección de memoria de x es: ", id(x))
print()

print("Valor de y: ", y)
print("La dirección de memoria de y es: ", id(y))
print()

print(R, z)
print()
print("La dirección de memoria de z es: ", id(R))
print("La dirección de memoria de R es: ", id(z))
