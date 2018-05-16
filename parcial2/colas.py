"""
Carlos Roberto Cueto Zumaya     A01209474
"""

import math


def menu():
    print("1.Reglas Generales Ley de little")
    print("2.M/M/1 (Tiempos de llegada exponenciales/Tiempo de servicio exponencial/ 1 servidor)")
    print("3.M/M/S (Tiempos de llegada exponenciales/Tiempo de servicio exponencial/ n servidor)")
    return 0


def reglas_generales():
    lamb = float(input("\nTasa media de llegadas λ: "))
    miu = float(input("Tasa media de servicio μ: "))
    s = float(input("Numero de servidores s: "))
    wq = float(input("Tiempo esperado Wq: "))

    ws = wq + (1 / miu)
    ls = lamb * ws
    lq = lamb * wq
    p = lamb / (s * miu)

    print("\nλ=%f ; μ=%f ; Ls=%f ; Lq=%f ; Ws=%f ; Wq=%f ; p=%f\n" % (lamb, miu, ls, lq, ws, wq, p))
    return 0


def mm1():
    lamb = float(input("\nTasa media de llegadas λ: "))
    miu = float(input("Tasa media de servicio μ: "))
    # wq = float(input("Tiempo esperado Wq: "))

    ls = lamb / (miu - lamb)
    lq = pow(lamb, 2) / (miu * (miu - lamb))
    ws = 1 / (miu - lamb)
    wq = lamb / (miu * (miu - lamb))
    p = lamb / miu

    print("\nλ=%f ; μ=%f ; Ls=%f ; Lq=%f ; Ws=%f ; Wq=%f ; p=%f\n" % (lamb, miu, ls, lq, ws, wq, p))

    n = int(input("Probabilidad n: "))
    t = float(input("Probabilidad t: "))

    aux = 0
    for i in range(n+1):
        # Pn=(1-p)p^n
        pn = (1 - p) * pow(p, i)
        aux += pn
        # P(Ls>n)=p^n+1
        pls = pow(p, i + 1)

        # print("P(%d)=%f ; Fp(%d)=%f" % (i, pn, i, aux))
        print("n: %d; Pn=%f ; PLs=%f" % (i, pn, pls))

    # P(Ws>t)=e^-μ(1-p)t
    pws = math.exp(-miu * (1 - p) * t)
    # P(Wq>t)=pe^-μ(1-p)t
    pwq = p * math.exp(-miu * (1 - p) * t)
    print("\nPWs=%f ; PWq=%f\n" % (pws, pwq))

    return 0


def mms():
    lamb = float(input("\nTasa media de llegadas λ: "))
    miu = float(input("Tasa media de servicio μ: "))
    s = int(input("Servidores s: "))

    p = lamb / (s * miu)

    helper = lamb / miu
    aux1 = 0
    for n in range(s):
        aux1 += pow(helper, n) / math.factorial(n)
    aux2 = pow(helper, s) / (math.factorial(s) * (1 - p))

    p0 = 1 / (aux1 + aux2)
    lq = (pow(helper, s) * p0 * p) / (math.factorial(s) * pow(1 - p, 2))
    wq = lq / lamb
    ws = wq + 1 / miu
    ls = lamb * ws

    print("\nλ=%f ; μ=%f ; s=%d ; p=%f" % (lamb, miu, s, p))
    print("p0=%f ; Ls=%f ; Lq=%f ; Ws=%f ; Wq=%f\n" % (p0, ls, lq, ws, wq))

    cs = int(input("Coste por unidad de tiempo y servidor Cs: "))
    cw = int(input("Coste de espera por unidad de tiempo y cliente Cw: "))

    cs = cs * s
    cw = cw * ls
    ct = cs + cw

    print("\nCs=%f ; Cw=%f ; Ct=%f\n" % (cs, cw, ct))

    i = int(input("P(n): "))

    pn = 0
    for n in range(i + 1):
        if n > s:
            pn = (pow(helper, n) * p0) / (math.factorial(s) * pow(s, n - s))
        if 0 <= n <= s:
            pn = pow(helper, n) * p0 / math.factorial(n)
        print("p(%d)=%f\n" % (n, pn))

    return 0


if __name__ == '__main__':

    while True:
        menu()
        option = int(input("Opcion: "))
        if option == 1:
            reglas_generales()
        if option == 2:
            mm1()
        if option == 3:
            mms()
