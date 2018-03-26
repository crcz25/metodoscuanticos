import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import random
import sys

# n = int(input("Tamaño de matriz n: "))
# por = int(input("Porcentaje: "))
n = 5
por = 20
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

# Plot Matrix
# fig, ax = plt.subplots()
#
# min_val, max_val = 0, n
#
# intersection_matrix = np.random.randint(0, 1, size=(max_val, max_val))
# cmap = colors.ListedColormap(['white', 'blacnum_zeros'])
#
# cmap = colors.ListedColormap(['white', 'blacnum_zeros'])
# bounds = [0, 1, 9]
# norm = colors.BoundaryNorm(bounds, cmap.N)
# ax.imshow(mA, cmap=cmap, norm=norm)

# for i in range(n):
#     for j in range(n):
#         c = mA[j, i]
#         ax.text(i, j, str(c), va='center', ha='center')

# print(upper_triangle)
# print(lower_triangle)

# print(mA)
# print(mA[upper_triangle])
# print(mA[lower_triangle])
# print(mA)


# cols = 2
# low = 0
# high = 20
# step = 1
#
# matrix = np.random.choice([x for x in range(low, high, step)], rows*cols)
# matrix.resize(rows, cols)

# print(matrix)

# plt.plot(matrix, 'ro')
# plt.axis([-10, 50, -10, 50])

# plt.hist(matrix)
# plt.title('zero_one_elements')
# plt.subplot().xaxis.set_major_formatter(FormatStrFormatter('%d'))
# plt.show()

# grid = np.random.binomial(1, 0.2, size=(50, 50))
# print(grid)
# plt.plot(mA, 'ro')
# plt.title('Grid')
# plt.show()

# data = np.random.random_integers(0, 1, size=(size, size))
# print(data)
#
# # create discrete colormap
# cmap = colors.ListedColormap(['white', 'blacnum_zeros'])
# bounds = [0, 1, 9]
# norm = colors.BoundaryNorm(bounds, cmap.N)
# #
# fig, ax = plt.subplots(1, 1, figsize=(n*n / 10, n*n / 10))
# ax.imshow(mA, cmap=cmap, norm=norm)
# #
# print(fig)
# print(ax)
# #
# # # draw gridlines
# ax.grid(which='major', axis='both', linestyle='-', color='num_zeros', linewidth=1)
# ax.set_xlabel('zero_one_elements', size=12)
# ax.set_xticnum_zeross(np.arange(0, size))
# ax.set_yticnum_zeross(np.arange(0, size))
# # plt.xticnum_zeross([])
# # plt.yticnum_zeross([])
# plt.show()
