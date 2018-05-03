from gauss import GEPP
import numpy as np


def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        return to_str(n//base, base) + convert_string[n % base]


if __name__ == "__main__":
    print("Leyendo matrices")
    # Load files
    P = []
    R = []
    maxS = []
    pol = []
    with open("p.txt", "r") as f:
        for line in f:
            P.append(np.matrix(line))

    with open("r.txt", "r") as f:
        for line in f:
            R.append(np.matrix(line))

    # alpha = float(input("Inserte el valor de alpha: "))
    # S = int(input("Inserte el valor de alpha: "))
    # estados = int(input("Numeros de estados: "))
    # acciones = int(input("Numeros de acciones: "))

    alpha = 0.6
    estados = 3
    acciones = len(P)
    totalPoliticas = pow(acciones, estados)
    print("alpha:", alpha, "acciones:", acciones, "estados:", estados, "Total de Politicas:", totalPoliticas)

    CS = []
    for i in range(acciones):
        for j in range(estados):
            auxP = np.squeeze(np.array(P[i][j]))
            auxR = np.squeeze(np.array(R[i][j]))
            auxCS = 0
            for k in range(estados):
                auxCS += auxP[k] * auxR[k]
            # print(auxCS)
            CS.append(auxCS)
    CS = np.reshape(CS, (acciones, estados))
    print("\nCS")
    print(CS)
    print()

    S = []
    for t in range(totalPoliticas):
        pos = to_str(t, acciones)
        pos = ((estados - len(pos)) * "0") + pos
        print(pos)
        pol.append(pos)
        aux = 0
        C = []
        newP = []
        newR = []
        for s in range(estados):
            indexC = int(pos[s])
            auxP = np.squeeze(np.array(P[indexC][s]))
            auxR = np.squeeze(np.array(R[indexC][s]))
            auxC = 0
            # print(auxP)
            # print(auxR)

            # Calcular C'S
            for j in range(estados):
                auxC += auxP[j] * auxR[j]
            C.append(round(auxC, 4))
            newP.append(auxP)
            newR.append(auxR)
        # print(C)

        # Encontrar matrices para evaluar politica
        newP = np.reshape(newP, (estados, estados))
        newR = np.reshape(newR, (estados, estados))

        gauss = newP.copy()

        for i in range(estados):
            auxVs = 0
            for j in range(estados):
                if i == j:
                    aux = 1 - (alpha * gauss[i][j])
                else:
                    aux = -alpha * gauss[i][j]
                gauss[i][j] = aux
            # print(aux)

        # print(gauss)
        V = GEPP(np.copy(gauss), np.copy(C))
        # print(VS)
        Vk = []
        for k in range(acciones):
            # print(CS[k])
            for i in range(estados):
                auxVs = 0
                auxP = np.squeeze(np.array(P[k]))
                # print(auxP)
                for j in range(estados):
                    auxVs += alpha * auxP[i][j] * V[j]
                    # print(alpha, "(", auxP[i][j], "*", V[j], ")")
                auxVs += CS[k][i]
                # print(auxVs)
                Vk.append(auxVs)

        Vk = np.reshape(Vk, (acciones, estados))
        print("Matriz P")
        print(newP)
        print("Matriz R")
        print(newR)
        print("V")
        print(V.round(decimals=4))
        print("C")
        print(C)
        print("Vk mejorado")
        print(Vk.round(decimals=4))

        solOp = []

        for i in range(acciones - 1):
            solPol = []
            solVs = []
            for j in range(estados):
                if Vk[i, j] > Vk[i + 1, j]:
                    solVs.append(Vk[i, j])
                    solPol.append(i)
                    # print(Vk[i, j], ">", Vk[i + 1, j])
                else:
                    solVs.append(Vk[i + 1, j])
                    solPol.append(i + 1)
                    # print(Vk[i, j], ">", Vk[i + 1, j])
            solOp.append(solVs)
            solOp.append(solPol)

            if solPol not in maxS:
                maxS.append(solPol)
            # else:
            #     exit(0)

        solOp = np.reshape(solOp, (acciones, estados))
        print("Solucion Optima")
        print(solOp)
        print(maxS)
        print()


        # if Vk.max() > max(maxS):
        #     maxS.pop()
        #     maxS.append(Vk.max())
        #     print(t)
        #     print(maxS)
        # pos = np.argmax(np.max(Vk, axis=0))
        # maxS.append(Vk.max())
    # print()
    # print("Soluciones")
    # print(maxS)
    # print(pol)
