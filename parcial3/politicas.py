from gauss import GEPP
import numpy as np

if __name__ == "__main__":
    # Load files
    P = []
    R = []
    with open("p.txt", "r") as f:
        for line in f:
            P.append(np.matrix(line))

    with open("r.txt", "r") as f:
        for line in f:
            R.append(np.matrix(line))


    # Calcular C(S,i)
    C = []
    for i in range(len(P)):
        auxC = 0
        for j in range(len(P[0])):
            auxP = P[i]
            auxR = R[i]
            # print(auxP[j])
            # print(auxR[j])
            # auxC = float(np.dot((auxP - auxR)**2, w.T))
            # for k in range(auxP[j].shape[j]):
            #     print(k)
            # for k in range(len(auxP[j])):
            #     auxC += auxP[k] * auxR[k]
            #     print(auxC)
        # C.append(auxC)

    # print(C)
    # print(P[0])
    # print(R[0])

    # A = np.array([
    #     [4, 2, -2],
    #     [2, 8, 4],
    #     [30, 12, -4]], dtype='f')
    # b = np.array([
    #     [10],
    #     [32],
    #     [24]], dtype='float')
    # # print(GENP(np.copy(A), np.copy(b)))
    # res = GEPP(A, b)
    #
    # print(res)
