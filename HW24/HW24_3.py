import pandas as pd
from sklearn.datasets import load_iris
from scipy import stats

iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target
df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

setosa = df[df['species'] == 'setosa']

petal_length_setosa = setosa['petal length (cm)']

mean_petal_length = petal_length_setosa.mean()

hypothesized_value = 1.5

t_stat, p_value = stats.ttest_1samp(petal_length_setosa, hypothesized_value)

print(f"mean petal length Iris setosa: {mean_petal_length:.2f} cm")
print(f"t-stat: {t_stat:.2f}")
print(f"p-value: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print("mean petal length Iris setosa differ significantly from 1.5 cm")
else:
    print("mean petal length Iris setosa not differ significantly from 1.5 cm")
