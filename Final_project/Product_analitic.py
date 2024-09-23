import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Deals1 = pd.read_excel('Deals1.xlsx')
Calls = pd.read_excel('Calls.xlsx')
Spend = pd.read_excel('Spend.xlsx')

successful_deals = Deals1[Deals1['Stage'] == 'Payment Done']
successful_deals_with_spend = pd.merge(successful_deals, Spend, left_on='Source', right_on='Source', how='left')
ad_performance = successful_deals_with_spend.groupby('Source').agg(
    total_successful_deals=('Id', 'count'),
    total_spend=('Spend', 'sum'),
    average_deal_value=('Offer Total Amount', 'mean')
).reset_index()

# расчет CAC для каждого источника
ad_performance['CAC_per_source'] = ad_performance['total_spend'] / ad_performance['total_successful_deals']
ad_performance.to_excel('ad_performance.xlsx', index=False)
print(ad_performance)

plt.figure(figsize=(12, 6))
sns.set_style("whitegrid")

# Барплот для успешных сделок
sns.barplot(x='total_successful_deals', y='Source', data=ad_performance, label='Total Successful Deals', color='b')
plt.title('Связь между источником и общим количеством успешных сделок')
plt.xlabel('Общее количество успешных сделок')

# Настройка второй оси Y для total_spend
ax2 = plt.twinx()
sns.lineplot(x='total_successful_deals', y='total_spend', data=ad_performance, ax=ax2, color='r', marker='o', label='Total Spend')
ax2.set_ylabel('') 

# Настройка легенды
plt.legend(loc='upper left', bbox_to_anchor=(0.8, 1), title=None, fontsize=10)

ax2.legend(loc='upper left', bbox_to_anchor=(0.8, 0.9), title=None, fontsize=10)

plt.tight_layout()
plt.show()
plt.savefig('Source_Deals.png')

