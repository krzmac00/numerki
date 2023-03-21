import tkinter as tk
import math as mat
import matplotlib.pyplot as plt
import numpy as np
from abc import ABC, abstractmethod

class Funkcja(ABC):

    @abstractmethod
    def __init__ (self):
        pass

    @abstractmethod
    def wartos_w_punkcie_x(self, x):
        pass

class Wielomian(Funkcja):

    def __init__ (self, wspolczynniki):
        self.wspolczynniki = wspolczynniki

    def wartos_w_punkcie_x(self, x):
        return np.polyval(self.wspolczynniki,x)
    
class Wykladnicza(Funkcja):

    def __init__ (self, wsx, potega):
        self.wsx = wsx
        self.potega = potega

    def wartos_w_punkcie_x(self, x):
        return self.wsx*(x**self.potega)
    
class Trygonometryczna(Funkcja):

    def __init__ (self, wsx, wsf):
        self.wsx = wsx
        self.wsf = wsf
    
    def wartos_w_punkcie_x(self, x):
        return self.wsf*mat.sin(x*self.wsx)

class Sinus(Trygonometryczna):
    
    def __init__ (self, wsx, wsf):
        super().__init__(wsx, wsf)

    def wartos_w_punkcie_x(self, x):
        return self.wsf*mat.sin(self.wsx*x)
    
class Cosinus(Trygonometryczna):
    
    def __init__ (self, wsx, wsf):
        super().__init__(wsx, wsf)

    def wartos_w_punkcie_x(self, x):
        return self.wsf*mat.cos(self.wsx*x)

cosinus = Trygonometryczna(2.0,2.0)
print
xpoints = np.arange(-1.0, 3.0, 0.0001)
#ypoints = cosinus.wartos_w_punkcie_x(xpoints)
#ypoints = 2.0*mat.cos(2.0*xpoints)
#x_b = [x0_b]
#x_f = [x0_f]
x = np.arange(0,4*np.pi,0.1)   # start,stop,step
y = np.sin(2.0*x)
#plt.plot(xpoints, ypoints)
plt.plot(x, y)
plt.axhline(y=0, color='k').set_linewidth(0.5)
plt.axvline(x=0, color='k').set_linewidth(0.5)
#plt.plot(x_b, y, label='x0 bisekcja', marker="o", markerfacecolor="red")
#plt.plot(x_f, y, label='x0 regula falsi', marker="o", markerfacecolor="green")
plt.legend()
plt.show()

side="right", expand="true", fill="both"

command= lambda: sprawdz_wybor_zlozenia(zestaw_funkcji, var_gf.get(), var_fg.get())



a = [5.0, 5.0, 0.0, 0.0, 1.0, 0.0, 3.2]

result = "f(x) = "
i=1

for i in a:
    if(a[i-1] != 0 ):
        if (i == 8):
            result += str(a[i-1])
        else:
            result += str(a[i-1]) + "x^" + str(7-i) + " + "

print(result)