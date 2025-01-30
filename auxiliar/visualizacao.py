import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set(style="whitegrid")
# def grafico_valor_tempo(data_daily):
        
#         plt.figure(figsize=(10,6))
#         plt.plot(data_daily, label = 'Preço')
#         plt.title("Evoluçao do Preço ao Longo do Tempo")
#         plt.xlabel('Tempo')
#         plt.ylabel('Preço')
#         plt.legend()
#         plt.show()
# def grafico_redimento(data_daily,volatilidade):
#         plt.figure(figsize=(10,6))
#         plt.plot(data_daily, label= 'Rendimento diário', color = 'green')
#         plt.title(f'Rendimento Diário (Volatilidade: {volatilidade:.2f}%)')
#         plt.ylabel('Tempo')
#         plt.xlabel('Rendimento')
#         plt.legend()
#         plt.show()
# def grafico_drawdonw(data_daily):
#         plt.figure(figsize=(10, 6))
#         plt.plot(data_daily, label='Drawdown', color='red')
#         plt.title(f'Drawdown (Máxima: {data_daily.min()}%)')
#         plt.xlabel('Tempo')
#         plt.ylabel('Drawdown (%)')
#         plt.legend()
#         plt.show()
def graficos(close,redimento,volatilidade,drawown,SMA10,SMA50):
        # grafico_valor_tempo(close)
        # grafico_redimento(redimento,volatilidade)
        # grafico_drawdonw(drawown)
        plt.figure(figsize=(10,6))
        plt.subplot(2, 2, 1)
        plt.plot(close, label = 'Preço')
        plt.title("Evoluçao do Preço ao Longo do Tempo")
        plt.xlabel('Tempo')
        plt.ylabel('Preço')
        plt.legend()

        plt.subplot(2, 2, 2)
        plt.plot(redimento, label= 'Rendimento diário', color = 'green')
        plt.title(f'Rendimento Diário (Volatilidade: {volatilidade:.2f}%)')
        plt.xlabel('Tempo')
        plt.ylabel('Rendimento')
        plt.legend()

        plt.subplot(2, 2, 3)
        plt.plot(drawown, label='Drawdown', color='red')
        plt.title(f'Drawdown (Máxima: {drawown.min()}%)')
        plt.xlabel('Tempo')
        plt.ylabel('Drawdown (%)')
        plt.legend()

        plt.subplot(2,2,4)
        plt.plot(close, label="Preço", color="blue")
        plt.plot(SMA10, label="Média Móvel (10 dias)", color="orange")
        plt.plot(SMA50,label="Média Móvel (50 dias)", color="green")
        plt.title("Preço com Médias Móveis")
        plt.legend()


        plt.tight_layout()
        plt.show()