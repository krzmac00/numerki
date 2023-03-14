from numpy import polyval
import math as mat
import matplotlib.pyplot as plt
import numpy as np

'''
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

plt.show()'''

p = [0, 0, 1.2, 2.56 , 3.90]
d =[1.2,2.56,3.90]
print(polyval(p, 2))
print(polyval(d, 2))
#print(2**8)