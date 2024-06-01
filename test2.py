import yfinance as yf

def dolar_price():
    dolar_ticker = 'USDBRL=X'
    dolar_data = yf.download(dolar_ticker, period="1d")
    dolar_price = '{:,.2f}'.format(dolar_data["Close"].iloc[-1])
    print(dolar_price)
    return dolar_price

dolar_price()