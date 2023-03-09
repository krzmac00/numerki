import tkinter as tk
 

window = tk.Tk()
window.title('Metody numeryczne - zadanie 1')
window.geometry('400x400')

#frame =tk.Frame(window)
 
l = tk.Label(window, bg='white', width=50, text='Wybierz funkcję', font=('Helvetica bold', 14))
l.pack()

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
        elif (var_wykladnicza.get() == 1):
            window.title('wykladnicza')
        elif (var_trygonometryczna.get() == 1):
            window.title('trygonometryczna')
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