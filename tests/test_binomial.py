from models.black_scholes import black_scholes_price
from models.binomial import binomial_price


def test_binomial_call_positive():
    price = binomial_price("call", 42, 40, 0.5, 0.05, 0.2, 100)
    assert price > 0


def test_binomial_put_positive():
    price = binomial_price("put", 42, 40, 0.5, 0.05, 0.2, 100)
    assert price > 0


def test_binomial_call_close_to_black_scholes():
    bs_price = black_scholes_price("call", 42, 40, 0.5, 0.05, 0.2)
    bin_price = binomial_price("call", 42, 40, 0.5, 0.05, 0.2, 500)

    assert abs(bs_price - bin_price) < 0.05


def test_binomial_put_close_to_black_scholes():
    bs_price = black_scholes_price("put", 42, 40, 0.5, 0.05, 0.2)
    bin_price = binomial_price("put", 42, 40, 0.5, 0.05, 0.2, 500)

    assert abs(bs_price - bin_price) < 0.05


def test_binomial_more_steps_improves_call_accuracy():
    bs_price = black_scholes_price("call", 42, 40, 0.5, 0.05, 0.2)

    bin_price_10 = binomial_price("call", 42, 40, 0.5, 0.05, 0.2, 10)
    bin_price_200 = binomial_price("call", 42, 40, 0.5, 0.05, 0.2, 200)

    error_10 = abs(bs_price - bin_price_10)
    error_200 = abs(bs_price - bin_price_200)

    assert error_200 < error_10