import pandas as pd
import string

data_str = input("Data: ").split()
i = 0
id = []
while i <= len(data_str) - 1:
    id.append(string.ascii_lowercase[i])
    i += 1
data = pd.Series(data_str, index=id)
print(data)
