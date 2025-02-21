class Empleado:
    def __init__(self, nombre, sueldo):

        if self.validar_nombre(nombre):
            self._nombre = nombre
        else:
            return 'Ingrese un nombre válido'
        
        if self.validar_sueldo(sueldo):
            self._sueldo = sueldo
        else:
            return 'Ingrese un sueldo digno'
        
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def sueldo(self):
        return self._sueldo
    
    @nombre.setter
    def nombre(self, nombre):
        if self.validar_nombre(nombre):
            self._nombre = nombre
        else:
            return 'Ingrese un nombre válido'

    @sueldo.setter
    def sueldo(self, sueldo):
        if self.validar_sueldo(sueldo):
            self._sueldo = sueldo
        else:
            return 'Ingrese un sueldo digno'
    
    def validar_nombre(self, nombre):
        return False if nombre == '' else True
    
    def validar_sueldo(self, sueldo):
        return True if 7000 < sueldo < 99999 else False
    
    def __str__(self):
        return  f'Nombre del empleado: {self._nombre}\n' \
                f'Sueldo del empleado: ${self._sueldo}' 
    
    def mostrar_detalles(self):
        return self.__str__()
    
                
    