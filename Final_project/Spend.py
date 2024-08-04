import pandas as pd

Spend = pd.read_excel("Spend.xlsx")
Spend = Spend.drop_duplicates()
print(Spend.isnull().sum())