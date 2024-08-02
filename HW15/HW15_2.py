import numpy as np
import matplotlib.pyplot as plt

n = 100   
p = 0.5   

size = 1000


binomial_data = np.random.binomial(n, p, size)

lambda_ = n * p

poisson_data = np.random.poisson(lambda_, size)

fig, axs = plt.subplots(1, 2, figsize=(12, 5))

axs[0].hist(binomial_data, bins=30, density=True, alpha=0.6, color='blue')
axs[0].set_title('Binomial distribution')
axs[0].set_xlabel('Meaning')
axs[0].set_ylabel('Frequency')

axs[1].hist(poisson_data, bins=30, density=True, alpha=0.6, color='green')
axs[1].set_title('Poisson distribution')
axs[1].set_xlabel('Meaning')
axs[1].set_ylabel('Frequency')

plt.tight_layout()
plt.show()
