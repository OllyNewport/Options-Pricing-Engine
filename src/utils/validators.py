def validate_option_type(option_type):
    if option_type not in ("call", "put"):
        raise ValueError("option_type must be 'call' or 'put'")


def validate_positive(value, name):
    if value <= 0:
        raise ValueError(f"{name} must be greater than 0")


def validate_non_negative(value, name):
    if value < 0:
        raise ValueError(f"{name} must be greater than or equal to 0")


def validate_option_inputs(option_type, S, K, T, r, sigma):
    validate_option_type(option_type)
    validate_positive(S, "S")
    validate_positive(K, "K")
    validate_positive(T, "T")
    validate_positive(sigma, "sigma")
    validate_non_negative(r, "r")


def validate_binomial_inputs(option_type, S, K, T, r, sigma, steps):
    validate_option_inputs(option_type, S, K, T, r, sigma)
    validate_positive(steps, "steps")


def validate_monte_carlo_inputs(option_type, S, K, T, r, sigma, simulations):
    validate_option_inputs(option_type, S, K, T, r, sigma)
    validate_positive(simulations, "simulations")