import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def graficos(close,redimento,volatilidade,drawdown,SMA10,SMA50):
        """faz a expocição do grafico: preço ao longo do tempo, volatilidade, drawdown"""
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
        plt.title(f'Drawdown (Máxima: {drawdown.min()}%)')
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