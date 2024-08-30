import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['species'] = iris.target

fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].scatter(iris_df['sepal length (cm)'], iris_df['sepal width (cm)'], c=iris_df['species'], cmap='viridis', edgecolor='k')
axes[0].set_xlabel('sepal length (cm)')
axes[0].set_ylabel('sepal width (cm)')
axes[0].set_title('sepal length vs sepal width')

axes[1].scatter(iris_df['petal length (cm)'], iris_df['petal width (cm)'], c=iris_df['species'], cmap='viridis', edgecolor='k')
axes[1].set_xlabel('petal length (cm)')
axes[1].set_ylabel('petal width (cm)')
axes[1].set_title('petal length vs petal width')

x_limits = [iris_df['sepal length (cm)'].min(), iris_df['sepal length (cm)'].max()]
y_limits = [iris_df['sepal width (cm)'].min(), iris_df['sepal width (cm)'].max()]

axes[0].set_xlim(x_limits)
axes[0].set_ylim(y_limits)

x_limits_petal = [iris_df['petal length (cm)'].min(), iris_df['petal length (cm)'].max()]
y_limits_petal = [iris_df['petal width (cm)'].min(), iris_df['petal width (cm)'].max()]

axes[1].set_xlim(x_limits_petal)
axes[1].set_ylim(y_limits_petal)

plt.tight_layout()
plt.show()
