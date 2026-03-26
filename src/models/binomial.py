import numpy as np
import math

def binomial_price(option_type, S, K, T, r, sigma, steps):
    dt = T / steps
    u = math.exp(sigma * math.sqrt(dt))
    d = 1 / u
    p = (math.exp(r * dt) - d) / (u - d)
    discount = math.exp(-r * dt)

    # Stock prices and option payoffs at expiry
    option_values = []

    for i in range(steps + 1):
        stock_price = S * (u ** i) * (d ** (steps - i))

        if option_type == "call":
            payoff = max(stock_price - K, 0)
        elif option_type == "put":
            payoff = max(K - stock_price, 0)
        else:
            raise ValueError("option_type must be 'call' or 'put'")
        
        option_values.append(payoff)

    # backward induction
    for step in range(steps - 1, -1, -1):
        for i in range(step + 1):
            option_values[i] = discount * (
                p * option_values[i + 1] + (1 - p) * option_values[i]
            )

    return option_values[0]