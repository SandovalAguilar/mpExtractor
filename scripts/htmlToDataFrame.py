'''
file -- htmlToDataFrame.py -- 
'''

# Liberias
import requests 
from bs4 import BeautifulSoup as bs
import json
import re
import pandas as pd

# Clases
class website: 

    site_name = "Mis Profesores"
    def __init__(self, URL, facultad):
        self.URL = URL
        self.facultad = facultad

# Funcion principal
def toDataFrame(URL_site, facultad):

    #URL_site = "https://www.misprofesores.com/escuelas/UANL-FCFM_2263"
    site = website(URL_site, facultad)
    
    html = requests.get(site.URL, verify = True)
    soup = bs(html.content, "html.parser")

    raw_json = soup.find_all('script', type = 'text/javascript')
    str_json = "[" + re.search(r'{"i.*":\s*"(.*?)"}', str(raw_json)).group() + "]"
    str_to_json = json.loads(str_json)
    
    df = pd.json_normalize(str_to_json)

    return df

# Este apartado solo debe utilizarse para realizar pruebas individuales del modulo
'''
if __name__ == "__main__":
    
    input_url = input()
    nombre_facultad = input()
    print(to_dataframe(input_url, nombre_facultad))
'''