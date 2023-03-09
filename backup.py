'''

def wspolczynniki_wielomian(int_stopien):
    clear_window()
    l = tk.Label(window, bg='white', width=50, text='Podaj współczynniki', font=('Helvetica bold', 14))
    l.pack()

def zatwierdz_stopien(stopien):
    try:
        int_stopien = int(stopien)
        if (int_stopien >= 0 and int_stopien <= 6):
            wspolczynniki_wielomian(int_stopien)
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


    '''