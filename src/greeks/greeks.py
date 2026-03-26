from models.black_scholes import get_d1_d2

import math
from scipy.stats import norm

def black_scholes_greeks(option_type, S, K, T, r, sigma):

    d1, d2 = get_d1_d2(S, K, T, r, sigma)

    if option_type == "call":
        delta = norm.cdf(d1)                                                                                        # Sensitivity to stock price
        theta = -(S * norm.pdf(d1) * sigma) / (2 * math.sqrt(T)) - r * K * math.exp(-r * T) * norm.cdf(d2)  # Sensitivity to time
        rho = K * T * math.exp(-r * T) * norm.cdf(d2)                                                                 #Sensitivity to interest rates
    elif option_type == "put":
        delta = norm.cdf(d1) - 1                                                                                    # Sensitivity to stock price
        theta = -(S * norm.pdf(d1) * sigma) / (2 * math.sqrt(T)) + r * K * math.exp(-r * T) * norm.cdf(-d2) # Sensitivity to time
        rho = -K * T * math.exp(-r * T) * norm.cdf(-d2)                                                             #Sensitivity to interest rates


    gamma = norm.pdf(d1) / (S * sigma * math.sqrt(T))                                                               # Sensetivity of delta
    vega = S * norm.pdf(d1) * math.sqrt(T)                                                                   # Sensitivity to volatility

    return delta, theta, rho, gamma, vega