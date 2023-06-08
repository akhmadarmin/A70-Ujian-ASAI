'''Untuk menghitung standar deviasi dari estimasi fungsi survival pada 𝑥 = 5000, 
kita bisa menggunakan formula standar deviasi dari fungsi survival yang diestimasi dalam distribusi Pareto.

Dalam hal ini, kita akan menggunakan informasi yang diberikan tentang invers matriks informasi.

Fungsi survival dari distribusi Pareto adalah S(x) = (𝜃 / 𝑥) ^ 𝛼, sehingga turunannya terhadap 𝛼 dan 𝜃 adalah 
S'(𝛼) = ln(𝜃 / 𝑥) * S(x) dan S'(𝜃) = -𝛼 / 𝜃 * S(x).
Berikut adalah kode Python yang mencakup rumus ini dan menghitung standar deviasi:
'''
import numpy as np

alpha = 3.0
theta = 1000.0

x = 5000

Sx = (theta / x)**alpha

Sx_alpha = np.log(theta / x) * Sx
Sx_theta = -alpha / theta * Sx

I_inv = np.array([[0.12, 0.0295], [0.0295, 0.33]])

std_dev = np.sqrt(Sx_alpha**2 * I_inv[0, 0] + 2 * Sx_alpha * Sx_theta * I_inv[0, 1] + Sx_theta**2 * I_inv[1, 1])
std_dev