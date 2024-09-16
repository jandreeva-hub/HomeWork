import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Чтение данных из Excel
Deals1 = pd.read_excel('Deals1.xlsx')
Quality_mapping = pd.read_excel('Quality_mapping.xlsx')  # Загрузка данных с описаниями

# Проверяем уникальные значения Quality_code в Deals1 и Quality_mapping
print("Unique values in Deals1 Quality_code:", Deals1['Quality_code'].unique())
print("Unique values in Quality_mapping Quality_code:", Quality_mapping['Quality_code'].unique())

# Объединение Deals1 с Quality_mapping для получения описаний
Deals1 = Deals1.merge(Quality_mapping[['Quality_code', 'Description']], how='left', left_on='Quality_code', right_on='Quality_code')

# Определяем столбцы для построения графиков
# Заменяем 'Quality_code' на 'Description' для визуализации
columns_to_plot = ['Description', 'Stage', 'Source', 'Product']

# Установка стиля для графиков
sns.set(style="whitegrid")

# Создаем подграфики для каждого столбца
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 10))
fig.suptitle('Distribution of Categories in Deals1', fontsize=16)

for ax, column in zip(axes.flatten(), columns_to_plot):
    if column in Deals1.columns:
        if column == 'Description':
            # Переименовываем заголовок для 'Description'
            sns.countplot(data=Deals1, x=column, ax=ax, palette='viridis')
            ax.set_title('Distribution of Quality')
        else:
            sns.countplot(data=Deals1, x=column, ax=ax, palette='viridis')
            ax.set_title(f'Distribution of {column}')
        
        # Устанавливаем пустую подпись оси X для столбцов Stage, Source, Product
        if column in ['Description', 'Stage', 'Source', 'Product']:
            ax.set_xlabel('')  # Убираем подпись оси X
        
        ax.set_ylabel('Count')
        ax.tick_params(axis='x', rotation=45)  # Поворачиваем метки на оси X для удобства чтения
        
    else:
        ax.set_title(f'Column {column} not found')
        ax.axis('off')  # Убираем график, если столбец не найден

# Подгоняем макет
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Сохранение в файл
plt.savefig('deals1_distribution.png')

# Показываем графики
plt.show()
