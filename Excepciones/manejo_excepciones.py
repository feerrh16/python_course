from ExceptionNumerosIdenticos import *

resultado = None

try:
	a = int(input('Primer valor: '))
	b = int(input('Segundo valor: '))

	if a == b:
		# Se utiliza la palabra reservada raise para desplegar mensajes
		raise ExceptionNumerosIdenticos('Números idénticos')

	resultado = a/b

except ZeroDivisionError as e:
	print(f'Ocurrió un error: {e}, {type(e)}')
except TypeError as e:
	print(f'Ocurrió un error: {e}, {type(e)}')
except Exception as e:
	print(f'Ocurrió un error: {e}, {type(e)}')
else:
	print('Sin registro de excepciones')
finally:
	print('Ejecución del bloque finally')

print(f'Resultado: {resultado}')
print('El programa no termina abruptamente, continúa la ejecución')