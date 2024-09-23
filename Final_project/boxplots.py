import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
import matplotlib.dates as mdates

Deals1 = pd.read_excel('Deals1.xlsx')
Calls = pd.read_excel('Calls.xlsx')
Spend = pd.read_excel('Spend.xlsx')
Quality_mapping = pd.read_excel('Quality_mapping.xlsx') 

# визуализация 'Распределение категориальных данных'

# Объединение Deals1 с Quality_mapping для получения описаний
# Deals1 = Deals1.merge(Quality_mapping[['Quality_code', 'Description']], how='left', left_on='Quality_code', right_on='Quality_code')

# # Определение столбцов для построения графиков
# columns_to_plot = ['Description', 'Stage', 'Source', 'Product', 'Level of Deutsch']

# # Исключение значения 'UNKNOWN' для 'Level of Deutsch'
# Deals1_filtered = Deals1[Deals1['Level of Deutsch'] != 'UNKNOWN']

# # Установка стиля для графиков
# sns.set(style="whitegrid")

# # Определение количества строк и столбцов для графиков
# n_columns = 2  # количество столбцов в сетке подграфиков
# n_rows = math.ceil(len(columns_to_plot) / n_columns)  # количество строк в сетке подграфиков

# # Создание подграфиков для каждого столбца
# fig, axes = plt.subplots(nrows=n_rows, ncols=n_columns, figsize=(15, 12))

# axes = axes.flatten()

# fig.suptitle('Распределение категориальных данных', fontsize=16)

# for i, column in enumerate(columns_to_plot):
#     if column in Deals1_filtered.columns:
#         # Сортировка значений по убыванию частоты
#         order = Deals1_filtered[column].value_counts().index
#         sns.countplot(data=Deals1_filtered, x=column, ax=axes[i], order=order, palette='viridis')
#         axes[i].set_title(f'Распределение {column}')
        
#         # Настройка осей
#         axes[i].set_xlabel('')
#         axes[i].set_ylabel('Количество')
#         axes[i].tick_params(axis='x', rotation=45)


# for j in range(i + 1, len(axes)):
#     fig.delaxes(axes[j])

# plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# plt.savefig('deals1_category_distribution.png')

# plt.show()


# Создание боксплотов для числовых данных Deals1
fig = plt.figure(figsize=(15, 12))  # Увеличиваем высоту фигуры

# Боксплот для 'Initial Amount Paid'
plt.subplot(3, 2, 1)
plt.boxplot([Deals1['Initial Amount Paid'].dropna()], patch_artist=True, labels=['Initial Amount Paid'])
plt.title('Первый взнос')
plt.grid(True)

# Боксплот для 'Offer Total Amount'
plt.subplot(3, 2, 5)
plt.boxplot(Deals1['Offer Total Amount'].dropna(), patch_artist=True)
plt.title('Общая сумма предложения')
plt.grid(True)

# Боксплот для 'Call Duration (in seconds)'
plt.subplot(3, 2, 2)
plt.boxplot(Calls['Call Duration (in seconds)'], patch_artist=True)
plt.title('Продолжительность звонков')
plt.grid(True)

# Боксплот для 'Spend'
plt.subplot(3, 2, 3)
plt.boxplot(Spend['Spend'].dropna(), patch_artist=True)
plt.title('Расходы на рекламу')
plt.grid(True)

# Боксплот для 'Impressions' и 'Clicks'
plt.subplot(3, 2, 4)
plt.boxplot([Spend['Impressions'].dropna(), Spend['Clicks'].dropna()], patch_artist=True, labels=['Impressions', 'Clicks'])
plt.title('Распределение показов и кликов')
plt.grid(True)

fig.suptitle('Распределение числовых данных', fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('combined_boxplots.png')
plt.show()





# import pandas as pd
# import matplotlib.pyplot as plt
# import scipy.stats as stats

# # Загрузка данных
# Deals1 = pd.read_excel('Deals1.xlsx')
# Quality_mapping = pd.read_excel('Quality_mapping.xlsx')

# # Преобразование дат
# Deals1['Closing Date'] = pd.to_datetime(Deals1['Closing Date'], errors='coerce')
# Deals1['Created'] = pd.to_datetime(Deals1['Created'], errors='coerce')

# # Удаление строк с пустыми значениями в датах
# Deals1 = Deals1.dropna(subset=['Closing Date', 'Created'])

# # Рассчитываем продолжительность сделки в днях
# Deals1['duration'] = (Deals1['Closing Date'] - Deals1['Created']).dt.days

# # Объединение данных с Quality_mapping для получения описаний качества
# Deals1 = Deals1.merge(Quality_mapping[['Quality_code', 'Description']], how='left', left_on='Quality_code', right_on='Quality_code')

# # Проведение ANOVA-теста
# anova_result = stats.f_oneway(
#     *[Deals1['duration'][Deals1['Description'] == desc] for desc in Deals1['Description'].unique()]
# )

# # Вывод результата ANOVA-теста
# p_value = anova_result.pvalue
# print(f"P-value ANOVA теста: {p_value:.4f}")

# # Агрегация данных по качеству (средняя продолжительность сделки для каждого уровня качества)
# quality_duration = Deals1.groupby('Description')['duration'].mean().reset_index()

# # Построение графика
# plt.figure(figsize=(10, 6))
# plt.bar(quality_duration['Description'], quality_duration['duration'], color='skyblue', edgecolor='black')
# plt.xlabel('Качество сделки')
# plt.ylabel('Средняя продолжительность сделки (дни)')
# plt.title('Связь качества сделки и средней продолжительности закрытия')
# plt.xticks(rotation=45)
# plt.grid(True)

# # Вывод p-value на график
# plt.text(0.5, max(quality_duration['duration']) * 1.05, f'P-value ANOVA: {p_value:.4f}',
#          horizontalalignment='center', fontsize=12, color='red')


# # Сохранение графика
# plt.savefig('quality_vs_duration.png')
# plt.show()




# # Plotting the distribution of deal durations in seconds (ignoring empty values)
# plt.figure(figsize=(12, 6))
# Deals1['duration_in_seconds'] = Deals1['duration'].dt.total_seconds()
# Deals1['duration_in_seconds'].plot(kind='hist', bins=50)
# plt.xlabel('Продолжительность (в секундах)')
# plt.ylabel('Количество сделок')
# plt.title('Распределение продолжительности сделок')
# plt.savefig('Распределение_продолжительности_сделок.png')
# plt.show()



# # Load the Deals1 and Level of Deutsch mapping data
# Deals1 = pd.read_excel('path_to_deals1.xlsx')
# Level_of_Deutsch_mapping = pd.read_excel('path_to_level_of_deutsch_mapping.xlsx')

# # Step 1: Filter deals where 'Stage' is not 'Lost'
# filtered_deals = Deals1[Deals1['Stage'] != 'Lost']

# # Step 2: Merge with the level mapping file on 'Level of Deutsch'
# merged_deals = filtered_deals.merge(Level_of_Deutsch_mapping, on='Level of Deutsch', how='left')

# # Step 3: Create a histogram of the distribution of 'Level of Deutsch' for successful deals
# plt.figure(figsize=(10, 6))
# plt.hist(merged_deals['Level of Deutsch'], bins=range(1, 8), edgecolor='black', align='left')
# plt.xticks(ticks=range(1, 7), labels=['A1', 'A2', 'B1', 'B2', 'C1', 'C2'])
# plt.title('Распределение уровней владения немецким языком для успешных сделок')
# plt.xlabel('Уровень владения немецким языком')
# plt.ylabel('Количество сделок')

# plt.savefig('Распределение уровней владения немецким языком для успешных сделок.png')
# # Show the plot
# plt.show()
