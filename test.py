import yfinance as yf

# S&P500 데이터 받아오기
sp500 = yf.download('^GSPC', start='2023-01-01', end='2023-12-31')
print("S&P500 데이터:")
print(sp500)

# XLY 데이터 받아오기
xly = yf.download('XLY', start='2023-01-01', end='2023-12-31')
print("XLY 데이터:")
print(xly)

# XLP 데이터 받아오기
xlp = yf.download('XLP', start='2023-01-01', end='2023-12-31')
print("XLP 데이터:")
print(xlp)