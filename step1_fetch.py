# yfinance is a library for downloading stock price history for free.
import yfinance as yf

# "AAPL" is Apple's ticker
ticker = "AAPL"

# .history() downloads the daily price data.
data = yf.Ticker(ticker).history(start="2024-09-03", end="2026-09-01")

# data is now a "DataFrame" 
# rows = dates, columns = Open, High, Low, Close, Volume.
print(data.head())      # .head() shows just the first 5 rows
print(f"\nTotal rows: {len(data)}")