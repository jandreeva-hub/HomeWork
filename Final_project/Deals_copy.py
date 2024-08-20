import numpy as np
import pandas as pd

import pandas as pd

# Пример исходного DataFrame
# Deals1 = pd.read_csv('your_data.csv')  # Загрузка вашего DataFrame из файла, если нужно

# Шаг 1: Создание DataFrame с уникальными значениями и сохранение в Excel
unique_qualities = Deals1[['Quality']].drop_duplicates().reset_index(drop=True)
unique_qualities[['Quality_Code', 'Quality_Description']] = unique_qualities['Quality'].str.split(' - ', expand=True)
unique_qualities.drop(columns=['Quality'], inplace=True)
unique_qualities['Quality_Description'] = unique_qualities['Quality_Description'].fillna('UNKNOWN')

# Сохраняем уникальные качества в Excel
unique_qualities.to_excel('unique_qualities.xlsx', index=False)

# Шаг 2: Разделение столбца 'Quality' на 'Quality_Code' и 'Quality_Description' в исходном DataFrame
Deals1[['Quality_Code', 'Quality_Description']] = Deals1['Quality'].str.split(' - ', expand=True)
Deals1.drop(columns=['Quality'], inplace=True)

# Шаг 3: Загрузка уникальных значений и создание словаря для замены
unique_qualities = pd.read_excel('unique_qualities.xlsx')

# Создаем словарь для преобразования описаний в коды
quality_dict = unique_qualities.set_index('Quality_Description')['Quality_Code'].to_dict()

# Кодируем значения в 'Quality_Description' на основе словаря
Deals1['Quality_Code'] = Deals1['Quality_Description'].map(quality_dict)

# Сохранение обновленного DataFrame, если необходимо
Deals1.to_excel('updated_deals1.xlsx', index=False)
