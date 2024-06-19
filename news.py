import yfinance as yf
from PIL import Image

# Imagens

image_bb = "/static/images/bb.jpg"
image_petro = "/static/images/petro.jpg"
image_ibov = "/static/images/ibov.png"
image_vale = "/static/images/vale.jpg"

# Função genérica para buscar notícias
def get_news(ticker):
    yf_ticker = yf.Ticker(ticker)
    news = yf_ticker.news

    if news:
        first_news_title = news[0]['title']
        first_news_link = news[0]['link']
        return first_news_title, first_news_link
    return "No news available.", "#", ""

# NOTICIAS IBOV
def noticias_ibov():
    ibov_ticker = "^BVSP"
    return get_news(ibov_ticker)

# NOTICIAS ACOES BB
def noticias_acoes_bb():
    ticker = 'BDORY'
    return get_news(ticker)

# NOTICIAS ACOES VALE
def noticias_acoes_vale():
    ticker = 'VALE'
    return get_news(ticker)

# NOTICIAS ACOES PETROBRAS
def noticias_acoes_petrobras():
    ticker = 'PETR4.SA'
    return get_news(ticker)
