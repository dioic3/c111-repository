import numpy as np
np.random.seed(10)
mtz = np.random.randint(1,51,16)
mtz1 = mtz.reshape(4,4)
#print(mtz1)

print(np.unique(mtz1,return_counts=True))
