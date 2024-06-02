import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta


# Função para obter o último dia útil
def obter_ultimo_dia_util(data):
    # Verifica se é fim de semana
    while data.weekday() >= 5:  # 5: Sábado, 6: Domingo
        data -= timedelta(days=1)
    return data


# Função para obter dados do último dia útil
def obter_dados_ultimo_dia_util(ticker, data):
    # Baixar os dados históricos da ação para o último dia útil
    dados = yf.download(ticker, start=data.strftime('%Y-%m-%d'), end=(data + timedelta(days=1)).strftime('%Y-%m-%d'))

    # Verificar se os dados estão disponíveis
    if not dados.empty:
        return dados
    else:
        return None


# Função para obter o preço do Ibovespa
def get_ibovespa_price():
    ibovespa_ticker = '^BVSP'
    ultimo_dia_util = obter_ultimo_dia_util(datetime.now())
    ibovespa_data = obter_dados_ultimo_dia_util(ibovespa_ticker, ultimo_dia_util)
    if ibovespa_data is not None:
        ibovespa_price = '{:,.0f}'.format(ibovespa_data["Close"].iloc[-1])
        return ibovespa_price
    else:
        return "Dados indisponíveis"


# Função para obter a maior alta do dia para ações
def alta_dia(tickers_file):
    with open(tickers_file, "r") as file:
        tickers = [ticker.strip() for ticker in file.readlines()]

    highest_gain = None
    highest_gain_ticker = None
    ultimo_dia_util = obter_ultimo_dia_util(datetime.now())

    for ticker in tickers:
        try:
            stock_data = obter_dados_ultimo_dia_util(ticker, ultimo_dia_util)
            if stock_data is not None:
                open_price = stock_data["Open"].iloc[0]
                close_price = stock_data["Close"].iloc[-1]
                daily_gain = (close_price - open_price) / open_price * 100

                # SE QUISER IMPRIMIR TODOS OS TICKERS
                print(ticker, open_price, close_price)

                if open_price == 0 or close_price == 0:
                    print(f"Preço de abertura ou de fechamento igual a zero para o ticker {ticker}. Pulando...")
                    continue

                if highest_gain is None or daily_gain > highest_gain:
                    highest_gain = daily_gain
                    highest_gain_ticker = ticker
        except Exception as e:
            print(f"Erro ao baixar dados para o ticker {ticker}: {e}")
            continue

    print(highest_gain_ticker, highest_gain)
    return highest_gain_ticker, highest_gain


# Função para obter a maior alta do dia para FIIs
def alta_dia_fii(tickers_file):
    with open(tickers_file, "r") as file:
        tickers_fii = [ticker.strip() for ticker in file.readlines()]

    highest_gain_fii = None
    highest_gain_ticker_fii = None
    ultimo_dia_util = obter_ultimo_dia_util(datetime.now())

    for ticker in tickers_fii:
        try:
            stock_data = obter_dados_ultimo_dia_util(ticker, ultimo_dia_util)
            if stock_data is not None:
                open_price_fii = stock_data["Open"].iloc[0]
                close_price_fii = stock_data["Close"].iloc[-1]
                daily_gain_fii = (close_price_fii - open_price_fii) / open_price_fii * 100

                # SE QUISER IMPRIMIR TODOS OS TICKERS
                print(ticker, open_price_fii, close_price_fii)

                if open_price_fii == 0 or close_price_fii == 0:
                    print(f"Preço de abertura ou de fechamento igual a zero para o ticker {ticker}. Pulando...")
                    continue

                if highest_gain_fii is None or daily_gain_fii > highest_gain_fii:
                    highest_gain_fii = daily_gain_fii
                    highest_gain_ticker_fii = ticker
        except Exception as e:
            print(f"Erro ao baixar dados para o ticker {ticker}: {e}")
            continue

    print(highest_gain_ticker_fii, highest_gain_fii)
    return highest_gain_ticker_fii, highest_gain_fii


# Função para obter o preço do dólar
def dolar_price():
    dolar_ticker = 'USDBRL=X'
    ultimo_dia_util = obter_ultimo_dia_util(datetime.now())
    dolar_data = obter_dados_ultimo_dia_util(dolar_ticker, ultimo_dia_util)
    if dolar_data is not None:
        dolar_price = '{:,.2f}'.format(dolar_data["Close"].iloc[-1])
        print(dolar_price)
        return dolar_price
    else:
        return "Dados indisponíveis"


# Execução das funções
print("Preço do Ibovespa:", get_ibovespa_price())
print("Maior alta do dia - Ações:", alta_dia("tickers.txt"))
print("Maior alta do dia - FIIs:", alta_dia_fii("tickers_fii.txt"))
print("Preço do Dólar:", dolar_price())
