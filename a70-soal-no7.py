import scipy.stats as stats

n = 6  # total pegawai
k = 5  # total pegawai laki2
alpha = 3
beta = 3

# menggunakan beta benimoial distribution
prob = stats.betabinom.pmf(k, n, alpha, beta)
print(f'Probability: {prob * 100:.2f}%')
