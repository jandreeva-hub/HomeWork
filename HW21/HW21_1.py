import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = fetch_california_housing()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name='Price')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

lin_reg = LinearRegression()
lin_reg.fit(X_train_scaled, y_train)
y_pred_lin = lin_reg.predict(X_test_scaled)

tree_reg = DecisionTreeRegressor()
tree_reg.fit(X_train_scaled, y_train)
y_pred_tree = tree_reg.predict(X_test_scaled)

def evaluate_model(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    return mse, r2

mse_lin, r2_lin = evaluate_model(y_test, y_pred_lin)
mse_tree, r2_tree = evaluate_model(y_test, y_pred_tree)

print("Linear regression:")
print(f"MSE: {mse_lin:.2f}")
print(f"R²: {r2_lin:.2f}")

print("\nDecision tree:")
print(f"MSE: {mse_tree:.2f}")
print(f"R²: {r2_tree:.2f}")

# Линейная регрессия
# Среднеквадратичная ошибка (MSE): 0.56 -средняя ошибка предсказаний модели
# Чем меньше значение MSE, тем лучше модель. 
# Коэффициент детерминации (R²): 0.58 -какая доля вариации в ценах на жилье объясняется моделью
# Mодель объясняет 58% вариации в данных. Оставшиеся 42% вариации не объясняются моделью и могут 
# быть вызваны другими факторами.

# Дерево решений
# Среднеквадратичная ошибка (MSE): 0.50
# Значение MSE для дерева решений меньше, чем у линейной регрессии. Это говорит о том, 
# что дерево решений в среднем делает более точные прогнозы, чем линейная регрессия. 
# MSE в 0.50 указывает на меньшую среднюю ошибку в предсказаниях.
# Коэффициент детерминации (R²): 0.62 -выше, чем у линейной регрессии, на 0.04.
# Дерево решений объясняет 62% вариации в ценах на жилье, что немного лучше, 
# чем 58% для линейной регрессии.

# Общая интерпретация
# Точность предсказаний: Дерево решений показывает небольшое, но заметное улучшение в 
# точности предсказаний по сравнению с линейной регрессией, как видно из меньшего значения 
# MSE и большего значения R². Это означает, что дерево решений может лучше улавливать сложные, 
# нелинейные зависимости в данных.

# Заключение
# Если основным приоритетом является простота и интерпретируемость модели, линейная регрессия 
# может быть предпочтительным выбором, несмотря на чуть меньшую точность. 
# Для получения наилучшей точности прогнозов дерево решений может быть лучшим выбором, но 
# требующим больше времени на настройку модели.