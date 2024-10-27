# Análisis de Precios y Productos por Supermercado

Este proyecto realiza un análisis exploratorio de los precios de diferentes productos en varios supermercados. El objetivo es identificar tendencias de precios, variabilidad en los precios entre supermercados y la diversidad de productos disponibles. Las visualizaciones interactivas ayudan a entender mejor las dinámicas de precios y la oferta de productos en cada supermercado.

## Estructura del Proyecto

El proyecto está organizado en las siguientes carpetas y archivos:

```
├── data/                  
├── notebooks/            
│   ├── 01_scrap_web.ipynb               
│   ├── 02_insercion_datos_en_BD.ipynb   
│   ├── 03_EDA_y_VISUALIZACION.ipynb     
│   └── 04_Conclusiones.ipynb            
├── src/                   
├── .gitignore            
└── README.md              
```

## Visualizaciones
El proyecto incluye las siguientes visualizaciones interactivas:

1. **Cantidad de Productos por Categoría y Supermercado**    
Muestra la cantidad de productos únicos disponibles en cada combinación de categoría y supermercado, ayudando a identificar la diversidad de la oferta en cada supermercado.

2. **Evolución del Precio Medio por Mes y Categoría**  
Gráfico que muestra cómo cambian los precios promedio de los productos por categoría a lo largo del tiempo, con subplots para cada supermercado.

3. **Precio Promedio por Supermercado con Variabilidad**  
Gráfico de barras que muestra el precio promedio en cada supermercado, junto con barras de error que representan la desviación estándar para indicar la variabilidad de los precios.

4. **Tendencia de Precios a lo Largo del Tiempo por Categoría**   
Gráfico de líneas que muestra la evolución de los precios para cada categoría de producto a lo largo del tiempo.

## Requisitos
El proyecto utiliza las siguientes bibliotecas de Python:
- `pandas`
- ``numpy``
- ``matplotlib``
- ``seaborn``
- ``plotly``
- ``beautifulsoup4``
- ``requests``

## Conclusión 
Las conclusiones del análisis están documentadas en el archivo ``04_Conclusiones.ipynb``.  
Consulta este archivo para obtener un resumen detallado de los hallazgos y las interpretaciones basadas en los gráficos generados.

## Next steps
- Continuar recogiendo datos periódicamente.
- Ampliar las categorías de los supermercados.

> Recuerda que para instalar una biblioteca desde una celda de jupiter debe poner (!) antes del comadno Ej:``!pip install seaborn``  
  
> No dudes en abir una issue si quieres contribuir a este proyecto