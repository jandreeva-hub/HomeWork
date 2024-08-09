import seaborn as sns
import pandas as pd
import scipy.stats as stats

tips = sns.load_dataset('tips')

smokers = tips[tips['smoker'] == 'Yes']['total_bill']
non_smokers = tips[tips['smoker'] == 'No']['total_bill']

t_stat, p_value = stats.ttest_ind(smokers, non_smokers)


print(f'Average score for smokers: {smokers.mean():.2f}')
print(f'Average score for non-smokers: {non_smokers.mean():.2f}')
print(f't-stat: {t_stat:.2f}')
print(f'p-value: {p_value:.4f}')


alpha = 0.05
if p_value < alpha:
    print("We reject the null hypothesis that mean scores differ between smokers and nonsmokers.")
else:
    print("We do not reject the null hypothesis: mean scores do not differ between smokers and nonsmokers.")
