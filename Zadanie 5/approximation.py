from abc import ABC, abstractmethod
import numpy as np
import math

def horner(poly, arg_x):
    result = 0
    for item in poly:
        result = result * arg_x + item
    return result

class Function(ABC):

    @abstractmethod
    def __init__ (self):
        pass

    @abstractmethod
    def function_at_x(self, x):
        pass

class Modul(Function):
     
    def __init__ (self):
        pass

    def function_at_x(self, x):
        return abs(2*x - 3)

class Zlozona(Function):

    def __init__(self):
        pass

    def function_at_x(self, x):
        return 2*np.sin(x)**2 - np.cos(x+2)
    
class Wielomian(Function):

    def __init__ (self, wspolczynniki):
        self.wspolczynniki = wspolczynniki

    def function_at_x(self, x):
        return horner(self.wspolczynniki,x)
    
class Trygonometryczna(Function):

    def __init__ (self):
        pass
    
    def function_at_x(self, x):
        return 2*np.sin(x)

def laguerre(deg, x):
    if deg == 0:
        return 1
    elif deg == 1:
        return x - 1
    else:
        l = np.zeros(deg + 1, dtype="double")
        l[0] = 1
        l[1] = x - 1
        for i in range(1, deg):
            l[i + 1] = (((x - (2 * i) - 1) * l[i]) - ((i * i) * l[i - 1]))
        return l[deg]


def laguerre_factors(function: Function, quadlevel, polylevel):
    roots, coefficients = np.polynomial.laguerre.laggauss(quadlevel)
    result = 0.0
    for i in range(0, quadlevel):
        result += function.function_at_x(roots[i]) * coefficients[i] * laguerre(polylevel, roots[i])

    return result / (math.factorial(polylevel) ** 2)


def mean_error(actual_y, approx_y):
    for i in range(len(actual_y)):
        actual_y[i] = abs(actual_y[i] - approx_y[i])

    return np.mean(actual_y)