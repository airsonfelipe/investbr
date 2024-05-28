import yfinance as yf


# NOTICIAS IBOV


def noticias_ibov():
    # Ticker do índice Ibovespa
    ibov_ticker = "^BVSP"

    # Obter o objeto Ticker do yfinance
    yf_ticker = yf.Ticker(ibov_ticker)

    # Obter notícias relacionadas ao índice Ibovespa
    news = yf_ticker.news

    return news

# Buscar notícias sobre a bolsa brasileira


news_data = noticias_ibov()

news1 = f"- {news_data[0]['title']}: {news_data[0]['link']}"
news2 = f"- {news_data[1]['title']}: {news_data[1]['link']}"
news3 = f"- {news_data[2]['title']}: {news_data[2]['link']}"
news4 = f"- {news_data[3]['title']}: {news_data[3]['link']}"

print(news1)
print(news2)
print(news3)
print(news4)




# NOTICIAS ACOES EM GERAL
def noticias_acoes_bb():
    # Ticker do índice Ibovespa
    ticker = 'BANCO DO BRASIL'

    # Obter o objeto Ticker do yfinance
    yf_ticker = yf.Ticker(ticker)

    # Obter notícias relacionadas ao índice Ibovespa
    news = yf_ticker.news
    return news

# Buscar notícias sobre a bolsa brasileira


news_data = noticias_acoes_bb()

news1_bb = f"- {news_data[0]['title']}: {news_data[0]['link']}"
news2_bb = f"- {news_data[1]['title']}: {news_data[1]['link']}"
news3_bb = f"- {news_data[2]['title']}: {news_data[2]['link']}"
news4_bb = f"- {news_data[3]['title']}: {news_data[3]['link']}"
print(' ')
print(news1_bb)
print(news2_bb)
print(news3_bb)
print(news4_bb)