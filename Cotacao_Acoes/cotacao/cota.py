import yfinance as yf

cotacao_bovespa = yf.download("^BVSP", start="2022-12-01", end="2023-04-01")
print(cotacao_bovespa)