from flask import Flask, render_template
from cotacoes import get_ibovespa_price, alta_dia, alta_dia_fii
from news import noticias_ibov, noticias_acoes_bb, noticias_acoes_vale, noticias_acoes_petrobras

app = Flask(__name__)

@app.route('/')
def homepage():
    # Obtendo os dados do Ibovespa
    ibovespa_price = get_ibovespa_price()

    # Obtendo os dados da maior alta do dia para ações
    highest_gain_ticker, highest_gain, highest_gain_close_price = alta_dia("tickers.txt")
    highest_gain_formatted = '{:.2f}'.format(highest_gain) if highest_gain is not None else "N/A"

    # Obtendo os dados da maior alta do dia para FIIs
    highest_gain_ticker_fii, highest_gain_fii, highest_gain_close_price_fii = alta_dia_fii("tickers_fii.txt")
    highest_gain_fii_formatted = '{:.2f}'.format(highest_gain_fii) if highest_gain_fii is not None else "N/A"

    # Obtendo as notícias
    first_news_ibov_title, first_news_ibov_link = noticias_ibov()
    first_news_bb_title, first_news_bb_link = noticias_acoes_bb()
    first_news_vale_title, first_news_vale_link = noticias_acoes_vale()
    first_news_petro_title, first_news_petro_link = noticias_acoes_petrobras()

    return render_template('homepage.html',
        ibovespa_price=ibovespa_price,
        highest_gain_ticker=highest_gain_ticker,
        highest_gain_formatted=highest_gain_formatted,
        highest_gain_close_price=highest_gain_close_price,
        highest_gain_ticker_fii=highest_gain_ticker_fii,
        highest_gain_fii_formatted=highest_gain_fii_formatted,
        highest_gain_close_price_fii=highest_gain_close_price_fii,
        first_news_ibov_title=first_news_ibov_title,
        first_news_ibov_link=first_news_ibov_link,
        first_news_bb_title=first_news_bb_title,
        first_news_bb_link=first_news_bb_link,
        first_news_vale_title=first_news_vale_title,
        first_news_vale_link=first_news_vale_link,
        first_news_petro_title=first_news_petro_title,
        first_news_petro_link=first_news_petro_link
    )

@app.route('/contacts')
def contact():
    return render_template('contacts.html')

if __name__ == "__main__":
    app.run(debug=True)
