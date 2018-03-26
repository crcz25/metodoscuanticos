import numpy as np
import random

n = int(input("Tamaño de matriz n: "))
por = int(input("Porcentaje: "))
# n = 20
# por = 60
p = int(n * n * (por / 100))

print("Matriz de %d x %d, con porcentaje %d y valor de P=%d" % (n, n, por, p))

mA = np.zeros((n, n), int)
mB = np.zeros((n, n), int)

unos = 0
zeros = 0

helper = int(n * (n-1) / 2)

upper_triangle = np.triu_indices(n, 1)
lower_triangle = np.tril_indices(n, -1)

# print("Upper triangle", upper_triangle)
# print("Lower triangle", lower_triangle)

m = [[], []]
holi = n - 1

while True:
    r1 = random.randint(0, holi)
    r2 = random.randint(0, holi)
    r3 = random.randint(0, holi)

    # print(m)
    # print(unos)

    if r1 != r2 and r2 != r3 and tuple((r1, r2)) not in m[0] and tuple((r2, r3)) not in m[1]:
        m[0].append(tuple((r1, r2)))
        m[1].append(tuple((r2, r3)))
        # print("non diagonal ", r1, ",", r2)
        unos += 1

    if unos >= p:
        break

for i, j in m[0]:
    mA[i, j] = 1

for i, j in m[1]:
    mB[i, j] = 1

print("\nMatriz A")
unos = 0
zeros = 0
for i in range(n):
    for j in range(n):
        print(mA[i, j], end=' ')
    aux = np.count_nonzero(mA[i] == 1)
    unos += aux
    zeros += np.count_nonzero(mA[i] == 0)
    print(' | %d' % aux)

print("Total de 0's: %d \nTotal de 1's: %d" % (zeros, unos))

print("\nMatriz B")
unos = 0
zeros = 0
for i in range(n):
    for j in range(n):
        print(mB[i, j], end=' ')
    aux = np.count_nonzero(mB[i] == 1)
    unos += aux
    zeros += np.count_nonzero(mB[i] == 0)
    print(' | %d' % aux)

print("Total de 0's: %d \nTotal de 1's: %d" % (zeros, unos))

# print(np.diag(mA))
# print(np.diag(mB))
# print(mA)


# size = helper * 2
# num_zeros = size - p
# zero_one_elements = np.array([0] * num_zeros + [1] * (size-num_zeros))
#
# np.random.shuffle(zero_one_elements)
#
# print(zero_one_elements)
# print(size)
# print(num_zeros)
# print(p)
# print(np.split(zero_one_elements, 2))
#
# aux1, aux2 = np.split(zero_one_elements, 2)
# # print(aux1)
# # print(aux2)
#
# mA[upper_triangle] = aux1
# mA[lower_triangle] = aux2
#