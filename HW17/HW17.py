import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt


population_size = 1000
population_yes = 600
sample_size = 100
sample_yes = 55  

p_hat = sample_yes / sample_size


standard_error = np.sqrt(p_hat * (1 - p_hat) / sample_size)

z_score = stats.norm.ppf(0.975)  

margin_of_error = z_score * standard_error
confidence_interval = (p_hat - margin_of_error, p_hat + margin_of_error)

print(f'Proportion of "Yes" in the sample: {p_hat:.2f}')
print(f'95% CI: {confidence_interval[0]:.2f} to {confidence_interval[1]:.2f}')




def simulate_sample_means(sample_size, num_samples):
    sample_means = []
    for _ in range(num_samples):
        sample = np.random.uniform(0, 1, sample_size)
        sample_means.append(np.mean(sample))
    return sample_means

num_samples = 1000

sample_sizes = [10, 30, 100]
plt.figure(figsize=(12, 8))

for size in sample_sizes:
    sample_means = simulate_sample_means(size, num_samples)
    plt.subplot(2, 2, sample_sizes.index(size) + 1)
    plt.hist(sample_means, bins=30, edgecolor='k', alpha=0.7)
    plt.title(f'Distribution of means\n Sample size {size}')
    plt.xlabel('Average value')
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()


# Обсуждение:

# Доверительный интервал:

# Доверительный интервал дает диапазон, в котором с вероятностью 95% находится истинная доля "Да"
# в генеральной совокупности. Это значение показывает, насколько точно выборка отражает популяцию. 
# Доверительный интервал учитывает стандартную ошибку и неопределенность выборки.

# Влияние размера выборки:

# При большом размере выборки распределение средних значений будет приближаться к 
# нормальному распределению благодаря Центральной предельной теореме. 
# Это заметно, когда размер выборки увеличивается (например, при размере 100).
# При меньших размерах выборки распределение средних будет менее нормальным и 
# может показывать больше вариации. Это видно при меньших размерах выборки 
# (например, при размере 10).