import pandas as pd
import numpy as np

Contacts = pd.read_excel("Contacts.xlsx")
#print(Contacts).head()

Contacts = Contacts.drop_duplicates()
print(Contacts.isnull().sum())


