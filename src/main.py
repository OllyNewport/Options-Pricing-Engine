from models.black_scholes import black_scholes_price
from models.binomial import binomial_price
from models.monte_carlo import monte_carlo_price
from greeks.greeks import black_scholes_greeks
from utils.market_data import get_latest_stock_price, get_historical_volatility

ticker = "AAPL"

S = get_latest_stock_price(ticker)
K = round(S)
T = 0.5
r = 0.05
sigma = get_historical_volatility(ticker)
option_type = "call"

steps = 100
simulations = 100000

bs_price = black_scholes_price(option_type, S, K, T, r, sigma)
bin_price = binomial_price(option_type, S, K, T, r, sigma, steps)
mc_price = monte_carlo_price(option_type, S, K, T, r, sigma, simulations, seed=42)

delta, theta, rho, gamma, vega = black_scholes_greeks(option_type, S, K, T, r, sigma)

print(f"Ticker: {ticker}")
print(f"Stock price (S): {S:.2f}")
print(f"Strike price (K): {K}")
print(f"Time to expiry (T): {T}")
print(f"Risk-free rate (r): {r}")
print(f"Historical volatility (sigma): {sigma:.4f}")
print()

print(f"Black-Scholes: £{bs_price:.4f}")
print(f"Binomial:      £{bin_price:.4f}")
print(f"Monte Carlo:   £{mc_price:.4f}")
print()

print(f"Delta: {delta:.6f}")
print(f"Gamma: {gamma:.6f}")
print(f"Vega:  {vega:.6f}")
print(f"Theta: {theta:.6f}")
print(f"Rho:   {rho:.6f}")