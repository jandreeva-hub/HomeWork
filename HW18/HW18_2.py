import seaborn as sns
import numpy as np
from scipy import stats


diamonds = sns.load_dataset('diamonds')
prices = diamonds['price']
mean_price = np.mean(prices)

hypothesized_mean = 4000

std_dev = np.std(prices, ddof=1)  
sample_size = len(prices)

z_statistic = (mean_price - hypothesized_mean) / (std_dev / np.sqrt(sample_size))
p_value = 2 * (1 - stats.norm.cdf(np.abs(z_statistic)))

print(f'Average price of diamonds: ${mean_price:.2f}')
print(f'SD: ${std_dev:.2f}')
print(f'z-statistic: {z_statistic:.2f}')
print(f'p-value: {p_value:.4f}')


alpha = 0.05
if p_value < alpha:
    print("We reject the null hypothesis: the average price of diamonds is significantly different from $4000.")
else:
    print("We do not reject the null hypothesis: the average price of diamonds does not differ significantly from $4000.")


