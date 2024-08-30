import pandas as pd

data = pd.read_csv('titanic.csv')
data = data.dropna(subset=['Age', 'Pclass', 'Survived'])

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
labels = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100']
data['AgeGroup'] = pd.cut(data['Age'], bins=bins, labels=labels, right=False)

grouped = data.groupby(['AgeGroup', 'Pclass'])
survival_rates = grouped['Survived'].mean().reset_index()

print(survival_rates)
