import pandas as pd
import numpy as np
Calls = pd.read_excel("Calls.xlsx")
Calls = Calls.drop_duplicates()
#filtered_Calls = Calls[(Calls['Call_Duration_seconds']>0) & (Calls['Call_Status'] != 'Missed')]
#print(Calls)

Calls =Calls.groupby('Call_Owner_Name')
print(Calls)