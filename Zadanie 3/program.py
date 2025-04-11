import pylab as pb
import numpy as np
import sympy as sp
from tkinter import *
from abc import ABC, abstractmethod
from interpolacjaNewtona import forward_interpolation, backward_interpolation
 
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

class Modul(Funkcja):
     
    def __init__ (self):
        pass

    def wartos_w_punkcie_x(self, x):
        return abs(x)
    
    def get_nazwa(self):
        result = "f(x) = |x|"
        return result

class Wielomian(Funkcja):

    def __init__ (self, wspolczynniki):
        self.wspolczynniki = wspolczynniki

    def wartos_w_punkcie_x(self, x):
        return horner(self.wspolczynniki,x)
    
    def get_nazwa(self):
        result = "f(x) = "
        for i in range(0, len(self.wspolczynniki)):
            if(self.wspolczynniki[i] != 0 ):
                if (i == (len(self.wspolczynniki)-1)):
                    result += str(self.wspolczynniki[i])
                else:
                    result += str(self.wspolczynniki[i]) + "x^" + str((len(self.wspolczynniki)-1)-i) + " + "

        return result

class Zlozenie_tryg(Funkcja):

    def __init__ (self):
        pass

    def wartos_w_punkcie_x(self, x):
        return 4 * np.sin(x) - 2 * np.cos(x)
    
    def get_nazwa(self):
        result = "f(x) = 4sin(x) - 2cos(x)"
        return result

class Zlozenie(Funkcja):

    def __init__ (self):
        pass

    def wartos_w_punkcie_x(self, x):
        return abs(np.cos(x**2) - 0.25*x)
    
    def get_nazwa(self):
        result = "f(x) = |cos(x^2)| - 0.25x"
        return result

def horner(poly, arg_x):
    result = 0
    for item in poly:
        result = result * arg_x + item
    return result

class Zpliku(Funkcja):
     
    def __init__ (self):
        pass

    def wartos_w_punkcie_x(self):
        pass
    
    def get_nazwa(self):
        result = "Dane z pliku"
        return result

def show_plot(arguments, function_value, start, end, nodes,function: Funkcja):    
    interpolation_x = []
    interpolation_y = []
    pb.plot(arguments, function_value, label='Wykres f(x)')
    pb.title(function.get_nazwa())
    interpolation_x = np.linspace(start, end, nodes)
    for x in interpolation_x:
        round(x, 8)
    interpolation_y = function.wartos_w_punkcie_x(interpolation_x)
    for y in interpolation_y:
        round(y, 8)
    interpolation_x = list(interpolation_x)
    interpolation_y = list(interpolation_y)
    x = sp.Symbol('x')
    forward_interpolation_formula = forward_interpolation(interpolation_x, interpolation_y)
    backward_interpolation_formula = backward_interpolation(interpolation_x, interpolation_y)
    forward_interpolation_coeffs = sp.Poly(forward_interpolation_formula, x).all_coeffs()
    backward_interpolation_coeffs = sp.Poly(backward_interpolation_formula, x).all_coeffs()
    values = []
    for argument in arguments:
        if argument < (arguments[-1] + arguments[0]) / 2:
            values.append(horner(forward_interpolation_coeffs, argument))
        else:
            values.append(horner(backward_interpolation_coeffs, argument))
    pb.scatter(interpolation_x, interpolation_y, label='węzły interpolacji')
    pb.plot(arguments, values, linestyle=":", label='wielomian interpolacyjny')
    pb.xlabel("x")
    pb.ylabel("y")
    fig = pb.gcf()
    string = 'Wykres ' + function.get_nazwa()
    fig.canvas.set_window_title(string)
    pb.grid(True)
    pb.legend(loc='upper right')
    pb.show(block=True)

def load_points():
    x = sp.Symbol('x')
    interpolation_x = []
    interpolation_y = []
    load_error_label.config(text="")
    not_correct = True
    while not_correct:
        try:
            with open("dane.txt", 'r') as dane:
                interpolation_x = dane.readline().split()
                interpolation_y = dane.readline().split()
            interpolation_x = [float(i) for i in interpolation_x]
            interpolation_y = [float(i) for i in interpolation_y]
            if len(interpolation_x) == len(interpolation_y) and len(interpolation_x) > 1:
                not_correct = False
        except ValueError:
            load_error_label.config(text="Błąd wczytywania danych")
    forward_interpolation_formula = forward_interpolation(interpolation_x, interpolation_y)
    backward_interpolation_formula = backward_interpolation(interpolation_x, interpolation_y)
    forward_interpolation_coeffs = sp.Poly(forward_interpolation_formula, x).all_coeffs()
    backward_interpolation_coeffs = sp.Poly(backward_interpolation_formula, x).all_coeffs()
    values = []
    values_back = []
    arguments = list(np.linspace(interpolation_x[0], interpolation_x[len(interpolation_x)-1], 1000))

    for i in range(len(arguments)):
        values.append(horner(forward_interpolation_coeffs, arguments[i]))
        values_back.append(horner(backward_interpolation_coeffs, arguments[i]))

    pb.title("Interpolacja danych z pliku")
    pb.scatter(interpolation_x, interpolation_y, label='węzły interpolacji')
    pb.plot(arguments, values, linestyle=":", label='interpolacja w przód')
    pb.plot(arguments, values_back, linestyle=":", label='interpolacja w tył')
    
    pb.xlabel("x")
    pb.ylabel("y")
    fig = pb.gcf()
    pb.grid(True)
    pb.legend(loc='upper right')
    pb.show(block=True)

def generate_results(start, end, nodes):
    function_label.config(text='Funkcja:', fg='black')
    range_error_label.config(text='')
    node_error_label.config(text='')
    try:
        float_start = float(start)
        float_end = float(end)
        if(float_end < float_start):
            float_start, float_end = float_end, float_start
        if(float_start == float_end):
            raise ValueError("ValueError")
    except ValueError:
        range_error_label.config(text='Podaj różne wartości całkowite lub ułamkowe - znak separatora to kropka')
        return
    try:
        int_nodes = int(nodes)
        if(int_nodes <= 1):
            raise ValueError("ValueError")
    except ValueError:
        node_error_label.config(text='Podaj wartość całkowitą większą od jeden')
        return
    
    if (var_linear.get() == 1) and (var_absolute.get() == 0) and (var_composite.get() == 0) and (var_polynomial.get() == 0) and (var_trygonometric.get() == 0):
        function = Wielomian([2,5])      
    elif (var_linear.get() == 0) and (var_absolute.get() == 1) and (var_composite.get() == 0) and (var_polynomial.get() == 0) and (var_trygonometric.get() == 0):
        function = Modul()
    elif (var_linear.get() == 0) and (var_absolute.get() == 0) and (var_composite.get() == 1) and (var_polynomial.get() == 0) and (var_trygonometric.get() == 0):
        function = Zlozenie()
    elif (var_linear.get() == 0) and (var_absolute.get() == 0) and (var_composite.get() == 0) and (var_polynomial.get() == 1) and (var_trygonometric.get() == 0):
        function = Wielomian([5,1,-10,4])
    elif (var_linear.get() == 0) and (var_absolute.get() == 0) and (var_composite.get() == 0) and (var_polynomial.get() == 0) and (var_trygonometric.get() == 1):
        function = Zlozenie_tryg()
    else:
        function_label.config(text='Wybierz jedną opcję!', fg='red')
        return

    arguments = list(np.linspace(float_start, float_end, 1000))
    function_value = []
    for argument in arguments:
        function_value.append(function.wartos_w_punkcie_x(argument))
    show_plot(arguments, function_value, float_start, float_end, int_nodes, function)



window = Tk()
window.title('Metody numeryczne - zadanie 3')
window.geometry('600x500')

var_linear = IntVar()
var_absolute = IntVar()
var_composite = IntVar()
var_polynomial = IntVar()
var_trygonometric = IntVar()

functions_frame = Frame(window, height=300, width=600, pady=10)
range_frame =  Frame(window, height=50, width=600, pady=10)
node_frame =  Frame(window, height=50, width=600, pady=10)

load_from_file_button = Button(window, text='INTERPOLACJA DANYCH Z PLIKU', width=30, font=('Helvetica bold', 14), command=lambda:load_points())
load_from_file_button.pack(pady=10)
load_error_label = Label(window, text="", font=('Helvetica', 12), fg='red')
load_error_label.pack()

function_label = Label(functions_frame, text='Funkcja:', font=('Helvetica', 12))
function_label.pack(anchor='w', pady=(0,10))
linear_check = Checkbutton(functions_frame, text='2x + 5', variable=var_linear, onvalue=1, offvalue=0)
linear_check.pack(anchor='w')
absolute_check= Checkbutton(functions_frame, text='|x|', variable=var_absolute, onvalue=1, offvalue=0)
absolute_check.pack(anchor='w')
composite_check = Checkbutton(functions_frame, text='|cos(x^2) - 0.25x|', variable=var_composite, onvalue=1, offvalue=0)
composite_check.pack(anchor='w')
polynomial_check = Checkbutton(functions_frame, text='5x^3 + x^2 - 10x + 4', variable=var_polynomial, onvalue=1, offvalue=0)
polynomial_check.pack(anchor='w')
trygonometric_check = Checkbutton(functions_frame, text='8cos(x) - 2sin(x)', variable=var_trygonometric, onvalue=1, offvalue=0)
trygonometric_check.pack(anchor='w')
functions_frame.pack()

range_label = Label(window, text='Przedział interpolacji:', font=('Helvetica', 12))
range_label.pack(pady=(10,0))
start_label = Label(range_frame, padx=1, text="początek: ")
start_label.grid(row=0, column=0)
start_entry = Entry(range_frame, width=4)
start_entry.grid(row=0, column=1, ipady=1, padx=(0, 10))
end_label = Label(range_frame, padx=1, text="koniec: ")
end_label.grid(row=0, column=3, padx=(10,0))
end_entry = Entry(range_frame, width=4)
end_entry.grid(row=0, column=4, ipady=1)
range_frame.pack()
range_error_label = Label(window, text="", font=('Helvetica', 12), fg='red')
range_error_label.pack()
node_label = Label(node_frame, padx=1, text="liczba węzłów interpolacji: ")
node_label.grid(row=0, column=0, ipady=1)
node_entry = Entry(node_frame, width=4)
node_entry.grid(row=0, column=1, ipady=1)
node_frame.pack()
node_error_label = Label(window, text="", font=('Helvetica', 12), fg='red')
node_error_label.pack()


results_button = Button(window, text='ZATWIERDŹ', width=25, font=('Helvetica bold', 14), command=lambda:generate_results(start_entry.get(), end_entry.get(), node_entry.get()))
results_button.pack(pady=10)

mainloop()