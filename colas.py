import math


def menu():
    print("1.Reglas Generales ")
    print("2.M/M/1 (Tiempos de llegada exponenciales/Tiempo de servicio exponencial/ 1 servidor)")
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
    s = float(input("Numero de servidores s: "))
    # wq = float(input("Tiempo esperado Wq: "))
    n = int(input("Probabilidad n: "))
    t = float(input("Probabilidad t: "))

    ls = lamb / (miu - lamb)
    lq = pow(lamb, 2) / (miu * (miu - lamb))
    ws = 1 / (miu - lamb)
    wq = lamb / (miu * (miu - lamb))
    p = lamb / (s * miu)

    print("\nλ=%f ; μ=%f ; Ls=%f ; Lq=%f ; Ws=%f ; Wq=%f ; p=%f\n" % (lamb, miu, ls, lq, ws, wq, p))

    aux = 0
    for i in range(n+1):
        # Pn=(1-p)p^n
        pn = (1 - p) * pow(p, i)
        aux += pn
        # P(Ls>n)=p^n+1
        pls = pow(p, i + 1)

        # print("P(%d)=%f ; Fp(%d)=%f" % (i, pn, i, aux))
        print("n: %d ; p=%f ; Pn=%f ; PLs=%f" % (i, p, pn, pls))

    # P(Ws>t)=e^-μ(1-p)t
    pws = math.exp(-miu * (1 - p) * t)
    # P(Wq>t)=pe^-μ(1-p)t
    pwq = p * math.exp(-miu * (1 - p) * t)
    print("\nPWs=%f ; PWq=%f" % (pws, pwq))

    return 0


if __name__ == '__main__':

    while True:
        menu()
        option = int(input("Opcion: "))
        if option == 1:
            reglas_generales()
        if option == 2:
            mm1()