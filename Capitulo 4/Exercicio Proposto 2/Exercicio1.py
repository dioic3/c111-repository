import numpy as np
#array com elementos positivos e negativos entre 0 e 1
np.random.seed(5)
arrayfloat = np.random.uniform(-1,1,10)

array = arrayfloat * 100
arry = np.trunc(array)
print(arry)
