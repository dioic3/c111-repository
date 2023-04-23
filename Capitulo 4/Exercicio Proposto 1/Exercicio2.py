# crie dois arrays: um de numeros pares de 0 a 51 e outro também de numero pares de 100 até 50. Em seguida, os concatene e mostre os resultados ordenados
import numpy as np
arr = np.arange(100,50,-1)
arr1 = np.arange(0,51)

arr3 = np.concatenate([arr,arr1])
arr4 = np.sort(arr3)
print(arr4)