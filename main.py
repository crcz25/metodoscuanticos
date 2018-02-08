import sys
import numpy as np
import scipy.stats as stats

def binomDist():
    print("\t\t\nBinomial")
    n = int(input("Introduce n: "))
    p = float(input("Introduce p: "))
    inf = int(input(("Introduce el rango inferior: ")))
    sup = int(input(("Introduce el rango superior: "))) + 1
    k = np.arange(inf,sup)
    binomial = stats.binom.pmf(k, n, p)

    print("\n   Probabilidades       Acumuladas")
    aux = 0
    j = inf
    for i in range(len(binomial)):
        aux += binomial[i]
        print("P(%d) = %f" % (j, binomial[i]), end='    ')
        print("F(%d) = %f" % (j, aux))
        j += 1
    print("\n")
    return 0

def menu():
    print("1.Binomial")


if __name__ == '__main__':
    while True:
        menu()
        option = int(input("Opcion: "))
        if option == 1:
            binomDist()
        elif option == 0:
            break

        # print("\t\tBinomial")
        # n = int(input("Introduce n: ")) + 1
        # p = float(input("Introduce p: "))
        # k = np.arange(n)
        # binomial = stats.binom.pmf(k, n, p)
        #
        # print("Probabilidades       Acumuladas")
        # aux = 0
        # for i in range(len(binomial)):
        #     aux += binomial[i]
        #     print("P(%d) = %f" % (i, binomial[i]), end='    ')
        #     print("F(%d) = %f" % (i, aux))
        # binomDist()



