import yfinance as yf
from datetime import datetime
import time

#### COTACAO IBOV
def get_ibovespa_price():
    ibovespa_ticker = '^BVSP'
    ibovespa_data = yf.download(ibovespa_ticker, period="1d")
    ibovespa_price = '{:,.0f}'.format(ibovespa_data["Close"].iloc[-1])
    return ibovespa_price

get_ibovespa_price()


#### ALTA DO DIA - STOCKS
def alta_dia():
    with open("tickers.txt", "r") as file:
        brazilian_tickers = [ticker.strip() for ticker in file.readlines()]

    highest_gain = None  # Variável para armazenar a maior alta do dia
    highest_gain_ticker = None  # Variável para armazenar o ticker com a maior alta do dia

    # Define o horário de abertura do mercado (por exemplo, 10:00 da manhã)
    market_open_time = datetime.now().replace(hour=10, minute=0, second=0, microsecond=0)

    for ticker in brazilian_tickers:
        try:
            # Baixa os dados da ação
            stock_data = yf.download(ticker, start=market_open_time)
            open_price = stock_data["Open"].iloc[0]
            close_price = stock_data["Close"].iloc[-1]
            daily_gain = (close_price - open_price) / open_price * 100

            # SE QUISER IMPRIMIR TODOS OS TICKERS
            print(ticker, open_price, close_price)

            if open_price == 0 or close_price == 0:
                print(f"Preço de abertura ou de fechamento igual a zero para o ticker {ticker}. Pulando...")
                continue
        except Exception as e:
            print(f"Erro ao baixar dados para o ticker {ticker}: {e}")
            continue  # Pula para o próximo ticker

        if highest_gain is None or daily_gain > highest_gain:
            highest_gain = daily_gain
            highest_gain_ticker = ticker

    print(close_price, highest_gain_ticker, highest_gain)
    return close_price, highest_gain_ticker, highest_gain
alta_dia()


#### ALTA DO DIA - FIIs
def alta_dia_fii():
    with open("tickers_fii.txt", "r") as file:
        brazilian_tickers_fii = [ticker.strip() for ticker in file.readlines()]

    highest_gain_fii = None  # Variável para armazenar a maior alta do dia
    highest_gain_ticker_fii = None  # Variável para armazenar o ticker com a maior alta do dia

    # Define o horário de abertura do mercado (por exemplo, 10:00 da manhã)
    market_open_time = datetime.now().replace(hour=10, minute=0, second=0, microsecond=0)

    for ticker in brazilian_tickers_fii:
        try:
            # Baixa os dados da ação
            stock_data = yf.download(ticker, start=market_open_time)
            open_price_fii = stock_data["Open"].iloc[0]
            close_price_fii = stock_data["Close"].iloc[-1]
            daily_gain_fii = (close_price_fii - open_price_fii) / open_price_fii * 100

            # SE QUISER IMPRIMIR TODOS OS TICKERS
            print(ticker, open_price_fii, close_price_fii)

            if open_price_fii == 0 or close_price_fii == 0:
                print(f"Preço de abertura ou de fechamento igual a zero para o ticker {ticker}. Pulando...")
                continue
        except Exception as e:
            print(f"Erro ao baixar dados para o ticker {ticker}: {e}")
            continue  # Pula para o próximo ticker

        if highest_gain_fii is None or daily_gain_fii > highest_gain_fii:
            highest_gain_fii = daily_gain_fii
            highest_gain_ticker_fii = ticker

    print(close_price_fii, highest_gain_ticker_fii, highest_gain_fii)
    return close_price_fii, highest_gain_ticker_fii, highest_gain_fii
alta_dia_fii()



