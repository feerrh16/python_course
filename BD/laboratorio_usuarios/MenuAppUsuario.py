from UsuarioDAO import *

opcion = None

while opcion != 5:
    try:
        print(f'''
        Bienvenido al sistema de administración de usuarios.
        1. Listar usuarios en sistema.
        2. Agregar un usuario al sistema.
        3. Actualizar registro de usuario.
        4. Eliminar registro de usuario.
        5. Salir.
        ''')
        opcion = int(input('Ingresa una opción: '))
        if opcion == 1:
            lista_usuarios = UsuarioDAO.seleccionar()
            for usuario in lista_usuarios:
                log.info(usuario)
        elif opcion == 2:
            usuario_tmp = input('Ingresa el Nombre del usuario: ')
            password_tmp = input('Ingresa la contraseña del usuario: ')
            usuario = Usuario(username=usuario_tmp, password=password_tmp)
            registro_agregado = UsuarioDAO.insertar(usuario)
            log.info(f'Usuario agregado a la Base de Datos: {registro_agregado}')
        elif opcion == 3:
            id_usuario_tmp = int(input('Ingrese el ID del registo a actualizar: '))
            usuario_tmp = input('Ingrese el nuevo nombre de usuario: ')
            password_tmp = input('Ingrese la nueva contraseña: ')
            usuario = Usuario(id_usuario_tmp, usuario_tmp, password_tmp)
            registro_actualizado = UsuarioDAO.actualizar(usuario)
            log.info(f'Usuario actualizado en la Base de Datos: {registro_actualizado}')
        elif opcion == 4:
            id_usuario_tmp = int(input('Ingrese el ID del registro a eliminar: '))
            usuario = Usuario(id_usuario=id_usuario_tmp)
            registro_borrado = UsuarioDAO.borrar(usuario)
            log.info(f'Usuario eliminado de la Base de Datos: {registro_borrado}')
    except Exception as e:
        log.error(f'Ocurrió una excepción:\n{e}')
        opcion = None
else:
    log.info('Fin de la ejecución')
    