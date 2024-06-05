from flask import Flask, render_template
from news import noticias_ibov, noticias_acoes_bb, noticias_acoes_vale, noticias_acoes_petrobras

app = Flask(__name__)

@app.route('/')
def homepage():

    # Obtendo as notícias
    first_news_ibov_title, first_news_ibov_link = noticias_ibov()
    first_news_bb_title, first_news_bb_link = noticias_acoes_bb()
    first_news_vale_title, first_news_vale_link = noticias_acoes_vale()
    first_news_petro_title, first_news_petro_link = noticias_acoes_petrobras()

    return render_template('homepage.html',

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
