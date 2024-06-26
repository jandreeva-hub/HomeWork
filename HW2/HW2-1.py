import numpy as np

list_1 = input("Enter digits separated by a space: ").split()
arrya_a = np.array(list_1, int)
num = int(input("Enter index: "))
print(f"Item {num} = {arrya_a[num]}")
slice = input('Enter index start:end+1 separated by ":" ').split(":")
print(arrya_a[int(slice[0]):int(slice[1])])
