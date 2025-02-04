import requests
import pandas as pd

def busca_dados_na_api(ticker,api_kay):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={api_kay}&outputsizer=compact'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "Time Series (Daily)" in data:
   
          return data
          
        else:
             raise ValueError('Dados nao encontrados ou ticker não encotrados.')
    else:
         raise ConnectionError("Erro ao conectar com Api")

