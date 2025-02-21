"""
Sergio Fernando Rodríguez Hernández
Curso de Udemy: Universidad de Python - POO, PySide, Tkinter, Django y Flask!
Tema: Operadores

Código → Ejercicio sobre Tienda de libros
"""

print("Verificación de la información introducida por el usuario.")
print()
Title = str(input("Ingrese el título del libro: "))
ID = int(input("Ingrese el número de identificación del libro: "))
Price = float(input("Ingrese el precio del libro: $"))
Shipment = input("¿El envío es gratuito? (Y/N): ")
print()

if str(Shipment) == "Y":
    Shipment = True
elif str(Shipment) == "N":
    Shipment = False
else:
    print("Ingrese una opción válida para el envío (Y/N)")

print("La información solicitada se muestra a continuación:")
print()
print(f"Título:             {Title}")
print(f"ID:                 {ID}")
print(f"Precio:             ${Price}")
print(f"Envío gratuito:     {Shipment}")
print()
print("Gracias por su atención")
