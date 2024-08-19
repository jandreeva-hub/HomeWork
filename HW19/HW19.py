import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import OrdinalEncoder


# Загрузка и первоначальная проверка данных
# 1. Загрузите датасет с данными о продажах подержанных машин
# 2. Вызовите первые и последние 5 строк в данных
# 3. Проверьте, какие типы данных имеет каждый столбец
# 4. Вычислите количество пропущенных значений в каждом столбце
# 5. Вычислите количество уникальных значений в каждой столбце (метод nununique, можно применить ко всему датасету сразу)
# 6. Проверьте датасет на наличие повторяющихся строк
# 7. Вычислите процент пропущенных значений в каждом столбцe
### Преобразование данных
# 1. Исключите из датасета колонки, которые не могут принести пользы
# 2. Создайте новый столбец на основе данных о годе выпуска автомобиля. Новый столбец должен показывать возраст автомобиля (за дату отсчета возьмите сегодняшнюю дату)
# 3. Разделите столбец с наименованием автомобиля на 2 столбца - столбец с маркой и столбец с моделью
# 4. Изучите столбец с маркой автомобиля. Рассмотрите уникальные значения столбца. Что необходимо исправить в столбце? Внесите необходимые корректировки
# 5. После создания датасета сбросьте изначальную колонку с полным названием автомобиля
# 6. Отделите числовые данные от единиц измерения в столбцах Mileage, Engine, Power, New_Price
# 7. Изучите новые столбцы с единицами измерения на предмет пропущенных и уникальных значений
# 8. Переведите данные с расходом топлива в единую систему измерения (1 km/kg=1.333 kmpl)

# ### Преобразование данных 2
# 1. Проверьте, есть ли опечатки в столбцах Fuel_Type, Transmission, Owner_Type
# 2. Проверьте, какому типу данных соответствует столбец Seats. Измените тип данных если это возможно
# 3. Приведите столбцы Engine, Power, New_Price к числовым типам. Проверьте, требуется ли унификация единиц измерения.
# 4. Проверьте, остались ли еще в датасете пропущенные значения. Почему? Что с ними можно сделать? 


dan = pd.read_csv("used_cars_data.csv")
# print(dan.head())
# print(dan.tail())
# print(dan.sample(10))
# print(dan.info())
# print(dan.dtypes)
# dan1 = pd.DataFrame({"zero":round(dan.isnull().sum()/dan.shape[0]*100,2)})
# dan1['zero'] = dan1['zero'].astype(str)+'%'
# print(dan1)
# print(dan.nunique())

dan.drop_duplicates()
dan = dan.drop(['Car_owner'], axis=1) # drop empty columns
#print(dan.head())

from datetime import timedelta
dan['Age'] = pd.to_datetime('2024-08-12')
dan['Age']

from datetime import timedelta, date
date.today()

dan['Age'] = date.today().year - dan['Year']
#print(dan['Age'])

dan['Marka'] = dan['Name'].str.split().str.get(0)
dan['Marka'].unique()
dan['Model'] = dan['Name'].str.split().str.get(1) + dan['Name'].str.split().str.get(2)
#print(dan['Model'])
dan['Marka'] = dan['Marka'].replace({'ISUZU': 'Isuzu', 'Mini' : 'Mini Cooper', 'Land' : 'Land Rover', 'OpelCorsa' : 'Opel'})
#print(dan.head())

dan['Mileage_value'] = dan['Mileage'].str.split().str.get(0).astype(float)
dan['Mileage_name'] = dan['Mileage'].str.split().str.get(1)
dan['Mileage_name']

dan = dan.drop(['Name'], axis=1) # drop empty columns
#print(dan.head())

dan['Engine_value'] = dan['Engine'].str.split().str.get(0).astype(float)
dan['Engine_name'] = dan['Engine'].str.split().str.get(1)
#print(dan['Engine_value'])

dan['Power_value'] = dan['Power'].str.split().str.get(0)
dan['Power_name'] = dan['Power'].str.split().str.get(1)

dan['Power_value'] = dan['Power_value'].replace({'null' : np.nan})

dan['Power_value'] = dan['Power_value'].astype(float)
#print(dan['Power_value'])

dan['New_Price_value'] = dan['New_Price'].str.split().str.get(0).astype(float)
dan['New_Price_name'] = dan['New_Price'].str.split().str.get(1)
dan['New_Price_name']

dan = dan.drop(['Mileage', 'Engine', 'Power', 'New_Price'], axis=1) # drop empty columns
#print(dan.head())

dan[
	    dan['Mileage_name'] == 'km/kg'
	]['Mileage_value'] =  dan[
	        dan['Mileage_name'] == 'km/kg'
	    ]['Mileage_value'] * 1.333

dan['Mileage_name'] = 'kmpl'
#print(dan.head())

dan[
	    dan['New_Price_name'] == 'Cr'
	]['New_Price_value'] =  dan[
	        dan['New_Price_name'] == 'Cr'
	    ]['New_Price_value'] * 100

dan['New_Price_name'] = 'Lakh'
#print(dan.head())


dan['Seats'].mode()[0]

dan['Seats'] = dan['Seats'].fillna(dan['Seats'].mode()[0])

#print(dan['Mileage_value'])
sns.histplot(dan['Mileage_value'])

dan['Mileage_value'] = dan['Mileage_value'].fillna(dan['Mileage_value'].median())
dan['Mileage_value'].median()

#print(dan['Engine_value'])
#sns.histplot(dan['Engine_value'])

dan['Engine_value'] = dan['Engine_value'].fillna(dan['Engine_value'].mode()[0])
dan['Engine_name'] = dan['Engine_name'].fillna('CC')
dan['Power_value'] = dan['Power_value'].fillna(dan['Power_value'].median())
dan['Power_name'] = dan['Power_name'].fillna('bhp')
dan['Engine_value'] = dan['Engine_value'].astype('int64')
dan['Seats'] = dan['Seats'].astype('int64')

grouped_dan = dan.groupby('Marka')['Price'].mean().reset_index()
mean_price_dict = grouped_dan.set_index('Marka')['Price'].to_dict()

# Заполнение пропусков в исходном DataFrame
dan['Price'] = dan.apply(lambda row: mean_price_dict[row['Marka']] if pd.isna(row['Price']) else row['Price'], axis=1)
sns.histplot(dan['Price'])
dan['Price'] = dan['Price'].fillna(dan['Price'].median())


#dan.to_csv('dan.csv', index=False)		

### Описательные статистики
# 1. Выведите описательные статистики числовых переменных
# 2. Какие выводы можно сделать?

# Kilometers_Driven пробег
# Mileage_value расход топлива
# Engine_value объем двигателя
# Engine_name  кубические сантиметры СС

### Одномерный анализ
# 1. Визуализируйте распределения числовых переменных с помощью гистограмм и боксплотов. Охарайктеризуйте распределения всех переменных
# 2. Визуализируйте категориальные переменные с помощью гистограмм (проведите необходимые преобразования если необходимо)
# 3. Создайте преобразованные колонки Price и Kilometers_Driven. Преобразование сделайте с помощью натурального логарифма (np.log1p)
# 4. Сравните распределение изначальных колонок и преобразованных

dan['Kilometers_Driven'] = dan['Kilometers_Driven'].replace(to_replace=6500000, value=650000) #замена явно ошибочного значения

#print(dan.head())
# print(dan.tail())
# print(dan.sample(10))
#print(dan.info())
#print(dan.dtypes)
# price_description = dan['Price'].describe()
# print(price_description)

# Построение гистограмм
variables = ['Year', 'Kilometers_Driven', 'Age', 'Mileage_value', 'Engine_value', 'Power_value', 'Price']

# Создание фигуры и подграфиков
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(18, 10), sharex=False, sharey=False)
axes = axes.flatten()  # Преобразуем массив подграфиков в плоский массив

for ax, var in zip(axes, variables):
    ax.hist(dan[var], color='skyblue', bins=20, edgecolor='black')
    ax.set_title(var)
    ax.set_xlabel(var)
    ax.set_ylabel('Частота')

# Убираем неиспользуемые подграфики (если их меньше чем переменных)
for i in range(len(variables), len(axes)):
    fig.delaxes(axes[i])

plt.suptitle('Распределение числовых переменных')

plt.tight_layout(rect=[0, 0, 1, 0.96])  # Подгонка для общего заголовка
plt.show()
#dan.describe()

# Список переменных для боксплотов
boxplot_vars = ['Price', 'Kilometers_Driven', 'Mileage_value', 'Engine_value', 'Power_value']

# Определяем количество строк и столбцов для подграфиков
n_vars = len(boxplot_vars)
n_cols = 3
n_rows = (n_vars + n_cols - 1) // n_cols  # Рассчитываем количество строк

fig, axes = plt.subplots(nrows=n_rows, ncols=n_cols, figsize=(18, n_rows * 5), sharey=False)
axes = axes.flatten()  # Преобразуем массив подграфиков в плоский массив

# Построение боксплотов
for ax, var in zip(axes, boxplot_vars):
    ax.boxplot(dan[var], vert=True, patch_artist=True,
               boxprops=dict(facecolor='skyblue', color='black'),
               whiskerprops=dict(color='black'),
               capprops=dict(color='black'),
               medianprops=dict(color='red'))
    ax.set_title(var)
    ax.set_xlabel('Значение')
    ax.set_ylabel('')

# Убираем неиспользуемые подграфики (если их больше чем переменных)
for i in range(len(boxplot_vars), len(axes)):
    fig.delaxes(axes[i])

plt.suptitle('Боксплоты для числовых переменных')

plt.tight_layout(rect=[0, 0, 1, 0.96])  # Подгонка для общего заголовка
plt.show()
stats = dan[['Price', 'Kilometers_Driven', 'Engine_value', 'Power_value']].describe()
print(stats)

# к нормальному распределению приближаются только данные 'Mileage_value', 
# средний расход топлива в выборке 18.14
# большинство машин на рынке произведены в 2011-2016 годах, им от 8 до 13 лет (mean 10.6)
# для Price, Kilometers_Driven, Engine_value, Power_value наблюдается сдвиг 
# распределения в сторону больших значений, необходимо преобразование 
# с помощью логарифмирования значений.

# Преобразование колонок с использованием np.log1p
dan['Price_log'] = np.log1p(dan['Price'])
dan['Kilometers_Driven_log'] = np.log1p(dan['Kilometers_Driven'])
dan['Mileage_value_log'] = np.log1p(dan['Mileage_value'])
dan['Engine_value_log'] = np.log1p(dan['Engine_value'])
dan['Power_value_log'] = np.log1p(dan['Power_value'])

# Создание фигуры и подграфиков
fig, axes = plt.subplots(nrows=2, ncols=5, figsize=(20, 10))

# Гистограмма для Price_log
sns.histplot(dan['Price_log'], bins=20, color='skyblue', edgecolor='black', ax=axes[0, 0])
axes[0, 0].set_title('Гистограмма распределения Price_log')
axes[0, 0].set_xlabel('Price_log')
axes[0, 0].set_ylabel('Частота')

# Гистограмма для Kilometers_Driven_log
sns.histplot(dan['Kilometers_Driven_log'], bins=20, color='salmon', edgecolor='black', ax=axes[0, 1])
axes[0, 1].set_title('Гистограмма распределения Kilometers_Driven_log')
axes[0, 1].set_xlabel('Kilometers_Driven_log')
axes[0, 1].set_ylabel('Частота')

# Гистограмма для Mileage_value_log
sns.histplot(dan['Mileage_value_log'], bins=20, color='lightgreen', edgecolor='black', ax=axes[0, 2])
axes[0, 2].set_title('Гистограмма распределения Mileage_value_log')
axes[0, 2].set_xlabel('Mileage_value_log')
axes[0, 2].set_ylabel('Частота')

# Гистограмма для Engine_value_log
sns.histplot(dan['Engine_value_log'], bins=20, color='lightcoral', edgecolor='black', ax=axes[0, 3])
axes[0, 3].set_title('Гистограмма распределения Engine_value_log')
axes[0, 3].set_xlabel('Engine_value_log')
axes[0, 3].set_ylabel('Частота')

# Гистограмма для Power_value_log
sns.histplot(dan['Power_value_log'], bins=20, color='lightblue', edgecolor='black', ax=axes[0, 4])
axes[0, 4].set_title('Гистограмма распределения Power_value_log')
axes[0, 4].set_xlabel('Power_value_log')
axes[0, 4].set_ylabel('Частота')

# Вертикальный боксплот для Price_log
sns.boxplot(y=dan['Price_log'], color='skyblue', ax=axes[1, 0])
axes[1, 0].set_title('Боксплот Price_log')
axes[1, 0].set_ylabel('Price_log')

# Вертикальный боксплот для Kilometers_Driven_log
sns.boxplot(y=dan['Kilometers_Driven_log'], color='salmon', ax=axes[1, 1])
axes[1, 1].set_title('Боксплот Kilometers_Driven_log')
axes[1, 1].set_ylabel('Kilometers_Driven_log')

# Вертикальный боксплот для Mileage_value_log
sns.boxplot(y=dan['Mileage_value_log'], color='lightgreen', ax=axes[1, 2])
axes[1, 2].set_title('Боксплот Mileage_value_log')
axes[1, 2].set_ylabel('Mileage_value_log')

# Вертикальный боксплот для Engine_value_log
sns.boxplot(y=dan['Engine_value_log'], color='lightcoral', ax=axes[1, 3])
axes[1, 3].set_title('Боксплот Engine_value_log')
axes[1, 3].set_ylabel('Engine_value_log')

# Вертикальный боксплот для Power_value_log
sns.boxplot(y=dan['Power_value_log'], color='lightblue', ax=axes[1, 4])
axes[1, 4].set_title('Боксплот Power_value_log')
axes[1, 4].set_ylabel('Power_value_log')

# Подгонка графиков
plt.tight_layout()
plt.show()

stats_log = dan[['Price', 'Kilometers_Driven', 'Engine_value', 'Power_value']].describe()
print(stats_log)

#Проверка распределния
from scipy import stats
def kolmogorov_smirnov_test(dan, columns, alpha=0.05):
    results = []
    for col in columns:
            
        data = dan[col].dropna()
              
        mean = data.mean()
        std = data.std()
               
    result = 'Распределение является нормальным' if stats.kstest_p >= alpha else 'Распределение не является нормальным'
        
    results.append({
            'Variable': col,
            'KS Statistic': stats.kstest_stat,
            'p-value': stats.kstest_p,
            'Result': result
        })
    
    return results

columns = ['Price', 'Kilometers_Driven', 'Mileage_value', 'Engine_value', 'Power_value',
'Price_log', 'Kilometers_Driven_log', 'Mileage_value_log', 'Engine_value_log', 'Power_value_log']

# Выполнение теста
ks_test_results = kolmogorov_smirnov_test(dan, columns, alpha=0.05)

# Создание DataFrame для результатов
ks_results_df = pd.DataFrame(ks_test_results)

# Вывод таблицы результатов
print(ks_results_df)

# несмотря на улучшение визуального восприятия гистограмм, 
# форма боксплотов и данные статистики показывают, 
# что данные не относятся к нормальному распределению.


# кодирование категориальных переменных

unique_owner_types = sorted(dan['Owner_Type'].unique())

# Правильный порядок значений и коды
correct_order = ['First', 'Second', 'Third', 'Fourth & Above']
correct_codes = range(1, len(correct_order) + 1)

print("Unique Owner Types:", unique_owner_types)
print("Correct Order:", correct_order)

# Создание словаря для сопоставления правильных значений и кодов
mapping_dict = dict(zip(correct_order, correct_codes))

# Создаем DataFrame для справки
mapping_Owner_Type = pd.DataFrame({
    'Owner_Type': correct_order,
    'Owner_Type_code': correct_codes
})

# Создаем словарь для кодирования
owner_type_mapping = dict(zip(mapping_Owner_Type['Owner_Type'], mapping_Owner_Type['Owner_Type_code']))

# Применяем кодирование
dan['Owner_Type_code'] = dan['Owner_Type'].map(owner_type_mapping)
print(mapping_Owner_Type)
#print(dan)

unique_fuel_types = sorted(dan['Fuel_Type'].unique())

fuel_type_codes = range(1, len(unique_fuel_types) + 1)

fuel_type_mapping = dict(zip(unique_fuel_types, fuel_type_codes))

dan['Fuel_Type_code'] = dan['Fuel_Type'].map(fuel_type_mapping)

mapping_df = pd.DataFrame({
    'Fuel_Type': unique_fuel_types,
    'Fuel_Type_code': fuel_type_codes
})

print(mapping_df)
# print(dan)

unique_Transmission = sorted(dan['Transmission'].unique())

# Создаем коды для уникальных значений (0 и 1)
if len(unique_Transmission) == 2:
    Transmission_codes = [0, 1]
else:
    raise ValueError("Бинарное кодирование применимо только к столбцам с двумя уникальными значениями.")

Transmission_mapping = dict(zip(unique_Transmission, Transmission_codes))

dan['Transmission_code'] = dan['Transmission'].map(Transmission_mapping)

mapping_Transmission = pd.DataFrame({
    'Transmission': unique_Transmission,
    'Transmission_code': Transmission_codes
})

print(mapping_Transmission)
#print(dan)

# Определяем уникальные значения в колонке 'Marka'
unique_Marka = sorted(dan['Marka'].unique())

Marka_codes = range(1, len(unique_Marka) + 1)

Marka_mapping = dict(zip(unique_Marka, Marka_codes))

dan['Marka_code'] = dan['Marka'].map(Marka_mapping)

mapping_Marka = pd.DataFrame({
    'Marka': unique_Marka,
    'Marka_code': Marka_codes
})

print(mapping_Marka)
	

dan = dan.drop(columns=['Transmission', 'Fuel_Type', 'Owner_Type'])

# Построение графиков для категориальных переменных
categorical_columns = ['Transmission_code', 'Owner_Type_code', 'Seats', 'Marka', 'Fuel_Type_code']

fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(12, 10), sharex=False, sharey=False)
axes = axes.flatten()  # Преобразуем массив подграфиков в плоский массив для удобства

for ax, col in zip(axes, categorical_columns):
    dan[col].value_counts().plot(kind='bar', ax=ax, color='skyblue', edgecolor='black')
    ax.set_title(f'Распределение {col}')
    ax.set_xlabel(col)
    ax.set_ylabel('Частота')
    ax.set_xticklabels(dan[col].value_counts().index, rotation=0, ha='center')

for i in range(len(categorical_columns), len(axes)):
    fig.delaxes(axes[i])

plt.suptitle('Распределение категориальных переменных')


plt.tight_layout(rect=[0, 0, 1, 0.96]) 
plt.show()

# Найти топ-10 значений в колонке 'Marka' для наглядности
top_10_markas = dan['Marka'].value_counts().nlargest(10)

# Построение гистограммы распределения топ-10 значений
plt.figure(figsize=(10, 6))
top_10_markas.plot(kind='bar', color='skyblue', edgecolor='black')

plt.title('Топ-10 распределение значений Marka')
plt.xlabel('Марка')
plt.ylabel('Частота')
plt.xticks(rotation=45, ha='right')  # Поворот меток оси x для улучшения читаемости

plt.tight_layout()
plt.show()

### Двумерный анализ
# 1. Постройте парные графики между числовыми переменными с помощью функции sns.pairplot
# 2. Сократите число столбцов, оставив только те пары, между которыми прослеживается взаимосвязь
# 3. Какие выводы можно сделать из парных графиков?
# 4. Исследуйте взаимосвязь цены (а также логарифмированной цены) и категориальных переменных с момощью столбчатых диаграмм
# 5. Включите в анализ из 4-го пункта переменные Seats и Car_age

# Вычисление средних значений 'Price' для каждой марки
mean_prices = dan.groupby('Marka')['Price'].mean().reset_index()
mean_prices_sorted = mean_prices.sort_values(by='Price', ascending=False)
 
plt.figure(figsize=(10, 6))
sns.barplot(x='Marka', y='Price', data=mean_prices_sorted, palette='viridis')

plt.title('Средние значения цен по маркам')
plt.xlabel('Marka')
plt.ylabel('Средняя цена')
plt.xticks(rotation=90)
plt.show()

# Боксплот для 'Price'
plt.figure(figsize=(10, 6))
sns.boxplot(x='Marka', y='Price', data=dan, palette='viridis')

plt.title('Боксплот разброса цен по маркам')
plt.xlabel('Marka')
plt.ylabel('Цена')
plt.xticks(rotation=90)
plt.show()

# Построение диаграммы рассеяния
fig, ax = plt.subplots(figsize=(10, 6))

scatter = ax.scatter(dan['Age'], dan['Kilometers_Driven'], c='blue', alpha=0.5, edgecolor='k')

ax.set_title('Соотношение между Kilometers_Driven и Age')
ax.set_xlabel('Age (лет)')
ax.set_ylabel('Kilometers_Driven')
ax.grid(True)

plt.tight_layout()
plt.show()

 #Выбор нужных столбцов
selected_columns = ['Kilometers_Driven', 'Age', 'Mileage_value', 'Engine_value', 'Power_value', 'Price']
dan_subset = dan[selected_columns]

# Построение парных графиков
sns.pairplot(dan_subset)
plt.suptitle('Парные графики числовых переменных', y=1.02) 
plt.show()

selected_columns = ['Kilometers_Driven', 'Age', 'Mileage_value', 'Engine_value', 'Power_value', 'Price']
dan_subset = dan[selected_columns]

# Построение парных графиков
pairplot = sns.pairplot(dan_subset)
plt.suptitle('Парные графики числовых переменных', y=1.02) 

# Вычисление корреляций
correlation_matrix = dan_subset.corr()

# Порог корреляции для отображения
correlation_threshold = 0.5

# Отображение значений корреляции на графиках и удаление графиков с низкой корреляцией
for i in range(len(selected_columns)):
    for j in range(len(selected_columns)):
        if i != j:
            ax = pairplot.axes[i, j]
            corr_value = correlation_matrix.iloc[i, j]
            # Добавление текста с корреляцией на график
            ax.annotate(f'{corr_value:.2f}', xy=(0.5, 0.5), xycoords='axes fraction',
                        ha='center', va='center', fontsize=10, color='red', bbox=dict(facecolor='white', alpha=0.8))
            # Удаление графиков с корреляцией ниже порога
            if abs(corr_value) < correlation_threshold:
                ax.set_visible(False)

# Фильтрация достоверных корреляций
filtered_corr_matrix = correlation_matrix.where(abs(correlation_matrix) >= correlation_threshold)

# Отображение только достоверных корреляций
print("Таблица достоверных корреляций:")
print(filtered_corr_matrix)

plt.show()

# Создание списка категориальных переменных для анализа
categorical_columns = ['Transmission_code', 'Owner_Type_code', 'Engine_value', 'Seats', 'Marka', 'Age']

# Настройка размера графиков
fig, axes = plt.subplots(nrows=len(categorical_columns), ncols=2, figsize=(12, 3 * len(categorical_columns)), sharex=False)

# Построение столбчатых диаграмм для каждой категориальной переменной
for i, col in enumerate(categorical_columns):
    # Средние значения Price и Price_log по каждой категории
    mean_price = dan.groupby(col)['Price'].mean()
    mean_price_log = dan.groupby(col)['Price_log'].mean()
    
    # # Средние значения Age по каждой категории (для добавления в график)
    # mean_age = dan.groupby(col)['Age'].mean()

    # Столбчатая диаграмма для Price
    sns.barplot(x=mean_price.index, y=mean_price.values, ax=axes[i, 0])
    axes[i, 0].set_title(f'mean Price by {col}')
    axes[i, 0].set_xlabel(col)
    axes[i, 0].set_ylabel('mean Price')
    axes[i, 0].tick_params(axis='x', rotation=45)

    # Столбчатая диаграмма для Price_log
    sns.barplot(x=mean_price_log.index, y=mean_price_log.values, ax=axes[i, 1])
    axes[i, 1].set_title(f'Price_log by {col}')
    axes[i, 1].set_xlabel(col)
    axes[i, 1].set_ylabel('Price_log')
    axes[i, 1].tick_params(axis='x', rotation=45)

    # Добавление среднего возраста на графики
    
# for ax in [axes[i, 0], axes[i, 1]]:
    
#     for index, value in enumerate(mean_age):
#             ax.text(index, value, 
          
# f'{value:.1f}', color='black', ha='center', va='bottom')

# Корректировка графиков
plt.tight_layout()
plt.suptitle('Взаимосвязь переменных с Price и Price_log', y=1.02)
plt.show()

### Многомерный анализ и заполнение пропусков
# 1. Постройте хит мап, измеряющий корреляции между переменными. Интерпретируйте результаты
# 2. Преобразуйте значения нулевого расхода топлива в пропуски. Aнализируйте получившееся количество пропусков
# 3. Заполните пропуски в столбцах Mileage, Engine, Power, Seats, New_Price, Price наиболее подходящим методом.
# 4. Сформируйте по одному предположению в данных, которые можно проверить с помощью ml-моделей и тестов

# Выбор нужных столбцов
selected_columns = ['Kilometers_Driven', 'Age', 'Mileage_value', 'Engine_value', 'Power_value', 'Price']
dan_subset = dan[selected_columns]

# Вычисление корреляций
correlation_matrix = dan_subset.corr()

# Построение тепловой карты
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', vmin=-1, vmax=1, center=0)
plt.title('Корреляционная матрица')
plt.show()

# Корреляция между Price и другими переменными: Обычно можно ожидать положительную корреляцию между Price и переменными,
# которые влияют на стоимость автомобиля, такими как Engine_value, Power_value, и Mileage_value. 
# Kilometers_Driven и Age могут иметь отрицательную корреляцию с Price, так как старые и более пробеговые 
# автомобили часто имеют меньшую стоимость.

# Корреляции между Kilometers_Driven, Age, Mileage_value, Engine_value, и Power_value:

# Age и Kilometers_Driven могут быть положительно скоррелированы, так как старые автомобили часто имеют больше пробега.
# Engine_valueиPower_valueсчет
# Mileage_value может иметь отрицательную корреляцию с Engine_valueи `Power_vPower_value, так как более мощные двигатели могут быть менее экономичными.
# В
# Price и Engine_value: Если коэффициент корреляции близок к 1, это означает, что автомобили с большим двигателем, как правило, имеют более высокую цену.
# Age и Price: Если коэффициент корреляции близок к -1, это указывает на то, что старые автомобили имеют тенденцию к более низкой цене.
# Mileage_value и Price: Если коэффициент корреляции близок к -1, это указывает на то, что автомобили с большим пробегом имеют тенденцию к более низкой цене.

# # Преобразование значений нулевого расхода топлива в пропуски
# dan['Mileage_value'] = dan['Mileage_value'].replace(0, np.nan)

# # Анализ количества пропусков
# missing_values = dan.isna().sum()

# print("Количество пропусков в каждом столбце:")
# print(missing_values)

#Заполнение пропусков New_Price_value в зависимости отсвязанных переменных
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer

# Отделяем строки с известными и неизвестными значениями 'New_Price_value'
dan_known = dan[dan['New_Price_value'].notna()]
dan_missing = dan[dan['New_Price_value'].isna()]

# Проверка наличия пропусков
if dan_missing.empty:
    print("Нет строк с пропущенными значениями в 'New_Price_value'.")
else:
    # Определяем независимые переменные и целевую переменную
    X_known = dan_known[['Mileage_value', 'Engine_value', 'Power_value', 'Seats', 'Price', 'Marka_code']]
    y_known = dan_known['New_Price_value']

    # Преобразование данных: заполнение пропусков
    imputer = SimpleImputer(strategy='mean')
    X_known = imputer.fit_transform(X_known)
    X_missing = imputer.transform(dan_missing[['Mileage_value', 'Engine_value', 'Power_value', 'Seats', 'Price', 'Marka_code']])

    # Создание и обучение модели
    model = LinearRegression()
    model.fit(X_known, y_known)

    # Прогнозирование пропущенных значений
    predicted_prices = model.predict(X_missing)

    # Заполнение пропусков в 'New_Price_value'
    dan.loc[dan['New_Price_value'].isna(), 'New_Price_value'] = predicted_prices

    # Печать заполненного DataFrame
    print("Заполненный DataFrame:")
    print(dan[['New_Price_value']])

# Предположение: "Цена автомобиля зависит от пробега, возраста и мощности двигателя."
# Проверка с помощью ML-моделей:

# Модель: Линейная регрессия
# Целевая переменная: Price
# Независимые переменные: Kilometers_Driven,Age,Engine_value, `Мощность_значенияPower_value

# Если модель показывает хорошую точность (высокий R^2 и низкий MSE), это подтверждает, 
# что цена автомобиля действительно зависит от пробега, возраста и мощности двигателя.

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Определяем независимые переменные и целевую переменную
X = dan[['Kilometers_Driven', 'Age', 'Engine_value', 'Power_value']]
y = dan['Price']

# Обработка пропусков
X = X.fillna(X.mean())
y = y.fillna(y.mean())

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучение модели
model = LinearRegression()
model.fit(X_train, y_train)

# Прогнозирование
y_pred = model.predict(X_test)

# Оценка модели
print("Среднеквадратичная ошибка:", mean_squared_error(y_test, y_pred))
print("Коэффициент детерминации (R^2):", r2_score(y_test, y_pred))

# Коэффициент детерминации (R²) показывает, какую долю вариации целевой 
# переменной (в данном случае Price) объясняет модель. 
# Значение R² равно 0.692, что означает, 
# что модель объясняет около 69.2% вариации в ценах на автомобили. 
# Это хороший результат, указывающий на то, что выбранные независимые 
# переменные (пробег, возраст, мощность двигателя) 
# имеют значимое влияние на цену.

# Предположение: "Автомобили разных марок имеют различия в средней цене."
# Проверка с помощью статистических тестов:

# Тест: ANOVA
# Целевая переменная: Price
# Независимая переменная: Marka

from scipy.stats import f_oneway

# список уникальных марок
unique_markas = dan['Marka'].unique()

# Создаем список для хранения цен по маркам
price_by_marka = [dan[dan['Marka'] == marka]['Price'].dropna() for marka in unique_markas]

# Выполнение ANOVA
f_stat, p_value = f_oneway(*price_by_marka)

print("Статистика F:", f_stat)
print("p-значение:", p_value)

# p-значение: 0.0 <0.05 предположение подтвердилось, 
# цена зависит от марки автомобиля
