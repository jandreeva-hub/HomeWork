import pandas as pd
import random


value = []
for val in range(365):
    value.append(random.randint(0, 1000))

date_random = pd.to_datetime('31.12.2022',dayfirst=True) + pd.timedelta_range(start=0, freq='1D', end='364D')
df = pd.DataFrame({'Date': date_random, 'Value': value})

df = df.set_index(['Date'])
print(df, "\n", df.dtypes)
filte_for_date = input("Enter dade start and date stop (dd-mm-YYYY): ").split()
start_date = pd.to_datetime(filte_for_date[0],dayfirst=True)
stop_date = pd.to_datetime(filte_for_date[1],dayfirst=True)

df_filter = df.loc[start_date:stop_date]
print(df_filter)