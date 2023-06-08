import scipy.stats as stats
import numpy as np

total_polis = 2000
polis_klaim = 400

p_hat = polis_klaim / total_polis
se = np.sqrt((p_hat * (1 - p_hat)) / total_polis)

z = stats.norm.ppf(0.975)

ci_upper = p_hat + z * se

print(ci_upper)
