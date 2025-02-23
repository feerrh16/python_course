"""
Sergio Fernando Rodríguez Hernández
Curso de Udemy: Universidad de Python - POO, PySide, Tkinter, Django y Flask!
Tema: Colecciones

Código → Calculadora de impuestos:
            Crear una función para calcular el total de un pago incluyendo un impuesto aplicado.

            La función se llama calcular_total()

            La función recibe dos parámetros:

                1. pago_sin_impuesto

                2. impuesto (Ej. Valor de 10, significa 10% de impuesto, Valor de 16 significa el 16% de impuesto)

            La función debe regresar el total del pago incluyendo el porcentaje de impuesto proporcionado.

            Ej. Si llamamos a la función calcular_total(1000, 16) debe retornar el valor 1,160.0

            Los valores los debe proporcionar el usuario y ser procesados con la función input, convirtiéndolos a tipo
            float.
"""


def calcular_total(pago_sin_impuesto, impuesto):
    return pago_sin_impuesto + (pago_sin_impuesto * (impuesto / 100))


pago_sin_impuesto = float(input("Ingrese su monto a pagar: $"))
impuesto = float(input("Ingrese el porcentaje del impuesto aplicado: %"))
pago_total = calcular_total(pago_sin_impuesto, impuesto)
print(f"El total del pago es de ${pago_total}")
