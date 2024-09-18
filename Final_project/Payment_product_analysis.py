#Анализ платежей и продуктов

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

Deals1 = pd.read_excel('Deals1.xlsx')
Calls = pd.read_excel('Calls (Done) (1).xlsx')
Spend = pd.read_excel('Spend (Done) (2).xlsx')

import matplotlib.pyplot as plt

# 1. Distribution and Success of Payment Types
# Group by Payment Type to calculate the total deals and successful deals
payment_analysis = Deals1.groupby('Payment Type').agg({
    'Id': 'count',  # Total deals
    'Stage': lambda x: (x == 'Payment Done').sum()  # Successful deals
}).reset_index()

# Calculate the success rate for each payment type
payment_analysis.rename(columns={'Id': 'Total Deals', 'Stage': 'Successful Deals'}, inplace=True)
payment_analysis['Success Rate'] = payment_analysis['Successful Deals'] / payment_analysis['Total Deals']

# Plotting Payment Type Distribution
fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.bar(payment_analysis['Payment Type'], payment_analysis['Total Deals'], color='skyblue', label='Total Deals')
ax1.set_xlabel('Payment Type')
ax1.set_ylabel('Total Deals')
ax1.set_title('Distribution of Payment Types')
plt.xticks(rotation=45)
plt.show()

# Plotting Payment Type Success Rate
fig, ax2 = plt.subplots(figsize=(10, 6))
ax2.bar(payment_analysis['Payment Type'], payment_analysis['Success Rate'], color='green', label='Success Rate')
ax2.set_xlabel('Payment Type')
ax2.set_ylabel('Success Rate')
ax2.set_title('Success Rate by Payment Type')
plt.xticks(rotation=45)
plt.show()
# 2. Popularity and Success of Products and Education Types

# Analyze Products
product_analysis = Deals1.groupby('Product').agg({
    'Id': 'count',  # Total deals
    'Stage': lambda x: (x == 'Payment Done').sum()  # Successful deals
}).reset_index()

# Calculate success rate for each product
product_analysis.rename(columns={'Id': 'Total Deals', 'Stage': 'Successful Deals'}, inplace=True)
product_analysis['Success Rate'] = product_analysis['Successful Deals'] / product_analysis['Total Deals']

# Plotting Product Popularity
fig, ax3 = plt.subplots(figsize=(10, 6))
ax3.bar(product_analysis['Product'], product_analysis['Total Deals'], color='skyblue', label='Total Deals')
ax3.set_xlabel('Product')
ax3.set_ylabel('Total Deals')
ax3.set_title('Popularity of Products')
plt.xticks(rotation=45)
plt.show()

# Plotting Product Success Rate
fig, ax4 = plt.subplots(figsize=(10, 6))
ax4.bar(product_analysis['Product'], product_analysis['Success Rate'], color='green', label='Success Rate')
ax4.set_xlabel('Product')
ax4.set_ylabel('Success Rate')
ax4.set_title('Success Rate by Product')
plt.xticks(rotation=45)
plt.show()

# Analyze Education Types
education_analysis = Deals1.groupby('Education Type').agg({
    'Id': 'count',  # Total deals
    'Stage': lambda x: (x == 'Payment Done').sum()  # Successful deals
}).reset_index()

# Calculate success rate for each education type
education_analysis.rename(columns={'Id': 'Total Deals', 'Stage': 'Successful Deals'}, inplace=True)
education_analysis['Success Rate'] = education_analysis['Successful Deals'] / education_analysis['Total Deals']

# Plotting Education Type Popularity
fig, ax5 = plt.subplots(figsize=(10, 6))
ax5.bar(education_analysis['Education Type'], education_analysis['Total Deals'], color='skyblue', label='Total Deals')
ax5.set_xlabel('Education Type')
ax5.set_ylabel('Total Deals')
ax5.set_title('Popularity of Education Types')
plt.xticks(rotation=45)
plt.show()

# Plotting Education Type Success Rate
fig, ax6 = plt.subplots(figsize=(10, 6))
ax6.bar(education_analysis['Education Type'], education_analysis['Success Rate'], color='green', label='Success Rate')
ax6.set_xlabel('Education Type')
ax6.set_ylabel('Success Rate')
ax6.set_title('Success Rate by Education Type')
plt.xticks(rotation=45)
plt.show()
