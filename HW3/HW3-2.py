import random
import numpy as np
import time

x= 12000000

arryay_a = np.arange(0, x)
for i in range(0, x):
    arryay_a[i] = random.randint(0, 1000)

print(arryay_a)

arryay_c = arryay_a.reshape(100, -1, order='C')
start_time = time.process_time()
arryay_r = arryay_c * arryay_c
end_time = time.process_time()
print(f"runtime multiplication C - style: {end_time - start_time} sec")

arryay_f = arryay_a.reshape(100, -1, order='F')
start_time = time.process_time()
arryay_r = arryay_f * arryay_f
end_time = time.process_time()
print(f"runtime multiplication F - style: {end_time - start_time} sec")

start_time = time.process_time()
arryay_r = arryay_c + arryay_c
end_time = time.process_time()
print(f"runtime SUM C - style: {end_time - start_time} sec")

start_time = time.process_time()
arryay_r = arryay_f + arryay_f
end_time = time.process_time()
print(f"runtime SUM F - style: {end_time - start_time} sec")
