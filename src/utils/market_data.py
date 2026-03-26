import numpy as np
import yfinance as yf


def get_latest_stock_price(ticker):
    stock = yf.Ticker(ticker)
    history = stock.history(period="5d")

    if history.empty:
        raise ValueError(f"No price data found for ticker '{ticker}'")

    return float(history["Close"].iloc[-1])


def get_historical_volatility(ticker, period="6mo"):
    stock = yf.Ticker(ticker)
    history = stock.history(period=period)

    if history.empty or len(history) < 2:
        raise ValueError(f"Not enough historical data found for ticker '{ticker}'")

    close_prices = history["Close"]
    log_returns = np.log(close_prices / close_prices.shift(1)).dropna()

    daily_vol = log_returns.std()
    annual_vol = daily_vol * np.sqrt(252)

    return float(annual_vol)