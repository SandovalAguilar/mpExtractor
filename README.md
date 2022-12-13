# mpExtractor

"mpExtractor" es un conjunto de scripts, escritos en python, que permiten obtener las calificaciones de maestros del sitio web "MisProfesores.com" en un dataframe o archivo csv.

## Instalación

Para utilizar los scripts "html_to_dataframe.py" y "data_analyzer" es necesario instalar las siguientes librerías a traves del gestor de paquetes [pip](https://pip.pypa.io/en/stable/).

```bash
pip install requests 
pip install BeautifulSoup
pip install pandas 
```

Si se desea exportar los resultados a un archivo PDF, es necesario instalar las siguientes librerías.

```bash
pip install dataframe-image
pip install fpdf
```

## Uso

Únicamente ejecutar el script "mpExtractor" e introducir una URL válida del sitio MisProfesores.com que corresponda a una facultad. Por ejemplo:

```
https://www.misprofesores.com/escuelas/UANL-FCFM_2263
```

Posteriormente se desplegarán una serie de opciones como:

- Generar un archivo CSV con todas las valoraciones.
- Generar un archivo CSV con todas las valoraciones más altas.
- Generar un archivo CSV con todas las valoraciones más bajas.
- Generar un reporte en PDF con el top de profesores con mejores y peores valoraciones.

Además, el orden toma en cuenta el número de reseñas de cada maestro: es decir, tiene más peso un maestro con 9 de calificación pero (por ejemplo)
20 reseñas, que uno con la misma calificación pero 5 reseñas.

## Notas adicionales

Este proyecto es un prototipo y podría contener errores. Además, también podría modificarse completamente en el futuro.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change. Please make sure to update tests as appropriate.

