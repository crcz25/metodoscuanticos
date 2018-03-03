import numpy
import math


def f(a, b):
    return 1 / (b - a)


if __name__ == '__main__':
    a = int(input("a: "))
    b = int(input("b: "))

    for i in range(100):
        r = numpy.random.uniform(0, 1)
        x1 = -r * (a - b) + a
        x2 = a + r * (b - a)
        print("[a,b]: [%d,%d] ; r: %f ; x1: %f ; x2: %f" % (a, b, r, x1, x2))






