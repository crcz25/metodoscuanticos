import sys
import numpy as np
import scipy.stats as stats
import math


def binomial_dist():
    print("\t\t\nBinomial")
    n = float(input("Introduce n: "))
    p = float(input("Introduce p: "))
    q = 1 - p
    media = n * p
    varianza = n * p * q
    desviacion = math.sqrt(n * p * q)
    inf = int(input(("Introduce el rango inferior: ")))
    sup = int(input(("Introduce el rango superior: "))) + 1
    k = np.arange(inf,sup)
    binomial = stats.binom.pmf(k, n, p)

    print("\n   Probabilidades       Acumuladas")
    cumulative = 0
    j = inf
    for i in range(len(binomial)):
        cumulative += binomial[i]
        print("P(%d) = %f" % (j, binomial[i]), end='    ')
        print("F(%d) = %f" % (j, cumulative))
        j += 1
    print("\nMedia: %f ; Varianza: %f ; Desviacion: %f \n" % (media, varianza, desviacion))

    return 0


def uniform_discrete_dist():
    inf = int(input(("Introduce el rango inferior: ")))
    sup = int(input(("Introduce el rango superior: "))) + 1
    k = np.arange(inf, sup)
    # data = [][]

    # for i in range():
    #     for j in range():
    #         end
    # end

    return 0


def poisson_process_dist():
    print("\t\t\nPoisson")
    alpha = float(input("Introduce alpha: "))
    time = float(input("Introduce area/tiempo: "))
    lambd = alpha * time
    inf = int(input(("Introduce el rango inferior: ")))
    sup = int(input(("Introduce el rango superior: "))) + 1
    k = np.arange(inf,sup)
    poisson = stats.poisson.pmf(k, lambd)

    print("\n   Probabilidades       Acumuladas")
    cumulative = 0
    j = inf
    for i in range(len(poisson)):
        cumulative += poisson[i]
        print("P(%d) = %f" % (j, poisson[i]), end='     ')
        print("F(%d) = %f" % (j, cumulative))
        j += 1

    return 0


def poisson_dist():
    print("\t\t\nPoisson")
    lambd = float(input("Introduce lambd: "))
    media = lambd
    varianza = lambd
    desviacion = math.sqrt(lambd)
    inf = int(input(("Introduce el rango inferior: ")))
    sup = int(input(("Introduce el rango superior: "))) + 1
    k = np.arange(inf,sup)
    poisson = stats.poisson.pmf(k, lambd)

    print("\n   Probabilidades       Acumuladas")
    cumulative = 0
    j = inf
    for i in range(len(poisson)):
        cumulative += poisson[i]
        print("P(%d) = %f" % (j, poisson[i]), end='     ')
        print("F(%d) = %f" % (j, cumulative))
        j += 1
    print("\nMedia: %f ; Varianza: %f ; Desviacion: %f \n" % (media, varianza, desviacion))

    return 0


def exp_dis():
    print("\t\t\nExponencial")
    lambd= float(input("Introduce lambd: "))
    inf = int(input(("Introduce el rango inferior: ")))
    sup = int(input(("Introduce el rango superior: "))) + 1
    k = np.arange(inf, sup)
    exp = 1 - np.exp(-lambd * k)

    print("\n   Probabilidades       Acumuladas")
    # cumulative = 0
    j = inf
    for i in range(len(exp)):
        # cumulative += exp[i]
        print("P(%d) = %f" % (j, exp[i]))
        # print("P(%d) = %f" % (j, exp[i]), end='     ')
        # print("F(%d) = %f" % (j, cumulative))
        j += 1

    return 0



def menu():
    print("1.Binomial")
    print("2.Poisson")
    print("3.Proceso de poisson")


if __name__ == '__main__':
    while True:
        menu()
        option = int(input("Opcion: "))
        if option == 1:
            binomial_dist()
        if option == 2:
            poisson_dist()
        if option == 3:
            poisson_process_dist()
            print("NOTA = Cuando x>=n es 1-f(a)")
        if option == 4:
            exp_dis()
        if option == 0:
            break

        # print("\t\tBinomial")
        # n = int(input("Introduce n: ")) + 1
        # p = float(input("Introduce p: "))
        # k = np.arange(n)
        # binomial = stats.binom.pmf(k, n, p)
        #
        # print("Probabilidades       Acumuladas")
        # cumulative = 0
        # for i in range(len(binomial)):
        #     cumulative += binomial[i]
        #     print("P(%d) = %f" % (i, binomial[i]), end='    ')
        #     print("F(%d) = %f" % (i, cumulative))
        # binomDist()



