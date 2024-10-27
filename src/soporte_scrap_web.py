# Importamos las librerías que necesitamos

# Librerías de extracción de actividades
# -----------------------------------------------------------------------
from bs4 import BeautifulSoup # type: ignore
import requests # type: ignore

# Tratamiento de actividades
# -----------------------------------------------------------------------
import pandas as pd # type: ignore
import numpy as np # type: ignore
import re
from time import sleep
import time
import multiprocessing
import asyncio
from datetime import datetime

# Importar librerías para automatización de navegadores web con Selenium
# -----------------------------------------------------------------------
from selenium import webdriver  # type: ignore # Selenium es una herramienta para automatizar la interacción con navegadores web.
from webdriver_manager.chrome import ChromeDriverManager  # type: ignore # ChromeDriverManager gestiona la instalación del controlador de Chrome.
from selenium.webdriver.common.keys import Keys  # type: ignore # Keys es útil para simular eventos de teclado en Selenium.
from selenium.webdriver.support.ui import Select  # type: ignore # Select se utiliza para interactuar con elementos <select> en páginas web.
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
from selenium.common.exceptions import NoSuchElementException # type: ignore # Excepciones comunes de selenium que nos podemos encontrar
from selenium.webdriver.common.by import By # type: ignore

import sys
sys.path.append("../")
from src import soporte as sp


def get_urls(input_data):

    urls_return = []
    try:
        driver = webdriver.Chrome()
        url=input_data[0]
        driver.get(url)
        driver.maximize_window()
        sleep(5)
        driver.find_element('css selector','#rcc-confirm-button').click()
        sleep(5)
        links = driver.find_elements(By.PARTIAL_LINK_TEXT, input_data[1])

        for i in links:
            urls_return.append(i.get_attribute("href"))

        driver.close()
    except:
        print("error en get_urls")

    return urls_return

def magic(input_data, texto):

    listilla= []

    try:
        args = [(i, texto) for i in input_data]

        with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
            resultados = pool.map(get_urls, args)

        for res in resultados:
            listilla.append(res)

    except:
        print("error en magic")
       
    return listilla

def get_list_productos(url_first):

    lista_productos_limpios = []
    try:
        list_urls_super = magic(url_first,"Acceder")

        list_con_categorias=[]

        for supermecados in list_urls_super:
            list_con_categorias.append(magic(supermecados,'Ver'))

        for categoria in list_con_categorias:
            for q in categoria:
                lista_productos_limpios.append(magic(q,'Histórico'))

    except:
        print("error en get_list_productos")

    return lista_productos_limpios

async def get_historico(url):
    
    df_hit_pr = pd.DataFrame()

    try:
        url_sopa = url

        res = requests.get(url_sopa)
        sopa = BeautifulSoup(res.content, "html.parser")

        tabla = sopa.find("tbody")
        tabla_fila = tabla.findAll("tr")
        
        if (res.status_code == 200 and tabla and tabla_fila):
            datos = url.split("/")[3:6]
            supermercado = ''
            categoria = ''
            productos = str(datos[2]).replace('-',' ')

            for x, y in sp.supermercados_dicc.items():
                if (str(datos[0]).replace('-',' ') == x):
                    supermercado = y
            
            for x, y in sp.categorias_dicc.items():
                if (str(datos[1]).replace('-',' ') == x):
                    categoria = y

            lista_historico = []
            
            for tr in tabla_fila:

                lista = tr.findAll("td")
                lista_intermedia = []

                for td in lista:
                    lista_intermedia.append(td.text)
                
                lista_intermedia.extend([supermercado,categoria,productos])
                lista_historico.append(lista_intermedia)

        df_hit_pr = pd.DataFrame(lista_historico)

    except:
        print("error en get_historico(url)")
 
    return df_hit_pr

async def load_datos_historico(lista_productos_limpios):
    df = pd.DataFrame()
    try:

        cola = []

        for sup in lista_productos_limpios:
            for cat in sup:
                for prod in cat:
                    cola.append(get_historico(prod))

        lista_resultado_df = await asyncio.gather(*cola) ## Función de tasks.py

        for i, r in enumerate(lista_resultado_df, 1):
                if (r.empty == False):
                    df = pd.concat([df, r])
                    df.reset_index(drop=True, inplace=True)

    except:
        print("error en load_datos_historico")

    return df

async def main():
    df = pd.DataFrame()

    lista_productos_limpios = get_list_productos(["https://super.facua.org/"])

    df = await load_datos_historico(lista_productos_limpios)

    df = df.rename(columns = {0: 'fecha', 
                    1: 'precio',
                    2: 'Variacion',
                    3: 'id_supermercado',
                    4: 'id_categoria',
                    5: 'producto'})

    return df

if __name__ == "__main__":
    asyncio.run(main())




