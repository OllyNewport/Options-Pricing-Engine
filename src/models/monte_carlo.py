import math
import numpy as np


def monte_carlo_price(option_type, S, K, T, r, sigma, simulations, seed=None):
    if seed is not None:
        np.random.seed(seed)

    z = np.random.standard_normal(simulations)
    ST = S * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * z)

    if option_type == "call":
        payoffs = np.maximum(ST - K, 0)
    elif option_type == "put":
        payoffs = np.maximum(K - ST, 0)
    else:
        raise ValueError("option_type must be 'call' or 'put'")

    return math.exp(-r * T) * np.mean(payoffs)

