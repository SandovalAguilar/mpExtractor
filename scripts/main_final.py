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
from os import system
import msvcrt
from rich.console import Console 
from art import *

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

    console = Console()

    
    # En esta variable se va a poner la URL del drive donde esta el manual
    url_manual = 'https://drive.google.com/file/d/1CY5WHe_YUzP8PSUbZLNO4cg6roFNwfl6/view?usp=sharing'

    # Funcion que pide URL y nombre y valida los datos
    df = validate_url()
    
    #Menu
    opcion = 0
    system('cls')
    while not(opcion == '8'):
        
        console.print("                ===========[MENU]=============", style="bold")
        console.print('             --------------------------------------')
        console.print("\n1.Resumen de Tabla Original              2.Tabla Maestros con mayor promedio", style="#1b8798")
        console.print("\n3.Tabla Maestros con menor promedio      4.Tabla con estadistica descriptiva", style="#e7d84b")
        console.print("\n5.Manual de Usuario                      6.Generar un archivo CSV", style="#d61c59")
        console.print("\n7.Generar un archivo PDF                 8.Salir", style="purple")
        
        

        opcion = input('---Cual opcion quiere escoger?: ')
        if(opcion == '1'):
            system("cls")
            console.print("                ===========[Tabla Original]=============", style="bold blue")
            # Imprime un resumen de la tabla original
            print(df.full_table)
            console.print("Presione una tecla para continuar...", style="bold")
            msvcrt.getch()
            system("cls")
        elif(opcion == '2'):
            system("cls")
            console.print("                ===========[Tabla Maestros Menor Promedio]=============", style="bold green")
            # Imprime un resumen de la tabla de los maestros con menor promedio
            print(df.min_table)
            console.print("Presione una tecla para continuar...", style ="bold")
            msvcrt.getch()
            system("cls")
        elif(opcion == '3'):
            system("cls")
            console.print("                ===========[Tabla Maestros Mayor Promedio]=============", style="bold red")
            # Imprime un resumen de la tabla de los maestros con mayor promedio
            print(df.max_table)
            console.print("Presione una tecla para continuar...", style="bold")
            msvcrt.getch()
            system("cls")
        elif(opcion == '4'):
            system("cls")
            console.print("                ===========[Tabla Estadistica]=============", style="bold #e7d84b")
            # Imprime una tabla con la estadistica descriptiva
            print(df.describe_data)
            console.print("Presione una tecla para continuar...", style="bold")
            msvcrt.getch()
            system("cls")
        elif(opcion == '5'):
            console.print("Se esta abriendo el manual en su navegador", style="underline")
            # Abre el manual en el navegador
            webbrowser.open_new(url_manual)
            system("cls")
        elif(opcion == '6'):
            # Pide de nuevo el nombre de la facultad (validar este dato)
            # Nota: es necesario pedir este dato para usar los modulos to_csv y to_pdf
            facultad_nombre = input("Ingrese el nombre de la Facultad: ")
            # Genera un archivo csv en la ruta del programa
            tc.to_csv(df.full_table, facultad_nombre)
        elif(opcion == '7'):
            # Pide de nuevo el nombre de la facultad (validar este dato)
            facultad_nombre = input("Ingrese el nombre de la Facultad: ")
            # Genera un reporte en PDF en la ruta del programa 
            tp.to_pdf(df)
        elif(opcion == '8'):
            console.print("                ~~~~~~~~~~~~~Saliendo Menu~~~~~~~~~~~~~", style="green")
            system('cls')

        else:
            system('cls')
            console.print("Intente De nuevo", style="underline red")
            print(r"""
         , ,\ ,'\,'\ ,'\ ,\ ,
   ,  ;\/ \' `'     `   '  /|
   |\/                      |
   :                        |
   :                        |
    |                       |
    |                       |
    :               -.     _|
     :                \     `.
     |         ________:______\
     :       ,'o       / o    ;
     :       \       ,'-----./
      \_      `--.--'        )
     ,` `.              ,---'|
     : `                     |
      `,-'                   |
      /      ,---.          ,'
   ,-'            `-,------'
  '   `.        ,--'
        `-.____/
               \
            """)
            console.print("Presione una tecla para continuar...", style="bold")
            msvcrt.getch()
            system('cls')


if __name__ == "__main__":
    main()