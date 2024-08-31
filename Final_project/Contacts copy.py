import pandas as pd
import numpy as np
from datetime import datetime
from tabulate import tabulate
from prettytable import PrettyTable
# Загрузка данных
Calls = pd.read_excel('Calls.xlsx', parse_dates=['Call Start Time'])
Calls = Calls.drop_duplicates()

Contacts = pd.read_excel("Contacts.xlsx", parse_dates=['Created Time', 'Modified Time'])
Contacts = Contacts.drop_duplicates()

# Объединение данных
C_C = pd.merge(Calls, Contacts, left_on='CONTACTID', right_on='Id')
C_C = C_C[(C_C['Call Duration (in seconds)'] > 0) & (C_C['Call Status'] != 'Missed')]

# Удаление ненужных столбцов
C_C = C_C.drop(columns=['Call Status', 'Dialled Number', 'Tag', 'Id_y'])

# Заполнение пропусков
C_C['Outgoing Call Status'] = C_C['Outgoing Call Status'].fillna('Completed')
C_C['Scheduled in CRM'] = C_C['Scheduled in CRM'].fillna('TRUE')

C_C = C_C.astype({col: 'int' for col in C_C.select_dtypes(include=['float64']).columns})

# Разделение 'Call Start Time' на дату и время и сохранение в формате datetime
C_C['Call_Start_Date'] = pd.to_datetime(C_C['Call Start Time'].dt.date)
C_C['Call_Start_Time'] = pd.to_datetime(C_C['Call Start Time'].dt.time.astype(str), format='%H:%M:%S').dt.time

# Оставляем только дату в 'Created Time' и 'Modified Time'
C_C['Created_Date'] = pd.to_datetime(C_C['Created Time'].dt.date)
C_C['Modified_Date'] = pd.to_datetime(C_C['Modified Time'].dt.date)

# Удаление исходных столбцов с полными датами и временами
C_C = C_C.drop(columns=['Call Start Time', 'Created Time', 'Modified Time'])

# Проверка результата
# print(C_C.head())
# print(C_C.dtypes)




#C_C.to_excel('C_C.xlsx', index=False)


#проверка совпадения 
# Deals1 = pd.read_excel("Deals.xlsx", parse_dates = ['Closing Date', 'Created Time'])
# print(C_C['CONTACTID']. isin (Deals1['Contact Name']). value_counts ())
# print(Deals1.shape[0])


C_C_describe_stats = C_C.describe().T  # Make sure to call describe() method
C_C_describe_stats.to_excel('C_C_describe_stats.xlsx', engine='openpyxl')
#print(C_C_describe_stats)

