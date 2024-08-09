import seaborn as sns
import scipy.stats as stats

tips = sns.load_dataset('tips')

total_bill = tips['total_bill']
tip = tips['tip']

corr_coefficient, p_value = stats.pearsonr(total_bill, tip)

print(f'Pearson correlation coefficient: {corr_coefficient:.4f}')
print(f'p-value: {p_value:.4f}')

alpha = 0.05
if p_value < alpha:
    print("The correlation is statistically significant.")
else:
    print("Correlation is not statistically significant.")
