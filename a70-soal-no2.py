alpha = 0.8
beta = 40

# Data observasi
kesalahan = 6
waktu_observasi = 100
kesalahan_per_jam = kesalahan / waktu_observasi

alpha_posterior = alpha + kesalahan_per_jam
beta_posterior = beta + 1  

ekspektasi_lambda = alpha_posterior / beta_posterior

ekspektasi_kesalahan = ekspektasi_lambda * 100
print(ekspektasi_kesalahan)