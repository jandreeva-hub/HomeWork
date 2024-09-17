import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

# # Анализ временных рядов
Deals1 = pd.read_excel('Deals1.xlsx')
Calls = pd.read_excel('Calls (Done) (1).xlsx')
Spend = pd.read_excel('Spend (Done) (2).xlsx')

# Проанализируйте тенденцию создания сделок с течением времени и их связь с звонками.

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
Deals1['duration'] = Deals1['Closing Date'] - Deals1['Created']
Deals1['closing_minutes'] = Deals1['Closing Date'].dt.hour * 60 + Deals1['Closing Date'].dt.minute
Deals1['duration_minutes'] = Deals1['duration'].dt.total_seconds() / 60
plt.figure(figsize=(12, 6))
plt.hist(Deals1['duration_minutes'].dropna(), bins=50)
plt.xlabel('Продолжительность (в минутах)')
plt.ylabel('Количество сделок')
plt.title('Распределение продолжительности сделок')
plt.show()





# Фильтрация строк с пропущенными значениями
filtered_deals = Deals1[Deals1['Closing Date'].notnull()]

# Создание столбца с месяцем и годом
filtered_deals['year_month'] = filtered_deals['Closing Date'].dt.to_period('M')

# Подсчет количества сделок по каждому месяцу
monthly_deals_count = filtered_deals.groupby('year_month').size().reset_index(name='deal_count')

# Преобразование period в datetime для удобного отображения
monthly_deals_count['year_month'] = monthly_deals_count['year_month'].dt.to_timestamp()

# Построение гистограммы
plt.figure(figsize=(14, 8))
plt.bar(monthly_deals_count['year_month'], monthly_deals_count['deal_count'], width=20, edgecolor='k')

# Настройка меток осей
plt.xlabel('Дата')
plt.ylabel('Количество сделок в месяц')
plt.title('Среднее количество сделок по месяцам')

# Форматирование даты на оси x
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # Форматирование даты
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())  # Показывать метки каждый месяц
plt.xticks(rotation=45)  # Поворот меток для лучшего отображения

plt.tight_layout()  # Для лучшего отображения графика
plt.show()




# Создание сводной таблицы для тепловой карты
#pivot_table = hourly_deals_by_date.pivot(index='closing_date', columns='closing_hour', values='count').fillna(0)






