"""
Sergio Fernando Rodríguez Hernández
Curso de Udemy: Universidad de Python - POO, PySide, Tkinter, Django y Flask!
Tema: Colecciones

Código → Conversión de temperatura.
            Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa.

            Función 1. Recibir un parámetro llamado celsius y regresar el valor equivalente a fahrenheit

                La función se llama: celsius_fahrenheit(celsius)

                La fórmula para convertir de celsius a fahrenheit es: celsius * 9/5 + 32

            Función 2. Recibir un parámetro llamado fahrenheit y regresar el valor equivalente a celsius:

                fahrenheit_celsius(fahrenheit)

                La fórmula para convertir de fahrenheit a celsius es:  (fahrenheit-32) * 5/9

            Los valores los debe proporcionar el usuario, utilizando la función input y convirtiéndolo a tipo float.

            Deben hacer al menos dos pruebas, una donde conviertan de grados celsius a grados fahrenheit, y otra donde
            conviertan de grados fahrenheit a grados celsius y mandar a imprimir los resultados
"""


def celsius_fahrenheit(celsius):
    fahrenheit = celsius * (9/5) + 32
    return 0


def fahrenheit_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    return 0
