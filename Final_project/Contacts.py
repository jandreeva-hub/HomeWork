import pandas as pd
import numpy as np
from datetime import datetime
Calls = pd.read_excel('Calls.xlsx', parse_dates = ['Call Start Time'])
Calls = Calls.drop_duplicates()

Contacts = pd.read_excel("Contacts.xlsx", parse_dates = ['Created Time', 'Modified Time'])
Contacts = Contacts.drop_duplicates()

C_C = pd.merge(Calls, Contacts, left_on='CONTACTID', right_on='Id') 
C_C = C_C[(C_C['Call Duration (in seconds)']>0) & (C_C['Call Status'] != 'Missed')]

C_C=C_C.drop(columns=['Call Status', 'Dialled Number', 'Tag', 'Id_y'])  

#заполнение пропусков
C_C['Outgoing Call Status'] = C_C['Outgoing Call Status'].fillna('Completed')
C_C['Scheduled in CRM'] = C_C['Scheduled in CRM'].fillna('TRUE')

C_C = C_C.astype({col: 'int' for col in C_C.select_dtypes(include=['float64']).columns})

# print(C_C.dtypes)
# print(C_C.isnull().sum())

C_C['Call_Start_Date'] = pd.to_datetime(C_C['Call Start Time'], format='%d.%m.%Y %H:%M')
C_C['Call_Start_Date'] = C_C['Call Start Time'].dt.date
C_C['Call_Start_Time'] = pd.to_datetime(C_C['Call Start Time'], format='%d.%m.%Y %H:%M')
C_C['Call_Start_Time'] = C_C['Call Start Time'].dt.time
C_C['Created_Date'] = pd.to_datetime(C_C['Created Time'], format='%d.%m.%Y %H:%M')
C_C['Created_Date'] = C_C['Created Time'].dt.date
C_C['Modified_Date'] = pd.to_datetime(C_C['Modified Time'], format='%d.%m.%Y %H:%M')
C_C['Modified_Date'] = C_C['Modified Time'].dt.date
C_C.drop(columns=['Call Start Time', 'Created Time', 'Modified Time'], inplace=True)


print(C_C.dtypes)
# print(C_C.head())
#C_C.to_excel('C_C.xlsx', index=False)

#проверка совпадения 
# Deals1 = pd.read_excel("Deals.xlsx", parse_dates = ['Closing Date', 'Created Time'])
# print(C_C['CONTACTID']. isin (Deals1['Contact Name']). value_counts ())
# print(Deals1.shape[0])
#print(C_C.shape[0])