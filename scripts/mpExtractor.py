'''
Proyecto Integrador de Aprendizaje

Ismael Sandoval Aguilar - 2086210
Alejandro Isaí Avila Avila - 1943548
Raziel Alejandro Ibarra Lucio - 2086238
Jesús Eduardo Brambila Duarte - 2086128
Ian Joshua Montoya Torres - 2086239

Programacion Orientada a Objetos - 031 - A2022
Prof. Jose Luis Candelario Tovar

27 de octubre de 2022
'''

# Librerias
import pandas as pd
import webbrowser 

# Clases

# Modulos
import html_to_dataframe as td
import data_analyzer as da
import to_csv as tc
import to_pdf as tp

#Comprobacion de URL
def validate_url():

    aux = True

    while aux == True:
        print('\n ===========[INGRESAR UNA URL VALIDA]=============')
        print('  --------------------------------------')

        input_url = input()

        print('\n ===========[INGRESAR EL NOMBRE DE LA FACULTAD]=============')
        print('  --------------------------------------')

        input_facultad = input()

        try:
            df = da.data_analyzer(input_url, input_facultad)
        except:
            print("URL NO VALIDA")
            continue

        aux = False

    return df

# Programa principal
def main():
    return 0;

if __name__ == "__main__":
    main()