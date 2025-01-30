import numpy as np
import pandas as pd
def redimento(data_daily):
    data_daily['Rendimento']= data_daily['Close'].pct_change()
    return data_daily['Rendimento']
    # if len(preço) < 2 :
    #     raise ValueError('dados insuficienes para fazer o calculo')
    # else:
    #     preço_atual = preço[0]
    #     preço_inicial = preço[-1]
    #     rentabilidade = preço_atual - preço_inicial
    #     rentabilidade = rentabilidade / preço_inicial
    #     rentabilidade = rentabilidade * 100
    #     return f"{rentabilidade:.2f}%"


def calcular_volatilidade(rendimento):
    volatilidade = rendimento.std()*np.sqrt(252)*100
    return volatilidade
    # variacao = [(preco[i]-preco[i+1])/preco[i+1] for i in range(len(preco)-1)]
    # volatilidade = np.std(variacao)
    # return f"{volatilidade:.2f}%"
def drawdonw_maximo(data_daily):
    df = data_daily
    df['Pico'] = df['Close'].cummax()
    df['Drawdown'] = (df['Close']-df['Pico'])/df['Pico']*100
    drawdonw_maximo = df['Drawdown'].min()
    return drawdonw_maximo

    
    
    #   df = data_daily
    #   valor_maximo = df['Close'].max()
    #   valor_minimo = df['Close'].min()
    #   drawdonw_maxi = (valor_maximo - valor_minimo)/valor_maximo
    #   drawdonw_maxi = drawdonw_maxi*100
    #   return drawdonw_maxi
    # pico = precos[0]  
    # drawdown_max = 0  

    # for preco in precos:  
    #     if preco > pico:  
    #         pico = preco
    #     drawdown = (pico - preco) / pico  
    #     drawdown_max = max(drawdown_max, drawdown)  
    
    # return f'{drawdown_max * 100:.2f}% ' 
def media_movel(data_daily):
    df = data_daily
    df["SMA_10"] = df["Close"].rolling(window=10).mean()
    df["SMA_50"] = df["Close"].rolling(window=50).mean()