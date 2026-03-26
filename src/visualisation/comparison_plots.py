import matplotlib.pyplot as plt
from pathlib import Path
from models.black_scholes import black_scholes_price
from models.binomial import binomial_price
from models.monte_carlo import monte_carlo_price


def plot_binomial_convergence(option_type, S, K, T, r, sigma, steps_list):
    bs_price = black_scholes_price(option_type, S, K, T, r, sigma)
    bin_prices = [binomial_price(option_type, S, K, T, r, sigma, steps) for steps in steps_list]

    output_dir = Path("outputs/figures")
    output_dir.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.plot(steps_list, bin_prices, marker="o", label="Binomial")
    plt.axhline(bs_price, linestyle="--", label="Black-Scholes")
    plt.xlabel("Steps")
    plt.ylabel("Option Price")
    plt.title(f"{option_type.capitalize()} Binomial Convergence")
    plt.legend()
    plt.grid(True)
    plt.savefig(output_dir / "binomial_convergence.png")
    plt.close()


def plot_monte_carlo_convergence(option_type, S, K, T, r, sigma, simulations_list, seed=42):
    bs_price = black_scholes_price(option_type, S, K, T, r, sigma)
    mc_prices = [
        monte_carlo_price(option_type, S, K, T, r, sigma, simulations, seed=seed)
        for simulations in simulations_list
    ]

    output_dir = Path("outputs/figures")
    output_dir.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.plot(simulations_list, mc_prices, marker="o", label="Monte Carlo")
    plt.axhline(bs_price, linestyle="--", label="Black-Scholes")
    plt.xlabel("Simulations")
    plt.ylabel("Option Price")
    plt.title(f"{option_type.capitalize()} Monte Carlo Convergence")
    plt.legend()
    plt.grid(True)
    plt.savefig(output_dir / "monte_carlo_convergence.png")
    plt.close()


def plot_model_comparison(option_type, S, K, T, r, sigma, steps, simulations, seed=42):
    bs_price = black_scholes_price(option_type, S, K, T, r, sigma)
    bin_price = binomial_price(option_type, S, K, T, r, sigma, steps)
    mc_price = monte_carlo_price(option_type, S, K, T, r, sigma, simulations, seed=seed)

    labels = ["Black-Scholes", "Binomial", "Monte Carlo"]
    prices = [bs_price, bin_price, mc_price]

    output_dir = Path("outputs/figures")
    output_dir.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.bar(labels, prices)
    plt.ylabel("Option Price")
    plt.title(f"{option_type.capitalize()} Model Comparison")
    plt.grid(True, axis="y")
    plt.savefig(output_dir / "model_comparison.png")
    plt.close()