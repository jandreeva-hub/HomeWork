import seaborn as sns
import matplotlib.pyplot as plt


tips = sns.load_dataset('tips')

numeric_tips = tips.select_dtypes(include=[float, int])

corr = numeric_tips.corr()

cmap = sns.diverging_palette(230, 20, as_cmap=True)

plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap=cmap, center=0, vmin=-1, vmax=1, fmt='.2f', linewidths=.5)

plt.title('Heat map of the correlation matrix of the dataset Tips')
plt.show()
