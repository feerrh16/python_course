class Orden:
    contador_ordenes = 0

    def __init__(self, computadoras):
        self._id_orden = Orden.generar_orden()
        self._computadoras = computadoras

    def agregar_computadora(self,computadora):
        self._computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ''
        for computadora in self._computadoras:
            computadoras_str += computadora.__str__()
        return  f'Número de orden: {self._id_orden}\n' \
                f'Computadoras:\n{computadoras_str}'

    @classmethod
    def generar_orden(cls):
        cls.contador_ordenes += 1
        return cls.contador_ordenes