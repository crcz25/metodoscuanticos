import numpy


def f1(x):
    return -1 / 6 + x / 12


def f2(x):
    return 4 / 3 - x / 6


def acep_rech():
    a1 = int(input("a1: "))
    b1 = int(input("b1: "))
    a2 = int(input("a2: "))
    b2 = int(input("b2: "))
    n = int(input("Num. de aceptados: "))

    mx1 = numpy.linspace(a1, b1, 50)
    mfx1 = f1(mx1)
    M1 = mfx1.max()

    mx2 = numpy.linspace(a2, b2, 50)
    mfx2 = f2(mx2)
    M2 = mfx2.max()

    if M1 > M2:
        M = M1
    else:
        M = M2

    print("\n[a1,b1]: [%d,%d] ; [a2,b2]: [%d,%d] ; M: %f\n" % (a1, b1, a2, b2, M))

    naceptados = 0
    nrechazos = 0
    aceptados = []
    media = 0
    desviacion_estandar = 0
    varianza = 0

    while naceptados < n:
        # random.uniform -> return a + (b-a) * self.random()
        r1 = numpy.random.uniform(0, 1)
        r2 = numpy.random.uniform(0, 1)

        x_asterisk = a1 + (b2 - a1) * r1

        if a1 <= x_asterisk <= b1:
            fx_asterisk = f1(x_asterisk)
            print("r1 = %f ; r2 = %f ; x* = %f ; f(x*) = %f" % (r1, r2, x_asterisk, fx_asterisk))
            print("r2 = %f <= f(x*)/M = %f" % (r2, fx_asterisk / M))
        elif a2 <= x_asterisk <= b2:
            fx_asterisk = f2(x_asterisk)
            print("r1 = %f ; r2 = %f ; x* = %f ; f(x*) = %f" % (r1, r2, x_asterisk, fx_asterisk))
            print("r2 = %f <= f(x*)/M = %f" % (r2, fx_asterisk / M))
        else:
            fx_asterisk = 0

        if r2 <= fx_asterisk / M:
            aceptados.append(x_asterisk)
            naceptados += 1
        else:
            nrechazos += 1

        print("Aceptados: %d" % naceptados, end=' ')
        print("Rechazos: %d\n" % nrechazos)

    total = naceptados + nrechazos
    media = numpy.mean(aceptados)
    print("Media: %f" % media)
    varianza = numpy.var(aceptados)
    print("Varianza: %f" % varianza)
    desviacion_estandar = numpy.std(aceptados)
    print("Desviacion Estandar: %f" % desviacion_estandar)
    print("Porcentaje de aceptados: %f %c" % (naceptados / total * 100, 37))
    print("\n")

    return 0


if __name__ == '__main__':

    while True:
        acep_rech()
