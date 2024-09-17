import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Чтение данных из Excel
Deals1 = pd.read_excel('Deals1.xlsx')
Calls = pd.read_excel('Calls (Done) (1).xlsx')
Spend = pd.read_excel('Spend (Done) (2).xlsx')
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


# # Создание боксплотов для данных Deals1
Deals1 = pd.read_excel('Deals1.xlsx')
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.boxplot([Deals1['SLA_minutes']], patch_artist=True, labels=['SLA_minutes'])
plt.title('SLA_minutes')
plt.grid(True)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.boxplot([Deals1['Initial Amount Paid']], patch_artist=True, labels=['Initial Amount Paid'])
plt.title('Initial Amount Paid')
plt.grid(True)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.boxplot([Deals1['Offer Total Amount']], patch_artist=True, labels=['Offer Total Amount'])
plt.title('Offer Total Amount')
plt.grid(True)

# Создание боксплотов для данных Calls
Calls = pd.read_excel('Calls.xlsx')
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.boxplot(Calls['Call Duration (in seconds)'], patch_artist=True)
plt.title('Call Duration (in seconds)')
plt.grid(True)

# Создание боксплотов для данных Spend
Spend = pd.read_excel('Spend.xlsx')
plt.subplot(1, 3, 2)
plt.boxplot(Spend['Spend'], patch_artist=True)
plt.title('Spend')
plt.grid(True)

plt.subplot(1, 3, 3)
plt.boxplot([Spend['Impressions'], Spend['Spend'], Spend['Clicks']], patch_artist=True, labels=['Impressions', 'Spend', 'Clicks'])
plt.title('Calls Data Boxplots')
plt.grid(True)



plt.tight_layout()
plt.show()


# # Проанализируйте тенденцию создания сделок с течением времени и их связь с звонками.

Calls = pd.read_excel('Calls.xlsx')
Deals1 = pd.read_excel('Deals1.xlsx')
# Установка индекса для возможности ресемплинга по времени
Calls.set_index('Call Start Date', inplace=True)
Deals1.set_index('Created', inplace=True)

# Агрегация по неделям (суммирование количества звонков и сделок)
calls_weekly = Calls.resample('W').count()
deals_weekly = Deals1.resample('W').count()

# Создание графика
fig, ax = plt.subplots(figsize=(10, 6))

# График для звонков (агрегированные по неделям)
ax.plot(calls_weekly.index, calls_weekly['Id'], label='Calls', color='blue')

# График для сделок (агрегированные по неделям)
ax.plot(deals_weekly.index, deals_weekly['Id'], label='Deals', color='green')

# Добавление подписей и легенды
ax.set_xlabel('Week')
ax.set_ylabel('Count')
ax.set_title('Weekly Calls and Deals')
ax.legend()

# Показ графика
plt.show()

#Изучите распределение времени закрытия сделок и продолжительность периода от создания до закрытия.

Deals1['duration'] = Deals1['closing_time'] - Deals1['creation_time']
# Извлечение только времени из времени закрытия
Deals1['closing_time_only'] = Deals1['closing_time'].dt.time

# Гистограмма распределения времени закрытия
plt.figure(figsize=(12, 6))
Deals1['closing_time_only'].value_counts().sort_index().plot(kind='bar')
plt.xlabel('Время закрытия сделки')
plt.ylabel('Количество сделок')
plt.title('Распределение времени закрытия сделок')
plt.show()
plt.figure(figsize=(12, 6))
Deals1['duration'].dt.total_seconds().plot(kind='hist', bins=50)
plt.xlabel('Продолжительность (в секундах)')
plt.ylabel('Количество сделок')
plt.title('Распределение продолжительности сделок')
plt.show()
