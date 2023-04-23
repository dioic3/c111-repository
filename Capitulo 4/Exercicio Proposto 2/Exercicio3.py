import numpy as np
np.random.seed(10)
mtz = np.random.randint(1,51,16)
mtz1 = mtz.reshape(4,4)
#print(mtz1)

linhas = [mtz1.mean(axis=1)[0],mtz1.mean(axis=1)[1],mtz1.mean(axis=1)[2],mtz1.mean(axis=1)[3]]
print(linhas)

colunas = [mtz1.mean(axis=0)[0],mtz1.mean(axis=0)[1],mtz1.mean(axis=0)[2],mtz1.mean(axis=0)[3]]
print(colunas)

print(max(linhas))
print(max(colunas))