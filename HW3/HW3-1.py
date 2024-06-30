import numpy as np
import time


arryay_a = np.random.randint(0, 1000, 1000000)
arryay_b = np.random.randint(0, 1000, 1000000)
arryay_c = np.zeros(1000000)

start_time = time.process_time()
for i in range (0, (len(arryay_a)-1)):
    arryay_c[i] = arryay_a[i] + arryay_b[i]
end_time = time.process_time()
print(f"for loop execution time: {end_time - start_time} sec")
print (arryay_c)

start_time = time.process_time()
arryay_c = arryay_a + arryay_b
end_time = time.process_time()
print(f"Execution time using NumPy : {end_time - start_time} sec")