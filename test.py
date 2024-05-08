import yfinance as yf

def alta_dia():
    with open("tickers.txt", "r") as file:
        brazilian_tickers = [ticker.strip() for ticker in file.readlines()]

    highest_gain = None  # Variável para armazenar a maior alta do dia
    highest_gain_ticker = None  # Variável para armazenar o ticker com a maior alta do dia

    for ticker in brazilian_tickers:
        # Baixa os dados da ação
        try:
            stock_data = yf.download(ticker, period="1d")
            open_price = stock_data["Open"].iloc[0]
            close_price = stock_data["Close"].iloc[-1]
            daily_gain = (close_price - open_price) / open_price * 100
            if highest_gain is None or daily_gain > highest_gain:
                highest_gain = daily_gain
                highest_gain_ticker = ticker
        except Exception as e:
            print(f"Erro ao baixar dados para o ticker {ticker}: {e}")

        # CRIEI ESSAS 2 LINHAS ABAIXO APENAS PARA PODER PEGAR O PRECO DE FECHAMENTO DO TICKER MAIS ALTO
        stock_data2 = yf.download(highest_gain_ticker, period="1d")
        close_price2 = stock_data2["Close"].iloc[-1]

    print(f"Maior alta do dia: {highest_gain_ticker} com {highest_gain}% de ganho.", close_price2)
    return highest_gain_ticker, highest_gain, close_price2

alta_dia()