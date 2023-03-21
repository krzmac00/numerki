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
        pass

class Sinus(Trygonometryczna):
    
    def __init__ (self, wsx, wsf):
        super().__init__(wsx, wsf)

    def wartos_w_punkcie_x(self, x):
        return mat.sin(self.wsf*mat.sin(self.wsx*x))
    
class Cosinus(Trygonometryczna):
    
    def __init__ (self, wsx, wsf):
        super().__init__(wsx, wsf)

    def wartos_w_punkcie_x(self, x):
        return mat.sin(self.wsf*mat.cos(self.wsx*x))
    

def bisekcja_iteracje(funkcja: Funkcja, a: float, b: float, iteracje: int):
    for i in range(iteracje):
        srodek = (a + b)/2.0
        if(funkcja.wartos_w_punkcie_x(srodek) == 0.0):
            break
        if (np.sign(funkcja.wartos_w_punkcie_x(a)) * np.sign(funkcja.wartos_w_punkcie_x(srodek))) < 0.0:
            b = srodek
        else:
            a = srodek
    return srodek

def bisekcja_dokladnosc(funkcja: Funkcja, a: float, b: float, epsilon: float):
    poprzedni_srodek = 0.0
    while(True):
        srodek = (a + b)/2.0
        if(np.abs((srodek - poprzedni_srodek)) < epsilon):
            break
        if(funkcja.wartos_w_punkcie_x(srodek) == 0.0):
            break
        if (np.sign(funkcja.wartos_w_punkcie_x(a)) * np.sign(funkcja.wartos_w_punkcie_x(srodek))) < 0.0:
            b = srodek
        else:
            a = srodek
        poprzedni_srodek = srodek
    return srodek

def falsi_iteracje(funkcja: Funkcja, a: float, b: float, iteracje: int):
    for i in range(iteracje):
        x = a - funkcja.wartos_w_punkcie_x(a) * (b - a)/(funkcja.wartos_w_punkcie_x(b) - funkcja.wartos_w_punkcie_x(a))
        if(funkcja.wartos_w_punkcie_x(x) == 0.0):
            break
        if (np.sign(funkcja.wartos_w_punkcie_x(a)) * np.sign(funkcja.wartos_w_punkcie_x(x))) < 0.0:
            b = x
        else:
            a = x
    return x

def falsi_dokladnosc(funkcja: Funkcja, a: float, b: float, epsilon: float):
    poprzedni_x = 0.0
    while(True):
        x = a - funkcja.wartos_w_punkcie_x(a) * (b - a)/(funkcja.wartos_w_punkcie_x(b) - funkcja.wartos_w_punkcie_x(a))
        if(np.abs((x - poprzedni_x)) < epsilon):
            break
        if(funkcja.wartos_w_punkcie_x(x) == 0.0):
            break
        if (np.sign(funkcja.wartos_w_punkcie_x(a)) * np.sign(funkcja.wartos_w_punkcie_x(x))) < 0.0:
            b = x
        else:
            a = x
        poprzedni_x = x
    return x

############################################################ POBIERANIE DANYCH OD UŻYTKOWNIKA ############################################################

#WIELOMIAN

def wyswietl_wyniki(funkcja: Funkcja, poczatek: float, koniec: float, iteracje: int, dokladnosc: float):
    clear_window()
    f1 = tk.Frame(window, pady=5)
    f_b = tk.Frame(window)
    f_f = tk.Frame(window)
    if(iteracje == 0):
        kryterium_zatrzymania = tk.Label(f1, font=('Helvetica bold', 12), text='Kryterium zatrzymania - dokładność: ')
        kryterium_zatrzymania_wartosc = tk.Label(f1, font=('Helvetica bold', 12), text=str(dokladnosc))
        x0_b = bisekcja_dokladnosc(funkcja, poczatek, koniec, dokladnosc)
        x0_f = falsi_dokladnosc(funkcja, poczatek, koniec, dokladnosc)
        x0b_wyswietl = tk.Label(f_b, bg='white', width=50, text=str(x0_b))
        x0f_wyswietl = tk.Label(f_f, bg='white', width=50, text=str(x0_f))
    else:
        kryterium_zatrzymania = tk.Label(f1, font=('Helvetica bold', 12), text='Kryterium zatrzymania - liczba iteracji: ')
        kryterium_zatrzymania_wartosc = tk.Label(f1, font=('Helvetica bold', 12), text=str(iteracje))
        x0_b = bisekcja_iteracje(funkcja, poczatek, koniec, iteracje)
        x0_f = falsi_iteracje(funkcja, poczatek, koniec, iteracje)
    
    
    l = tk.Label(window, bg='white', width=50, text='WYNIKI', font=('Helvetica bold', 14))
    l.pack()
    kryterium_zatrzymania.grid(row=0, column=0)
    kryterium_zatrzymania_wartosc.grid(row=0, column=1)
    f1.pack()

    l_bisekcja = tk.Label(window, bg='white', width=50, text='METODA BISEKCJI', font=('Helvetica bold', 14))
    l_bisekcja.pack()

    tk.Label(f_b, bg='white', width=50, text='Miejsce zerowe: ').grid(row=0,column=0)
    x0b_wyswietl.grid(row=0,column=1)
    f_b.pack()

    l_falsi = tk.Label(window, bg='white', width=50, text='METODA REGULA FALSI', font=('Helvetica bold', 14))
    l_falsi.pack()
    
    tk.Label(f_f, bg='white', width=50, text='Miejsce zerowe: ').grid(row=0,column=0)
    x0f_wyswietl.grid(row=0,column=1)
    f_f.pack()

    button_wyjdz = tk.Button(window, text='WYJDŹ', font=('Helvetica bold', 12),
                                        command=window.destroy)
    button_wyjdz.pack(pady=10)

def zatwierdz_wybor_kryterium_wielomian(wspolczynniki, poczatek, koniec, var_iteracje, var_dokladnosc, iteracje, dokladnosc):
    wielomian = Wielomian(wspolczynniki)
    if((var_iteracje == 0 and var_dokladnosc == 0) or (var_iteracje == 1 and var_dokladnosc == 1)):
        l = tk.Label(window, fg='red', width=50, text='Wybierz jedno kryterium!')
        l.pack()
    elif(var_iteracje == 1):
        try:
            int_iteracje = int(iteracje)
            if(int_iteracje <= 0):
                raise ValueError("ValueError")
            wyswietl_wyniki(wielomian, poczatek, koniec, int_iteracje, 0)
        except ValueError:
            lp = tk.Label(window, fg='red', width=60, text='Podaj wartość calkowiotliczbowa większą od zera!')
            lp.pack()
    else:
        try:
            float_dokladnosc = float(dokladnosc)
            if(float_dokladnosc <= 0):
                raise ValueError("ValueError")
            wyswietl_wyniki(wielomian, poczatek, koniec, 0, float_dokladnosc)
        except ValueError:
            lp = tk.Label(window, fg='red', width=80, text='Podaj wartość zmiennoprzecinkową float większą od zera!')
            lp.pack()

def wybor_kryterium_wielomian(wspolczynniki, poczatek: float, koniec: float):
    clear_window()
    l = tk.Label(window, bg='white', width=50, text='Wybierz kryterium zatrzymania', font=('Helvetica bold', 14))
    l.pack()
    var_iteracje = tk.IntVar()
    var_dokladnosc = tk.IntVar()
    f = tk.Frame(window, pady=5)
    check_iteracje = tk.Checkbutton(f, text='liczba iteracji:', variable=var_iteracje, onvalue=1, offvalue=0)
    check_iteracje.grid(row=0, column=0, padx=(10,10))
    iteracje = tk.Entry(f, width=4)
    iteracje.grid(row=0, column=1)
    check_dokladnosc = tk.Checkbutton(f, text='dokładność:', variable=var_dokladnosc, onvalue=1, offvalue=0)
    check_dokladnosc.grid(row=1, column=0, padx=(10,10))
    dokladnosc = tk.Entry(f, width=4)
    dokladnosc.grid(row=1, column=1)
    f.pack(anchor='w')
    button_zatwierdz_wybor = tk.Button(window, text='ZATWIERDŹ', font=('Helvetica bold', 12),
                                        command=lambda: zatwierdz_wybor_kryterium_wielomian(
                                        wspolczynniki, poczatek, koniec, var_iteracje.get(), var_dokladnosc.get(), iteracje.get(), dokladnosc.get()))
    button_zatwierdz_wybor.pack(pady=10)

def zatwierdz_przedzial_wielomian(wspolczynniki, poczatek, koniec):
    try:
        float_poczatek = float(poczatek)
    except ValueError:
        lp = tk.Label(window, fg='red', width=80, text='Podaj wartość zmiennoprzecinkową float, separatorem musi być kropka.')
        lp.pack()
    try:
        float_koniec = float(koniec)
    except ValueError:
        lk = tk.Label(window, fg='red', width=80, text='Podaj wartość zmiennoprzecinkową float, separatorem musi być kropka.')
        lk.pack()
    if ((np.polyval(wspolczynniki, float_poczatek) * np.polyval(wspolczynniki,float_koniec)) > 0 ):
        l = tk.Label(window, fg='red', width=80, text='BRAK miejsca zerowego w podanym przedziale - PODAJ INNY PRZEDZIAŁ')
        l.pack()
    else:
       if(float_poczatek > float_koniec):
           float_poczatek, float_koniec = float_koniec, float_poczatek
       wybor_kryterium_wielomian(wspolczynniki, float_poczatek, float_koniec)

def podaj_przedzial_wielomian(wspolczynniki):
    clear_window()
    l = tk.Label(window, bg='white', width=50, text='Podaj granice przedziału', font=('Helvetica bold', 14))
    l.pack()
    fpoczatek = tk.Frame(window, pady=5)
    tk.Label(fpoczatek, padx=1, text="Początek przedziału").grid(row=0, column=0)
    poczatek = tk.Entry(fpoczatek, width=4)
    poczatek.grid(row=0, column=1, ipady=1)
    fpoczatek.pack()
    fkoniec = tk.Frame(window, pady=5)
    tk.Label(fkoniec, padx=1, text="Koniec przedziału").grid(row=0, column=0)
    koniec = tk.Entry(fkoniec, width=4)
    koniec.grid(row=0, column=1, ipady=1)
    fkoniec.pack()
    button_zatwierdz_przedzial_wielomian = tk.Button(window, text='ZATWIERDŹ', font=('Helvetica bold', 12), 
                                                     command= lambda: zatwierdz_przedzial_wielomian(wspolczynniki, poczatek.get(), koniec.get()))
    button_zatwierdz_przedzial_wielomian.pack(pady=10)


#FUNKCJA WYKŁADNICZA

def bisekcja_wykladnicza():
    return

def oblicz_wykladnicza(wsx, potega, poczatek, koniec, iteracje, dokladnosc):
    return

def zatwierdz_wybor_kryterium_wykladnicza(wsx, potega, poczatek, koniec, var_iteracje, var_dokladnosc, iteracje, dokladnosc):
    if((var_iteracje == 0 and var_dokladnosc == 0) or (var_iteracje == 1 and var_dokladnosc == 1)):
        l = tk.Label(window, fg='red', width=50, text='Wybierz jedno kryterium!')
        l.pack()
    elif(var_iteracje == 1):
        try:
            int_iteracje = int(iteracje)
            if(int_iteracje <= 0):
                raise ValueError("ValueError")
            oblicz_wykladnicza(wsx, potega, poczatek, koniec, int_iteracje, 0)
        except ValueError:
            lp = tk.Label(window, fg='red', width=80, text='Podaj wartosc calkowiotliczbowa większą od zera!')
            lp.pack()
    else:
        try:
            float_dokladnosc = float(dokladnosc)
            if(float_dokladnosc <= 0):
                raise ValueError("ValueError")
            oblicz_wykladnicza(wsx, potega, poczatek, koniec, 0, float_dokladnosc)
        except ValueError:
            lp = tk.Label(window, fg='red', width=80, text='Podaj wartosc zmiennoprzecinkową float większą od zera!')
            lp.pack()

def wybor_kryterium_wykladnicza(wsx, potega, poczatek, koniec):
    clear_window()
    l = tk.Label(window, bg='white', width=50, text='Wybierz kryterium zatrzymania', font=('Helvetica bold', 14))
    l.pack()
    var_iteracje = tk.IntVar()
    var_dokladnosc = tk.IntVar()
    f = tk.Frame(window, pady=5)
    check_iteracje = tk.Checkbutton(f, text='liczba iteracji:', variable=var_iteracje, onvalue=1, offvalue=0)
    check_iteracje.grid(row=0, column=0, padx=(10,10))
    iteracje = tk.Entry(f, width=4)
    iteracje.grid(row=0, column=1)
    check_dokladnosc = tk.Checkbutton(f, text='dokladnosc:', variable=var_dokladnosc, onvalue=1, offvalue=0)
    check_dokladnosc.grid(row=1, column=0, padx=(10,10))
    dokladnosc = tk.Entry(f, width=4)
    dokladnosc.grid(row=1, column=1)
    f.pack(anchor='w')
    button_zatwierdz_wybor = tk.Button(window, text='ZATWIERDŹ', font=('Helvetica bold', 12),
                                        command=lambda: zatwierdz_wybor_kryterium_wykladnicza(
                                        wsx, potega, poczatek, koniec, var_iteracje.get(), var_dokladnosc.get(), iteracje.get(), dokladnosc.get()))
    button_zatwierdz_wybor.pack(pady=10)

def zatwierdz_przedzial_wykladnicza(wsx, potega, poczatek, koniec):
    try:
        float_poczatek = float(poczatek)
    except ValueError:
        lp = tk.Label(window, fg='red', width=80, text='Podaj wartość zmiennoprzecinkową float, separatorem musi być kropka.')
        lp.pack()
    try:
        float_koniec = float(koniec)
    except ValueError:
        lk = tk.Label(window, fg='red', width=80, text='Podaj wartość zmiennoprzecinkową float, separatorem musi być kropka.')
        lk.pack()
    if ((float_poczatek**potega) * (float_koniec**potega)) > 0:
        l = tk.Label(window, fg='red', width=80, text='BRAK miejsca zerowego w podanym przedziale - PODAJ INNY PRZEDZIAŁ')
        l.pack()
    else:
       if(float_poczatek > float_koniec):
           float_poczatek, float_koniec = float_koniec, float_poczatek
       wybor_kryterium_wykladnicza(wsx, potega, poczatek, koniec)

def podaj_przedzial_wykladnicza(wsx, potega):
    clear_window()
    l = tk.Label(window, bg='white', width=50, text='Podaj granice przedziału', font=('Helvetica bold', 14))
    l.pack()
    fpoczatek = tk.Frame(window, pady=5)
    tk.Label(fpoczatek, padx=1, text="Początek przedziału").grid(row=0, column=0)
    poczatek = tk.Entry(fpoczatek, width=4)
    poczatek.grid(row=0, column=1, ipady=1)
    fpoczatek.pack()
    fkoniec = tk.Frame(window, pady=5)
    tk.Label(fkoniec, padx=1, text="Koniec przedziału").grid(row=0, column=0)
    koniec = tk.Entry(fkoniec, width=4)
    koniec.grid(row=0, column=1, ipady=1)
    fkoniec.pack()
    button_zatwierdz_przedzial_wielomian = tk.Button(window, text='ZATWIERDŹ', font=('Helvetica bold', 12), 
                                                     command= lambda: zatwierdz_przedzial_wykladnicza(wsx, potega, poczatek.get(), koniec.get()))
    button_zatwierdz_przedzial_wielomian.pack(pady=10)

#FUNKCJA TRYGONOMETRYCZNA

def zatwierdz_wybor_kryterium_trygonometryczna(funkcja, wsx, wsf, poczatek, koniec, var_iteracje, var_dokladnosc, iteracje, dokladnosc):
    if((var_iteracje == 0 and var_dokladnosc == 0) or (var_iteracje == 1 and var_dokladnosc == 1)):
        l = tk.Label(window, fg='red', width=50, text='Wybierz jedno kryterium!')
        l.pack()
        return
    elif(var_iteracje == 1):
        try:
            int_iteracje = int(iteracje)
            if(int_iteracje <= 0):
                raise ValueError("ValueError")
            oblicz_trygonometryczna(funkcja, wsx, wsf, poczatek, koniec, int_iteracje, 0)
        except ValueError:
            lp = tk.Label(window, fg='red', width=80, text='Podaj wartość calkowiotliczbowa większą od zera!')
            lp.pack()
            return
    else:
        try:
            float_dokladnosc = float(dokladnosc)
            if(float_dokladnosc <= 0):
                raise ValueError("ValueError")
            oblicz_wielomian(funkcja, wsx, wsf, poczatek, koniec, 0, float_dokladnosc)
        except ValueError:
            lp = tk.Label(window, fg='red', width=80, text='Podaj wartość zmiennoprzecinkową float większą od zera!')
            lp.pack()

def wybor_kryterium_trygonometryczna(funkcja, wsx, wsf, poczatek, koniec):
    clear_window()
    l = tk.Label(window, bg='white', width=50, text='Wybierz kryterium zatrzymania', font=('Helvetica bold', 14))
    l.pack()
    var_iteracje = tk.IntVar()
    var_dokladnosc = tk.IntVar()
    f = tk.Frame(window, pady=5)
    check_iteracje = tk.Checkbutton(f, text='liczba iteracji:', variable=var_iteracje, onvalue=1, offvalue=0)
    check_iteracje.grid(row=0, column=0, padx=(10,10))
    iteracje = tk.Entry(f, width=4)
    iteracje.grid(row=0, column=1)
    check_dokladnosc = tk.Checkbutton(f, text='dokladnosc:', variable=var_dokladnosc, onvalue=1, offvalue=0)
    check_dokladnosc.grid(row=1, column=0, padx=(10,10))
    dokladnosc = tk.Entry(f, width=4)
    dokladnosc.grid(row=1, column=1)
    f.pack(anchor='w')
    button_zatwierdz_wybor = tk.Button(window, text='ZATWIERDŹ', font=('Helvetica bold', 12),
                                        command=lambda: zatwierdz_wybor_kryterium_trygonometryczna(
                                        funkcja, wsx, wsf, poczatek, koniec, var_iteracje.get(), var_dokladnosc.get(), iteracje.get(), dokladnosc.get()))
    button_zatwierdz_wybor.pack(pady=10)

def zatwierdz_przedzial_trygonometryczna(funkcja, wsx, wsf, poczatek, koniec):
    try:
        float_poczatek = float(poczatek)
        float_koniec = float(koniec)
    except ValueError:
        lp = tk.Label(window, fg='red', width=80, text='Podaj wartość zmiennoprzecinkową float, separatorem musi być kropka.')
        lp.pack()
        return
    if(funkcja == "sinus"):
        if (mat.sin(wsx*float_poczatek) * mat.sin(wsx*float_koniec)) > 0:
            l = tk.Label(window, fg='red', width=80, text='BRAK miejsca zerowego w podanym przedziale - PODAJ INNY PRZEDZIAŁ')
            l.pack()
        else:
            if(float_poczatek > float_koniec):
                float_poczatek, float_koniec = float_koniec, float_poczatek
            wybor_kryterium_trygonometryczna(funkcja, wsx, wsf, poczatek, koniec)
    else:
        if (mat.cos(wsx*float_poczatek) * mat.cos(wsx*float_koniec)) > 0:
            l = tk.Label(window, fg='red', width=80, text='BRAK miejsca zerowego w podanym przedziale - PODAJ INNY PRZEDZIAŁ')
            l.pack()
        else:
            if(float_poczatek > float_koniec):
                float_poczatek, float_koniec = float_koniec, float_poczatek
            wybor_kryterium_trygonometryczna(funkcja, wsx, wsf, poczatek, koniec)

def podaj_przedzial_trygonometryczna(funkcja, wsx, wsf):
    clear_window()
    l = tk.Label(window, bg='white', width=50, text='Podaj granice przedziału', font=('Helvetica bold', 14))
    l.pack()
    fpoczatek = tk.Frame(window, pady=5)
    tk.Label(fpoczatek, padx=1, text="Początek przedziału").grid(row=0, column=0)
    poczatek = tk.Entry(fpoczatek, width=4)
    poczatek.grid(row=0, column=1, ipady=1)
    fpoczatek.pack()
    fkoniec = tk.Frame(window, pady=5)
    tk.Label(fkoniec, padx=1, text="Koniec przedziału").grid(row=0, column=0)
    koniec = tk.Entry(fkoniec, width=4)
    koniec.grid(row=0, column=1, ipady=1)
    fkoniec.pack()
    button_zatwierdz_przedzial_wielomian = tk.Button(window, text='ZATWIERDŹ', font=('Helvetica bold', 12), 
                                                     command= lambda: zatwierdz_przedzial_trygonometryczna(funkcja, wsx, wsf, poczatek.get(), koniec.get()))
    button_zatwierdz_przedzial_wielomian.pack(pady=10)

def clear_window():
    for widgets in window.winfo_children():
        widgets.destroy()

########################################################################## MAIN ##########################################################################

#stworzenie okna
window = tk.Tk()
window.title('Metody numeryczne - zadanie 1')
window.geometry('500x400')
var_wielomian = tk.IntVar()
var_wykladnicza = tk.IntVar()
var_trygonometryczna = tk.IntVar()
var_zlozenie = tk.IntVar()
l = tk.Label(window, bg='white', width=50, text='Wybierz funkcję', font=('Helvetica bold', 14))
button_zatwierdz = tk.Button(window, text='ZATWIERDŹ', font=('Helvetica bold', 12), state='disabled', command=zatwierdz_wybor_funkcji)

wybor_funkcji()

 
window.mainloop()