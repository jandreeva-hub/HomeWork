import pandas as pd

Deals1 = pd.read_excel('Deals1.xlsx')

# Сортировка таблицы по уникальным значениям в 'Contact Name'
grouped_data = Deals1.sort_values(by='Contact Name')

# Сохранение результата в новый Excel файл
grouped_data.to_excel('Grouped_Deals_By_Contact_Name.xlsx', index=False)

# Вывод первых 5 строк для проверки
print(grouped_data.head())


print('file is created')

