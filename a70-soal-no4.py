import scipy.stats as stats

# Parameter prior
alpha_prior = 4
theta_prior = 0.005
previous_claim = 1000

alpha_posterior = alpha_prior + 1
theta_posterior = 1 / (1 / theta_prior + previous_claim)

expected_claim = 1 / (0.8 * stats.gamma.mean(alpha_posterior, scale=theta_posterior) +
                      0.4 * 0.5 * stats.gamma.mean(alpha_posterior, scale=2*theta_posterior))

expected_claim