from abc import ABC, abstractmethod
import math as mat
import numpy as np

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
        return abs(x)

class Homograficzna(Function):

    def __init__(self):
        pass

    def function_at_x(self, x):
        if(x==0): return 1/0.15
        else: return 1/x
    
class Wielomian(Function):

    def __init__ (self, wspolczynniki):
        self.wspolczynniki = wspolczynniki

    def function_at_x(self, x):
        return np.polyval(self.wspolczynniki,x)
    
class Trygonometryczna(Function):

    def __init__ (self):
        pass
    
    def function_at_x(self, x):
        return 2*np.sin(x)


def weight_ex(x):
     return mat.exp(-x)

def GaussLaguerreRule(nodes, function : Function):
   result = 0.0
   xi, Ai = np.polynomial.laguerre.laggauss(nodes)
   for i in range(0, nodes):
       result = result + function.function_at_x(xi[i])*Ai[i]
   return result


def simpson_formula(a, b, function : Function, ex : int):
    h = (b - a) / 2
    if(ex==0):
        result = function.function_at_x(a) + 4 * function.function_at_x(a + h) + function.function_at_x(b)
    else:
        result = weight_ex(a)*function.function_at_x(a) + 4 * weight_ex(a + h)*function.function_at_x(a + h) + weight_ex(b)*function.function_at_x(b)
    result *= h / 3
    return result

def simpson(a, b, precision, function : Function, ex : int):
    step = (b - a) / 2
    last = simpson_formula(a, b, function, ex)
    actual = simpson_formula(a, step, function, ex) + simpson_formula(step, b, function, ex)
    result = actual
    n = 3
    while mat.fabs(actual - last) > precision:
        last = actual
        result = 0
        i = 0
        step = (b - a) / n
        x0 = a
        x1 = x0 + step
        while i < n:
            result += simpson_formula(x0, x1, function, ex)
            x0 = x1
            x1 += step
            i += 1
        actual = result
        n += 1
    return actual

def simpson_infninty(a, precision, function : Function, ex : int):
    b = 10
    result = simpson(a, b, precision, function, ex)
    while(True):
        inc = simpson(b, b+2, precision, function, ex)
        result += inc
        b += 2
        if(inc > precision):
            continue
        else:
            break
    return result
