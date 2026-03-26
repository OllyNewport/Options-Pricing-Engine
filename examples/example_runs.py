from models.black_scholes import black_scholes_price
from models.binomial import binomial_price
from models.monte_carlo import monte_carlo_price
from greeks.greeks import black_scholes_greeks
from utils.implied_vol import implied_volatility


def run_example():
    S = 42
    K = 40
    T = 0.5
    r = 0.05
    sigma = 0.2
    option_type = "put"
    steps = 100
    simulations = 100000

    bs_price = black_scholes_price(option_type, S, K, T, r, sigma)
    bin_price = binomial_price(option_type, S, K, T, r, sigma, steps)
    mc_price = monte_carlo_price(option_type, S, K, T, r, sigma, simulations, seed=42)
    delta, theta, rho, gamma, vega = black_scholes_greeks(option_type, S, K, T, r, sigma)
    iv = implied_volatility(option_type, bs_price, S, K, T, r)

    print("Example Run")
    print(f"Option type: {option_type}")
    print(f"Black-Scholes: {bs_price:.6f}")
    print(f"Binomial:      {bin_price:.6f}")
    print(f"Monte Carlo:   {mc_price:.6f}")
    print()
    print(f"Delta: {delta:.6f}")
    print(f"Gamma: {gamma:.6f}")
    print(f"Vega:  {vega:.6f}")
    print(f"Theta: {theta:.6f}")
    print(f"Rho:   {rho:.6f}")
    print()
    print(f"Implied Volatility: {iv:.6f}")


if __name__ == "__main__":
    run_example()