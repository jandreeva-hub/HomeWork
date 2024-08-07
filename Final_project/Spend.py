import pandas as pd
import numpy as np

Spend = pd.read_excel("Spend.xlsx")
Spend = Spend.drop_duplicates()
# print(Spend.isnull().sum())
# print(Spend.dtypes)
#удаление пустых строк
Spend = Spend.dropna(how='all')

#Spend.to_excel('Spend.xlsx', index=False)

# Spend['Date'] = pd.to_datetime(Spend['Date'], format='%d.%m.%Y %H:%M')
# Spend['tracked_Date'] = Spend['Date'].dt.date
# Spend.drop(columns=['Date'], inplace=True)
#Spend.to_excel('Spend.xlsx', index=False)

#Spend_group = Spend.groupby('Source')['Campaign'].nunique()

#print(Spend_group)
#print(Spend.dtypes)

Spend = pd.DataFrame(Spend)

# Список значений, для которых нужно заполнить 'Campaign'
sources_to_update = ['Bloggers', 'CRM', 'Offline', 'Organic', 'Partnership', 'Radio', 'SMM', 'Telegram posts']

# Заполнение значений в столбце Campaign значением 'unknown', если Source соответствует одному из значений в списке
Spend.loc[Spend['Source'].isin(sources_to_update), 'Campaign'] = 'unknown'

#print(Spend)

df = pd.DataFrame(Spend)

# Значения, для которых нужно заменить пропуски
values_to_fill = ['Facebook Ads', 'Google Ads', 'Test', 'Tiktok Ads', 'Webinar', 'Youtube Ads']

# Получение уникальных значений из столбца 'Campaign' по группам в 'Source'
def fill_campaign(group):
    unique_campaigns = group['Campaign'].dropna().unique()
    group['Campaign'] = group['Campaign'].apply(lambda x: np.random.choice(unique_campaigns) if pd.isna(x) else x)
    return group

# Применение функции к каждой группе
df = df.groupby('Source', group_keys=False).apply(fill_campaign)

#print(df)
#df.to_excel('df.xlsx', index=False)

