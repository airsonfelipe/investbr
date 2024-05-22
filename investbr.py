from flask import Flask, render_template
from datetime import datetime
import time
from cotacoes import get_ibovespa_price, alta_dia, alta_dia_fii

app = Flask(__name__)

@app.route('/')
def homepage():

    ibovespa_price = get_ibovespa_price()

    close_price, highest_gain_ticker, highest_gain = alta_dia()
    highest_gain_formatted = '{:.2f}'.format(highest_gain)
    close_price_formatted = "{:.2f}".format(close_price)

    close_price_fii, highest_gain_ticker_fii, highest_gain_fii = alta_dia_fii()
    highest_gain_fii_formatted = '{:.2f}'.format(highest_gain_fii)
    close_price_fii_formatted = "{:.2f}".format(close_price_fii)

    return render_template('homepage.html',
    ibovespa_price=ibovespa_price, highest_gain_ticker=highest_gain_ticker,
    highest_gain_formatted=highest_gain_formatted, close_price_formatted=close_price_formatted,
    close_price_fii_formatted=close_price_fii_formatted, highest_gain_ticker_fii=highest_gain_ticker_fii,
    highest_gain_fii_formatted=highest_gain_fii_formatted)


@app.route('/contacts')
def contact():
    return render_template('contacts.html')


# colocar site no ar
if __name__ == "__main__":
    app.run(debug=True)


    # INSTRUCOES DE COMO CRIAR PAGINA WEB CM PYTHON
    # No terminal instale o Flask: pip install Flask
    # criar a 1 pagina do site
    # route -> financialWebSite.com/
    # funcao -> o que voce quer exibir naquela pagina
    # template