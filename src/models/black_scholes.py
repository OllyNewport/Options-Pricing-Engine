import math
from scipy.stats import norm

def get_d1_d2(S, K, T, r, sigma):
    d1 = (math.log(S/K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - (sigma * math.sqrt(T))
    return d1, d2

def black_scholes_price(option_type, S, K, T, r, sigma):

    d1, d2 = get_d1_d2(S, K, T, r, sigma)

    C = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    P = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

    if option_type == "put":
        return P
    elif option_type == "call":
        return C