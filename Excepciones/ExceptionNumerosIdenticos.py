class ExceptionNumerosIdenticos(Exception):
	def __init__(self, mensaje):
		# message es un atributo de la clase Exception
		self.message = mensaje