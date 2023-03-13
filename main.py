import tkinter as tk
 
#WIELOMIAN

def wspolczynniki_wielomianu():
    clear_window()
    l = tk.Label(window, bg='white', width=50, text='Podaj współczynniki', font=('Helvetica bold', 14))
    l.pack()
    frame = tk.Frame(window, pady=5)
    ws6 = tk.Entry(frame, width=4,).grid(row=0, column=0, ipady=1)
    tk.Label(frame, padx=1, text="x^6 +").grid(row=0, column=1)
    ws5 = tk.Entry(frame, width=4).grid(row=0, column=2, ipady=1)
    tk.Label(frame, text="x^5 +").grid(row=0, column=3)
    ws4 = tk.Entry(frame, width=4).grid(row=0, column=4, ipady=1)
    tk.Label(frame, text="x^4 +").grid(row=0, column=5)
    ws3 = tk.Entry(frame, width=4).grid(row=0, column=6, ipady=1)
    tk.Label(frame, text="x^3 +").grid(row=0, column=7)
    ws2 = tk.Entry(frame, width=4).grid(row=0, column=8, ipady=1)
    tk.Label(frame, text="x^2 +").grid(row=0, column=9)
    ws1 = tk.Entry(frame, width=4).grid(row=0, column=10, ipady=1)
    tk.Label(frame, text="x +").grid(row=0, column=11)
    ws0 = tk.Entry(frame, width=4).grid(row=0, column=12)
    frame.pack()
    button_zatwierdz_stopien = tk.Button(window, text='ZATWIERDŹ', font=('Helvetica bold', 12), command= lambda: zatwierdz_stopien())
    button_zatwierdz_stopien.pack(pady=10)

def zatwierdz_stopien():
    stopien = '20'
    try:
        int_stopien = int(stopien)
        if (int_stopien >= 0 and int_stopien <= 6):
            wspolczynniki_wielomianu(int_stopien)
        else:
            l3 = tk.Label(window, fg='red', width=50, text= stopien + ' nie jest z przediału 0 - 6')
            l3.pack()
    except ValueError:
        l3 = tk.Label(window, fg='red', width=50, text='błedny stopien')
        l3.pack()

def stopien_wielomianu():
    clear_window()
    l = tk.Label(window, bg='white', width=50, text='Podaj stopien wielomianu', font=('Helvetica bold', 14))
    l.pack()
    l2 = tk.Label(window, bg='white', width=50, text='zakres: 0 - 6')
    l2.pack()
    stopien = tk.Entry(window, width=10)
    stopien.pack()
    button_zatwierdz_stopien = tk.Button(window, text='ZATWIERDŹ', font=('Helvetica bold', 12), command= lambda: zatwierdz_stopien(stopien.get()))
    button_zatwierdz_stopien.pack(pady=10)

#FUNKCJA WYKŁADNICZA

def wspolczynniki_wykladnicza():
    clear_window()
    l = tk.Label(window, bg='white', width=50, text='Podaj współczynnik i potęgę x', font=('Helvetica bold', 14))
    l.pack()
    frame = tk.Frame(window, pady=5)
    wsx = tk.Entry(frame, width=4,).grid(row=0, column=0, ipady=1)
    tk.Label(frame, padx=1, text="x^").grid(row=0, column=1)
    potega = tk.Entry(frame, width=4).grid(row=0, column=2, ipady=1)
    frame.pack()
    button_zatwierdz_stopien = tk.Button(window, text='ZATWIERDŹ', font=('Helvetica bold', 12), command= lambda: zatwierdz_stopien())
    button_zatwierdz_stopien.pack(pady=10)

#FUNKCJA TRYGONOMETRYCZNA

def wprowadz_sinus():
    clear_window()

def wprowadz_cosinus():
    clear_window()

def zatwierdz_trygonometryczna(var_sinus, var_cosinus):
    if((var_sinus == 0 and var_cosinus == 0) or (var_sinus == 1 and var_cosinus == 1)):
        return
    elif(var_sinus == 1):
        wprowadz_sinus()
    else:
        wprowadz_cosinus()


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