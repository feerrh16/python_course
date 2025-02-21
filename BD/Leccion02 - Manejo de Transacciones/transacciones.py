import psycopg2 as db

conexion = db.connect(
    user = 'postgres',
    password = 'admin',
    host = '127.0.0.1',
    port = '5432',
    database = 'test_db'
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            cursor = conexion.cursor()
            sentencia = 'INSERT INTO persona(nombre, apellido, mail) VALUES(%s, %s, %s)'
            valores = ('Alejandro', 'Rojas', 'arojas@mail.com')
            cursor.execute(sentencia, valores)
            
            sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, mail = %s WHERE id_persona = %s'
            valores = ('Juan', 'Pérez', 'jperez@mail.com', 1)
            cursor.execute(sentencia, valores)
            
except Exception as e:
    print(f'Ocurrió un error: {e}. Se ha realizado un rollback de la transacción.')
finally:
    conexion.close()
    print('Fin de la transacción, commit realizado.')
    