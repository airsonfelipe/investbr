import yfinance as yf

def noticias_acoes_vale():
    ticker = 'PETROBRAS'
    yf_ticker = yf.Ticker(ticker)
    news = yf_ticker.news
    print(news)

noticias_acoes_vale()