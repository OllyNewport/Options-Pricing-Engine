from models.black_scholes import black_scholes_price
from models.binomial import binomial_price
from models.monte_carlo import monte_carlo_price
from greeks.greeks import black_scholes_greeks

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

print("Black-Scholes: £", round(bs_price, 2))
print("Binomial: £", round(bin_price, 2))
print("Monte Carlo: £", round(mc_price, 2))
print()

print("delta =", delta)
print("gamma =", gamma)
print("vega =", vega)
print("theta =", theta)
print("rho =", rho)