
import numpy as np
arr = np.arange(100,50,-1)
arr1 = np.arange(0,51)

arr3 = np.concatenate([arr,arr1])
arr4 = np.flip(np.sort(arr3))
print(arr4)