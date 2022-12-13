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

# Comprobacion del nombre de la facultad
def validateString(input_facultad):

    while not(str.isalpha(input_facultad)):
        print("NOMBRE NO VALIDO")
        input_facultad = input()
    
    return input_facultad

# Comprobacion de URL
def validateURL():

    while True:
        print('\n ===========[INGRESAR UNA URL VALIDA]=============')
        print('  --------------------------------------')

        input_url = input()

        try:
            df = td.htmlToDataFrame(input_url)
        except:
            print("URL NO VALIDA")
        else:
            break

    return df

# Programa principal
def main():

    print(validateURL())

    return 0

if __name__ == "__main__":
    main()