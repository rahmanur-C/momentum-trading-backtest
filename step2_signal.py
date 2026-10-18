import yfinance as yf

ticker = "AAPL"
data = yf.Ticker(ticker).history(start="2024-09-03", end="2026-09-01")
# .pct_change() calculates the day-on-day % change
data["daily_return"] = data["Close"].pct_change()

# .rolling(10) creates a 10-day moving window; .sum() adds up the daily returns inside it.
data["momentum_10d"] = data["daily_return"].rolling(window=10).sum()

# if the past 10 days were positive,"in" (1) tomorrow.
# If negative, "out" (0) 
# .shift(1) allows lookahead bias controls
data["position"] = (data["momentum_10d"] > 0).astype(int).shift(1)

print(data[["Close", "daily_return", "momentum_10d", "position"]].tail(15))