from greeks.greeks import black_scholes_greeks


def test_call_delta_range():
    delta, theta, rho, gamma, vega = black_scholes_greeks("call", 42, 40, 0.5, 0.05, 0.2)
    assert 0 <= delta <= 1


def test_put_delta_range():
    delta, theta, rho, gamma, vega = black_scholes_greeks("put", 42, 40, 0.5, 0.05, 0.2)
    assert -1 <= delta <= 0


def test_gamma_positive():
    delta, theta, rho, gamma, vega = black_scholes_greeks("call", 42, 40, 0.5, 0.05, 0.2)
    assert gamma > 0


def test_vega_positive():
    delta, theta, rho, gamma, vega = black_scholes_greeks("call", 42, 40, 0.5, 0.05, 0.2)
    assert vega > 0


def test_call_rho_positive():
    delta, theta, rho, gamma, vega = black_scholes_greeks("call", 42, 40, 0.5, 0.05, 0.2)
    assert rho > 0


def test_put_rho_negative():
    delta, theta, rho, gamma, vega = black_scholes_greeks("put", 42, 40, 0.5, 0.05, 0.2)
    assert rho < 0