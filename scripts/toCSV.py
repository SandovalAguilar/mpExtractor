'''
 * Authors: Ismael Sandoval Aguilar, Edgar Iván Hinojosa Saldaña.
 * Created: 27.10.2022
'''

'''
file -- toCSV.py -- 
'''

# Librerias 
import pandas as pd
from datetime import date
from pathlib import Path

# Modulos
import dataAnalyzer as da
import htmlToDataFrame as td

# Funcion principal
def toCSV(df, facultad, tableType):
    
    script_path = str(Path( __file__ ).absolute())
    today_date = str(date.today())
    df = df.to_csv( facultad + '_' + tableType + '_' + today_date + '.csv', index = False)

    print("Archivo creado satisfactoriamente en la ruta " + script_path + " con la fecha: " + today_date, flush = True)

# Este apartado solo debe utilizarse para realizar pruebas individuales del modulo
'''
if __name__ == "__main__":
    
    input_url = input()
    nombre_facultad = input()
    to_csv(da.data_analyzer(input_url, nombre_facultad).full_table, nombre_facultad)
'''