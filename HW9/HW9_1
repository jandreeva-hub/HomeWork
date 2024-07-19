import seaborn as sns
import pandas as pd
import random


df = sns.load_dataset('titanic')
print (df.isnull().sum())
df_age =  df['age'].fillna(df['age'].mean()).round(1)
df['age'] = df_age

#value_counts = df['deck'].value_counts()
#print(value_counts)

available_values = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
random_filled = df['deck'].fillna(random.choice(available_values))
df['deck'] = random_filled

#value_counts = df['embarked'].value_counts()
#print(value_counts)

available_values_1 = ['C', 'S','Q']
random_filled_1 = df['embarked'].fillna(random.choice(available_values_1))
df['embarked'] = random_filled_1

#value_counts = df['embark_town'].value_counts()
#print(value_counts)

df.loc[df['embarked'] == 'C', 'embark_town'] = 'Cherbourg'
df.loc[df['embarked'] == 'S', 'embark_town'] = 'Southampton'
df.loc[df['embarked'] == 'Q', 'embark_town'] = 'Queenstown'
print (df.isnull().sum())