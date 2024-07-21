import seaborn as sns
from sklearn.preprocessing import OrdinalEncoder


df = sns.load_dataset('titanic')
#print(df.head())
#df.info()
#print(df.embark_town.value_counts())

encoder = OrdinalEncoder()
encoded_df = encoder.fit_transform(df[['sex', 'embark_town','embarked', 'class', 'deck']])
df[['sex', 'embark_town','embarked', 'class', 'deck']] = encoded_df
print(df.head())
