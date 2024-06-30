import pandas as pd

keys = input("Enter column names: ").split()
array = []
while True:
    data = input("Enter details (enter 'end' to end): ").split()
    if data[0] != "end":
        array.append({keys[0]: data[0], keys[1]: data[1], keys[2]: data[2]})
    else: break
df = pd.DataFrame(array)
print(df)

key = input("Enter a name for the column to display: ")
print(df[key])