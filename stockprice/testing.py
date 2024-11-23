import yfinance as yf


ticker = yf.Ticker('AAPL')
historical = ticker.history(period = '1d')

print(historical)