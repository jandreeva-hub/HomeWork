import numpy as np


len_arrya = int(input("Entery range: "))

arrya_a = np.random.randint(1, 11, len_arrya)
arrya_b = np.random.randint(1, 11, len_arrya)

arrya_c = arrya_a * arrya_b

print(arrya_a, "\n", arrya_b, "\n", arrya_c)

