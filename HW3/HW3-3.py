import random
import numpy as np


n = int(input("Enter matrix size N: "))
arryay = np.identity(n)
for i in range(n):
    for j in range(n):
        arryay[i][j] = random.randint(-10, 10)
print("N = \n", arryay)
det_arryay = np.linalg.det(arryay)
print("matrix determinant = ", det_arryay)

if det_arryay != 0:
    print("inverse matrix: \n", np.linalg.inv(arryay))
else:
    print("there is no inverse matrix")
