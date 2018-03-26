import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import random

# n = int(input("Tamaño de matriz n: "))
# por = int(input("Porcentaje: "))
n = 5
por = 60
p = int(n * n * (por / 100))

print("Matriz de %d x %d, con porcentaje %d y valor de P=%d" % (n, n, por, p))
mA = np.zeros((n, n), int)

unos = 0
zeros = 0

helper = int(n * (n-1) / 2)

upper_triangle = np.triu_indices(n, 1)
lower_triangle = np.tril_indices(n, -1)

size = helper * 2
num_zeros = size - p
zero_one_elements = np.array([0] * num_zeros + [1] * (size-num_zeros))

np.random.shuffle(zero_one_elements)

# print(zero_one_elements)
# print(size)
# print(num_zeros)
# print(p)
# print(np.split(zero_one_elements, 2))

aux1, aux2 = np.split(zero_one_elements, 2)
# print(aux1)
# print(aux2)

mA[upper_triangle] = aux1
mA[lower_triangle] = aux2

for i in range(n):
    for j in range(n):
        print(mA[i, j], end=' ')
    aux = np.count_nonzero(mA[i] == 1)
    unos += aux
    zeros += np.count_nonzero(mA[i] == 0)
    print(' | %d' % aux)

print("Total de 0's: %d \nTotal de 1's: %d" % (zeros, unos))
