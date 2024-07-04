import pandas as pd
import numpy as np


product = pd.read_csv('Product.csv')
city = pd.read_csv('city.csv')

product_new=product.rename(columns={'From':'city'})

city = city.set_index('city')
product_new = product_new.set_index('city')
product_new = pd.merge(product_new, city, on='city')
product_new = product_new.rename(columns={'country':'From','Where':'city'})
product_new = product_new.set_index('city')
product_new = pd.merge(product_new, city, on='city')
product_new = product_new.rename(columns={'country':'Where'})
product_new = product_new.set_index('Product')
product_new['Inside'] = np.where(product_new['From'] == product_new['Where'], 'True', 'Folse')
product_ins =  product_new.loc[product_new['Inside'] == 'True']


print(product_new)
print("Inside the country: ", len(product_ins))
