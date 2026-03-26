import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
src_path = project_root / "src"

if str(src_path) not in sys.path:
    sys.path.append(str(src_path))

from models.black_scholes import black_scholes_price
from visualisation.comparison_plots import (
    plot_model_comparison,
    plot_binomial_convergence,
    plot_monte_carlo_convergence,
)
from visualisation.sensitivity_plots import (
    plot_price_vs_stock,
    plot_price_vs_volatility,
    plot_delta_vs_stock,
    plot_vega_vs_volatility,
)
from visualisation.payoff_plots import plot_payoff


def export_all_figures():
    S = 42
    K = 40
    T = 0.5
    r = 0.05
    sigma = 0.2
    option_type = "put"
    steps = 100
    simulations = 100000
    seed = 42

    bs_price = black_scholes_price(option_type, S, K, T, r, sigma)

    print("Saving model comparison...")
    plot_model_comparison(option_type, S, K, T, r, sigma, steps, simulations, seed=seed)

    print("Saving binomial convergence...")
    plot_binomial_convergence(option_type, S, K, T, r, sigma, [5, 10, 25, 50, 100, 200, 500])

    print("Saving monte carlo convergence...")
    plot_monte_carlo_convergence(option_type, S, K, T, r, sigma, [100, 1000, 5000, 10000, 50000, 100000], seed=seed)

    print("Saving price vs stock...")
    plot_price_vs_stock(option_type, K, T, r, sigma, 20, 70)

    print("Saving price vs volatility...")
    plot_price_vs_volatility(option_type, S, K, T, r, 0.05, 0.8)

    print("Saving delta vs stock...")
    plot_delta_vs_stock(option_type, K, T, r, sigma, 20, 70)

    print("Saving vega vs volatility...")
    plot_vega_vs_volatility(option_type, S, K, T, r, 0.05, 0.8)

    print("Saving payoff...")
    plot_payoff(option_type, K, premium=bs_price)

    print("All figures exported to outputs/figures/")


if __name__ == "__main__":
    export_all_figures()