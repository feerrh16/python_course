import psycopg2

conexion = psycopg2.connect(
    user='postgres', 
    password='admin', 
    host='127.0.0.1',
    port='5432',
    database='test_db')

# Inserción de varios registros
try:
    with conexion:
            with conexion.cursor() as cursor:
                sentencia = 'INSERT INTO persona(nombre, apellido, mail) VALUES(%s, %s, %s)'
                valores = (
                     ('Mario', 'Ponce', 'mponce@mail.com'), 
                     ('Marco', 'Cantú', 'mcantu@mail.com'), 
                     ('Angel', 'Quintana', 'aquintana@mail.com'), 
                     ('María', 'González', 'mgonzalez@mail.com'), 
                     )
                cursor.executemany(sentencia, valores)
                registros_insertados = cursor.rowcount
                print(f'Registros insertados: {registros_insertados}')
except Exception as e:
     print(f'Ocurrió un error: {e}')
finally:
    conexion.close()     

"""
Inserción de un único registro
try:
    with conexion:
            with conexion.cursor() as cursor:
                sentencia = 'INSERT INTO persona(nombre, apellido, mail) VALUES(%s, %s, %s)'
                valores = ('Carlos', 'Lara', 'clara@mail.com')
                cursor.execute(sentencia, valores)
                registros_insertados = cursor.rowcount
                print(f'Registros insertados: {registros_insertados}')
except Exception as e:
     print(f'Ocurrió un error: {e}')
finally:
    conexion.close()     
"""