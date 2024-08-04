import pandas as pd
import numpy as np
Calls = pd.read_excel("Calls.xlsx")
Calls = Calls.drop_duplicates()
filtered_Calls = Calls[(Calls['Call_Duration_seconds']>0) & (Calls['Call_Status'] != 'Missed')]
#Calls = Calls[Calls.Call_Status =='Missed']
#print(Calls)

filtered_Calls.to_excel('filtered_calls.xlsx', index=False)

#print(Contacts.isnull().sum())

# Calls_filled = Calls['CONTACTID'].combine_first(Contacts['Id'])
# print(Calls_filled.isnull().sum())

# # Удалите неактуальные столбцы (например, столбцы 'irrelevant_col1' и 'irrelevant_col2')
# df = df.drop(columns=['irrelevant_col1', 'irrelevant_col2'])
# # Замена отсутствующих значений на среднее значение для числовых столбцов
# df['numeric_col'] = df['numeric_col'].fillna(df['numeric_col'].mean())

# # Замена отсутствующих значений на медиану для другой числовой колонки
# df['another_numeric_col'] = df['another_numeric_col'].fillna(df['another_numeric_col'].median())

# # Заполнение пропусков вперед
# df = df.fillna(method='ffill')

# # Заполнение пропусков назад
# df = df.fillna(method='bfill')

# # Удаление строк с отсутствующими значениями
# df = df.dropna()

# # Удаление столбцов с отсутствующими значениями
# df = df.dropna(axis=1)
# # Преобразование столбца с датами из строки в тип datetime
# df['date_col'] = pd.to_datetime(df['date_col'], format='%Y-%m-%d')

# # Преобразование столбца в числовой тип данных
# df['numeric_col'] = pd.to_numeric(df['numeric_col'], errors='coerce')

# # Преобразование столбца в строковый тип данных
# df['str_col'] = df['str_col'].astype(str)
