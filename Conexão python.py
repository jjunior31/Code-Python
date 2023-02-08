import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"

# Faz uma solicitação HTTP ao site
response = requests.get(url)

# Verifica se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Analisa o HTML da página com BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Extrai o título da página
    title = soup.find("title").text

    print("Título da página:", title)
else:
    print("Falha ao obter a página")
    
    
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.example.com"

# Faz uma solicitação HTTP ao site
response = requests.get(url)

# Verifica se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Analisa o HTML da página com BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Encontra a tabela na página
    table = soup.find("table")

    # Cria um dataframe a partir da tabela
    df = pd.read_html(str(table))[0]

    # Salva o dataframe em um arquivo CSV
    df.to_csv("dados.csv", index=False)

    print("Dados salvos em dados.csv")
else:
    print("Falha ao obter a página")
    
    
