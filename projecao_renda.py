import pandas as pd
import yfinance as yf

yf.pdr_override()


# -------------------      ENCONTRAR IPCA ATUALIZADO        -----------------------
def consulta_ipca(codigo_bcb):
    url = f'http://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_bcb}/dados?formato=json'
    df = pd.read_json(url)
    df['data'] = pd.to_datetime(df['data'], dayfirst=True)
    df.set_index('data', inplace=True)
    return df


ipca = consulta_ipca(433)
ipca = ipca.loc['2024-01-01':'2024-06-05']
total_ipca = ipca['valor'].sum()

print('Total do IPCA no ano de 2024, até agora, é de: ', total_ipca)

# -------------------      PROJEÇÃO RENDA ANUAL             -----------------------

inflacao_anual = total_ipca / 100

renda_desejada_anual = 240000  # por ano
renda_desejada_acoes = renda_desejada_anual / 2
renda_desejada_fiis = renda_desejada_anual / 2

tickers_proporcao = {
    'BBAS3.SA': 0.06,
    'SANB4.SA': 0.06,
    'ITSA4.SA': 0.06,
    'BBDC3.SA': 0.06,
    'B3SA3.SA': 0.02,
    'TAEE11.SA': 0.05,
    'EGIE3.SA': 0.05,
    'TRPL4.SA': 0.05,
    'ALUP11.SA': 0.05,
    'RAIZ4.SA': 0.03,
    'BBSE3.SA': 0.13,
    'SAPR4.SA': 0.13,
    'VIVT3.SA': 0.10,
    'VALE3.SA': 0.05,
    'KLBN4.SA': 0.05,
    'AGRO3.SA': 0.05,
    'HGLG11.SA': 0.05,
    'BTAL11.SA': 0.05,
    'BTLG11.SA': 0.05,
    'XPLG11.SA': 0.05,
    'GGRC11.SA': 0.05,
    'HGBS11.SA': 0.125,
    'HSML11.SA': 0.125,
    'HGRE11.SA': 0.15,
    'KNRI11.SA': 0.05,
    'ALZR11.SA': 0.05,
    'KNCR11.SA': 0.08,
    'MCCI11.SA': 0.085,
    'CVBI11.SA': 0.085
}


# Função para obter a cotação mais recente e o dividend yield
def valor_dy(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    info = ticker.info
    dividend_yield = info.get('dividendYield')

    # Tenta obter o histórico de preços para o último dia
    stock_info = ticker.history(period='1d')

    # Se não houver dados disponíveis, tenta pegar dados do último mês
    if stock_info.empty:
        stock_info = ticker.history(period='1mo')

    # Se ainda não houver dados, retorna None
    if stock_info.empty:
        return None, None

    # Pega o último preço de fechamento disponível
    current_price = stock_info['Close'].iloc[-1]
    return current_price, dividend_yield


# Dividir tickers em ações e FIIs
acoes = {k: v for k, v in tickers_proporcao.items() if not k.endswith('11.SA')}
fiis = {k: v for k, v in tickers_proporcao.items() if k.endswith('11.SA')}


# Função para calcular e exibir a quantidade de papéis necessários
def calcular_papeis(tickers, renda_desejada):
    for ticker_symbol, proporcao in tickers.items():
        current_price, dividend_yield = valor_dy(ticker_symbol)

        if current_price is None or dividend_yield is None:
            print(f'Não foi possível obter o valor ou o DY de {ticker_symbol}.')
            current_price = float(input(f'Por favor, insira o valor atual de {ticker_symbol}: '))
            dividend_yield = float(input(f'Por favor, insira o dividend yield de {ticker_symbol} (em %): ')) / 100

        renda_por_empresa = renda_desejada * proporcao

        print(f'Valor de {ticker_symbol}: R${current_price:.2f}')
        print(f'DY de {ticker_symbol}: {dividend_yield * 100:.2f}%')
        print(f'Renda desejada por {ticker_symbol}: R${renda_por_empresa:.2f}')

        # Cálculo da quantidade de papéis necessários
        dividendo_por_acao = dividend_yield * current_price
        quantidade_papel = renda_por_empresa / dividendo_por_acao

        print(f'Renda por empresa: R${renda_por_empresa:.2f}')
        print(f'Dividendo por ação: R${dividendo_por_acao:.2f}')
        print(f'Quantidade de papéis necessários: {quantidade_papel:.2f}\n')


# Calcular papéis necessários para ações
print("Ações:\n")
calcular_papeis(acoes, renda_desejada_acoes)

# Calcular papéis necessários para FIIs
print("Fundos Imobiliários:\n")
calcular_papeis(fiis, renda_desejada_fiis)
