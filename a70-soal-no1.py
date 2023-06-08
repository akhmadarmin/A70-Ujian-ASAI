from scipy import integrate
import numpy as np

# Parameter distribusi Pareto
alpha = 3.7
theta = 120
deductible = 25

# Fungsi massa probabilitas Pareto
def f(x):
    return alpha * theta**alpha / x**(alpha + 1) if x >= theta else 0

# Fungsi untuk E[X] dan E[X^2]
def expected_x(x):
    return x * f(x) if x > deductible else 0

def expected_x_squared(x):
    return x**2 * f(x) if x > deductible else 0

# Menghitung E[X] dan E[X^2]
E_X, _ = integrate.quad(expected_x, deductible, np.inf)
E_X_squared, _ = integrate.quad(expected_x_squared, deductible, np.inf)

# Menghitung varians
variance = E_X_squared - E_X**2
variance