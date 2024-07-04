import pandas as pd
import numpy as np

lines = int(input("len: "))
date = []
for i in range(lines):
    date.append(input("date: ").split())
df = pd.DataFrame(date, columns=['Name', 'Age', 'Region'])
df['Age'] = df['Age'].astype(int)

print(df, "\n", df.dtypes)
print(f"number of records- {len(df)}")
print(f"average age -  {df['Age'].mean()}")
print(f"unique regions: \n {df.groupby('Region').count()}")
print (f"Youngest: \n  {df[df['Age'] == df['Age'].min()]}")