from flask import Flask, render_template
from news import noticias_ibov, noticias_acoes_bb, noticias_acoes_vale, noticias_acoes_petrobras
from cotacoes import preco_abertura_list, preco_fechamento_list, variacao_percentual_list, ativos


app = Flask(__name__)

@app.route('/')
def homepage():
    # Obtendo as notícias
    first_news_ibov_title, first_news_ibov_link = noticias_ibov()
    first_news_bb_title, first_news_bb_link = noticias_acoes_bb()
    first_news_vale_title, first_news_vale_link = noticias_acoes_vale()
    first_news_petro_title, first_news_petro_link = noticias_acoes_petrobras()

    # Calculando a maior alta e a maior baixa
    highest_gain = max(variacao_percentual_list)
    lowest_drop = min(variacao_percentual_list)

    return render_template('homepage.html',
        first_news_ibov_title=first_news_ibov_title,
        first_news_ibov_link=first_news_ibov_link,
        first_news_bb_title=first_news_bb_title,
        first_news_bb_link=first_news_bb_link,
        first_news_vale_title=first_news_vale_title,
        first_news_vale_link=first_news_vale_link,
        first_news_petro_title=first_news_petro_title,
        first_news_petro_link=first_news_petro_link,

        preco_abertura=preco_abertura_list,
        preco_fechamento=preco_fechamento_list,
        variacao_percentual=variacao_percentual_list,

        highest_gain=highest_gain,
        lowest_drop=lowest_drop,
    )

@app.route('/stocks')
def stocks():
    # Juntando os dados em uma lista de dicionários
    stocks_data = []
    for ticker, open_price, close_price, variation in zip(ativos, preco_abertura_list, preco_fechamento_list,
                                                          variacao_percentual_list):
        stocks_data.append({
            'ticker': ticker,
            'open_price': open_price,
            'close_price': close_price,
            'variation': variation
        })

    # Ordena a lista de ações pela variação percentual (do maior para o menor)
    stocks_data_sorted = sorted(stocks_data, key=lambda x: x['variation'], reverse=True)

    return render_template('stocks.html', stocks_data=stocks_data_sorted)

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == "__main__":
    app.run(debug=True)
