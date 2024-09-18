import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

# # # Анализ временных рядов
Deals1 = pd.read_excel('Deals1.xlsx')
Calls = pd.read_excel('Calls (Done) (1).xlsx')
Spend = pd.read_excel('Spend (Done) (2).xlsx')

# # Проанализируйте тенденцию создания сделок с течением времени и их связь с звонками.

# Calls = pd.read_excel('Calls.xlsx')
# Deals1 = pd.read_excel('Deals1.xlsx')
# # Установка индекса для возможности ресемплинга по времени
# Calls.set_index('Call Start Date', inplace=True)
# Deals1.set_index('Created', inplace=True)

# # Агрегация по неделям (суммирование количества звонков и сделок)
# calls_weekly = Calls.resample('W').count()
# deals_weekly = Deals1.resample('W').count()

# # Создание графика
# fig, ax = plt.subplots(figsize=(10, 6))

# # График для звонков (агрегированные по неделям)
# ax.plot(calls_weekly.index, calls_weekly['Id'], label='Calls', color='blue')

# # График для сделок (агрегированные по неделям)
# ax.plot(deals_weekly.index, deals_weekly['Id'], label='Deals', color='green')

# # Добавление подписей и легенды
# ax.set_xlabel('Week')
# ax.set_ylabel('Count')
# ax.set_title('Weekly Calls and Deals')
# ax.legend()

# # Показ графика
# plt.show()

# #Изучите распределение времени закрытия сделок и продолжительность периода от создания до закрытия.
# Deals1['duration'] = Deals1['Closing Date'] - Deals1['Created']
# Deals1['closing_minutes'] = Deals1['Closing Date'].dt.hour * 60 + Deals1['Closing Date'].dt.minute
# Deals1['duration_minutes'] = Deals1['duration'].dt.total_seconds() / 60
# plt.figure(figsize=(12, 6))
# plt.hist(Deals1['duration_minutes'].dropna(), bins=50)
# plt.xlabel('Продолжительность (в минутах)')
# plt.ylabel('Количество сделок')
# plt.title('Распределение продолжительности сделок')
# plt.show()





# # Фильтрация строк с пропущенными значениями
# filtered_deals = Deals1[Deals1['Closing Date'].notnull()]

# # Создание столбца с месяцем и годом
# filtered_deals['year_month'] = filtered_deals['Closing Date'].dt.to_period('M')

# # Подсчет количества сделок по каждому месяцу
# monthly_deals_count = filtered_deals.groupby('year_month').size().reset_index(name='deal_count')

# # Преобразование period в datetime для удобного отображения
# monthly_deals_count['year_month'] = monthly_deals_count['year_month'].dt.to_timestamp()

# # Построение гистограммы
# plt.figure(figsize=(14, 8))
# plt.bar(monthly_deals_count['year_month'], monthly_deals_count['deal_count'], width=20, edgecolor='k')

# # Настройка меток осей
# plt.xlabel('Дата')
# plt.ylabel('Количество сделок в месяц')
# plt.title('Среднее количество сделок по месяцам')

# # Форматирование даты на оси x
# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # Форматирование даты
# plt.gca().xaxis.set_major_locator(mdates.MonthLocator())  # Показывать метки каждый месяц
# plt.xticks(rotation=45)  # Поворот меток для лучшего отображения

# plt.tight_layout()  # Для лучшего отображения графика
# plt.show()




# Создание сводной таблицы для тепловой карты
#pivot_table = hourly_deals_by_date.pivot(index='closing_date', columns='closing_hour', values='count').fillna(0)

# Фильтрация строк с пропущенными значениями в столбце 'Closing Date'
filtered_deals = Deals1[Deals1['Closing Date'].notnull()]

# Создание столбца с неделями (год-неделя)
filtered_deals['year_week'] = filtered_deals['Closing Date'].dt.to_period('W').apply(lambda r: r.start_time)

# Подсчет количества сделок по каждой неделе
weekly_deals_count = filtered_deals.groupby('year_week').size().reset_index(name='deal_count')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Построение линейного графика
plt.figure(figsize=(14, 8))
plt.plot(weekly_deals_count['year_week'], weekly_deals_count['deal_count'], marker='o', linestyle='-', color='b')

# Настройка меток осей
plt.xlabel('Дата (неделя)')
plt.ylabel('Количество сделок в неделю')
plt.title('Количество сделок по неделям')

# Форматирование даты на оси x
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # Форматирование даты как "год-месяц-день"
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-W%U'))  # Форматирование как "год-неделя"
plt.xticks(rotation=45)  # Поворот меток для лучшего отображения

# Автоматическое улучшение отображения
plt.tight_layout()

# Отображение графика
plt.show()

# Фильтрация строк с пропущенными значениями в столбце 'Closing Date'
filtered_deals = Deals1[Deals1['Closing Date'].notnull()]

# Создание столбца с месяцем (год-месяц)
filtered_deals['year_month'] = filtered_deals['Closing Date'].dt.to_period('M')

# Подсчет количества сделок по каждому месяцу
monthly_deals_count = filtered_deals.groupby('year_month').size().reset_index(name='deal_count')

# Преобразование period в datetime для удобного отображения на графике
monthly_deals_count['year_month'] = monthly_deals_count['year_month'].dt.to_timestamp()
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Построение линейного графика
plt.figure(figsize=(14, 8))
plt.plot(monthly_deals_count['year_month'], monthly_deals_count['deal_count'], marker='o', linestyle='-', color='b')

# Настройка меток осей
plt.xlabel('Дата (месяц)')
plt.ylabel('Количество сделок в месяц')
plt.title('Количество сделок по месяцам')

# Форматирование даты на оси x
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # Форматирование оси x как "год-месяц"
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())  # Метки по месяцам
plt.xticks(rotation=45)  # Поворот меток для лучшего отображения

# Автоматическое улучшение отображения
plt.tight_layout()

# Отображение графика
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Фильтрация строк с пропущенными значениями в 'Created' и 'Call Start Date'
deals_data = Deals1[Deals1['Created'].notnull()]
calls_data = Calls[Calls['Call Start Date'].notnull()]

# Создание столбца с неделями для сделок
deals_data['creation_week'] = deals_data['Created'].dt.to_period('W').apply(lambda r: r.start_time)

# Создание столбца с неделями для звонков
calls_data['call_week'] = calls_data['Call Start Date'].dt.to_period('W').apply(lambda r: r.start_time)

# Подсчет сделок по неделям
weekly_deals_count = deals_data.groupby('creation_week').size().reset_index(name='deal_count')

# Подсчет звонков по неделям
weekly_calls_count = calls_data.groupby('call_week').size().reset_index(name='call_count')

# Построение графика для сделок и звонков
plt.figure(figsize=(14, 8))

# Построение графика для сделок
plt.plot(weekly_deals_count['creation_week'], weekly_deals_count['deal_count'], label='Сделки', marker='o', linestyle='-')

# Построение графика для звонков
plt.plot(weekly_calls_count['call_week'], weekly_calls_count['call_count'], label='Звонки', marker='x', linestyle='--')

# Объединение данных о сделках и звонках по неделям
merged_weekly_data = pd.merge(weekly_deals_count, weekly_calls_count, left_on='creation_week', right_on='call_week', how='inner')

# Вычисление коэффициента корреляции Пирсона по неделям
correlation = merged_weekly_data['deal_count'].corr(merged_weekly_data['call_count'])

# Настройка меток
plt.xlabel('Неделя')
plt.ylabel('Количество сделок и звонков')
plt.title('Тенденция создания сделок и активность звонков по неделям')
plt.legend()

# Добавление значения корреляции на график
plt.text(0.05, 0.95, f"Корреляция: {correlation:.2f}", transform=plt.gca().transAxes, fontsize=12, verticalalignment='top', bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="white"))

# Поворот меток для оси x
plt.xticks(rotation=45)

# Автоматическое улучшение отображения
plt.tight_layout()

# Отображение графика
plt.show()



