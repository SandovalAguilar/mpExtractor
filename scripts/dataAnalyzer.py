'''
 * Authors: Ismael Sandoval Aguilar, Edgar Iván Hinojosa Saldaña.
 * Created: 27.10.2022
'''

'''
file -- dataAnalyzer.py -- 
'''

# Librerias
import pandas as pd

# Modulos
import htmlToDataFrame as td

# Clases
class results():

    tables_names = [
        'minTable',
        'maxTable',
        'describeTable',
        'fullTable'
    ]

    def __init__(self, minTable, maxTable, describeData, fullTable):
        self.minTable = minTable
        self.maxTable = maxTable
        self.describeData = describeData
        self.fullTable = fullTable

# Funcion principal
def dataAnalyzer(df):

    # Nuevos nombres para las columnas
    newNames = {
        'i' : 'ID', 
        'n' : 'Nombre', 
        'a' : 'Apellido', 
        'd' : 'Departamento / Facultad',
        'm' : '# de calif.',
        'c' : 'Promedio'
    }

    df = df.rename(columns = newNames)

    # Cambiar el tipo de variale de cada columna
    newTypes = {
        'ID' : 'int',
        '# de calif.' : 'int',
        'Promedio' : 'float'
    }

    df = df.astype(newTypes)

    # Eliminar valores nulos
    nullValues = df.loc[df["Promedio"].isnull()]
    df = df.dropna()

    # Razon entre el numero de calif. y el promedio
    df['Razon'] = df['# de calif.'] / df['Promedio']

    # Top profesores con mejores reseñas
    resultadosMax = df.loc[
        (df["Promedio"] > df["Promedio"].mean()) & 
        (df["# de calif."] > df["# de calif."].mean()) & 
        (df['Razon'] > df['Razon'].mean())]

    resultadosMax = resultadosMax.sort_values(by = "Razon", ascending = False).reset_index(drop = True)
    resultadosMax = resultadosMax.sort_values(by = 'Promedio', ascending = False).reset_index(drop = True)

    # Top profesores con peores reseñas
    resultadosMin = df.loc[
        (df["Promedio"] < df["Promedio"].mean()) & 
        (df["# de calif."] > df["# de calif."].mean()) & 
        (df['Razon'] > df['Razon'].mean())]


    resultadosMin = resultadosMin.sort_values(by = "Razon", ascending = False).reset_index(drop = True)
    resultadosMin = resultadosMin.sort_values(by = 'Promedio').reset_index(drop = True)

    # Estadistica descriptiva

    describeData = df[['# de calif.', 'Promedio', 'Razon']].describe()

    # Se retorna un objeto con los dataframes resultantes
    finalResults = results(resultadosMin, resultadosMax, describeData, df)

    return finalResults

# Este apartado solo debe utilizarse para realizar pruebas individuales del modulo
'''
if __name__ == "__main__":
    
    input_url = 'https://www.misprofesores.com/escuelas/UANL-FCFM_2263'
    nombre_facultad = 'FCFM'
    print(dataAnalyzer(td.toDataFrame(input_url)).fullTable)
'''