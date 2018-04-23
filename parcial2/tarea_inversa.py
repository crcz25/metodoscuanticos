import numpy
import math


def f1(x):
    return (1 / 2) * (x - 2)


def f2(x):
    return (1 / 2) * (2 - (x / 3))


if __name__ == '__main__':
    a1 = 2
    b1 = 3

    a2 = 2
    b2 = 6

    r1 = 0
    x1 = math.sqrt(4 * r1) + 2
    print("[a1,b1]: [%d,%d] ; r: %f ; x1: %f" % (a1, b1, r1, x1))

    r2 = 2 / 3
    x2 = 6 + math.sqrt(9 - 12 * r2)
    print("[a2,b2]: [%d,%d] ; r: %f ; x2: %f" % (a2, b2, r2, x2))






