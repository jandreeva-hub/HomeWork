import numpy as np
import random as rn

dim = input("Enter matrix dimensions MxN: ").split("x")
array_a = np.eye(int(dim[0]), int(dim[1]))
array_b = np.eye(int(dim[0]), int(dim[1]))
for i in range(int(dim[0])):
    for j in range(int(dim[1])):
        array_a[i][j] = rn.randint(0, 10)

for i in range(int(dim[0])):
    for j in range(int(dim[1])):
        array_b[i][j] = rn.randint(0, 10)

print(f"A = {array_a}\nB = {array_b}")

operation = input("Select the operation: addition -1, multiplication -2 , transpose -3 :")

if operation == "1":
    print("Summa = ", array_a + array_b)
elif operation == "2":
    print("Difference = ", array_a - array_b)
else:
    print("Transposed A:\n ", array_a.transpose(), "\nTransposed B:\n ", array_b.transpose())
