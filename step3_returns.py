import yfinance as yf

ticker = "AAPL"
data = yf.Ticker(ticker).history(start="2024-09-03", end="2026-09-01")

data["daily_return"] = data["Close"].pct_change()
data["momentum_10d"] = data["daily_return"].rolling(window=10).sum()
data["position"] = (data["momentum_10d"] > 0).astype(int).shift(1)

data["strategy_return"] = data["position"] * data["daily_return"]

data["buy_and_hold_growth"] = (1 + data["daily_return"]).cumprod()
data["strategy_growth"] = (1 + data["strategy_return"]).cumprod()

print(data[["buy_and_hold_growth", "strategy_growth"]].tail(10))

final_bh = data["buy_and_hold_growth"].iloc[-1]
final_strat = data["strategy_growth"].iloc[-1]
print(f"\nBuy & hold: £1 became £{final_bh:.2f}")
print(f"Momentum strategy: £1 became £{final_strat:.2f}")
in_days = data[data["position"] == 1]["daily_return"]
out_days = data[data["position"] == 0]["daily_return"]
print(f"Days in market: {len(in_days)}, average daily return: {in_days.mean():.4%}")
print(f"Days in cash:   {len(out_days)}, average daily return on those days: {out_days.mean():.4%}")