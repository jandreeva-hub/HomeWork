import numpy as np
import pandas as pd

Deals = pd.read_excel("Deals.xlsx")
Deals['Quality'] = Deals['Quality'].fillna('UNKNOWN')  
# # Определение правильного порядка значений
# def encode_categorical(df, column_name, correct_order=None, codes_start=0):
#     if correct_order:
#         unique_values = correct_order
#     else:
#         # Если порядок не задан, используем уникальные значения в порядке их появления
#         unique_values = sorted(df[column_name].unique())
    
#     codes = range(codes_start, len(unique_values) + codes_start)
#     mapping_dict = dict(zip(unique_values, codes))
#     df[f'{column_name}_code'] = df[column_name].map(mapping_dict)
#     return pd.DataFrame({
#         column_name: unique_values,
#         f'{column_name}_code': codes
#     })

# # правильный порядок для 'Quality'
# correct_order_Level_of_Deutsch = ['0', 'A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'UNKNOWN']
# correct_order_Quality = ['A', 'B', 'C', 'D', 'E', 'UNKNOWN']
# Level_of_Deutsch_mapping = encode_categorical(Deals, 'Level of Deutsch', correct_order=correct_order_Level_of_Deutsch)
# Quality_mapping = encode_categorical(Deals, 'Quality', correct_order=correct_order_Quality)

# print(Level_of_Deutsch_mapping)
# print(Quality_mapping)
#print(Deals.head())
print(Deals.isnull().sum())