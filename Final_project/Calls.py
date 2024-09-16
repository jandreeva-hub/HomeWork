import pandas as pd
import statistics
import numpy as np
Calls = pd.read_excel(
    'Calls (Done) (1).xlsx',
    dtype={
        'Id': 'str',
        'CONTACT ID':'str',
        },
    parse_dates=['Call Start Date',
        'Call Start Time'
        ]
)
Calls = Calls.drop_duplicates()
#filtered_Calls = Calls[(Calls['Call_Duration_seconds']>0) & (Calls['Call_Status'] != 'Missed')]
#print(Calls)
# Удаление строк, где значения в столбцах 'Call Type', 'Call Duration (in seconds)' и 'CONTACT ID' пустые
Calls = Calls.dropna(subset=['Call Type', 'CONTACT ID', 'Call Duration (in seconds)'])
Calls = Calls[(Calls['Call Type'] != '') & (Calls['CONTACT ID'] != '')]

# Удаление ненужных столбцов
Calls = Calls.drop(columns=['Dialled Number','Outgoing Call Status', 'Scheduled in CRM', 'Tag'])

Calls['Call Duration (in seconds)'] = pd.to_numeric(Calls['Call Duration (in seconds)'], errors='coerce')
Calls.to_excel('Calls.xlsx', index=False) 
print(Calls.dtypes)
Calls_mode = statistics.mode(Calls['Call Duration (in seconds)'])
Calls_range_value = np.ptp(Calls[['Call Duration (in seconds)']])
Calls_describe_stats = Calls[['Call Duration (in seconds)']].describe().T
print(Calls_mode)
print(Calls_range_value)
print(Calls_describe_stats)

