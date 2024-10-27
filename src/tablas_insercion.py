import pandas as pd
import sys
sys.path.append("../")
from src import soporte as sp

def create_table_supermercados(conn, cursor):
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS supermercados (
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(50) UNIQUE NOT NULL
            )
        """)
        conn.commit()
    except:
        print(f"Error al crear la tabla: supermercados")
    
def insert_supermercados(conn, cursor):
    """
    Inserta los supermercados del diccionario en la tabla 'supermercados'.
    """
    try:
        for nombre, id in sp.supermercados_dicc.items():
            cursor.execute("""
                INSERT INTO supermercados (id, nombre) VALUES (%s, %s)
                ON CONFLICT (nombre) DO NOTHING
            """, (id, nombre))
        conn.commit()
    except Exception as e:
        print(f"Error al insertar los supermercados: {e}")

def create_table_categorias(conn, cursor):
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS categorias (
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(50) UNIQUE NOT NULL
            )
        """)
        conn.commit()
    except:
        print(f"Error al crear la tabla: categorias")
    
def insert_categorias(conn, cursor):
    """
    Inserta las categorias del diccionario en la tabla 'categorias'.
    """
    try:
        for nombre, id in sp.categorias_dicc.items():
            cursor.execute("""
                INSERT INTO categorias (id, nombre) VALUES (%s, %s)
                ON CONFLICT (nombre) DO NOTHING
            """, (id, nombre))
        conn.commit()
    except:
        print(f"Error al insertar los categorias")

def create_table_productos_hist_precios(conn, cursor):
    try:
    
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id SERIAL PRIMARY KEY,
                fecha DATE NOT NULL,
                precio DECIMAL(10, 2) NOT NULL,
                variacion VARCHAR(100),
                id_supermercado INTEGER NOT NULL,
                id_categoria INTEGER NOT NULL,
                producto VARCHAR(255) NOT NULL,
                FOREIGN KEY (id_supermercado) REFERENCES supermercados (id),
                FOREIGN KEY (id_categoria) REFERENCES categorias (id)
            )
        """)
        conn.commit()
    except:
        print(f"Error al crear la tabla 'productos")


def insert_data_productos_hist_precios(conn, cursor, df):
    try:
        for index, row in df.iterrows():
                cursor.execute("""
                    INSERT INTO productos (fecha, precio, variacion, id_supermercado, id_categoria, producto)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (
                    pd.to_datetime(row['fecha'], format='%d/%m/%Y').date(), 
                    float(row['precio'].replace(',', '.')),
                    row['Variacion'],
                    row['id_supermercado'],
                    row['id_categoria'],
                    row['producto']
                ))
        conn.commit()
    except :
        print(f"Error al cargar datos en la tabla: productos")


def main(conn, cursor, df):
    create_table_supermercados(conn,cursor)

    insert_supermercados(conn,cursor)

    create_table_categorias(conn,cursor)

    insert_categorias(conn,cursor)

    create_table_productos_hist_precios(conn,cursor)

    insert_data_productos_hist_precios(conn,cursor,df)

    

