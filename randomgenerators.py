import numpy
import random
import os


def menu():
    print("1.Generador congruencial lineal")
    print("2.Cuadrados medios")
    print("3.Aceptacion y rechazo")
    return 0


def lcg():
    a = int(input("a: "))
    c = int(input("c: "))
    m = int(input("m: "))
    zi = int(input("Z0: "))
    # n = int(input("Iteraciones: "))
    period = []
    n = 50

    if m < 0:
        print("Error, m > 0")
    if 0 >= a >= m - 1:
        print("Error, 0 <= a <= m - 1")
    if 0 >= c >= m - 1:
        print("Error, 0 <= c <= m - 1")
    if 0 >= zi >= m - 1:
        print("Error, 0<= Z0 <= m - 1")

    print("\nm\tc\tz\ta\tZi+1\t\tR\t\tItr")
    for i in range(n):
        z = zi
        zi = ((a * zi) + c) % m
        period.append(zi)
        r = zi / m

        if i == 0:
            print("%d\t%d\t%d\t%d\t%d\t\t%f\t%d" % (m, c, z, a, zi, r, i + 1))
        else:
            period.count(zi)
            # print(period.count(zi))
            print("\t\t%d\t\t%d\t\t%f\t%d" % (z, zi, r, i + 1))
            if int(period.count(zi)) > 1:
                # print("Periodo completado")
                print("Longitud del periodo %d" % i)
                print("\n")
                return 0

    print("\n")
    return 0


def mid_square():
    zi = int(input("Z0: "))
    digits = int(input("n: "))
    x = len(str(zi)) * 2

    if not 4*digits > len(str(zi)):
        print("holi")

    n = int(input("Iteraciones: "))

    print("\nItr\t\tZi\t\tZi2\t\tR")
    for i in range(n):
        zi2 = str(zi * zi).zfill(x)
        r = int(zi2[x // 4:x * 3 // 4])
        zi = r
        print("%d\t%d\t%s\t%d" % (i + 1, zi, zi2, r))

    print("\n")

    return 0


def f(x):
    return 2 * x


def acep_rech():
    a = int(input("a: "))
    b = int(input("b: "))
    n = int(input("Iteraciones: "))
    # n = int(input("Num. de aceptados: "))

    mx = numpy.linspace(a, b, 25)
    mfx = f(mx)
    m = 0
    M = mfx.max()

    print("\n[a,b]: [%d,%d] ; M: %d\n" % (a, b, M))

    naceptados = 0
    nrechazos = 0

    # while naceptados < n:
    #     # random.uniform -> return a + (b-a) * self.random()
    #     r1 = numpy.random.uniform(0, 1)
    #     r2 = numpy.random.uniform(0, 1)
    #
    #     x_asterisk = a + (b - a) * r1
    #     fx_asterisk = f(x_asterisk)
    #
    #     print("r1 = %f ; r2 = %f ; x* = %f ; f(x*) = %f" % (r1, r2, x_asterisk, fx_asterisk))
    #     print("r2 = %f <= f(x*)/M = %f" % (r2, fx_asterisk / M))
    #
    #     if r2 <= fx_asterisk / M:
    #         naceptados += 1
    #     else:
    #         nrechazos += 1
    #
    #     print("Aceptados: %d" % naceptados, end=' ')
    #     print("Rechazos: %d\n" % nrechazos)
    #
    # print("\n")

    for i in range(n):
        # random.uniform -> return a + (b - a) * self.random()
        # random.random -> return random [0.0,1.0)
        r1 = random.uniform(a, b)
        r2 = random.random()
        # r2 = int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1)

        x_asterisk = r1
        fx_asterisk = f(x_asterisk)

        print("r1= %f ; r2= %f ; x*= %f ; f(x*)= %f" % (r1, r2, x_asterisk, fx_asterisk))
        print("%f <= %f" % (r2, fx_asterisk / M))

        if r2 <= fx_asterisk / M:
            naceptados += 1
        else:
            nrechazos += 1

        print("Aceptados: %d" % naceptados, end=' ')
        print("Rechazos: %d" % nrechazos)

    print("\n")
    return 0


if __name__ == '__main__':

    while True:
        menu()
        option = int(input("Opcion: "))
        if option == 1:
            lcg()
        if option == 2:
            mid_square()
        if option == 3:
            acep_rech()

