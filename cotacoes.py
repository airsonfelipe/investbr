import pandas as pd
import pandas_datareader.data as pdr
import yfinance
from datetime import datetime, timedelta

# Configurações do Pandas para exibir todas as colunas e linhas
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

def obter_datas():
    data_atual = datetime.now().date()
    data_30_dias_atras = data_atual - timedelta(days=30)
    return data_atual.strftime('%Y-%m-%d'), data_30_dias_atras.strftime('%Y-%m-%d')

def cotacoes_stocks():
    with open('tickers.txt', 'r') as file:
        ativos = file.read().splitlines()

    data_atual, data_30_dias_atras = obter_datas()

    yfinance.pdr_override()
    data_inicial = data_30_dias_atras
    data_final = data_atual

    tabela_cotacoes = pdr.get_data_yahoo(ativos, data_inicial, data_final)[['Open', 'Adj Close']]
    preco_abertura = tabela_cotacoes.iloc[-1]['Open']
    preco_fechamento = tabela_cotacoes.iloc[-1]['Adj Close']
    variacao_percentual = ((preco_fechamento - preco_abertura) / preco_abertura) * 100

    preco_abertura_list = preco_abertura.tolist()
    preco_fechamento_list = preco_fechamento.tolist()
    variacao_percentual_list = variacao_percentual.tolist()

    return preco_abertura_list, preco_fechamento_list, variacao_percentual_list, ativos, tabela_cotacoes


def cotacoes_fii():
    with open('tickers_fii.txt', 'r') as file:
        ativos_fii = file.read().splitlines()

    data_atual, data_30_dias_atras = obter_datas()

    yfinance.pdr_override()
    data_inicial = data_30_dias_atras
    data_final = data_atual

    tabela_cotacoes_fii = pdr.get_data_yahoo(ativos_fii, data_inicial, data_final)[['Open', 'Adj Close']]
    preco_abertura_fii = tabela_cotacoes_fii.iloc[-1]['Open']
    preco_fechamento_fii = tabela_cotacoes_fii.iloc[-1]['Adj Close']
    variacao_percentual_fii = ((preco_fechamento_fii - preco_abertura_fii) / preco_abertura_fii) * 100

    preco_abertura_list_fii = preco_abertura_fii.tolist()
    preco_fechamento_list_fii = preco_fechamento_fii.tolist()
    variacao_percentual_list_fii = variacao_percentual_fii.tolist()

    return preco_abertura_list_fii, preco_fechamento_list_fii, variacao_percentual_list_fii, ativos_fii, tabela_cotacoes_fii


def get_ibovespa_price():
    ibovespa_ticker = '^BVSP'
    ibovespa_data = yfinance.download(ibovespa_ticker, period="1d")
    ibovespa_price = '{:,.0f}'.format(ibovespa_data["Close"].iloc[-1])
    return ibovespa_price

get_ibovespa_price()
