"""
Programa creado por: Molinex para la materia Metodos Cuantitativos
    Integrantes:
        Carlos Roberto Cueto Zumaya
        Diego Alfredo Ballesteros Bautista
        Jorge Armando Guzman Flores
"""
import numpy as np
import scipy.stats as stats
import math

# Distribucion binomial


def binomial_dist():
    print("\t\t\nBinomial")
    n = float(input("Introduce n: "))
    p = float(input("Introduce p: "))
    q = 1 - p
    media = n * p
    varianza = n * p * q
    desviacion = math.sqrt(n * p * q)
    inf = int(input("Introduce el rango inferior: "))
    sup = int(input("Introduce el rango superior: ")) + 1
    k = np.arange(inf, sup)
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

# Distribucion uniforme discreta


def uniform_discrete_dist():
    print("\t\t\nDistribucion uniforme discreta")
    size = int(input("Num. de X's: "))
    x = [0] * size

    for i in range(size):
        x[i] = float(input("X: "))

    valor_esperado = 0
    varianza = 0

    print("\n   Probabilidades")
    for i in range(size):
        valor_esperado += x[i] / size
        px = x[i]/size
        print("P(%d) = %f" % (x[i], px))

    for i in range(size):
        varianza += math.pow((x[i] - valor_esperado), 2) / size

    desviacion = math.sqrt(varianza)
    print("\nValor esperado (u): %f ; Varianza: %f ; Desviacion: %f \n" % (valor_esperado, varianza, desviacion))

    return 0

# Formulas generales


def gral_dist():
    print("\t\t\nFormulas Generales")
    size = int(input("Num. de X's: "))
    x = [0] * size
    px = [0] * size
    for i in range(size):
        x[i] = float(input("Introduce X: "))
        px[i] = float(input("Introduce P(x): "))

    valor_esperado = 0
    varianza = 0

    print("\n   Probabilidades       Acumuladas")
    cumulative = 0
    for i in range(size):
        valor_esperado += x[i] * px[i]
        cumulative += px[i]
        print("P(%d) = %f" % (x[i], px[i]), end='    ')
        print("F(%d) = %f" % (x[i], cumulative))
    for i in range(size):
        varianza += math.pow((x[i] - valor_esperado), 2) * px[i]

    desviacion = math.sqrt(varianza)
    print("\nValor esperado (u): %f ; Varianza: %f ; Desviacion: %f \n" % (valor_esperado, varianza, desviacion))

    return 0

# Processo de distribucion de posion, alfa y area-tiempo


def poisson_process_dist():
    print("\t\t\nPoisson")
    alpha = float(input("Introduce alpha: "))
    time = float(input("Introduce area/tiempo: "))
    lambd = alpha * time
    media = lambd
    varianza = lambd
    desviacion = math.sqrt(lambd)
    inf = int(input("Introduce el rango inferior: "))
    sup = int(input("Introduce el rango superior: ")) + 1
    k = np.arange(inf, sup)
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

# Distribucion de posion


def poisson_dist():
    print("\t\t\nPoisson")
    lambd = float(input("Introduce lambd: "))
    media = lambd
    varianza = lambd
    desviacion = math.sqrt(lambd)
    inf = int(input("Introduce el rango inferior: "))
    sup = int(input("Introduce el rango superior: ")) + 1
    k = np.arange(inf, sup)
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

# Distribucion exponencial


def exp_dis():
    print("\t\t\nExponencial")
    lambd = float(input("Introduce lambd: "))
    inf = int(input("Introduce el rango inferior: "))
    sup = int(input("Introduce el rango superior: ")) + 1
    k = np.arange(inf, sup)
    exp = 1 - np.exp(-lambd * k)

    media = 1 / lambd
    varianza = 1 / (lambd * lambd)
    desviacion = math.sqrt(1 / (lambd * lambd))

    print("\n   Probabilidades       Acumuladas")
    # cumulative = 0
    j = inf
    for i in range(len(exp)):
        # cumulative += exp[i]
        print("P(%d) = %f" % (j, exp[i]))
        # print("P(%d) = %f" % (j, exp[i]), end='     ')
        # print("F(%d) = %f" % (j, cumulative))
        j += 1
    if inf != (sup-1):
        print("\n")
        print("P(%d, %d) = %f" % (inf, (sup-1), (exp[-1]-exp[0])))
    else:
        print("\n")
        print("P(X <= %d) = %f" % (inf, (exp[0])))
        print("P(X > %d) = %f" % (inf, (1-exp[0])))

    print("\nMedia: %f ; Varianza: %f ; Desviacion: %f \n" % (media, varianza, desviacion))

    return 0


def menu():
    print("1.Binomial")
    print("2.Poisson")
    print("3.Proceso de poisson")
    print("4.Exponencial")
    print("5.Uniforme Discreta")
    print("6.Formulas Generales")

    return 0


if __name__ == '__main__':
    print("MOLINEX - Carlos Cueto, Diego Ballesteros, Jorge Guzman")
    print("Programa para calcular distribuciones vistas en primer parcial de Metodos Cuantitativos\n")
    while True:
        menu()
        option = int(input("Opcion: "))
        if option == 1:
            binomial_dist()
        if option == 2:
            poisson_dist()
        if option == 3:
            poisson_process_dist()
            print("NOTA = Cuando x>=n es 1-p(x<a)")
        if option == 4:
            exp_dis()
            print("NOTA = 1-e^-(lambd)(x)")
        if option == 5:
            uniform_discrete_dist()
        if option == 6:
            gral_dist()
        if option == 0:
            break
