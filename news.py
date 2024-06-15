import yfinance as yf


# NOTICIAS IBOV
def noticias_ibov():
    ibov_ticker = "^BVSP"
    yf_ticker = yf.Ticker(ibov_ticker)
    news = yf_ticker.news

    if news:
        first_news_ibov_title = news[0]['title']
        first_news_ibov_link = news[0]['link']
        return first_news_ibov_title, first_news_ibov_link
    return "No news available.", "#"


# NOTICIAS ACOES BB
def noticias_acoes_bb():
    ticker = 'BDORY'
    yf_ticker = yf.Ticker(ticker)
    news = yf_ticker.news

    if news:
        first_news_bb_title = news[0]['title']
        first_news_bb_link = news[0]['link']
        return first_news_bb_title, first_news_bb_link
    return "No news available.", "#"


# NOTICIAS ACOES VALE
def noticias_acoes_vale():
    ticker = 'VALE'
    yf_ticker = yf.Ticker(ticker)
    news = yf_ticker.news

    if news:
        first_news_vale_title = news[0]['title']
        first_news_vale_link = news[0]['link']
        return first_news_vale_title, first_news_vale_link
    return "No news available.", "#"


# NOTICIAS ACOES PETROBRAS
def noticias_acoes_petrobras():
    ticker = 'PETROBRAS'
    yf_ticker = yf.Ticker(ticker)
    news = yf_ticker.news

    if news:
        first_news_petro_title = news[0]['title']
        first_news_petro_link = news[0]['link']
        return first_news_petro_title, first_news_petro_link
    return "No news available.", "#"

#