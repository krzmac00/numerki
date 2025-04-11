import matplotlib.pyplot as plt
import numpy as np
import math as mat

def wielomian1(x):
    return np.polyval([2,-16,32,-54], x)

def trygonometryczna1(x):
    return 2*np.sin(0.5*np.cos(x))

def wykladnicza(x):
    return 2**x*mat.exp(x)+1

def bisekcja_iteracje(funkcja, a: float, b: float, iteracje: int):
    poprzedni_srodek = 0.0
    for i in range(iteracje):
        srodek = (a + b)/2.0
        if(funkcja(srodek) == 0.0):
            break
        if (np.sign(funkcja(a)) * np.sign(funkcja(srodek))) < 0.0:
            b = srodek
        else:
            a = srodek
        dokladnosc = np.abs(srodek - poprzedni_srodek)
        poprzedni_srodek = srodek
    return srodek, dokladnosc

def bisekcja_dokladnosc(funkcja, a: float, b: float, epsilon: float):
    poprzedni_srodek = 0.0
    iteracje = 0
    while(True):
        iteracje += 1
        srodek = (a + b)/2.0
        dokladnosc = np.abs(srodek - poprzedni_srodek)
        if(dokladnosc < epsilon):
            break
        if(funkcja(srodek) == 0.0):
            break
        if (np.sign(funkcja(a)) * np.sign(funkcja(srodek))) < 0.0:
            b = srodek
        else:
            a = srodek
        poprzedni_srodek = srodek
    return srodek, dokladnosc, iteracje

def falsi_iteracje(funkcja, a: float, b: float, iteracje: int):
    poprzedni_x = 0.0
    for i in range(iteracje):
        x = a - funkcja(a) * (b - a)/(funkcja(b) - funkcja(a))
        if(funkcja(x) == 0.0):
            break
        if (np.sign(funkcja(a)) * np.sign(funkcja(x))) < 0.0:
            b = x
        else:
            a = x
        dokladnosc = np.abs(x - poprzedni_x)
        poprzedni_x = x
    return x, dokladnosc

def falsi_dokladnosc(funkcja, a: float, b: float, epsilon: float):
    poprzedni_x = 0.0
    iteracje = 0
    while(True):
        iteracje += 1
        x = a - funkcja(a) * (b - a)/(funkcja(b) - funkcja(a))
        dokladnosc = np.abs(x - poprzedni_x)
        if(dokladnosc < epsilon):
            break
        if(funkcja(x) == 0.0):
            break
        if (np.sign(funkcja(a)) * np.sign(funkcja(x))) < 0.0:
            b = x
        else:
            a = x
        poprzedni_x = x
    return x, dokladnosc, iteracje


miejsca_po_przecinku_bisekcja=[]
miejsca_po_przecinku_falsi=[]
iteracje = np.arange(1,31,1)

for i in range(1,31):
    miejsca_po_przecinku_bisekcja.append(bisekcja_iteracje(wielomian1,1.0,7.0,i)[1])
    miejsca_po_przecinku_falsi.append(falsi_iteracje(wielomian1,1.0,7.0,i)[1])

plt.plot(iteracje, miejsca_po_przecinku_bisekcja, 'o', label='bisekcja', color='blue')
plt.plot(iteracje, miejsca_po_przecinku_falsi, 'o', label='reguła falsi', color='red')
plt.gca().invert_yaxis()
plt.title("f(x) = 2x^3-16x^2+32x-54\nprzedział: <1; 7>")
plt.xlabel("liczba iteracji")
plt.ylabel("dokładność")
plt.legend()
plt.show()

zadana_dokladnosc = [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001, 0.00000001, 0.00000001, 0.000000001]
liczba_iteracji_bisekcja = []
liczba_iteracji_falsi = []

for i in range(0,10):
    liczba_iteracji_bisekcja.append(bisekcja_dokladnosc(wielomian1,1.0,7.0,zadana_dokladnosc[i])[2])
    liczba_iteracji_falsi.append(falsi_dokladnosc(wielomian1,1.0,7.0,zadana_dokladnosc[i])[2])

bars = ('0.1', '0.01', '0.001', '0.0001', '10^-5', '10^-6', '10^-7', '10^-8', '10^-9', '10^-10')
plt.figure(figsize=(10,5))
 
# Create bars
plt.bar(bars, liczba_iteracji_bisekcja, color = 'blue', alpha=0.5, label = 'bisekcja')
plt.bar(bars, liczba_iteracji_falsi, color = 'red', alpha=0.5, label = 'regula falsi')
  
# Create names on the x-axis
plt.xticks(bars, bars)
plt.legend(frameon=False)
plt.xlabel('dokładność', fontsize=12, color='#323232')
plt.ylabel('liczba iteracji', fontsize=12, color='#323232')
plt.title("f(x) = 2x^3-16x^2+32x-54\nprzedział: <1; 7>")
plt.show()

#########################################################################################################################

miejsca_po_przecinku_bisekcja=[]
miejsca_po_przecinku_falsi=[]
iteracje = np.arange(1,31,1)

for i in range(1,31):
    miejsca_po_przecinku_bisekcja.append(bisekcja_iteracje(trygonometryczna1,-1.0,3.0,i)[1])
    miejsca_po_przecinku_falsi.append(falsi_iteracje(trygonometryczna1,-1.0,3.0,i)[1])

plt.plot(iteracje, miejsca_po_przecinku_bisekcja, 'o', label='bisekcja', color='blue')
plt.plot(iteracje, miejsca_po_przecinku_falsi, 'o', label='reguła falsi', color='red')
plt.gca().invert_yaxis()
plt.title("f(x) = 2sin(0.5cos(x))\nprzedział: <-1; 3>")
plt.xlabel("liczba iteracji")
plt.ylabel("dokładność")
plt.legend()
plt.show()

zadana_dokladnosc = [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001, 0.00000001, 0.00000001, 0.000000001]
liczba_iteracji_bisekcja = []
liczba_iteracji_falsi = []

for i in range(0,10):
    liczba_iteracji_bisekcja.append(bisekcja_dokladnosc(trygonometryczna1,-1.0,3.0,zadana_dokladnosc[i])[2])
    liczba_iteracji_falsi.append(falsi_dokladnosc(trygonometryczna1,-1.0,3.0,zadana_dokladnosc[i])[2])

bars = ('0.1', '0.01', '0.001', '0.0001', '10^-5', '10^-6', '10^-7', '10^-8', '10^-9', '10^-10')
plt.figure(figsize=(10,5))
 
# Create bars
plt.bar(bars, liczba_iteracji_bisekcja, color = 'blue', alpha=0.5, label = 'bisekcja')
plt.bar(bars, liczba_iteracji_falsi, color = 'red', alpha=0.5, label = 'regula falsi')
  
# Create names on the x-axis
plt.xticks(bars, bars)
plt.legend(frameon=False)
plt.xlabel('dokładność', fontsize=12, color='#323232')
plt.ylabel('liczba iteracji', fontsize=12, color='#323232')
plt.title("f(x) = 2sin(0.5cos(x))\nprzedział: <-1; 3>")
plt.show()

#########################################################################################################################

miejsca_po_przecinku_bisekcja=[]
miejsca_po_przecinku_falsi=[]
iteracje = np.arange(1,31,1)

for i in range(1,31):
    miejsca_po_przecinku_bisekcja.append(bisekcja_iteracje(wykladnicza,-3.0,1.0,i)[1])
    miejsca_po_przecinku_falsi.append(falsi_iteracje(wykladnicza,-3.0,1.0,i)[1])

plt.plot(iteracje, miejsca_po_przecinku_bisekcja, 'o', label='bisekcja', color='blue')
plt.plot(iteracje, miejsca_po_przecinku_falsi, 'o', label='reguła falsi', color='red')
plt.gca().invert_yaxis()
plt.title("f(x) = 2^x - e^x + 1\nprzedział: <-3; 1>")
plt.xlabel("liczba iteracji")
plt.ylabel("dokładność")
plt.legend()
plt.show()

zadana_dokladnosc = [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001, 0.00000001, 0.00000001, 0.000000001]
liczba_iteracji_bisekcja = []
liczba_iteracji_falsi = []

for i in range(0,10):
    liczba_iteracji_bisekcja.append(bisekcja_dokladnosc(wykladnicza,-3.0,1.0,zadana_dokladnosc[i])[2])
    liczba_iteracji_falsi.append(falsi_dokladnosc(wykladnicza,-3.0,1.0,zadana_dokladnosc[i])[2])

bars = ('0.1', '0.01', '0.001', '0.0001', '10^-5', '10^-6', '10^-7', '10^-8', '10^-9', '10^-10')
plt.figure(figsize=(10,5))
 
# Create bars
plt.bar(bars, liczba_iteracji_bisekcja, color = 'blue', alpha=0.5, label = 'bisekcja')
plt.bar(bars, liczba_iteracji_falsi, color = 'red', alpha=0.5, label = 'regula falsi')
  
# Create names on the x-axis
plt.xticks(bars, bars)
plt.legend(frameon=False)
plt.xlabel('dokładność', fontsize=12, color='#323232')
plt.ylabel('liczba iteracji', fontsize=12, color='#323232')
plt.title("f(x) = 2^x - e^x + 1\nprzedział: <-3; 1>")
plt.show()