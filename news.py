import yfinance as yf
import requests
import bs4


# Função genérica para buscar notícias
def get_news(ticker):
    yf_ticker = yf.Ticker(ticker)
    news = yf_ticker.news

    if news:
        first_news_title = news[0]['title']
        first_news_link = news[0]['link']
        return first_news_title, first_news_link
    return "No news available.", "#"

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

# Imagens das noticias acima

image_bb = "/static/images/bb.jpg"
image_petro = "/static/images/petro.jpg"
image_ibov = "/static/images/ibov.png"
image_vale = "/static/images/vale.jpg"
img_adv01 = "/static/images/advertisement_here_01.png"
img_logo_home = "/static/images/logo_home.png"



# NOTICIAS MEIO DA PAGINA

url = 'https://www.infomoney.com.br/mercados/'
headers = {
    'Cache-Control': 'no-cache, no-store, must-revalidate',
    'Pragma': 'no-cache',
    'Expires': '0'
}
requisicao = requests.get(url, headers=headers)
pagina = bs4.BeautifulSoup(requisicao.text, "html.parser")

# Pegar os elementos dentro de <a> que tenham a classe "article-card__asset-link"
lista_noticias = pagina.find_all("a", class_="article-card__asset-link")

# Pegar os elementos dentro de <img> que tenham a classe "aspect-ratio__image"
imagem_noticia = pagina.find_all("img", class_="aspect-ratio__image")
def noticias_meio_pagina():
    noticias = []
    for noticia, imagem in zip(lista_noticias, imagem_noticia):
        noticia_titulo = noticia.get("title")
        noticia_link = noticia.get("href")
        imagem_url = imagem.get("src")
        noticias.append((noticia_titulo, noticia_link, imagem_url))
    return noticias
# Exemplo de uso
noticias = noticias_meio_pagina()
for titulo, link, imagem in noticias:
    print(titulo)
    print(link)
    print(imagem)
    print("#############")