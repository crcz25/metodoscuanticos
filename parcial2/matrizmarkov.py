import numpy as np

cols = int(input("Num. columnas: "))
n = int(input("Potencia: "))


# agregar mult de v0
matrix = np.loadtxt('matriz.txt', usecols=range(cols))
m = np.linalg.matrix_power(matrix, n)


print("\n")
print(matrix)
print("\n")
print(m)
