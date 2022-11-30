# MP Extractor

"MP Extractor" es un conjunto de scripts, escritos en python, que permiten obtener las calificaciones de maestros del sitio web "MisProfesores.com" en un dataframe o archivo csv.

## Instalación

Para utilizar los scripts "html_to_dataframe.py" y "data_analyzer" es necesario instalar las siguientes librerías a traves del gestor de paquetes [pip](https://pip.pypa.io/en/stable/).

```bash
pip install requests 
pip install BeautifulSoup
pip install pandas 
```

Si se desea exportar los resultados a un archivo PDF, es necesario instalar la siguiente librería.

```bash
pip install dataframe-image
pip install fpdf
```

## Uso

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
