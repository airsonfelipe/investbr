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





"""
import pandas as pd
import pandas_datareader.data as pdr
import yfinance as yf


def get_open_and_close_price(ticker_symbol):
    # Obtém o objeto Ticker da ação
    ticker = yf.Ticker(ticker_symbol)

    # Tenta obter o histórico de preços para o último dia
    stock_info = ticker.history(period='1d')

    # Se não houver dados disponíveis, retorna None
    if stock_info.empty:
        return None, None, None

    # Pega o preço de abertura e fechamento disponíveis para o último dia
    open_price = stock_info['Open'].iloc[-1]
    close_price = stock_info['Close'].iloc[-1]
    date = stock_info.index[-1]

    if open_price is not None and close_price is not None:
        # Calcula a diferença percentual entre o preço de fechamento e abertura
        difference = ((close_price - open_price) / open_price) * 100
        print(f'A cotação de abertura da ação {ticker_symbol} no dia {date.date()} foi: R${open_price:.2f}')
        print(f'A cotação de fechamento da ação {ticker_symbol} no dia {date.date()} foi: R${close_price:.2f}')
        print(f'A empresa {ticker_symbol} valorizou {difference:.2f}% no dia {date.date()}.')
    elif open_price is None:
        print(f'O preço de abertura da ação {ticker_symbol} não está disponível.')
    elif close_price is None:
        print(f'O preço de fechamento da ação {ticker_symbol} não está disponível.')

    # Exibe o link para obter mais informações sobre a ação
    print(f'Mais informações sobre a ação {ticker_symbol}: '
          f'https://www.google.com/search?q={ticker_symbol.replace(".", "%2E")}+cota%C3%A7%C3%A3o')


# Exemplo de uso
ticker_symbol = 'AGRO3.SA'
get_open_and_close_price(ticker_symbol)
"""