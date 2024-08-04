import pandas as pd

Deals = pd.read_excel("Deals.xlsx")
Deals = Deals.drop_duplicates()
print(Deals.isnull().sum())