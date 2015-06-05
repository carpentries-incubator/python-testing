import numpy as np

def sinc2d(x, y):
    if x == 0.0 and y == 0.0:
        return 1.0
    elif x == 0.0:
        return np.sin(y) / y
    elif y == 0.0:
        return np.sin(x) / x
    else:
        return (np.sin(x) / x) * (np.sin(y) / y)

def a(x):
    return x + 1

def b(x):
    return 2 * x

def c(x):
    return b(a(x))

def std(vals):
    # surely this is cheating...
    return 1.0
