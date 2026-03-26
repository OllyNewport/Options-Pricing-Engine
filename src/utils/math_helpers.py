import math
from scipy.stats import norm


def get_d1_d2(S, K, T, r, sigma):
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    return d1, d2


def normal_cdf(x):
    return norm.cdf(x)


def normal_pdf(x):
    return norm.pdf(x)