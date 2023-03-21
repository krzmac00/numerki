import tkinter as tk
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
    @abstractmethod
    def get_nazwa(self):
        pass

class Zlozenie(Funkcja):

    def __init__ (self, funkcja_zewnetrzna: Funkcja, funkcja_wewnetrzna: Funkcja):
        self.funkcja_zewnetrzna = funkcja_zewnetrzna
        self.funkcja_wewnetrzna = funkcja_wewnetrzna

    def wartos_w_punkcie_x(self, x):
        return self.funkcja_zewnetrzna.wartos_w_punkcie_x(self.funkcja_wewnetrzna.wartos_w_punkcie_x(x))
    
    def get_nazwa(self):
        return "y = g(f(x)), g = " + self.funkcja_zewnetrzna.get_nazwa() + ", f = " + self.funkcja_wewnetrzna.get_nazwa()

class Wielomian(Funkcja):

    def __init__ (self, wspolczynniki):
        self.wspolczynniki = wspolczynniki

    def wartos_w_punkcie_x(self, x):
        return np.polyval(self.wspolczynniki,x)
    
    def get_nazwa(self):
        result = "f(x) = "
        for i in range(0,7):
            if(self.wspolczynniki[i] != 0 ):
                if (i == 6):
                    result += str(self.wspolczynniki[i])
                else:
                    result += str(self.wspolczynniki[i]) + "x^" + str(6-i) + " + "

        return result
    
class Wykladnicza(Funkcja):

    def __init__ (self, wsx, przesuniecie):
        self.wsx = wsx
        self.przesuniecie = przesuniecie

    def wartos_w_punkcie_x(self, x):
        return self.wsx**x - self.przesuniecie
    
    def get_nazwa(self):
        return "f(x) = " + str(self.wsx) + "^x - " + str(self.przesuniecie)
    
class Trygonometryczna(Funkcja):

    def __init__ (self, wsx, wsf):
        self.wsx = wsx
        self.wsf = wsf
    
    def wartos_w_punkcie_x(self, x):
        pass

    def get_nazwa(self):
        pass

class Sinus(Trygonometryczna):
    
    def __init__ (self, wsx, wsf):
        super().__init__(wsx, wsf)

    def wartos_w_punkcie_x(self, x):
        return self.wsf*np.sin(self.wsx*x)

    def get_nazwa(self):
        return "f(x) = " + str(self.wsf) + "sin(" + str(self.wsx) + ")"
    
class Cosinus(Trygonometryczna):
    
    def __init__ (self, wsx, wsf):
        super().__init__(wsx, wsf)

    def wartos_w_punkcie_x(self, x):
        return self.wsf*np.cos(self.wsx*x)
    
    def get_nazwa(self):
        return "f(x) = " + str(self.wsf) + "cos(" + str(self.wsx) + ")"

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
def zatwierdz_wspolczynniki_wielomianu(ws6, ws5, ws4, ws3, ws2, ws1, ws0):
    try:
        #6
        if (len(ws6) == 0):
            float_ws6 = 0.0
        else:
            float_ws6 = float(ws6)
        #5
        if (len(ws5) == 0):
            float_ws5 = 0.0
        else:
            float_ws5 = float(ws5)
        #4
        if (len(ws4) == 0):
            float_ws4 = 0.0
        else:
            float_ws4 = float(ws4)
        #3
        if (len(ws3) == 0):
            float_ws3 = 0.0
        else:
            float_ws3 = float(ws3)
        #2
        if (len(ws2) == 0):
            float_ws2 = 0.0
        else:
            float_ws2 = float(ws2)
        #1
        if (len(ws1) == 0):
            float_ws1 = 0.0
        else:
            float_ws1 = float(ws1)
        #0
        if (len(ws0) == 0):
            float_ws0 = 0.0
        else:
            float_ws0 = float(ws0)
        if(float_ws1 == 0 and float_ws2 == 0 and float_ws3 == 0 and float_ws4 == 0 and float_ws5 == 0 and float_ws6 == 0):
            if(float_ws0 == 0):
                l = tk.Label(window, fg='red', width=80, text='Przynajmniej jeden ze współczynników przy x musi być różny od zera')
                l.pack()
            else:
                l = tk.Label(window, fg='red', width=80, text='Podaj funkcję inną niż funkcja stała')
                l.pack()
            return
        wspolczynniki = [float_ws6, float_ws5, float_ws4, float_ws3, float_ws2, float_ws1, float_ws0]
        wielomian = Wielomian(wspolczynniki)
        podaj_przedzial(wielomian)
    except ValueError:
        l = tk.Label(window, fg='red', width=50, text='Współczynnik musi być typu float')
        l.pack()

def wspolczynniki_wielomianu():
    clear_window()
    l = tk.Label(window, bg='white', width=50, text='Podaj współczynniki', font=('Helvetica bold', 14))
    l.pack()
    frame = tk.Frame(window, pady=5)
    ws6 = tk.Entry(frame, width=4,)
    ws6.grid(row=0, column=0, ipady=1)
    tk.Label(frame, padx=1, text="x^6 +").grid(row=0, column=1)
    ws5 = tk.Entry(frame, width=4)
    ws5.grid(row=0, column=2, ipady=1)
    tk.Label(frame, text="x^5 +").grid(row=0, column=3)
    ws4 = tk.Entry(frame, width=4)
    ws4.grid(row=0, column=4, ipady=1)
    tk.Label(frame, text="x^4 +").grid(row=0, column=5)
    ws3 = tk.Entry(frame, width=4)
    ws3.grid(row=0, column=6, ipady=1)
    tk.Label(frame, text="x^3 +").grid(row=0, column=7)
    ws2 = tk.Entry(frame, width=4)
    ws2.grid(row=0, column=8, ipady=1)
    tk.Label(frame, text="x^2 +").grid(row=0, column=9)
    ws1 = tk.Entry(frame, width=4)
    ws1.grid(row=0, column=10, ipady=1)
    tk.Label(frame, text="x +").grid(row=0, column=11)
    ws0 = tk.Entry(frame, width=4)
    ws0.grid(row=0, column=12)
    frame.pack()
    button_zatwierdz_stopien = tk.Button(window, text='ZATWIERDŹ', font=('Helvetica bold', 12), 
                                         command= lambda: zatwierdz_wspolczynniki_wielomianu(ws6.get(), ws5.get(), ws4.get(), ws3.get(), ws2.get(), ws1.get(), ws0.get()))
    button_zatwierdz_stopien.pack(pady=10)

#FUNKCJA WYKŁADNICZA

def zatwierdz_wspolczynniki_wykladnicza(wsx, przesuniecie):
    try:
        float_wsx = float(wsx)
        if (float_wsx == 0):
            raise ValueError("ValueError")
        float_przesuniecie = float(przesuniecie)
        if (float_przesuniecie == 0):
            raise ValueError("ValueError")
        wykladnicza = Wykladnicza(float_wsx, float_przesuniecie)
        podaj_przedzial(wykladnicza)
    except ValueError:
        lf = tk.Label(window, fg='red', width=80, text='Podaj wartosci zmiennoprzecinkowe float różne od zera, separatorem musi być kropka.')
        lf.pack()

def wspolczynniki_wykladnicza():
    clear_window()
    l = tk.Label(window, bg='white', width=50, text='Podaj współczynnik i potęgę x', font=('Helvetica bold', 14))
    l.pack()
    frame = tk.Frame(window, pady=5)
    wsx = tk.Entry(frame, width=4,)
    wsx.grid(row=0, column=0, ipady=1)
    tk.Label(frame, padx=1, text="^x -").grid(row=0, column=1)
    przesuniecie = tk.Entry(frame, width=4)
    przesuniecie.grid(row=0, column=2, ipady=1)
    frame.pack()
    button_zatwierdz_wspolczynniki_wykladnicza= tk.Button(window, text='ZATWIERDŹ', font=('Helvetica bold', 12), 
                                                          command= lambda: zatwierdz_wspolczynniki_wykladnicza(wsx.get(), przesuniecie.get()))
    button_zatwierdz_wspolczynniki_wykladnicza.pack(pady=10)

#FUNKCJA TRYGONOMETRYCZNA

def zatwierdz_wspolczynniki_trygonometryczna(nazwa_funkcji, wsx, wsf):
    try:
        float_wsx = float(wsx)
        float_wsf = float(wsf)
        if (float_wsx != 0 and float_wsf != 0):
            if(nazwa_funkcji == 'sinus'):
                sinus = Sinus(float_wsx, float_wsf)
                podaj_przedzial(sinus)
            else:
                cosinus = Cosinus(float_wsx, float_wsf)
                podaj_przedzial(cosinus)
        else:
            lf = tk.Label(window, fg='red', width=50, text= 'Współczynniki muszą być różne od zera!')
            lf.pack()
    except ValueError:
        lf = tk.Label(window, fg='red', width=80, text='Podaj wartosc zmiennoprzecinkową float, separatorem musi być kropka.')
        lf.pack()

def wspolczynniki_trygonometryczna(nazwa_funkcji):
    clear_window()
    l = tk.Label(window, bg='white', width=50, text='Podaj współczynniki', font=('Helvetica bold', 14))
    l.pack()
    frame = tk.Frame(window, pady=5)
    wsf = tk.Entry(frame, width=4,)
    wsf.grid(row=0, column=0, ipady=1)
    if(nazwa_funkcji == 'sinus'):
        tk.Label(frame, padx=1, text="sin(").grid(row=0, column=1)
    else:
        tk.Label(frame, padx=1, text="cos(").grid(row=0, column=1)
    wsx = tk.Entry(frame, width=4)
    wsx.grid(row=0, column=2, ipady=1)
    tk.Label(frame, padx=1, text="x)").grid(row=0, column=3)
    frame.pack()
    button_zatwierdz_stopien = tk.Button(window, text='ZATWIERDŹ', font=('Helvetica bold', 12),
                                         command= lambda: zatwierdz_wspolczynniki_trygonometryczna(nazwa_funkcji, wsf.get(),wsx.get()))
    button_zatwierdz_stopien.pack(pady=10)


def zatwierdz_trygonometryczna(var_sinus, var_cosinus):
    if((var_sinus == 0 and var_cosinus == 0) or (var_sinus == 1 and var_cosinus == 1)):
        l = tk.Label(window, fg='red', width=50, text='Wybierz jedną funkcję!')
        l.pack()
    elif(var_sinus == 1):
        wspolczynniki_trygonometryczna('sinus')
    else:
        wspolczynniki_trygonometryczna('cosinus')

def wybor_trygonometryczna():
    clear_window()
    l = tk.Label(window, bg='white', width=50, text='Wybierz funkcję', font=('Helvetica bold', 14))
    l.pack()
    var_sinus = tk.IntVar()
    var_cosinus = tk.IntVar()
    check_sinus = tk.Checkbutton(window, text='sinus', variable=var_sinus, onvalue=1, offvalue=0)
    check_sinus.pack(anchor='w', padx=(10,10))
    check_cosinus = tk.Checkbutton(window, text='cosinus', variable=var_cosinus, onvalue=1, offvalue=0)
    check_cosinus.pack(anchor='w', padx=(10,10))    
    button_zatwierdz_tryg = tk.Button(window, text='ZATWIERDŹ', font=('Helvetica bold', 12), 
                                      command=lambda: zatwierdz_trygonometryczna(var_sinus.get(), var_cosinus.get()))
    button_zatwierdz_tryg.pack(pady=10)

#METODY WSPÓLNE

def wyswietl_wyniki(funkcja: Funkcja, poczatek: float, koniec: float, iteracje: int, dokladnosc: float):
    clear_window()
    f1 = tk.Frame(window, pady=5)
    f_b = tk.Frame(window, width=500)
    f_f = tk.Frame(window, width=500)
    if(iteracje == 0):
        kryterium_zatrzymania = tk.Label(f1, font=('Helvetica', 10), text='Kryterium zatrzymania - dokładność: ')
        kryterium_zatrzymania_wartosc = tk.Label(f1, font=('Helvetica bold', 10), text=str(dokladnosc))
        x0_b = bisekcja_dokladnosc(funkcja, poczatek, koniec, dokladnosc)
        x0_f = falsi_dokladnosc(funkcja, poczatek, koniec, dokladnosc)
        
    else:
        kryterium_zatrzymania = tk.Label(f1, font=('Helvetica', 10), text='Kryterium zatrzymania - liczba iteracji: ')
        kryterium_zatrzymania_wartosc = tk.Label(f1, font=('Helvetica bold', 10), text=str(iteracje))
        x0_b = bisekcja_iteracje(funkcja, poczatek, koniec, iteracje)
        x0_f = falsi_iteracje(funkcja, poczatek, koniec, iteracje)
    
    
    l = tk.Label(window, bg='white', width=50, text='WYNIKI', font=('Helvetica bold', 14))
    l.pack()
    kryterium_zatrzymania.grid(row=0, column=0)
    kryterium_zatrzymania_wartosc.grid(row=0, column=1)
    f1.pack()

    l_bisekcja = tk.Label(window, bg='white', width=100, text='METODA BISEKCJI', font=('Helvetica bold', 11))
    l_bisekcja.pack()
    tk.Label(f_b, text='Miejsce zerowe: ').grid(row=0,column=0)
    x0b_wyswietl = tk.Label(f_b, width=20, text=str(x0_b))
    x0b_wyswietl.grid(row=0,column=1)
    f_b.pack()

    l_falsi = tk.Label(window, bg='white', width=100, text='METODA REGULA FALSI', font=('Helvetica bold', 11))
    l_falsi.pack()
    tk.Label(f_f, text='Miejsce zerowe: ').grid(row=0,column=0)
    x0f_wyswietl = tk.Label(f_f, width=20, text=str(x0_f))
    x0f_wyswietl.grid(row=0,column=1)
    f_f.pack()

    button_wyjdz = tk.Button(window, text='WYJDŹ', font=('Helvetica bold', 12),
                                        command=window.destroy)
    button_wyjdz.pack(pady=10)

#WYKRES PYPLOT
    xpoints = np.arange(poczatek, koniec, 0.0001)
    ypoints = funkcja.wartos_w_punkcie_x(xpoints)
    x_b = [x0_b]
    x_f = [x0_f]
    y = [0]
    plt.plot(xpoints, ypoints)
    plt.axhline(y=0, color='k').set_linewidth(0.5)
    plt.axvline(x=0, color='k').set_linewidth(0.5)
    plt.plot(x_b, y, label='x0 bisekcja', marker="o", markerfacecolor="red")
    plt.plot(x_f, y, label='x0 regula falsi', marker="o", markerfacecolor="green")
    plt.title(funkcja.get_nazwa())
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()

def zatwierdz_wybor_kryterium(funkcja: Funkcja, poczatek: float, koniec: float, var_iteracje, var_dokladnosc, iteracje: int, dokladnosc: float):
    if((var_iteracje == 0 and var_dokladnosc == 0) or (var_iteracje == 1 and var_dokladnosc == 1)):
        l = tk.Label(window, fg='red', width=50, text='Wybierz jedno kryterium!')
        l.pack()
    elif(var_iteracje == 1):
        try:
            int_iteracje = int(iteracje)
            if(int_iteracje <= 0):
                raise ValueError("ValueError")
            wyswietl_wyniki(funkcja, poczatek, koniec, int_iteracje, 0)
        except ValueError:
            lp = tk.Label(window, fg='red', width=60, text='Podaj wartość calkowiotliczbowa większą od zera!')
            lp.pack()
    else:
        try:
            float_dokladnosc = float(dokladnosc)
            if(float_dokladnosc <= 0):
                raise ValueError("ValueError")
            wyswietl_wyniki(funkcja, poczatek, koniec, 0, float_dokladnosc)
        except ValueError:
            lp = tk.Label(window, fg='red', width=80, text='Podaj wartość zmiennoprzecinkową float większą od zera!')
            lp.pack()

def wybor_kryterium(funkcja: Funkcja, poczatek: float, koniec: float):
    clear_window()
    l = tk.Label(window, bg='white', width=50, text='Wybierz kryterium zatrzymania', font=('Helvetica bold', 14))
    l.pack()
    var_iteracje = tk.IntVar()
    var_dokladnosc = tk.IntVar()
    f = tk.Frame(window, pady=5)
    check_iteracje = tk.Checkbutton(f, text='liczba iteracji:', variable=var_iteracje, onvalue=1, offvalue=0)
    check_iteracje.grid(sticky='w', row=0, column=0, padx=(10,10))
    iteracje = tk.Entry(f, width=4)
    iteracje.grid(sticky='e', row=0, column=1)
    check_dokladnosc = tk.Checkbutton(f, text='dokładność:', variable=var_dokladnosc, onvalue=1, offvalue=0)
    check_dokladnosc.grid(sticky='w', row=1, column=0, padx=(10,10))
    dokladnosc = tk.Entry(f, width=10)
    dokladnosc.grid(sticky='e', row=1, column=1)
    f.pack(anchor='w')
    button_zatwierdz_wybor = tk.Button(window, text='ZATWIERDŹ', font=('Helvetica bold', 12),
                                        command=lambda: zatwierdz_wybor_kryterium(
                                        funkcja, poczatek, koniec, var_iteracje.get(), var_dokladnosc.get(), iteracje.get(), dokladnosc.get()))
    button_zatwierdz_wybor.pack(pady=10)

def zatwierdz_przedzial(funkcja: Funkcja, poczatek, koniec):
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
    if ((funkcja.wartos_w_punkcie_x(float_poczatek) * funkcja.wartos_w_punkcie_x(float_koniec)) > 0 ):
        l = tk.Label(window, fg='red', width=80, text='Znaki funkcji na krańcach przedziału nie są przeciwne - PODAJ INNY PRZEDZIAŁ')
        l.pack()
    else:
       if(float_poczatek > float_koniec):
           float_poczatek, float_koniec = float_koniec, float_poczatek
       wybor_kryterium(funkcja, float_poczatek, float_koniec)

def podaj_przedzial(funkcja: Funkcja):
    clear_window()
    l = tk.Label(window, bg='white', width=50, text='Podaj granice przedziału', font=('Helvetica bold', 14))
    l.pack()
    fpoczatek = tk.Frame(window, pady=5)
    tk.Label(fpoczatek, padx=1, text="Początek przedziału:").grid(sticky = 'w', row=0, column=0)
    poczatek = tk.Entry(fpoczatek, width=4)
    poczatek.grid(sticky='e', row=0, column=1, ipady=1)
    fpoczatek.pack()
    fkoniec = tk.Frame(window, pady=5)
    tk.Label(fkoniec, padx=1, text="Koniec przedziału:").grid(sticky = 'w', row=0, column=0)
    koniec = tk.Entry(fkoniec, width=4)
    koniec.grid(sticky='e', row=0, column=1, ipady=1, padx=(9,0))
    fkoniec.pack()
    button_zatwierdz_przedzial = tk.Button(window, text='ZATWIERDŹ', font=('Helvetica bold', 12), 
                                                     command= lambda: zatwierdz_przedzial(funkcja, poczatek.get(), koniec.get()))
    button_zatwierdz_przedzial.pack(pady=10)

##################################################################### ZŁOŻENIE FUNKCJ ####################################################################

def zatwierdz_wybor_zlozenia(zestaw_funkcji, var_gf, var_fg, f1, f2, var_cos):
    if ((var_gf == 0 and var_fg == 0) or (var_fg == 1 and var_gf == 1)):
        l = tk.Label(window, fg='red', width=80, text='Wybierz jedno ze złożeń')
        l.pack()
        return
    if (zestaw_funkcji == 1):
        float_f1 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        for i in range(0, 7):
            if (len(f1[i]) != 0):
                float_f1[i] = float(f1[i])
        wielomian = Wielomian(float_f1)
        wykladnicza = Wykladnicza(float(f2[0]), float(f2[1]))
        if (var_gf == 1):
            zlozenie = Zlozenie(wykladnicza, wielomian)
        else:
            zlozenie = Zlozenie(wielomian, wykladnicza)
    elif (zestaw_funkcji == 2):
        float_f1 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        for i in f1:
            if (len(f1[i-1]) != 0):
                float_f1[i-1] = float(f1[i-1])
        wielomian = Wielomian(float_f1)
        if (var_cos == 1):
            trygonometryczna = Cosinus(float(f2[0]), float(f2[1]))
        else:
            trygonometryczna = Sinus(float(f2[0]), float(f2[1]))
        if (var_gf == 1):
            zlozenie = Zlozenie(trygonometryczna, wielomian)
        else:
            zlozenie = Zlozenie(wielomian, trygonometryczna)
    else:
        wykladnicza = Wykladnicza(float(f1[0]), float(f1[1]))
        if (var_cos == 1):
            trygonometryczna = Cosinus(float(f2[0]), float(f2[1]))
        else:
            trygonometryczna = Sinus(float(f2[0]), float(f2[1]))
        if (var_gf == 1):
            zlozenie = Zlozenie(trygonometryczna, wykladnicza)
        else:
            zlozenie = Zlozenie(wykladnicza, trygonometryczna)
    podaj_przedzial(zlozenie)

def zmien_cosinus(var_vos, cos: tk.Label):
    if(var_vos == 1):
        cos.config(text="cos(")
    else:
        cos.config(text="sin(")

def wybor_zlozenie(zestaw_funkcji):
    clear_window()
    #WPISYWANIE WIELOMIAN
    frame_wielomian = tk.Frame(window, pady=5)
    tk.Label(frame_wielomian, padx=1, text="f(x) = ").grid(row=0, column=0)
    ws6 = tk.Entry(frame_wielomian, width=4,)
    ws6.grid(row=0, column=1, ipady=1)
    tk.Label(frame_wielomian, padx=1, text="x^6 +").grid(row=0, column=2)
    ws5 = tk.Entry(frame_wielomian, width=4)
    ws5.grid(row=0, column=3, ipady=1)
    tk.Label(frame_wielomian, text="x^5 +").grid(row=0, column=4)
    ws4 = tk.Entry(frame_wielomian, width=4)
    ws4.grid(row=0, column=5, ipady=1)
    tk.Label(frame_wielomian, text="x^4 +").grid(row=0, column=6)
    ws3 = tk.Entry(frame_wielomian, width=4)
    ws3.grid(row=0, column=7, ipady=1)
    tk.Label(frame_wielomian, text="x^3 +").grid(row=0, column=8)
    ws2 = tk.Entry(frame_wielomian, width=4)
    ws2.grid(row=0, column=9, ipady=1)
    tk.Label(frame_wielomian, text="x^2 +").grid(row=0, column=10)
    ws1 = tk.Entry(frame_wielomian, width=4)
    ws1.grid(row=0, column=11, ipady=1)
    tk.Label(frame_wielomian, text="x +").grid(row=0, column=12)
    ws0 = tk.Entry(frame_wielomian, width=4)
    ws0.grid(row=0, column=13)
    #WPISYWANIE WYKŁADNICZA
    frame_wykladnicza = tk.Frame(window, pady=5)
    wykladnicza_fg = tk.Label(frame_wykladnicza, padx=1, text="")
    wykladnicza_fg.grid(row=0, column=0)
    wsx_wykladnicza = tk.Entry(frame_wykladnicza, width=4,)
    wsx_wykladnicza.grid(row=0, column=1, ipady=1)
    tk.Label(frame_wykladnicza, padx=1, text="^x -").grid(row=0, column=2)
    przesuniecie = tk.Entry(frame_wykladnicza, width=4)
    przesuniecie.grid(row=0, column=3, ipady=1)
    #WPISYWANIE TRYGONOMETRYCZNA
    frame_trygonometryczna = tk.Frame(window, pady=5)
    tk.Label(frame_trygonometryczna, padx=1, text="g(x) = ").grid(row=0, column=0)
    wsf = tk.Entry(frame_trygonometryczna, width=4,)
    wsf.grid(row=0, column=1, ipady=1)
    cos = tk.Label(frame_trygonometryczna, padx=1, text="sin(")
    cos.grid(row=0, column=2)
    wsx_trygonometryczna = tk.Entry(frame_trygonometryczna, width=4)
    wsx_trygonometryczna.grid(row=0, column=3, ipady=1)
    tk.Label(frame_trygonometryczna, padx=1, text="x)").grid(row=0, column=4)
    var_cos = tk.IntVar()
    czy_cos = tk.Checkbutton(frame_trygonometryczna, text='cos', variable=var_cos, onvalue=1, offvalue=0, 
                             command= lambda: zmien_cosinus(var_cos.get(), cos))
    czy_cos.grid(row=0, column=5)

    if (zestaw_funkcji == 1):
        wykladnicza_fg.config(text="g(x) = ")
        frame_wielomian.pack(anchor='w')
        frame_wykladnicza.pack(anchor='w')
        button_zatwierdz_wybor_zlozenia = tk.Button(window, text='ZATWIERDŹ', font=('Helvetica bold', 12),
                                                command= lambda: zatwierdz_wybor_zlozenia(zestaw_funkcji, var_gf.get(), var_fg.get(),
                                                                                          [ws6.get(), ws5.get(), ws4.get(), ws3.get(), ws2.get(), ws1.get(), ws0.get()],
                                                                                          [wsx_wykladnicza.get(), przesuniecie.get()], 0))
    elif (zestaw_funkcji == 2):
        frame_wielomian.pack(anchor='w')
        frame_trygonometryczna.pack(anchor='w')
        button_zatwierdz_wybor_zlozenia = tk.Button(window, text='ZATWIERDŹ', font=('Helvetica bold', 12),
                                                command= lambda: zatwierdz_wybor_zlozenia(zestaw_funkcji, var_gf.get(), var_fg.get(),
                                                                                          [ws6.get(), ws5.get(), ws4.get(), ws3.get(), ws2.get(), ws1.get(), ws0.get()]
                                                                                          [wsx_trygonometryczna.get(), wsf.get()], var_cos.get()))
    else:
        wykladnicza_fg.config(text="f(x) = ")
        frame_wykladnicza.pack(anchor='w')
        frame_trygonometryczna.pack(anchor='w')
        button_zatwierdz_wybor_zlozenia = tk.Button(window, text='ZATWIERDŹ', font=('Helvetica bold', 12),
                                                command= lambda: zatwierdz_wybor_zlozenia(zestaw_funkcji, var_gf.get(), var_fg.get(),
                                                                                          [wsx_wykladnicza.get(), przesuniecie.get()],
                                                                                          [wsx_trygonometryczna.get(), wsf.get()], var_cos.get()))
    #WYBÓR g(f(x)) f(g(x))
    var_gf = tk.IntVar()
    var_fg = tk.IntVar()
    frame_zlozenie = tk.Frame(window, pady=5)
    check_gf = tk.Checkbutton(frame_zlozenie, text='g(f(x))', variable=var_gf, onvalue=1, offvalue=0)
    check_gf.pack(anchor='w', padx=(10,10))
    check_fg = tk.Checkbutton(frame_zlozenie, text='f(g(x))', variable=var_fg, onvalue=1, offvalue=0)
    check_fg.pack(anchor='w', padx=(10,10))
    frame_zlozenie.pack(anchor='w')
    button_zatwierdz_wybor_zlozenia.pack(pady=10)

def zatwierdz_wybor_funkcji():
    if (button_zatwierdz['state'] == 'normal'):
        if (var_zlozenie.get() == 1):
            if(var_wielomian.get() == 1 and var_wykladnicza.get() == 1):
                zestaw_funkcji = 1
            elif(var_wielomian.get() == 1 and var_trygonometryczna.get() == 1):
                zestaw_funkcji = 2
            elif(var_wykladnicza.get() == 1 and var_trygonometryczna.get() == 1):
                zestaw_funkcji = 3
            window.title('Zlożenie funkcji')
            wybor_zlozenie(zestaw_funkcji)
        else:
            if (var_wielomian.get() == 1):
                window.title('Wielomian')
                wspolczynniki_wielomianu()
            elif (var_wykladnicza.get() == 1):
                window.title('Funkcja wykładnicza')
                wspolczynniki_wykladnicza()
            elif (var_trygonometryczna.get() == 1):
                window.title('Funkcja trygonometryczna')
                wybor_trygonometryczna()
    else:
        return
 
def wyswietl_wybor_funkcji():
    button_zatwierdz['state'] = 'normal'
    if (var_zlozenie.get() == 1):
        l.config(text='Wybrano złożenie funkcji - wybierz 2 funkcje', width=80, fg='black')
        if (((var_wielomian.get() == 1) and (var_wykladnicza.get() == 1) and (var_trygonometryczna.get() == 0)) or 
            (var_wielomian.get() == 1) and (var_wykladnicza.get() == 0) and (var_trygonometryczna.get() == 1) or 
            (var_wielomian.get() == 0) and (var_wykladnicza.get() == 1) and (var_trygonometryczna.get() == 1)):
            return
        else:
            button_zatwierdz['state'] = 'disabled'
            l.config(text='Wybierz dwie funkcje', fg='black')
    else:
        if (var_wielomian.get() == 0) and (var_wykladnicza.get() == 0) and (var_trygonometryczna.get() == 0):
            l.config(text='Wybierz funkcję', fg='black')
            button_zatwierdz['state'] = 'disabled'
        elif (var_wielomian.get() == 1) and (var_wykladnicza.get() == 0) and (var_trygonometryczna.get() == 0):
            l.config(text='Wybrano wielomian', fg='black')
        elif (var_wielomian.get() == 0) and (var_wykladnicza.get() == 1) and (var_trygonometryczna.get() == 0):
            l.config(text='Wybrano funkcję wykładniczą', fg='black')
        elif (var_wielomian.get() == 0) and (var_wykladnicza.get() == 0) and (var_trygonometryczna.get() == 1):
            l.config(text='Wybrano funkcję trygnonometryczną')
        else:
            button_zatwierdz['state'] = 'disabled'
            l.config(text='Wybierz jedną opcję!', fg='red')


def wybor_funkcji():
    l.pack()
    check_wielomian = tk.Checkbutton(window, text='wielomian', variable=var_wielomian, onvalue=1, offvalue=0, command=wyswietl_wybor_funkcji)
    check_wielomian.pack(anchor='w', padx=(10,10))
    check_wykladnicza = tk.Checkbutton(window, text='wykładnicza', variable=var_wykladnicza, onvalue=1, offvalue=0, command=wyswietl_wybor_funkcji)
    check_wykladnicza.pack(anchor='w', padx=(10,10))
    check_trygonometryczna = tk.Checkbutton(window, text='trygonometryczna', variable=var_trygonometryczna, onvalue=1, offvalue=0, command=wyswietl_wybor_funkcji)
    check_trygonometryczna.pack(anchor='w', padx=(10,10))
    check_zlozenie = tk.Checkbutton(window, text='złozenie', variable=var_zlozenie, onvalue=1, offvalue=0, command=wyswietl_wybor_funkcji)
    check_zlozenie.pack(anchor='w', padx=(10,10))
    button_zatwierdz.pack(pady=10)

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