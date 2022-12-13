'''
 * Authors: Ismael Sandoval Aguilar, Edgar Iván Hinojosa Saldaña.
 * Created: 27.10.2022
'''

'''
file -- htmlToDataFrame.py -- 
'''

# Liberias
import requests 
from bs4 import BeautifulSoup as bs
import json
import re
import pandas as pd

# Funcion principal
def toDataFrame(URL_site):

    #URL_site = "https://www.misprofesores.com/escuelas/UANL-FCFM_2263"
    
    html = requests.get(URL_site, verify = True)
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
    print(toDataFrame(input_url))
'''