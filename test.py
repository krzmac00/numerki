import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from abc import ABC, abstractmethod

a = [5.0, 5.0, 3.3, -3.2, 1.0, 0.0, 3.2]

result = "f(x) = "


for i in range(0,7):
    if(a[i] != 0 ):
        if (i == 6):
            result += str(a[i])
        else:
            result += str(a[i]) + "x^" + str(6-i) + " + "

print(result)