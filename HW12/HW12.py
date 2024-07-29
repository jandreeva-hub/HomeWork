import polars as pl
import seaborn as sns
import numpy as np
import pandas as pd
tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')

#print(tips)
#print(flights)

selected_flights = flights[['year', 'month', 'passengers']]
#print(selected_flights)

fl = flights.groupby(['year']).agg({'passengers': 'sum'}).reset_index()
#print(fl)

tips['year'] = np.random.randint ( 1949 , 1960 ,size=( 244 , 1 ))
#print(tips)

joined_df = tips.join(fl.set_index('year'), on='year', how='left') 
print(joined_df.head(10))

f_tips=tips[tips['time'] == 'Dinner']
#print(f_tips)

flights_subset = flights.head(50)
# print(flights_subset)

result = pd.concat([f_tips, flights_subset])
print(result.head(10))