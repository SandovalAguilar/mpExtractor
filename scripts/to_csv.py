'''
file -- to_csv.py -- 
'''

# Librerias 
import pandas as pd
from datetime import date
from pathlib import Path

# Modulos
import data_analyzer as da
import html_to_dataframe as td

# Programa principal
def to_csv(df, facultad):
    
    script_path = str(Path( __file__ ).absolute())
    today_date = str(date.today())
    df = df.to_csv( facultad + '_data_' + today_date + '.csv', index = False)

    print("Archivo creado satisfactoriamente en la ruta " + script_path + " con la fecha: " + today_date)

# Este apartado solo debe utilizarse para realizar pruebas individuales del modulo
'''
if __name__ == "__main__":
    
    input_url = input()
    nombre_facultad = input()
    to_csv(da.data_analyzer(input_url, nombre_facultad).full_table, nombre_facultad)
'''