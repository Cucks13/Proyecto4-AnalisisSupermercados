import psycopg2 

def conexion(USUARIO, PASSWORD, HOST, NOMBRE):

    try:
        user = USUARIO
        password = PASSWORD
        host = HOST
        database = NOMBRE

        conn = psycopg2.connect(
            user=user,
            password=password,
            host=host,
            database=database
        )

        cursor = conn.cursor()
        return conn, cursor

    except Exception as e:
        print(f"Error al conectarse a la base de datos: {e}")
        raise

def cerrar_conexion(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()
