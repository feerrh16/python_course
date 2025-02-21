"""
Sergio Fernando Rodríguez Hernández
Curso de Udemy: Universidad de Python - POO, PySide, Tkinter, Django y Flask!
Tema: Tipos de datos y procesamiento de entrada de datos por parte del usuario
"""

# Tipo Entero (int). Con este tipo de dato podemos realizar operaciones aritméticas.
x = 10
y = 5

# la función type imprime en pantalla el tipo de Dato al que apunta nuestra variable.

print("Enteros")
print("x =", x)
print("y =", y)
print("")

print("x es de tipo:", type(x))
print("y es de tipo:", type(y))
print("")

print("Resultados")
print("El resultado de la suma es:", x + y)
print("El resultado de la resta es:", x - y)
print("El resultado de la multiplicación es:", x * y)
print("El resultado de la división es:", x / y)
print("")

# Tipo Flotante (float)
x = 10.0
y = 2.5

print("flotantes")
print("x =", x)
print("y =", y)
print("")

print("x es de tipo:", type(x))
print("y es de tipo:", type(y))
print("")

print("Resultados")
print("El resultado de la suma es:", x + y)
print("El resultado de la resta es:", x - y)
print("El resultado de la multiplicación es:", x * y)
print("El resultado de la división es:", x / y)
print("")

# Tipo Cadena (str). En caso de Top3, es una variable tipo Tuple, ya que almacena varios strings

"""
Para concatenar podemos usar comas (,) o el operador suma (+). 
Las comas ponen un espacio en automático
entre las cadenas cuando se imprimen en pantalla.
Para concatenar utilizando el operador suma, se deben establecer los espacios, como se muestra abajo
"""

# Concatenación con comas
Top3 = "One Ok Rock", "Green Day", "Nujabes"

print("Concatenación con comas")
print("")

print("Mi Top 3 es:", Top3)
print("Top3 es de tipo:", type(Top3))
print("")

print("Mi música favorita es de:", Top3)
print("")

# Concatenación con operador suma
OOR = "One Ok Rock"
GD = "Green Day"
SC = "Nujabes"

print("Concatenación con operador suma")
print("")

print(OOR)
print("OOR es de tipo:", type(OOR))
print("")

print(GD)
print("GD es de tipo:", type(GD))
print("")

print(SC)
print("SC es de tipo:", type(SC))
print("")

print("Mi música favorita es de:" + " " + OOR + ", " + GD + " y " + SC)
print("")

"""
Podemos convertir un tipo de dato string a un int utilizando la función int, como se muestra abajo
"""

HorasClase = "6"
HorasTransporte = "3"

print("Horas en clase:", HorasClase)
print(type(HorasClase))
print("")

print("Horas en transporte:", HorasTransporte)
print(type(HorasTransporte))
print("")

print("Concatenando:", HorasClase + HorasTransporte)
print("Operando:", int(HorasClase) + int(HorasTransporte))
print("")

# Tipo Booleano (bool)
Comp = 420 < 69

print("La comparación 420 < 69 tiene un valor:", Comp)
print("Comp es de tipo:", type(Comp))
print("")

# Procesamiento de Entrada de datos por el usuario (función input)
"""
Para procesar los datos de Entrada por parte del usuario se utiliza la función input.
El código de abajo nos muestra cómo solicitar la entrada de un par de datos al usuario y
posteriormente imprimirlos en una sola oración.
"""

# Información de un libro

Titulo = input("¿Cuál es el título del libro? ")
Autor = input("¿Quién es el autor del libro? ")
Tiempo = input("¿En qué año fue escrito? ")
print("")

print(Titulo, "fue escrito por", Autor, "en el año", int(Tiempo))
print("")

print("Fin del programa y de la lección.")
