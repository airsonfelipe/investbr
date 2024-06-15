import matplotlib.pyplot as plt
from io import BytesIO
import base64
from cotacoes import cotacoes_stocks

def criar_grafico():
    _, _, _, _, tabela_cotacoes = cotacoes_stocks()  # Ignorando os outros retornos, pegando apenas tabela_cotacoes

    plt.figure(figsize=(10, 6))  # Ajuste os valores conforme necessário
    tabela_cotacoes['Adj Close'].plot()
    plt.title('Preço de fechamento ajustado nos últimos 30 dias')
    plt.xlabel('Data')
    plt.ylabel('Preço (R$)')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    grafico_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return grafico_base64

grafico_base64 = criar_grafico()
