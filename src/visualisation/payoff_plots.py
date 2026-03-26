import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def option_payoff(option_type, stock_prices, K, premium=0.0):
    stock_prices = np.array(stock_prices)

    if option_type == "call":
        payoff = np.maximum(stock_prices - K, 0) - premium
    elif option_type == "put":
        payoff = np.maximum(K - stock_prices, 0) - premium
    else:
        raise ValueError("option_type must be 'call' or 'put'")

    return payoff


def plot_payoff(option_type, K, premium=0.0, stock_min=None, stock_max=None, num_points=200):
    if stock_min is None:
        stock_min = K * 0.5
    if stock_max is None:
        stock_max = K * 1.5

    stock_prices = np.linspace(stock_min, stock_max, num_points)
    payoffs = option_payoff(option_type, stock_prices, K, premium)

    output_dir = Path("outputs/figures")
    output_dir.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.plot(stock_prices, payoffs, label=f"{option_type.capitalize()} Payoff")
    plt.axhline(0, linestyle="--")
    plt.axvline(K, linestyle="--", label=f"Strike = {K}")
    plt.xlabel("Stock Price at Expiry")
    plt.ylabel("Profit / Loss")
    plt.title(f"{option_type.capitalize()} Option Payoff")
    plt.legend()
    plt.grid(True)
    plt.savefig(output_dir / "payoff.png")
    plt.close()