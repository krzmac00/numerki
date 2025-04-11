import math as mat
import sympy as sp


#wyznaczenie tabeli różnic skończonych
def finite_difference(tab_y):
    nodes = len(tab_y)
    delta_y = [[]]
    delta_y[0] = tab_y
    for counter in range(1, nodes):
        delta_y.append([round(delta_y[counter - 1][i + 1] - delta_y[counter - 1][i], 8)
                        for i in range(nodes - counter)])
    return delta_y

#interpolacja lewej połowy przedziału
def forward_interpolation(tab_x, tab_y):
    h = tab_x[1] - tab_x[0]
    nodes = len(tab_y)
    delta_y = finite_difference(tab_y)
    args_x = sp.Symbol('x')
    q = (args_x - tab_x[0])/h
    coefficients = []
    for i in range(nodes):
        coefficients.append(round(delta_y[i][0]/mat.factorial(i), 4))
    polynomial = [coefficients[0], q * coefficients[1]]
    i = 1
    qt = q
    for i in range(len(coefficients) - 2):
        qt -= 1
        q *= qt
        polynomial.append(q * coefficients[i + 2])
    value = 0
    for item in polynomial:
        value += item
    value = sp.simplify(value)
    return value

#interpolacja prawej połowy przedziału
def backward_interpolation(tab_x, tab_y):
    args_x = sp.Symbol('x')
    h = tab_x[1] - tab_x[0]
    q = (args_x - tab_x[-1])/h
    nodes = len(tab_y)
    delta_y = finite_difference(tab_y)
    coefficients = []
    for i in range(nodes):
        coefficients.append(round(delta_y[i][-1] / mat.factorial(i), 4))
    wielomian = [coefficients[0], q * coefficients[1]]
    i = 1
    qt = q
    for i in range(len(coefficients) - 2):
        qt += 1
        q *= qt
        wielomian.append(q * coefficients[i + 2])
    value = 0
    for item in wielomian:
        value += item
    value = sp.simplify(value)
    return value
