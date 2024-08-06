import pandas as pd
import numpy as np

Spend = pd.read_excel("Spend.xlsx")
Spend = Spend.drop_duplicates()
# print(Spend.isnull().sum())
# print(Spend.dtypes)
#удаление пустых строк
Spend = Spend.dropna(how='all')

#Spend.to_excel('Spend.xlsx', index=False)

# Spend['Date'] = pd.to_datetime(Spend['Date'], format='%d.%m.%Y %H:%M')
# Spend['tracked_Date'] = Spend['Date'].dt.date
# Spend.drop(columns=['Date'], inplace=True)
#Spend.to_excel('Spend.xlsx', index=False)

Spend_group = Spend.groupby('Source')['Campaign'].nunique()

print(Spend_group)
#print(Spend.dtypes)


#fillna_const.Embarked.fillna('S', inplace = True)