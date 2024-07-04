import pandas as pd
import matplotlib.pyplot as plt
import numpy


power = {}
for i in range(1,26):
    power[i] = list(numpy.random.randint(100, 1000, 30))

df =pd.DataFrame(power)
df_sum = pd.Series(df.sum(axis=0))

plt.pie(list(df_sum.values), labels=df_sum.index, shadow=False, autopct='%1.1f%%', startangle=180 )
plt.title("Круговая диаграмма")
plt.show()

plt.hist(list(df_sum.values), bins=25, histtype='bar', alpha = 1 )
plt.show()