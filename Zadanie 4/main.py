from tkinter import *
from calki import *


def get_function():
    function_error_label.config(text='')
    if(var_linear.get() == 1 and var_absolute.get() == 0 and var_reciprocal.get() == 0 and var_polynomial.get() == 0 and var_trygonometric.get() == 0):
        funkcja = Wielomian([2,5])
    elif(var_linear.get() == 0 and var_absolute.get() == 1 and var_reciprocal.get() == 0 and var_polynomial.get() == 0 and var_trygonometric.get() == 0):
        funkcja = Modul()
    elif(var_linear.get() == 0 and var_absolute.get() == 0 and var_reciprocal.get() == 1 and var_polynomial.get() == 0 and var_trygonometric.get() == 0):
        funkcja = Homograficzna()
    elif(var_linear.get() == 0 and var_absolute.get() == 0 and var_reciprocal.get() == 0 and var_polynomial.get() == 1 and var_trygonometric.get() == 0):
        funkcja = Wielomian([2,0,-2,0])
    elif(var_linear.get() == 0 and var_absolute.get() == 0 and var_reciprocal.get() == 0 and var_polynomial.get() == 0 and var_trygonometric.get() == 1):
        funkcja = Trygonometryczna()
    else:
        function_error_label.config(text='Wybierz jedną funkcję')
        return 1
    return funkcja

def calculate_Newton(a, b, precision, Newton_error_label):
    Newton_error_label.config(text='')
    float_a = 0
    float_b = 0
    float_precision = 0

    function = get_function()
    if (function == 1): return

    if(var_infinity.get() == 0):
        try:
            float_a = float(a)
            float_b = float(b)
            float_precision = float(precision)
            if(float_b < float_a):
                float_a, float_b = float_b, float_a
            if(float_precision <= 0):
                raise ValueError("ValueError")
        except ValueError:
            Newton_error_label.config(text='Podaj rzeczywiste a, b oraz dokładność > 0')
            return
        if(float_a == float_b):
            result = 0
            Newton_result_label.config(text='Wynik: 0')
            return
    else:
        try:
            float_a = float(a)
            float_precision = float(precision)
            if(float_precision <= 0):
                raise ValueError("ValueError")
        except ValueError:
            Newton_error_label.config(text='Podaj rezeczywiste b oraz dokładność > 0')
            return
    
    if(var_infinity.get() == 1):
        result = simpson_infninty(float_a, float_precision, function, var_weight_ex.get())
    else:
        result = simpson(float_a, float_b, float_precision, function, var_weight_ex.get())
    
    text_result = 'Wynik: ' + str(result)
    Newton_result_label.config(text=text_result)
    return


def calculate_Gauss(Gauss_error_label):
    Gauss_error_label.config(text='')
    
    function = get_function()
    if (function == 1): return

    if(node_2.get() == 1 and node_3.get() == 0 and node_4.get() == 0 and node_5.get() == 0):
        result = GaussLaguerreRule(2, function)
    elif(node_2.get() == 0 and node_3.get() == 1 and node_4.get() == 0 and node_5.get() == 0):
        result = GaussLaguerreRule(3, function)
    elif(node_2.get() == 0 and node_3.get() == 0 and node_4.get() == 1 and node_5.get() == 0):
        result = GaussLaguerreRule(4, function)
    elif(node_2.get() == 0 and node_3.get() == 0 and node_4.get() == 0 and node_5.get() == 1):
        result = GaussLaguerreRule(5, function)
    else:
        Gauss_error_label.config(text='Wybierz ilość węzłów')
        return
    text_result = 'Wynik: ' + str(result)
    Gauss_result_label.config(text=text_result)


window = Tk()
window.title('Metody numeryczne - zadanie 4')
window.geometry('800x450')

var_linear = IntVar()
var_absolute = IntVar()
var_reciprocal = IntVar()
var_polynomial = IntVar()
var_trygonometric = IntVar()
var_infinity = IntVar()
var_weight_ex = IntVar()
node_2 = IntVar()
node_3 = IntVar()
node_4 = IntVar()
node_5 = IntVar()

function_frame = Frame(window, height=100, width=800)
Newton_frame = Frame(window, height=300, width=400)
Newton_range_frame = Frame(Newton_frame, height=200, width=400)
Newton_precision_frame = Frame(Newton_frame, height=100, width=400)
Gauss_frame = Frame(window, height=300, width=400)
Gauss_nodes_frame = Frame(Gauss_frame, height=100, width=400)


# functions frame 
choose_function_label = Label(function_frame, text='Wybierz funkcję:', font=('Helvetica', 12))
choose_function_label.pack()

linear_check = Checkbutton(function_frame, text='2x + 5', variable=var_linear, onvalue=1, offvalue=0)
linear_check.pack(anchor='w')
absolute_check= Checkbutton(function_frame, text='|x|', variable=var_absolute, onvalue=1, offvalue=0)
absolute_check.pack(anchor='w')
reciprocal_check = Checkbutton(function_frame, text='1/x', variable=var_reciprocal, onvalue=1, offvalue=0)
reciprocal_check.pack(anchor='w')
polynomial_check = Checkbutton(function_frame, text='2x^3 - 2x', variable=var_polynomial, onvalue=1, offvalue=0)
polynomial_check.pack(anchor='w')
trygonometric_check = Checkbutton(function_frame, text='2sin(x)', variable=var_trygonometric, onvalue=1, offvalue=0)
trygonometric_check.pack(anchor='w')
function_error_label = Label(function_frame, text="", font=('Helvetica', 12), fg='red')
function_error_label.pack()


# Newton frame
function_label = Label(Newton_frame, text='KWADRATURA NEWTONA:', font=('Helvetica', 12))
function_label.pack()
Newton_header_label = Label(Newton_frame, text='Całkowanie na przedziale [a; b] lub [a; +oo)', font=('Helvetica', 10))
Newton_header_label.pack()

# Newton range frame
# a
a_label = Label(Newton_range_frame, padx=1, text="a: ")
a_label.grid(row=0, column=0)
a_entry = Entry(Newton_range_frame, width=4)
a_entry.grid(row=0, column=1, ipady=1)
# b
b_label = Label(Newton_range_frame, padx=1, text="b: ")
b_label.grid(row=1, column=0)
b_entry = Entry(Newton_range_frame, width=4)
b_entry.grid(row=1, column=1, ipady=1)
b_infinity_check = Checkbutton(Newton_range_frame, text='[a; +oo)', variable=var_infinity, onvalue=1, offvalue=0)
b_infinity_check.grid(row=1, column=2, padx=5)
Newton_range_frame.pack()

# precision frame
precision_label = Label(Newton_precision_frame, padx=1, text="dokładność: ")
precision_label.grid(row=0, column=0)
precision_entry = Entry(Newton_precision_frame, width=8)
precision_entry.grid(row=0, column=1)
Newton_precision_frame.pack()

# weight
weight_ex_check = Checkbutton(Newton_frame, text='dodaj wagę e^(-x)', variable=var_weight_ex, onvalue=1, offvalue=0)
weight_ex_check.pack()
# result
Newton_result_label = Label(Newton_frame, text='Wynik: ', font=('Helvetica', 12), pady=5)
Newton_result_label.pack()
Newton_calculate_button = Button(Newton_frame, text='OBLICZ', width=25, font=('Helvetica bold', 12), command=lambda:calculate_Newton(a_entry.get(), b_entry.get(), precision_entry.get(), Newton_error_label))
Newton_calculate_button.pack(pady=10, anchor='s')
# error
Newton_error_label = Label(Newton_frame, text="", font=('Helvetica', 12), fg='red')
Newton_error_label.pack()


# Gauss frame
Gauss_title_label = Label(Gauss_frame, text='KWADRATURA GAUSSA:', font=('Helvetica', 12))
Gauss_title_label.pack()
Gauss_header_label = Label(Gauss_frame, text='Całkowanie na przedziale [0; +oo) z wagą e^(-x)', font=('Helvetica', 10))
Gauss_header_label.pack()
Label(Gauss_frame, text="").pack()
nodes_label = Label(Gauss_frame, text="liczba węzłów:")
nodes_label.pack()

# nodes frame
node_2_check = Checkbutton(Gauss_nodes_frame, text='2', variable=node_2, onvalue=1, offvalue=0)
node_2_check.grid(row=0,column=0)
node_3_check = Checkbutton(Gauss_nodes_frame, text='3', variable=node_3, onvalue=1, offvalue=0)
node_3_check.grid(row=0,column=1)
node_4_check = Checkbutton(Gauss_nodes_frame, text='4', variable=node_4, onvalue=1, offvalue=0)
node_4_check.grid(row=0,column=2)
node_5_check = Checkbutton(Gauss_nodes_frame, text='5', variable=node_5, onvalue=1, offvalue=0)
node_5_check.grid(row=0,column=3)
Gauss_nodes_frame.pack()
Label(Gauss_frame, text="", pady=3).pack()

# result
Gauss_result_label = Label(Gauss_frame, text='Wynik: ', font=('Helvetica', 12), pady=5)
Gauss_result_label.pack()
Gauss_calculate_button = Button(Gauss_frame, text='OBLICZ', width=25, font=('Helvetica', 12), command=lambda: calculate_Gauss(Gauss_error_label))
Gauss_calculate_button.pack(pady=10, anchor='s')
#error
Gauss_error_label = Label(Gauss_frame, text="", font=('Helvetica', 12), fg='red')
Gauss_error_label.pack()


function_frame.pack(pady=10)
Newton_frame.pack(side=LEFT, fill=BOTH, expand=True)
Gauss_frame.pack(side=LEFT, fill=BOTH, expand=True)

mainloop()