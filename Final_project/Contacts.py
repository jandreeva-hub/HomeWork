import pandas as pd
import numpy as np
from datetime import datetime
from tabulate import tabulate
from prettytable import PrettyTable
# Загрузка данных
Contacts = pd.read_excel(
    'Contacts (Done) (1).xlsx',
    dtype={
        'Id': 'str'
        },
    parse_dates=[
        'Created Date'
        ]
)

Contacts = Contacts.drop_duplicates()

# Удаление ненужных столбцов
Contacts = Contacts.drop(columns=['Created Time','Modified Time'])
print(Contacts.dtypes)
# C_C = C_C.astype({col: 'int' for col in C_C.select_dtypes(include=['float64']).columns})

# # Разделение 'Call Start Time' на дату и время и сохранение в формате datetime
# C_C['Call_Start_Date'] = pd.to_datetime(C_C['Call Start Time'].dt.date)
# C_C['Call_Start_Time'] = pd.to_datetime(C_C['Call Start Time'].dt.time.astype(str), format='%H:%M:%S').dt.time

# # Оставляем только дату в 'Created Time' и 'Modified Time'
# C_C['Created_Date'] = pd.to_datetime(C_C['Created Time'].dt.date)
# C_C['Modified_Date'] = pd.to_datetime(C_C['Modified Time'].dt.date)

# print(Contacts.head())





Contacts.to_excel('Contacts.xlsx', index=False)


#проверка совпадения 
# Deals1 = pd.read_excel("Deals.xlsx", parse_dates = ['Closing Date', 'Created Time'])
# print(C_C['CONTACTID']. isin (Deals1['Contact Name']). value_counts ())
# print(Deals1.shape[0])


# C_C_describe_stats = C_C.describe().T  # Make sure to call describe() method
# C_C_describe_stats.to_excel('C_C_describe_stats.xlsx', engine='openpyxl')
#print(C_C_describe_stats)


# # Предположим, что вы уже имеете три DataFrame: Deals1, df, C_C

# # Получаем описательную статистику
# Deals1_describe_stats = Deals1.describe().T
# df_describe_stats = df.describe().T
# C_C_describe_stats = C_C.describe().T

# # Объединяем результаты в один DataFrame
# # Добавляем префиксы для различения данных
# Deals1_describe_stats['Source'] = 'Deals1'
# df_describe_stats['Source'] = 'df'
# C_C_describe_stats['Source'] = 'C_C'

# # Объединяем результаты в один DataFrame
# combined_stats = pd.concat([Deals1_describe_stats, df_describe_stats, C_C_describe_stats])

# # Записываем объединенные результаты в новый CSV файл
# combined_stats.to_csv('stat_describe.csv')


