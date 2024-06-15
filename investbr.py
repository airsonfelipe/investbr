from flask import Flask, render_template
from news import noticias_ibov, noticias_acoes_bb, noticias_acoes_vale, noticias_acoes_petrobras
from cotacoes import cotacoes_stocks, cotacoes_fii, get_ibovespa_price
from graficos import grafico_base64

app = Flask(__name__)

@app.route('/')
def homepage():
    first_news_ibov_title, first_news_ibov_link, first_news_ibov_image = noticias_ibov()
    first_news_bb_title, first_news_bb_link, first_news_bb_image = noticias_acoes_bb()
    first_news_vale_title, first_news_vale_link, first_news_vale_image = noticias_acoes_vale()
    first_news_petro_title, first_news_petro_link, first_news_petro_image = noticias_acoes_petrobras()

    ibovespa_price = get_ibovespa_price()

    preco_abertura_list, preco_fechamento_list, variacao_percentual_list, ativos, tabela_cotacoes = cotacoes_stocks()
    preco_abertura_list_fii, preco_fechamento_list_fii, variacao_percentual_list_fii, ativos_fii, tabela_cotacoes_fii = cotacoes_fii()

    highest_gain = {}
    lowest_drop = {}
    if variacao_percentual_list:
        max_variation_index = variacao_percentual_list.index(max(variacao_percentual_list))
        min_variation_index = variacao_percentual_list.index(min(variacao_percentual_list))

        highest_gain = {
            'ticker': ativos[max_variation_index],
            'variation': variacao_percentual_list[max_variation_index],
            'close_price': preco_fechamento_list[max_variation_index]
        }
        lowest_drop = {
            'ticker': ativos[min_variation_index],
            'variation': variacao_percentual_list[min_variation_index],
            'close_price': preco_fechamento_list[min_variation_index]
        }

    highest_gain_fii = {}
    lowest_drop_fii = {}
    if variacao_percentual_list_fii:
        max_variation_index_fii = variacao_percentual_list_fii.index(max(variacao_percentual_list_fii))
        min_variation_index_fii = variacao_percentual_list_fii.index(min(variacao_percentual_list_fii))

        highest_gain_fii = {
            'ticker': ativos_fii[max_variation_index_fii],
            'variation': variacao_percentual_list_fii[max_variation_index_fii],
            'close_price': preco_fechamento_list_fii[max_variation_index_fii]
        }
        lowest_drop_fii = {
            'ticker': ativos_fii[min_variation_index_fii],
            'variation': variacao_percentual_list_fii[min_variation_index_fii],
            'close_price': preco_fechamento_list_fii[min_variation_index_fii]
        }

    return render_template('homepage.html',
        first_news_ibov_title=first_news_ibov_title,
        first_news_ibov_link=first_news_ibov_link,
        first_news_ibov_image=first_news_ibov_image,
        first_news_bb_title=first_news_bb_title,
        first_news_bb_link=first_news_bb_link,
        first_news_bb_image=first_news_bb_image,
        first_news_vale_title=first_news_vale_title,
        first_news_vale_link=first_news_vale_link,
        first_news_vale_image=first_news_vale_image,
        first_news_petro_title=first_news_petro_title,
        first_news_petro_link=first_news_petro_link,
        first_news_petro_image=first_news_petro_image,

        preco_abertura=preco_abertura_list,
        preco_fechamento=preco_fechamento_list,
        variacao_percentual=variacao_percentual_list,

        highest_gain=highest_gain,
        lowest_drop=lowest_drop,

        preco_abertura_fii=preco_abertura_list_fii,
        preco_fechamento_fii=preco_fechamento_list_fii,
        variacao_percentual_fii=variacao_percentual_list_fii,

        highest_gain_fii=highest_gain_fii,
        lowest_drop_fii=lowest_drop_fii,

        ibovespa_price=ibovespa_price
    )

@app.route('/stocks')
def stocks():
    preco_abertura_list, preco_fechamento_list, variacao_percentual_list, ativos, tabela_cotacoes = cotacoes_stocks()

    stocks_data = []
    for ticker, open_price, close_price, variation in zip(ativos, preco_abertura_list, preco_fechamento_list, variacao_percentual_list):
        stocks_data.append({
            'ticker': ticker,
            'open_price': open_price,
            'close_price': close_price,
            'variation': variation
        })

    stocks_data_sorted = sorted(stocks_data, key=lambda x: x['variation'], reverse=True)

    return render_template('stocks.html', stocks_data=stocks_data_sorted, grafico_base64=grafico_base64)

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == "__main__":
    app.run(debug=True)
