import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, precision_recall_curve

data = load_breast_cancer()
X, y = data.data, data.target

#Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Создание и обучение модели логистической регрессии
model = LogisticRegression(max_iter=10000, random_state=42)
model.fit(X_train, y_train)

#Прогнозирование на тестовых данных
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]  # Вероятности для положительного класса

#Оценка модели
print("Classification Report:\n", classification_report(y_test, y_pred))

#Построение кривой Precision-Recall
precision, recall, _ = precision_recall_curve(y_test, y_prob)

plt.figure(figsize=(10, 6))
plt.plot(recall, precision, marker='.')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.grid(True)
plt.show()


#Precision (Точность):
# Класс 0: Точность равна 0.97. Это означает, что из всех предсказанных случаев класса 0, 97% были правильными.
# Класс 1: Точность равна 0.98. Это означает, что из всех предсказанных случаев класса 1, 98% были правильными.

# Recall (Полнота):
# Класс 0: Полнота равна 0.97. Это означает, что из всех настоящих случаев класса 0, 97% были правильно идентифицированы моделью.
# Класс 1: Полнота равна 0.98. Это означает, что из всех настоящих случаев класса 1, 98% были правильно идентифицированы моделью.

# F1-score:
# Класс 0: F1-score равен 0.97. Это среднее гармоническое между точностью и полнотой для класса 0.
# Класс 1: F1-score равен 0.98. Это среднее гармоническое между точностью и полнотой для класса 1.

# Accuracy (Точность):
# Общая точность модели составляет 0.98. Это означает, что модель правильно классифицировала 98% всех примеров.

# Macro Average:
# Precision: 0.97
# Recall: 0.97
# F1-score: 0.97
# Среднее значение метрик (precision, recall, F1-score) для всех классов, рассчитываемое как 
# простое среднее.
# Weighted Average:
# Precision: 0.98
# Recall: 0.98
# F1-score: 0.98
# Среднее значение метрик (precision, recall, F1-score), взвешенное по количеству образцов в 
# каждом классе.
# Интерпретация

# Сбалансированные результаты: F1-score для обоих классов близки к 1, что свидетельствует о сбалансированности модели в плане точности и полноты.
# Общая точность: Общая точность в 0.98 подтверждает, что модель в целом очень точна и эффективна для этого набора данных.
# Эти результаты указывают на то, что модель логистической регрессии хорошо обучена и хорошо справляется с задачей классификации, что делает ее подходящей для применения в практических задачах, связанных с выявлением рака молочной железы.