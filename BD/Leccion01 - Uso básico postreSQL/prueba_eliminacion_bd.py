import psycopg2

conexion = psycopg2.connect(
    user='postgres', 
    password='admin', 
    host='127.0.0.1',
    port='5432',
    database='test_db'
)

"""
Eliminación de un registro
try:
    with conexion:
            with conexion.cursor() as cursor:
                sentencia = ('DELETE FROM persona WHERE id_persona = %s')
                entrada = input('Proporciona el ID a eliminar: ')
                valores = (entrada, ) 
                cursor.execute(sentencia, valores)
                registros_eliminados = cursor.rowcount
                print(f'Registros eliminados: {registros_eliminados}')
except Exception as e:
     print(f'Ocurrió un error: {e}')
finally:
    conexion.close()     
"""
# Eliminación de varios registros
try:
    with conexion:
            with conexion.cursor() as cursor:
                sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
                entrada = input('Proporciona los IDs a eliminar separados por comas: ')
                valores = (tuple(entrada.split(',')), )
                cursor.execute(sentencia, valores)
                registros_eliminados = cursor.rowcount
                print(f'Registros eliminados: {registros_eliminados}')
except Exception as e:
     print(f'Ocurrió un error: {e}')
finally:
    conexion.close()     
