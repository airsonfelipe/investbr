"""
import pandas as pd
import pandas_datareader.data as pdr
import yfinance

yfinance.pdr_override()

ativos = ['ITUB3.SA', 'PETR4.SA', 'VALE3.SA']

data_inicial = '2024-05-01'
data_final = '2024-06-03'

tabela_cotacoes = pdr.get_data_yahoo('ITUB3.SA', data_inicial, data_final)
print(tabela_cotacoes)

"""

import yfinance as yf
import pandas as pd

# Define o ticker da ação (por exemplo, AAPL para Apple)
ticker_symbol = 'AGRO3.SA'

# Obtém o objeto Ticker da ação
ticker = yf.Ticker(ticker_symbol)


# Função para obter a cotação mais recente
def get_latest_stock_price(ticker):

    # Tenta obter o histórico de preços para o último dia
    stock_info = ticker.history(period='1d')

    # Se não houver dados disponíveis, tenta pegar dados do último mês
    if stock_info.empty:
        stock_info = ticker.history(period='1mo')

    # Se ainda não houver dados, retorna None
    if stock_info.empty:
        return None

    # Pega o último preço de fechamento disponível
    current_price = stock_info['Close'].iloc[-1]
    return current_price


# Busca a cotação atual
current_price = get_latest_stock_price(ticker)

if current_price is not None:
    print(f'A cotação atual da ação {ticker_symbol} é: ${current_price:.2f}')
else:
    print(f'Não foi possível obter a cotação da ação {ticker_symbol}.')
