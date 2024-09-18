#Анализ эффективности работы отдела продаж
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

Deals1 = pd.read_excel('Deals1.xlsx')
Calls = pd.read_excel('Calls (Done) (1).xlsx')
Spend = pd.read_excel('Spend (Done) (2).xlsx')

# Perform the analysis for deal owners and campaigns
# Counting total deals, successful deals, and total sales amount
owner_campaign_analysis = Deals1.groupby(['Deal Owner Name', 'Source']).agg({
    'Id': 'count',  # Total deals
    'Stage': lambda x: (x == 'Closed Won').sum(),  # Successful deals
    'Offer Total Amount': 'sum'  # Total sales amount
}).reset_index()

# Rename columns
owner_campaign_analysis.rename(columns={'Id': 'Total Deals', 'Stage': 'Successful Deals'}, inplace=True)
owner_campaign_analysis['Conversion Rate'] = owner_campaign_analysis['Successful Deals'] / owner_campaign_analysis['Total Deals']
import matplotlib.pyplot as plt

# # Plot for Total Deals by Deal Owner and Source
# fig, ax1 = plt.subplots(figsize=(12, 6))
# for source in owner_campaign_analysis['Source'].unique():
#     subset = owner_campaign_analysis[owner_campaign_analysis['Source'] == source]
#     ax1.bar(subset['Deal Owner Name'], subset['Total Deals'], label=source)

# ax1.set_xlabel('Deal Owner')
# ax1.set_ylabel('Total Deals')
# ax1.set_title('Total Deals by Deal Owner and Source')
# ax1.legend(title='Source')
# plt.xticks(rotation=45)
# plt.show()



# # Update the analysis to use 'Payment Done' as the success criteria
# owner_campaign_analysis = Deals1.groupby(['Deal Owner Name', 'Source']).agg({
#     'Id': 'count',  # Total deals
#     'Stage': lambda x: (x == 'Payment Done').sum(),  # Successful deals
#     'Offer Total Amount': 'sum'  # Total sales amount
# }).reset_index()

# # Calculate conversion rate
# owner_campaign_analysis.rename(columns={'Id': 'Total Deals', 'Stage': 'Successful Deals'}, inplace=True)
# owner_campaign_analysis['Conversion Rate'] = owner_campaign_analysis['Successful Deals'] / owner_campaign_analysis['Total Deals']

# # Plot for Conversion Rate by Deal Owner and Source using a bar chart
# fig, ax2 = plt.subplots(figsize=(12, 6))

# # Unique deal owners
# deal_owners = owner_campaign_analysis['Deal Owner Name'].unique()
# x = np.arange(len(deal_owners))  # the label locations
# width = 0.2  # the width of the bars

# # Plot bars for each source
# for i, source in enumerate(owner_campaign_analysis['Source'].unique()):
#     subset = owner_campaign_analysis[owner_campaign_analysis['Source'] == source]
#     # Match the order of deal owners to ensure correct alignment
#     conversion_rates = []
#     for owner in deal_owners:
#         if owner in subset['Deal Owner Name'].values:
#             conversion_rate = subset[subset['Deal Owner Name'] == owner]['Conversion Rate'].values[0]
#         else:
#             conversion_rate = 0  # Assign 0 if the deal owner has no deals from this source
#         conversion_rates.append(conversion_rate)
    
#     # Align bar positions based on the number of sources
#     ax2.bar(x + i * width, conversion_rates, width, label=source)

# ax2.set_xlabel('Deal Owner')
# ax2.set_ylabel('Conversion Rate')
# ax2.set_title('Conversion Rate by Deal Owner and Source')
# ax2.set_xticks(x + width * (len(owner_campaign_analysis['Source'].unique()) - 1) / 2)
# ax2.set_xticklabels(deal_owners, rotation=45)
# ax2.legend(title='Source')
# plt.show()



# # Update the analysis to use 'Payment Done' as the success criteria
# owner_campaign_analysis = Deals1.groupby(['Deal Owner Name', 'Source']).agg({
#     'Id': 'count',  # Total deals
#     'Stage': lambda x: (x == 'Payment Done').sum(),  # Successful deals
#     'Offer Total Amount': 'sum'  # Total sales amount
# }).reset_index()

# # Calculate conversion rate
# owner_campaign_analysis.rename(columns={'Id': 'Total Deals', 'Stage': 'Successful Deals'}, inplace=True)
# owner_campaign_analysis['Conversion Rate'] = owner_campaign_analysis['Successful Deals'] / owner_campaign_analysis['Total Deals']

# # Unique deal owners and sources
# deal_owners = owner_campaign_analysis['Deal Owner Name'].unique()
# sources = owner_campaign_analysis['Source'].unique()

# # Create a matrix to hold conversion rates for stacking
# conversion_matrix = np.zeros((len(deal_owners), len(sources)))

# # Populate the matrix with conversion rates
# for i, owner in enumerate(deal_owners):
#     for j, source in enumerate(sources):
#         subset = owner_campaign_analysis[(owner_campaign_analysis['Deal Owner Name'] == owner) & (owner_campaign_analysis['Source'] == source)]
#         if not subset.empty:
#             conversion_matrix[i, j] = subset['Conversion Rate'].values[0]

# # Plot stacked bar chart
# fig, ax = plt.subplots(figsize=(12, 6))

# # Bottom values for stacking
# bottom = np.zeros(len(deal_owners))

# # Plot each source's conversion rates on top of each other
# for j, source in enumerate(sources):
#     ax.bar(deal_owners, conversion_matrix[:, j], bottom=bottom, label=source)
#     bottom += conversion_matrix[:, j]  # Update the bottom for the next stack

# ax.set_xlabel('Deal Owner')
# ax.set_ylabel('Conversion Rate')
# ax.set_title('Stacked Bar Chart: Conversion Rate by Deal Owner and Source')

# # Place the legend outside the plot area
# ax.legend(title='Source', bbox_to_anchor=(1.05, 1), loc='upper left')
# plt.xticks(rotation=45)
# plt.tight_layout()  # Adjust layout to make room for the legend
# plt.show()




# # Plot for Total Sales Amount by Deal Owner and Source
# fig, ax3 = plt.subplots(figsize=(12, 6))
# for source in owner_campaign_analysis['Source'].unique():
#     subset = owner_campaign_analysis[owner_campaign_analysis['Source'] == source]
#     ax3.bar(subset['Deal Owner Name'], subset['Offer Total Amount'], label=source)

# ax3.set_xlabel('Deal Owner')
# ax3.set_ylabel('Total Sales Amount')
# ax3.set_title('Total Sales Amount by Deal Owner and Source')
# ax3.legend(title='Source')
# plt.xticks(rotation=45)
# plt.show()


