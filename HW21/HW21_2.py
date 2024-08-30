import numpy as np
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

wine = load_wine()
X = wine.data
y = wine.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

log_reg = LogisticRegression(max_iter=1000)
log_reg.fit(X_train_scaled, y_train)
y_pred_log_reg = log_reg.predict(X_test_scaled)

tree_clf = DecisionTreeClassifier()
tree_clf.fit(X_train_scaled, y_train)
y_pred_tree = tree_clf.predict(X_test_scaled)

def evaluate_classification_model(y_true, y_pred):
    accuracy = accuracy_score(y_true, y_pred)
    report = classification_report(y_true, y_pred, output_dict=True)
    return accuracy, report

accuracy_log_reg, report_log_reg = evaluate_classification_model(y_test, y_pred_log_reg)
accuracy_tree, report_tree = evaluate_classification_model(y_test, y_pred_tree)

print("Logistic regression:")
print(f"Accuracy: {accuracy_log_reg:.2f}")
print("Classification Report:\n", report_log_reg)

print("\nDecision tree:")
print(f"Accuracy: {accuracy_tree:.2f}")
print("Classification Report:\n", report_tree)

#Логистическая регрессия
#Точность: 1.00
# Интерпретация: Логистическая регрессия правильно классифицировала все образцы в тестовой выборке. 
# Это очень высокий результат, который может указывать на то, что модель хорошо справляется с 
# задачей на текущем наборе данных.
# Дерево решений
# Точность: 0.94
# Интерпретация: Дерево решений правильно классифицировало 94% образцов в тестовой выборке. 
# Этот результат немного ниже по сравнению с логистической регрессией, но все равно демонстрирует 
# хорошее качество модели.
