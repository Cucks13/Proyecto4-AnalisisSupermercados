<div style="text-align: center;">
  <img src="https://github.com/Hack-io-Data/Imagenes/blob/main/01-LogosHackio/logo_naranja@4x.png?raw=true" alt="esquema" />
</div>

# Proyecto: Análisis de Precios de Supermercados

## Descripción General

El objetivo de este proyecto es que utilices herramientas de scraping, procesamiento y análisis de datos para recolectar información sobre productos y precios de diferentes supermercados en España. La fuente principal de datos será la página web [FACUA: Precios Supermercados](https://super.facua.org/). A partir de los datos recolectados, deberás crear una base de datos en SQL, realizar un análisis exploratorio y generar visualizaciones que permitan extraer conclusiones sobre la variabilidad de precios entre supermercados y otras posibles tendencias.

La página [FACUA: Precios Supermercados](https://super.facua.org/) proporciona información actualizada sobre los precios de productos básicos en seis grandes supermercados de España: Alcampo, Carrefour, Dia, Eroski, Hipercor y Mercadona. Los usuarios pueden comparar precios de productos como aceite y leche, observar la evolución de precios en diferentes fechas, y ver las mayores subidas de precios recientes. La plataforma revisa a diario la evolución de los precios, permitiendo a los consumidores estar informados sobre las fluctuaciones y posibles abusos en los precios.



## Objetivos Específicos

- **Scraping de datos**: Extraer información detallada de todos los productos disponibles en la web de FACUA para cada uno de los supermercados listados.

- **Almacenamiento en base de datos**: Crear una base de datos en SQL que almacene la información recolectada de manera estructurada.

- **Análisis de Datos**: Debes realizar los siguientes análisis utilizando Python y Pandas:

   - **Comparación de Precios entre Supermercados**: Determinar qué supermercados ofrecen los precios más bajos y cuáles son más caros para cada producto.

   - **Análisis de la Evolución de Precios**: Estudiar cómo han cambiado los precios de los productos a lo largo del tiempo en distintos supermercados.

   - **Detección de Anomalías**: Identificar subidas o bajadas de precios inusuales que podrían señalar prácticas abusivas o promociones.

   - **Análisis de la Dispersión de Precios**: Evaluar la variabilidad de los precios de un mismo producto en diferentes supermercados.

   - **Comparación de Precios Promedio**: Calcular y comparar los precios promedio de cada producto en diferentes supermercados.

- **Visualización de datos**: Generar gráficos y visualizaciones que presenten de manera clara y comprensible los resultados del análisis.


## Requisitos del Proyecto

### 1. Scraping de Datos

- Deberás crear un script en Python que utilice Selenium o Beautiful Soup para navegar por la página de FACUA y extraer el histórico de los precios de todos los productos. 

- El script debe ser capaz de recorrer todos los supermercados y productos disponibles en la página.

- La información extraída debe ser almacenada inicialmente en un formato estructurado (por ejemplo, un archivo CSV).

### 2. Creación de la Base de Datos

- Utilizando SQL, debes diseñar una base de datos relacional que pueda almacenar toda la información de manera eficiente.

- Debes cargar los datos del archivo CSV (o el formato elegido) en la base de datos SQL usando Psycopg2. 

### 3. Análisis y Visualización de Datos

- Con los datos almacenados en SQL, debes escribir consultas SQL para extraer subconjuntos de datos que te permitan realizar análisis específicos.

- Utilizando Pandas, debes cargar los datos extraídos y realizar un análisis exploratorio, identificando patrones como las diferencias de precios entre supermercados, productos más caros o más baratos, etc.



## Como Entregar el Proyecto

La entrega del proyecto se realizará a través de una **issue en GitHub**, trabajando en un repositorio propio en tu cuenta personal. Los pasos que deberás seguir para hacer la entrega del proyecto son:


- **Crear un nuevo repositorio en tu cuenta de GitHub:**

   - Crea un nuevo repositorio llamado `Proyecto4-AnalisisFacua`. Este nombre es obligatorio, no podremos llamarlo de otra forma. 

   - Configuralo como público. 


- **Desarrolla el proyecto:**

   - Implementa el código de los juegos según las especificaciones y guías proporcionadas.

   - Recuerda hacer commits regulares mientras avanzas en el desarrollo:

     ```bash
     git add .
     git commit -m "Descripción del avance"
     git push
     ```


- **Crear una issue en el repositorio original del curso:**

   - Ve al repositorio original del curso y dirígete a la pestaña de **Issues**.

- **Abrir una nueva issue para tu entrega:**

   - Haz clic en **New Issue** y llena los siguientes campos:

     - **Título:** Usa el formato "Entrega Proyecto: ProyectoMineríaDatos - [Tu Nombre]".

     - **Descripción:** En la descripción, incluye:

       - Una breve explicación de tu proyecto.

       - Instrucciones para ejecutar tu código (si aplica).

       - Un enlace a tu repositorio personal donde está alojado el proyecto.


## 🚀 Entrega del Proyecto 🚀

**Fecha y hora límite:**

🗓️ **Lunes a las 9:00 AM.**


**Nota importante:**

⚠️ **Todos los proyectos que sean entregados o modificados después de la hora límite (lunes a las 9:00 AM) se considerarán como no entregados.** Por favor, asegúrate de completar y enviar tu trabajo a tiempo para evitar problemas.


# 🎤 Presentación de Proyectos 🎤

El lunes a primera hora tendremos las **presentaciones de los proyectos**. La dinámica será la siguiente:

- De forma **aleatoria**, seleccionaremos entre **3 y 5 alumnos** para presentar su proyecto.

- Cada alumno tendrá **5 minutos** para explicar su proyecto y hacer una demo en vivo. Durante este tiempo podrán mostrar cómo funciona su juego y resaltar las características principales.

**Detalles importantes:**
- Es importante que lleguéis puntuales, ya que comenzaremos las presentaciones de inmediato.

- Asegúrate de que tu código esté listo y funcional para la demo.

- Todos debemos estar preparados para presentar, ya que la selección será completamente aleatoria.
