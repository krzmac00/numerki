from numpy import polyval
import math as mat
import matplotlib.pyplot as plt
import numpy as np


a = float(input())
b = float(input())
c = float(input())
t = np.arange(a, b, 0.01)
s = (t**c)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='x', ylabel='y',
       title= 'x^' + str(c))
ax.grid()

plt.show()

#p = [1, 2 , 3]
#print(polyval(p, 2))
#print(2**8)