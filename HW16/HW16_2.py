from scipy.stats import norm

mean = 30
std_dev = 5

z_low = (25 - mean) / std_dev
z_high = (35 - mean) / std_dev

probability = norm.cdf(z_high) - norm.cdf(z_low)
print(f"probability: {probability:.4f}")
