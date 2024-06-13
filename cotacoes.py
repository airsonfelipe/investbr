import pandas as pd
import pandas_datareader.data as pdr
import yfinance
from datetime import datetime, timedelta

# Configurações do Pandas para exibir todas as colunas e linhas
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

def obter_datas():
    # Obter a data atual
    data_atual = datetime.now().date()

    # Calcular a data de 30 dias atrás
    data_30_dias_atras = data_atual - timedelta(days=30)

    # Formatar as datas no formato 'YYYY-MM-DD'
    data_atual_formatada = data_atual.strftime('%Y-%m-%d')
    data_30_dias_atras_formatada = data_30_dias_atras.strftime('%Y-%m-%d')

    # Retornar as datas formatadas
    return data_atual_formatada, data_30_dias_atras_formatada

# Leitura dos ativos de um arquivo de texto
with open('tickers.txt', 'r') as file:
    ativos = file.read().splitlines()

# Exemplo de uso da função
data_atual, data_30_dias_atras = obter_datas()
print("Data de hoje:", data_atual)
print("Data de 30 dias atrás:", data_30_dias_atras)

# Configuração do Yahoo Finance
yfinance.pdr_override()

# Definição das datas inicial e final
data_inicial = data_30_dias_atras
data_final = data_atual

# Obtendo os dados do Yahoo Finance para cada ativo na lista
tabela_cotacoes = pdr.get_data_yahoo(ativos, data_inicial, data_final)[['Open', 'Adj Close']]
# print(tabela_cotacoes)

# Obtendo o preço de abertura e de fechamento do último dia
preco_abertura = tabela_cotacoes.iloc[-1]['Open']
preco_fechamento = tabela_cotacoes.iloc[-1]['Adj Close']
print('Preço de abertura:', preco_abertura)
print('Preço de fechamento:', preco_fechamento)

# Calculando a variação percentual
variacao_percentual = ((preco_fechamento - preco_abertura) / preco_abertura) * 100
print('Variação percentual:', variacao_percentual)

# Convertendo os dados para listas para exibição
preco_abertura_list = preco_abertura.tolist()
preco_fechamento_list = preco_fechamento.tolist()
variacao_percentual_list = variacao_percentual.tolist()

def get_ibovespa_price():
    ibovespa_ticker = '^BVSP'
    ibovespa_data = yfinance.download(ibovespa_ticker, period="1d")
    ibovespa_price = '{:,.0f}'.format(ibovespa_data["Close"].iloc[-1])
    return ibovespa_price

get_ibovespa_price()