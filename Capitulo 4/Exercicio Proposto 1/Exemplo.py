# importar o numpy
import numpy as np

# criando um numpy array 1-D
#arrayB = np.array([1,2,3,4])
#print(type(arrayB)) #mostrar o tipo de estrutura de dados
#print(arrayB)

# criando um numpy array de 2-D (matriz)
#mtz = np.array([
 #   [1,2,3],
 #   [1,2,3],
 #   [1,2,3]
#])
#print(mtz[0,2])
#print(mtz[:2,2:])

#ESTRUTURANDO NUMPY ARRAYS COM FUNÇÕES DO NUMPY
#funções zeros
#arrr = np.zeros(10)
#print(arrr)
#funcoes ones
#mtz = np.ones([3,3])
#print(mtz)

#funcao arange
# podemos usar o conceito de reshape (remodelamento) -> devem ser compativeis
#mtz1 = np.arange(1,13,1).reshape(3,4)
#print(mtz1)

#funcao linspace
#arr = np.linspace(0,100,11)
#print(arr)

# ordenando e concatenando arrays
# usa o sort para ordenar e .flip para deixar o inverso

# CONCATENACAO DE NUMPY ARRAYS
#arr = np.array([1,2,3,4])
#arr1 = np.array([5,6,7,8])

#arr2 = np.concatenate([arr, arr1])
#print(arr2)
