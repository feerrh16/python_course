from logger_base import *
from Usuario import *
from Conexion import *
from CursorDelPool import *

class UsuarioDAO:
    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username = %s, password = %s WHERE id_usuario = %s'
    _BORRAR = 'DELETE FROM usuario WHERE id_usuario = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios
        
    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Registro insertado en la Base de Datos:\n{usuario}')
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Registro actualizado en la Base de Datos:\n{usuario}')
            return cursor.rowcount
        
    @classmethod
    def borrar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.id_usuario, )
            cursor.execute(cls._BORRAR, valores)
            log.debug(f'Registro eliminado de la Base de Datos:\n{usuario}')
            return cursor.rowcount
        

if __name__ == '__main__':
    # Inserción de un registro
    usuario1 = Usuario(username='SirRinoceronte', password='r1n0c3r0nt3')
    usuarios_insertados = UsuarioDAO.insertar(usuario1)
    log.debug(f'Registro insertado en la Base de Datos:\n{usuarios_insertados}')

    # Seleccionar objetos
    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)
