import numpy as np

list_1 = input("Enter 5 digits separated by a space.").split()
list_2 = input("Enter 5 digits separated by a space.").split()
arrya_a = np.array(list_1, float)
arrya_b = np.array(list_2, float)

arrya_c = arrya_a + arrya_b

print(arrya_c)



