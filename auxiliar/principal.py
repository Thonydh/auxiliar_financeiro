import api
from calculos import redimento, calcular_volatilidade,drawdonw_maximo, media_movel
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from visualizacao import graficos
Api_Key = '9IZKALK83MT3S0T5'

def main():
    ticker = input('digite o ticker da ação (exemplo: IBM):').upper()
    
    
    try:
        preco = []
        dado =  api.busca_dados_na_api(ticker,Api_Key)
        for data_serie, valores in dado['Time Series (Daily)'].items():
            preço_de_fechamento = valores['4. close']
            preco.append(float(preço_de_fechamento))
        data_daily = pd.DataFrame({'Close': preco})
        rendimentos = redimento(data_daily)

        print(f'rendimento diario:{rendimentos}')
        media_movel(data_daily)
        volatilidade = calcular_volatilidade(rendimentos)
        print(f'Volatilidade: {volatilidade}')
        drawdonw = drawdonw_maximo(data_daily)
        print(f'Drawdonw maximo: {drawdonw }')
        graficos(data_daily['Close'],data_daily['Rendimento'], volatilidade,data_daily['Drawdown'], data_daily['SMA_10'],data_daily['SMA_50'])

        

        
    except:
        print('Ocoreu um erro')
    
if __name__ == '__main__':
    main()