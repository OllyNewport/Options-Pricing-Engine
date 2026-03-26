import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from models.black_scholes import black_scholes_price
from greeks.greeks import black_scholes_greeks


def plot_price_vs_stock(option_type, K, T, r, sigma, stock_min, stock_max, num_points=200):
    stock_prices = np.linspace(stock_min, stock_max, num_points)
    prices = [black_scholes_price(option_type, S, K, T, r, sigma) for S in stock_prices]

    output_dir = Path("outputs/figures")
    output_dir.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.plot(stock_prices, prices, label="Option Price")
    plt.axvline(K, linestyle="--", label=f"Strike = {K}")
    plt.xlabel("Stock Price")
    plt.ylabel("Option Price")
    plt.title(f"{option_type.capitalize()} Price vs Stock Price")
    plt.legend()
    plt.grid(True)
    plt.savefig(output_dir / "price_vs_stock.png")
    plt.close()


def plot_price_vs_volatility(option_type, S, K, T, r, vol_min, vol_max, num_points=200):
    volatilities = np.linspace(vol_min, vol_max, num_points)
    prices = [black_scholes_price(option_type, S, K, T, r, sigma) for sigma in volatilities]

    output_dir = Path("outputs/figures")
    output_dir.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.plot(volatilities, prices, label="Option Price")
    plt.xlabel("Volatility")
    plt.ylabel("Option Price")
    plt.title(f"{option_type.capitalize()} Price vs Volatility")
    plt.legend()
    plt.grid(True)
    plt.savefig(output_dir / "price_vs_volatility.png")
    plt.close()


def plot_delta_vs_stock(option_type, K, T, r, sigma, stock_min, stock_max, num_points=200):
    stock_prices = np.linspace(stock_min, stock_max, num_points)
    deltas = [black_scholes_greeks(option_type, S, K, T, r, sigma)[0] for S in stock_prices]

    output_dir = Path("outputs/figures")
    output_dir.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.plot(stock_prices, deltas, label="Delta")
    plt.axvline(K, linestyle="--", label=f"Strike = {K}")
    plt.xlabel("Stock Price")
    plt.ylabel("Delta")
    plt.title(f"{option_type.capitalize()} Delta vs Stock Price")
    plt.legend()
    plt.grid(True)
    plt.savefig(output_dir / "delta_vs_stock.png")
    plt.close()


def plot_vega_vs_volatility(option_type, S, K, T, r, vol_min, vol_max, num_points=200):
    volatilities = np.linspace(vol_min, vol_max, num_points)
    vegas = [black_scholes_greeks(option_type, S, K, T, r, sigma)[4] for sigma in volatilities]

    output_dir = Path("outputs/figures")
    output_dir.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.plot(volatilities, vegas, label="Vega")
    plt.xlabel("Volatility")
    plt.ylabel("Vega")
    plt.title(f"{option_type.capitalize()} Vega vs Volatility")
    plt.legend()
    plt.grid(True)
    plt.savefig(output_dir / "vega_vs_volatility.png")
    plt.close()