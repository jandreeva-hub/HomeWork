import numpy as np
import matplotlib.pyplot as plt


num_pairs = 10000
pairs = np.random.uniform(0, 1, (num_pairs, 2))

sums = np.sum(pairs, axis=1)

plt.hist(sums, bins=30, edgecolor='black', density=True)
plt.title('Histogram of sums of pairs of values')
plt.xlabel('Sum')
plt.ylabel('Probability Density')
plt.grid(True)
plt.show()
