import numpy as np

mtz = np.arange(1,26,1).reshape(5,5)
lenght = np.size(mtz)
dimension = np.shape(mtz)
if lenght % 2:
    print(lenght)
    arr = mtz.reshape(25)
    print(arr)
else:
    print(dimension)
