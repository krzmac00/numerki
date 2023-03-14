import tkinter as tk
import math as mat
import matplotlib.pyplot as plt
import numpy as np
 

#WIELOMIAN

def bisekcja_wielomian():
    return

def oblicz_wielomian(wspolczynniki, poczatek, koniec, iteracje, dokladnosc):
    return

def zatwierdz_wybor_kryterium_wielomian(wspolczynniki, poczatek, koniec, var_iteracje, var_dokladnosc, iteracje, dokladnosc):
    if((var_iteracje == 0 and var_dokladnosc == 0) or (var_iteracje == 1 and var_dokladnosc == 1)):
        l = tk.Label(window, fg='red', width=50, text='Wybierz jedno kryterium!')
        l.pack()
    elif(var_iteracje == 1):
        try:
            int_iteracje = int(iteracje)
            if(int_iteracje <= 0):
                raise ValueError("ValueError")
            oblicz_wielomian(wspolczynniki, poczatek, koniec, int_iteracje, 0)
        except ValueError:
            lp = tk.Label(window, fg='red', width=50, text='Podaj wartosc calkowiotliczbowa większą od zera!')
            lp.pack()
    else:
        try:
            float_dokladnosc = float(dokladnosc)
            if(float_dokladnosc <= 0):
                raise ValueError("ValueError")
            oblicz_wielomian(wspolczynniki, poczatek, koniec, 0, float_dokladnosc)
        except ValueError:
            lp = tk.Label(window, fg='red', width=50, text='Podaj wartosc zmiennoprzecinkową większą od zera!')
            lp.pack()

def wybor_kryterium_wielomian(wspolczynniki, poczatek, koniec):
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
                                        command=lambda: zatwierdz_wybor_kryterium_wielomian(
                                        wspolczynniki, poczatek, koniec, var_iteracje.get(), var_dokladnosc.get(), iteracje.get(), dokladnosc.get()))
    button_zatwierdz_wybor.pack(pady=10)

def zatwierdz_przedzial_wielomian(wspolczynniki, poczatek, koniec):
    try:
        float_poczatek = float(poczatek)
    except ValueError:
        lp = tk.Label(window, fg='red', width=50, text='podaj wartosc float, separatorem musi być kropka.')
        lp.pack()
    try:
        float_koniec = float(koniec)
    except ValueError:
        lk = tk.Label(window, fg='red', width=50, text='podaj wartosc float, separatorem musi być kropka.')
        lk.pack()
    if ((np.polyval(wspolczynniki, float_poczatek) * np.polyval(wspolczynniki,float_koniec)) > 0 ):
        l = tk.Label(window, fg='red', width=50, text='BRAK miejsca zerowego w podanym przedziale - PODAJ INNY PRZEDZIAŁ')
        l.pack()
    else:
       if(float_poczatek > float_koniec):
           float_poczatek, float_koniec = float_koniec, float_poczatek
       wybor_kryterium_wielomian(wspolczynniki, poczatek, koniec)

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
        wspolczynniki = [float_ws6, float_ws5, float_ws4, float_ws3, float_ws2, float_ws1, float_ws0]
        podaj_przedzial_wielomian(wspolczynniki)
    except ValueError:
        l = tk.Label(window, fg='red', width=50, text='współczynnik musi być typu float')
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
    button_zatwierdz_stopien = tk.Button(window, text='ZATWIERDŹ', font=('Helvetica bold', 12), command= lambda: zatwierdz_wspolczynniki_wielomianu(ws6.get(), ws5.get(), ws4.get(), ws3.get(), ws2.get(), ws1.get(), ws0.get()))
    button_zatwierdz_stopien.pack(pady=10)

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
            oblicz_wielomian(wsx, potega, poczatek, koniec, int_iteracje, 0)
        except ValueError:
            lp = tk.Label(window, fg='red', width=50, text='Podaj wartosc calkowiotliczbowa większą od zera!')
            lp.pack()
    else:
        try:
            float_dokladnosc = float(dokladnosc)
            if(float_dokladnosc <= 0):
                raise ValueError("ValueError")
            oblicz_wielomian(wsx, potega, poczatek, koniec, 0, float_dokladnosc)
        except ValueError:
            lp = tk.Label(window, fg='red', width=50, text='Podaj wartosc zmiennoprzecinkową większą od zera!')
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
        lp = tk.Label(window, fg='red', width=50, text='podaj wartosc float, separatorem musi być kropka.')
        lp.pack()
    try:
        float_koniec = float(koniec)
    except ValueError:
        lk = tk.Label(window, fg='red', width=50, text='podaj wartosc float, separatorem musi być kropka.')
        lk.pack()
    if ((float_poczatek**potega) * (float_koniec**potega)) > 0:
        l = tk.Label(window, fg='red', width=50, text='BRAK miejsca zerowego w podanym przedziale - PODAJ INNY PRZEDZIAŁ')
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
                                                     command= lambda: zatwierdz_przedzial_wielomian(wsx, potega, poczatek.get(), koniec.get()))
    button_zatwierdz_przedzial_wielomian.pack(pady=10)

def zatwierdz_wspolczynniki_wykladnicza(wsx, potega):
    try:
        float_wsx = float(wsx)
        if (float_wsx == 0):
            raise ValueError("ValueError")
        float_potega = float(potega)
        if (float_potega == 0):
            raise ValueError("ValueError")
        podaj_przedzial_wykladnicza(float_wsx, float_potega)
    except ValueError:
        lf = tk.Label(window, fg='red', width=50, text='Podaj wartosci float różne od zera, separatorem musi być kropka.')
        lf.pack()

def wspolczynniki_wykladnicza():
    clear_window()
    l = tk.Label(window, bg='white', width=50, text='Podaj współczynnik i potęgę x', font=('Helvetica bold', 14))
    l.pack()
    frame = tk.Frame(window, pady=5)
    wsx = tk.Entry(frame, width=4,)
    wsx.grid(row=0, column=0, ipady=1)
    tk.Label(frame, padx=1, text="x^").grid(row=0, column=1)
    potega = tk.Entry(frame, width=4)
    potega.grid(row=0, column=2, ipady=1)
    frame.pack()
    button_zatwierdz_wspolczynniki_wykladnicza= tk.Button(window, text='ZATWIERDŹ', font=('Helvetica bold', 12), 
                                                          command= lambda: zatwierdz_wspolczynniki_wykladnicza(wsx.get(), potega.get()))
    button_zatwierdz_wspolczynniki_wykladnicza.pack(pady=10)

#FUNKCJA TRYGONOMETRYCZNA

def oblicz_trygonometryczna(funkcja, wsx, wsf, poczatek, koniec, var_iteracje, var_dokladnosc, iteracje, dokladnosc):
    return

def zatwierdz_wybor_kryterium_trygonometryczna(funkcja, wsx, wsf, poczatek, koniec, var_iteracje, var_dokladnosc, iteracje, dokladnosc):
    if((var_iteracje == 0 and var_dokladnosc == 0) or (var_iteracje == 1 and var_dokladnosc == 1)):
        l = tk.Label(window, fg='red', width=50, text='Wybierz jedno kryterium!')
        l.pack()
    elif(var_iteracje == 1):
        try:
            int_iteracje = int(iteracje)
            if(int_iteracje <= 0):
                raise ValueError("ValueError")
            oblicz_trygonometryczna(funkcja, wsx, wsf, poczatek, koniec, int_iteracje, 0)
        except ValueError:
            lp = tk.Label(window, fg='red', width=50, text='Podaj wartosc calkowiotliczbowa większą od zera!')
            lp.pack()
    else:
        try:
            float_dokladnosc = float(dokladnosc)
            if(float_dokladnosc <= 0):
                raise ValueError("ValueError")
            oblicz_wielomian(funkcja, wsx, wsf, poczatek, koniec, 0, float_dokladnosc)
        except ValueError:
            lp = tk.Label(window, fg='red', width=50, text='Podaj wartosc zmiennoprzecinkową większą od zera!')
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
    except ValueError:
        lp = tk.Label(window, fg='red', width=50, text='podaj wartosc float, separatorem musi być kropka.')
        lp.pack()
    try:
        float_koniec = float(koniec)
    except ValueError:
        lk = tk.Label(window, fg='red', width=50, text='podaj wartosc float, separatorem musi być kropka.')
        lk.pack()
    if(funkcja == "sinus"):
        if (mat.sin(wsx*float_poczatek) * mat.sin(wsx*float_koniec)) > 0:
            l = tk.Label(window, fg='red', width=50, text='BRAK miejsca zerowego w podanym przedziale - PODAJ INNY PRZEDZIAŁ')
            l.pack()
        else:
            if(float_poczatek > float_koniec):
                float_poczatek, float_koniec = float_koniec, float_poczatek
            wybor_kryterium_trygonometryczna(funkcja, wsx, wsf, poczatek, koniec)
    else:
        if (mat.cos(wsx*float_poczatek) * mat.cos(wsx*float_koniec)) > 0:
            l = tk.Label(window, fg='red', width=50, text='BRAK miejsca zerowego w podanym przedziale - PODAJ INNY PRZEDZIAŁ')
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

def zatwierdz_wspolczynniki_trygonometryczna(funkcja, wsx, wsf):
    try:
        float_wsf = float(wsf)
        if (float_wsf != 0):
            wspolczynniki_wielomianu()
        else:
            lf = tk.Label(window, fg='red', width=50, text= 'nie może być 0')
            lf.pack()
    except ValueError:
        lf = tk.Label(window, fg='red', width=50, text='podaj wartosc float, separatorem musi być kropka.')
        lf.pack()
    
    try:
        float_wsf = float(wsx)
        if (float_wsf != 0):
            wspolczynniki_wielomianu()
        else:
            lx = tk.Label(window, fg='red', width=50, text= 'nie może być 0')
            lx.pack()
    except ValueError:
        lx = tk.Label(window, fg='red', width=50, text='podaj wartosc float, separatorem musi być kropka.')
        lx.pack()
    

def wprowadz_trygonometryczna(funkcja):
    clear_window()
    l = tk.Label(window, bg='white', width=50, text='Podaj współczynniki', font=('Helvetica bold', 14))
    l.pack()
    frame = tk.Frame(window, pady=5)
    wsf = tk.Entry(frame, width=4,)
    wsf.grid(row=0, column=0, ipady=1)
    if(funkcja == 'sinus'):
        tk.Label(frame, padx=1, text="sin(").grid(row=0, column=1)
    else:
        tk.Label(frame, padx=1, text="cos(").grid(row=0, column=1)
    wsx = tk.Entry(frame, width=4)
    wsx.grid(row=0, column=2, ipady=1)
    tk.Label(frame, padx=1, text="x)").grid(row=0, column=3)
    frame.pack()
    button_zatwierdz_stopien = tk.Button(window, text='ZATWIERDŹ', font=('Helvetica bold', 12),
                                         command= lambda: zatwierdz_wspolczynniki_trygonometryczna(funkcja, wsf.get(),wsx.get()))
    button_zatwierdz_stopien.pack(pady=10)


def zatwierdz_trygonometryczna(var_sinus, var_cosinus):
    if((var_sinus == 0 and var_cosinus == 0) or (var_sinus == 1 and var_cosinus == 1)):
        return
    elif(var_sinus == 1):
        wprowadz_trygonometryczna('sinus')
    else:
        wprowadz_trygonometryczna('cosinus')


def wspolczynniki_trygonometryczna():
    clear_window()

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
    button_zatwierdz_tryg = tk.Button(window, text='ZATWIERDŹ', font=('Helvetica bold', 12), command=lambda: zatwierdz_trygonometryczna(var_sinus.get(), var_cosinus.get()))
    button_zatwierdz_tryg.pack(pady=10)


def clear_window():
    for widgets in window.winfo_children():
        widgets.destroy()

def wpisanie_funkcji(nazwa):
    if (nazwa == 'wielomian'):
        
        window.title('wielomian')
    else:
        return
    
def zatwierdz_wybor_funkcji():
    if (button_zatwierdz['state'] == 'normal'):
        if (var_wielomian.get() == 1):
            window.title('wielomian')
            wspolczynniki_wielomianu()
        elif (var_wykladnicza.get() == 1):
            window.title('funkcja wykladnicza')
            wspolczynniki_wykladnicza()
        elif (var_trygonometryczna.get() == 1):
            window.title('funkcja trygonometryczna')
            wybor_trygonometryczna()
        elif (var_zlozenie.get() == 1):
            window.title('zlozenie')
    else:
        return
 
def print_selection():
    button_zatwierdz['state'] = 'normal'
    if (var_wielomian.get() == 0) & (var_wykladnicza.get() == 0) & (var_trygonometryczna.get() == 0) & (var_zlozenie.get() == 0):
         l.config(text='Wybierz funkcję', fg='black')
         button_zatwierdz['state'] = 'disabled'
    elif (var_wielomian.get() == 1) & (var_wykladnicza.get() == 0) & (var_trygonometryczna.get() == 0) & (var_zlozenie.get() == 0):
        l.config(text='Wybrano wielomian', fg='black')
    elif (var_wielomian.get() == 0) & (var_wykladnicza.get() == 1) & (var_trygonometryczna.get() == 0) & (var_zlozenie.get() == 0):
        l.config(text='Wybrano funkcję wykładniczą', fg='black')
    elif (var_wielomian.get() == 0) & (var_wykladnicza.get() == 0) & (var_trygonometryczna.get() == 1) & (var_zlozenie.get() == 0):
        l.config(text='Wybrano funkcję trygnonometryczną')
    elif (var_wielomian.get() == 0) & (var_wykladnicza.get() == 0) & (var_trygonometryczna.get() == 0) & (var_zlozenie.get() == 1):
        l.config(text='Wybrano złożenie funkcji', fg='black')
    else:
        button_zatwierdz['state'] = 'disabled'
        l.config(text='Wybierz jedną opcję!', fg='red')


#stworzenie okna
window = tk.Tk()
window.title('Metody numeryczne - zadanie 1')
window.geometry('500x400')

l = tk.Label(window, bg='white', width=50, text='Wybierz funkcję', font=('Helvetica bold', 14))
l.pack()

var_wielomian = tk.IntVar()
var_wykladnicza = tk.IntVar()
var_trygonometryczna = tk.IntVar()
var_zlozenie = tk.IntVar()
check_wielomian = tk.Checkbutton(window, text='wielomian', variable=var_wielomian, onvalue=1, offvalue=0, command=print_selection)
check_wielomian.pack(anchor='w', padx=(10,10))
check_wykladnicza = tk.Checkbutton(window, text='wykładnicza', variable=var_wykladnicza, onvalue=1, offvalue=0, command=print_selection)
check_wykladnicza.pack(anchor='w', padx=(10,10))
check_trygonometryczna = tk.Checkbutton(window, text='trygonometryczna', variable=var_trygonometryczna, onvalue=1, offvalue=0, command=print_selection)
check_trygonometryczna.pack(anchor='w', padx=(10,10))
check_zlozenie = tk.Checkbutton(window, text='złozenie', variable=var_zlozenie, onvalue=1, offvalue=0, command=print_selection)
check_zlozenie.pack(anchor='w', padx=(10,10))

button_zatwierdz = tk.Button(window, text='ZATWIERDŹ', font=('Helvetica bold', 12), state='disabled', command=zatwierdz_wybor_funkcji)
button_zatwierdz.pack(pady=10)
 
window.mainloop()