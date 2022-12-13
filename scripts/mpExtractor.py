'''
 * "mpExtractor" es un conjunto de scripts, escritos en python, 
 * que permiten obtener las calificaciones de maestros del sitio 
 * web "MisProfesores.com" en un dataframe o archivo csv.
 *
 * Authors: Ismael Sandoval Aguilar, Edgar Iván Hinojosa Saldaña.
 * Created: 27.10.2022
'''

# Librerias
import pandas as pd
import webbrowser 
import os 

# Clases

# Modulos
import htmlToDataFrame as td
import dataAnalyzer as da
import toCSV as tc
import toPDF as tp

# Comprobacion del nombre de la facultad
def validateName():
    while True:
        print('\n ===========[INGRESAR UN ACRONIMO VALIDO]=============')
        print('  --------------------------------------')

        inputFacultad = input()

        if not(str.isalpha(inputFacultad)):
            print("ACRONIMO NO VALIDO")
        else:
            break    
    
    return inputFacultad

# Comprobacion de URL
def validateURL():
    while True:
        print('\n ===========[INGRESAR UNA URL VALIDA]=============')
        print('  --------------------------------------')

        try:
            dataFrame = td.toDataFrame(input())
        except:
            print("URL NO VALIDA")
        else:
            break

    return dataFrame

def printMenu():
    os.system('cls||clear')
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Generar archivo CSV de la tabla completa")
    print("2. Generar archivo CSV de los mejores profesores")
    print("3. Generar archivo CSV de los peores profesores")
    print("4. Generar reporte en PDF")
    print("5. Salir")
    print(67 * "-")

# Menu de opciones
def menuSelector(dataFrame, schoolName):
    loop = True

    while loop:
        printMenu()            
        choice = input("Seleccione una opcion valida [1-5]: ")

        if choice == '1':     
            tc.toCSV(dataFrame.fullTable, schoolName, 'full_table')
            input("Presione cualquier tecla para continuar...")

        if choice == '2':     
            tc.toCSV(dataFrame.maxTable, schoolName, 'max_table')
            input("Presione cualquier tecla para continuar...")

        if choice == '3':     
            tc.toCSV(dataFrame.minTable, schoolName, 'min_table')
            input("Presione cualquier tecla para continuar...")

        if choice == '4':     
            tp.toPDF(dataFrame)
            input("Presione cualquier tecla para continuar...")

        elif choice == '5':
            loop = False
        
        else:
            input("Opcion invalida. Presione cualquier tecla para continuar...")


# Programa principal
def main():
    dataFrame = da.dataAnalyzer(validateURL()) 
    schoolName = validateName()

    menuSelector(dataFrame, schoolName)

    return 0

if __name__ == "__main__":
    main()