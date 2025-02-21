import psycopg2

conexion = psycopg2.connect(
    user='postgres', 
    password='admin', 
    host='127.0.0.1',
    port='5432',
    database='test_db')
"""
Actualización de un registro
try:
    with conexion:
            with conexion.cursor() as cursor:
                sentencia = ('UPDATE persona SET nombre = %s, apellido = %s, mail = %s WHERE id_persona = %s')
                valores = ('Carlos', 'Juárez', 'cjuarez@mail.com', 1)
                cursor.execute(sentencia, valores)
                registros_actualizados = cursor.rowcount
                print(f'Registros actualizados: {registros_actualizados}')
except Exception as e:
     print(f'Ocurrió un error: {e}')
finally:
    conexion.close()     
"""

# Actualización de varios registros

try:
    with conexion:
            with conexion.cursor() as cursor:
                sentencia = ('UPDATE persona SET nombre = %s, apellido = %s, mail = %s WHERE id_persona = %s')
                valores = (
                    ('Juan', 'Juárez', 'cjuarez@mail.com', 1), 
                    ('Ivonne', 'Gutiérrez', 'igutierrez@mail.com', 2), 
                    )
                cursor.executemany(sentencia, valores)
                registros_actualizados = cursor.rowcount
                print(f'Registros actualizados: {registros_actualizados}')
except Exception as e:
     print(f'Ocurrió un error: {e}')
finally:
    conexion.close()     
