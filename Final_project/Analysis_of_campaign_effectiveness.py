import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

Deals1 = pd.read_excel('Deals1.xlsx')
Calls = pd.read_excel('Calls (Done) (1).xlsx')
Spend = pd.read_excel('Spend (Done) (2).xlsx')
#Анализ эффективности кампаний: 
# 1. Сравните эффективность различных кампаний с точки зрения генерации лидов и коэффициента конверсии.

# Calculate the number of leads generated by each source
leads_by_source = Deals1.groupby('Source').size().reset_index(name='Leads Generated')

# Ensure that we sum only numeric columns in the 'spend_df' DataFrame
numeric_columns = Spend.select_dtypes(include='number').columns.tolist()

# Merge with spend data to get the spend and clicks for each source
source_performance_df = pd.merge(leads_by_source, Spend.groupby('Source')[numeric_columns].sum().reset_index(), on='Source', how='left')

# Calculate conversion rate and cost per lead
source_performance_df['Conversion Rate'] = source_performance_df['Leads Generated'] / source_performance_df['Clicks']
source_performance_df['Cost per Lead'] = source_performance_df['Spend'] / source_performance_df['Leads Generated']

# Clean up any infinities or NaNs resulting from division by zero
source_performance_df.replace([float('inf'), -float('inf')], None, inplace=True)
source_performance_df.fillna(0, inplace=True)
import matplotlib.pyplot as plt

# Set up the figure and axes for plotting
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar plot for Leads Generated
ax1.bar(source_performance_df['Source'], source_performance_df['Leads Generated'], color='b', alpha=0.6, label='Leads Generated')
ax1.set_xlabel('Source')
ax1.set_ylabel('Leads Generated')
ax1.set_title('Source Performance: Leads Generated and Conversion Rate')
ax1.legend(loc='upper left')

# Create a second y-axis for Conversion Rate
ax2 = ax1.twinx()
ax2.plot(source_performance_df['Source'], source_performance_df['Conversion Rate'], color='g', marker='o', label='Conversion Rate')
ax2.set_ylabel('Conversion Rate')
ax2.legend(loc='upper right')

# Show the plot
plt.xticks(rotation=45)
plt.show()




# Assuming 'deals_df' and 'spend_df' DataFrames are already defined
# Merge deals with spend data to include campaign information
deals_campaign_df = pd.merge(Deals1, Spend, on='Source', how='left')

# Calculate the number of leads generated by each campaign
leads_by_campaign = deals_campaign_df.groupby('Campaign').size().reset_index(name='Leads Generated')

# Ensure numeric columns in 'spend_df'
numeric_columns = Spend.select_dtypes(include='number').columns.tolist()

# Merge with spend data to get spend and clicks for each campaign
campaign_performance_df = pd.merge(leads_by_campaign, Spend.groupby('Campaign')[numeric_columns].sum().reset_index(), on='Campaign', how='left')

# Calculate conversion rate and cost per lead for each campaign
campaign_performance_df['Conversion Rate'] = campaign_performance_df['Leads Generated'] / campaign_performance_df['Clicks']
campaign_performance_df['Cost per Lead'] = campaign_performance_df['Spend'] / campaign_performance_df['Leads Generated']

# Clean up any infinities or NaNs resulting from division by zero
campaign_performance_df.replace([float('inf'), -float('inf')], None, inplace=True)
campaign_performance_df.fillna(0, inplace=True)

# Display the DataFrame
print(campaign_performance_df)




# Assuming 'source_performance_df' DataFrame is already defined and contains necessary metrics
# Extract relevant metrics for plotting
sources = source_performance_df['Source']
leads_generated = source_performance_df['Leads Generated']
conversion_rate = source_performance_df['Conversion Rate']
cost_per_lead = source_performance_df['Cost per Lead']

# Plotting
fig, ax1 = plt.subplots(figsize=(12, 6))

# Bar plot for Leads Generated
ax1.bar(sources, leads_generated, color='b', alpha=0.6, label='Leads Generated')
ax1.set_xlabel('Source')
ax1.set_ylabel('Leads Generated')
ax1.set_title('Marketing Source Effectiveness: Quality Lead Generation')
ax1.legend(loc='upper left')

# Create a second y-axis for Conversion Rate
ax2 = ax1.twinx()
ax2.plot(sources, conversion_rate, color='g', marker='o', label='Conversion Rate')
ax2.set_ylabel('Conversion Rate')
ax2.legend(loc='upper right')

# Show the plot
plt.xticks(rotation=45)
plt.show()

# Plotting Cost per Lead
fig, ax3 = plt.subplots(figsize=(12, 6))
ax3.bar(sources, cost_per_lead, color='r', alpha=0.6, label='Cost per Lead')
ax3.set_xlabel('Source')
ax3.set_ylabel('Cost per Lead')
ax3.set_title('Marketing Source Efficiency: Cost per Lead')
ax3.legend(loc='upper left')
plt.xticks(rotation=45)
plt.show()
