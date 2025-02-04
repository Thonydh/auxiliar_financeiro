import numpy as np
import pandas as pd
def redimento(data_daily):
    """calcula o redimento"""
    data_daily['Rendimento']= data_daily['Close'].pct_change()
    return data_daily['Rendimento']
   


def calcular_volatilidade(rendimento):
    """faz  calculo de volatilidade"""
    volatilidade = rendimento.std()*np.sqrt(252)*100
    return volatilidade
    
def drawdonw_maximo(data_daily):
    """faz o calculo do drawdonw maximo com base nos dados da api alfa vantage"""
    df = data_daily
    df['Pico'] = df['Close'].cummax()
    df['Drawdown'] = (df['Close']-df['Pico'])/df['Pico']*100
    drawdonw_maximo = df['Drawdown'].min()
    return f'{drawdonw_maximo:.2f}'

    
def media_movel(data_daily):
    """faz o calculo da media de lucro aparti de um determinado tempo"""
    df = data_daily
    df["SMA_10"] = df["Close"].rolling(window=10).mean()
    df["SMA_50"] = df["Close"].rolling(window=50).mean()