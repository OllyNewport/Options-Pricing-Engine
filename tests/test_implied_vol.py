from utils.implied_vol import implied_volatility
from models.black_scholes import black_scholes_price


def test_implied_volatility_recovers_true_sigma_call():
    true_sigma = 0.2
    market_price = black_scholes_price("call", 42, 40, 0.5, 0.05, true_sigma)
    iv = implied_volatility("call", market_price, 42, 40, 0.5, 0.05)
    assert abs(iv - true_sigma) < 1e-4


def test_implied_volatility_recovers_true_sigma_put():
    true_sigma = 0.2
    market_price = black_scholes_price("put", 42, 40, 0.5, 0.05, true_sigma)
    iv = implied_volatility("put", market_price, 42, 40, 0.5, 0.05)
    assert abs(iv - true_sigma) < 1e-4


def test_implied_volatility_positive():
    market_price = black_scholes_price("call", 42, 40, 0.5, 0.05, 0.2)
    iv = implied_volatility("call", market_price, 42, 40, 0.5, 0.05)
    assert iv > 0