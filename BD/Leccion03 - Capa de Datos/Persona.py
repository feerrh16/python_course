from logger_base import *

class Persona:
    def __init__(self, id_persona = None, nombre = None, apellido = None, mail = None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._mail = mail

    def __str__(self):
        return  f'''
                ID: {self._id_persona}
                Nombre: {self._nombre}
                Apellido = {self._apellido}
                Correo: {self._mail}
                '''
    
    @property
    def id_persona(self):
        return self._id_persona
    
    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido
    
    @property
    def mail(self):
        return self._mail
    
    @mail.setter
    def mail(self, mail):
        self._mail
    
if __name__ == '__main__':
    persona1 = Persona(1, 'Juan', 'Pérez', 'jperez@mail.com')
    log.debug(persona1)

    # Simular un INSERT INTO
    persona1 = Persona(nombre='Juan', apellido='Pérez', mail='jperez@mail.com')
    log.debug(persona1)

    #Simular un DELETE
    persona1 = Persona(id_persona=1)
    log.debug(persona1)
    