import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df = sns.load_dataset('iris')
#print(df)

petal_length_species_counts = df.groupby(['petal_length', 'species']).size().reset_index(name='count')

sns.barplot(x='petal_length', y='count', hue='species', data=petal_length_species_counts)
plt.title('Iris Species Distribution by Petal Length')
plt.xlabel('Petal Length')
plt.ylabel('Count')
plt.show()


  