from models.black_scholes import black_scholes_price
from utils.validators import validate_option_type, validate_positive, validate_non_negative


def implied_volatility(option_type, market_price, S, K, T, r, tol=1e-6, max_iter=1000):
    validate_option_type(option_type)
    validate_positive(market_price, "market_price")
    validate_positive(S, "S")
    validate_positive(K, "K")
    validate_positive(T, "T")
    validate_non_negative(r, "r")

    low = 1e-6
    high = 5.0

    for _ in range(max_iter):
        mid = (low + high) / 2
        price = black_scholes_price(option_type, S, K, T, r, mid)

        if abs(price - market_price) < tol:
            return mid

        if price < market_price:
            low = mid
        else:
            high = mid

    return mid