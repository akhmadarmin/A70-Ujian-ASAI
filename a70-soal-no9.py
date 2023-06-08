import math

# parameter yang diketahui
expected_population_frequency = 0.8
observed_frequency = 112 / 1000
variance = 0.12
n = 1000
new_exposure = 1000

# hitung faktor k
k = (0.1 * expected_population_frequency)**2 / variance

# hitung kredibilitas parsial
Z = n / (n + k)

# hitung frekuensi klaim yang diharapkan
expected_frequency = Z * observed_frequency + (1 - Z) * expected_population_frequency

# hitung jumlah klaim yang diharapkan
expected_claims = expected_frequency * new_exposure

print(round(expected_claims))
