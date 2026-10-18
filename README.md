# Momentum Trading Backtest

A Python backtest of a simple rule-based momentum strategy on Apple (AAPL) stock, compared with buy-and-hold.

## Strategy

Hold the stock on day t+1 if the sum of daily returns over the previous 10 trading days is positive; otherwise hold cash. The signal is shifted by one day so the model only uses information that was available at the time (no lookahead bias).

## Result

Period: 3 September 2024 to 31 August 2026, adjusted close prices from Yahoo Finance via `yfinance`. The dates are fixed in the scripts so the result can be reproduced.

| | Value of 1 unit invested |
|---|---|
| Momentum rule | 1.07 |
| Buy and hold | 1.43 |

That is a 7% return for the rule against 43% for buy-and-hold, so the rule underperformed.

To look at why, `step3_returns.py` also compares average daily returns. On the 216 days the rule held cash, Apple averaged +0.16% per day, against +0.04% on the 283 days it held the stock. That is consistent with the rule missing rebound days, but the gap is small compared with day-to-day variation in Apple's returns, so on its own it is weak evidence. Transaction costs are not modelled and would make the strategy look worse.

## Scripts

| Script | What it does |
|---|---|
| `step1_fetch.py` | Downloads and previews the price data |
| `step2_signal.py` | Calculates daily returns, the 10-day momentum score and the buy/cash position |
| `step3_returns.py` | Compares the strategy with buy-and-hold, prints the final values, and compares average daily returns on invested days and cash days |

## Limitations

- One stock, one parameter (a 10-day window), no tuning and no out-of-sample test.
- No transaction costs.
- This is single-stock time-series momentum. The academic literature (Jegadeesh and Titman, 1993) studies cross-sectional momentum, which ranks many stocks against each other. That version was not tested here.
- A 10-day lookback is much shorter than the 3 to 12 month periods used in that literature, and research generally reports reversal rather than momentum at very short horizons. This test did not examine that.

## Run

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python3 step3_returns.py
