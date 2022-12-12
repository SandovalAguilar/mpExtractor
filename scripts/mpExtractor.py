'''
 * "mpExtractor" es un conjunto de scripts, escritos en python, 
 * que permiten obtener las calificaciones de maestros del sitio 
 * web "MisProfesores.com" en un dataframe o archivo csv.
 *
 * Authors: Ismael Sandoval Aguilar, Edgar Iván Hinojosa Saldaña.
 * Created:   27.10.2022
'''

# Librerias
import pandas as pd
import webbrowser 

# Clases

# Modulos
import htmlToDataFrame as td
import dataAnalyzer as da
import toCSV as tc
import toPDF as tp

#Comprobacion de URL
def validateURL():

    aux = True

    while aux == True:
        print('\n ===========[INGRESAR UNA URL VALIDA]=============')
        print('  --------------------------------------')

        input_url = input()

        print('\n ===========[INGRESAR EL ACRONIMO DE LA FACULTAD]=============')
        print('  --------------------------------------')

        input_facultad = input()

        try:
            df = da.dataAnalyzer(input_url, input_facultad)
        except:
            print("URL NO VALIDA")
            continue

        aux = False

    return df

# Programa principal
def main():

    df = validateURL()



    return 0;

if __name__ == "__main__":
    main()