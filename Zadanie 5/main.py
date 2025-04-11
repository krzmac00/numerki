import matplotlib.pyplot as plt
from tkinter import *
from approximation import *
import numpy as np

def get_function():
    function_error_label.config(text='')
    if(var_linear.get() == 1 and var_absolute.get() == 0 and var_complex.get() == 0 and var_polynomial.get() == 0 and var_trygonometric.get() == 0):
        funkcja = Wielomian([2,5])
    elif(var_linear.get() == 0 and var_absolute.get() == 1 and var_complex.get() == 0 and var_polynomial.get() == 0 and var_trygonometric.get() == 0):
        funkcja = Modul()
    elif(var_linear.get() == 0 and var_absolute.get() == 0 and var_complex.get() == 1 and var_polynomial.get() == 0 and var_trygonometric.get() == 0):
        funkcja = Zlozona()
    elif(var_linear.get() == 0 and var_absolute.get() == 0 and var_complex.get() == 0 and var_polynomial.get() == 1 and var_trygonometric.get() == 0):
        funkcja = Wielomian([2,0,-2,0])
    elif(var_linear.get() == 0 and var_absolute.get() == 0 and var_complex.get() == 0 and var_polynomial.get() == 0 and var_trygonometric.get() == 1):
        funkcja = Trygonometryczna()
    else:
        function_error_label.config(text='Wybierz jedną funkcję')
        return 1
    return funkcja

def approximate(a, b, degree, nodes, error_label):
    error_label.config(text='')
    float_a = 0
    float_b = 0
    int_degree = 0
    int_nodes = 0

    function = get_function()
    if (function == 1): return

    try:
        float_a = float(a)
        float_b = float(b)
        if(float_b < float_a):
            float_a, float_b = float_b, float_a
    except ValueError:
        error_label.config(text='Podaj rzeczywiste a, b')
        return
    if(float_a == float_b):
        approximation_error_label.config(text='Błąd aproksymacji: 0')
        return
    
    try:
        int_degree = int(degree)
        if(int_degree <= 0):
            raise ValueError("ValueError")
    except ValueError:
        error_label.config(text='Stopień wielomianu musi być większy od 0')
        return
    
    try:
        int_nodes = int(nodes)
        if(int_nodes < 1):
            raise ValueError("ValueError")
    except ValueError:
        error_label.config(text='Liczba węzłów musi być większy od 1')
        return

    factors = np.zeros(int_degree + 1)
    for i in range(int_degree + 1):
        factors[i] = laguerre_factors(function, int_nodes, i)

    xs = np.linspace(float_a, float_b, 1000, endpoint=True)
    ys = []
    for x in xs:
        yi = 0.0
        for i in range(int_degree + 1):
            yi += factors[i] * laguerre(i, x)
        ys.append(yi)

    xs2 = np.linspace(float_a, float_b, 1000, endpoint=True)
    ys2 = []
    for x in xs2:
        ys2.append(function.function_at_x(x))

    plt.plot(xs, ys, 'r', label='approximation')
    plt.plot(xs2, ys2, 'y', label='real')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(title='Legenda', loc='best', fontsize='xx-small')
    plt.grid(b=True, axis='both')
    plt.show()

    error = mean_error(ys, ys2)
    text = 'Błąd aproksymacji: ' + str(error)
    approximation_error_label.config(text=text)

window = Tk()
window.title('Metody numeryczne - zadanie 5')
window.geometry('800x450')

var_linear = IntVar()
var_absolute = IntVar()
var_complex = IntVar()
var_polynomial = IntVar()
var_trygonometric = IntVar()

function_frame = Frame(window, height=200, width=800)
range_frame = Frame(window, height=200, width=400)
degree_frame = Frame(window, height=100, width=400)


# functions frame 
choose_function_label = Label(function_frame, text='Wybierz aproksymowaną funkcję:', font=('Helvetica', 12))
choose_function_label.pack()

linear_check = Checkbutton(function_frame, text='2x + 5', variable=var_linear, onvalue=1, offvalue=0)
linear_check.pack(anchor='w')
absolute_check= Checkbutton(function_frame, text='|2x - 3|', variable=var_absolute, onvalue=1, offvalue=0)
absolute_check.pack(anchor='w')
complex_check = Checkbutton(function_frame, text='2sin^2(x) - cos(x+2)', variable=var_complex, onvalue=1, offvalue=0)
complex_check.pack(anchor='w')
polynomial_check = Checkbutton(function_frame, text='2x^3 - 2x', variable=var_polynomial, onvalue=1, offvalue=0)
polynomial_check.pack(anchor='w')
trygonometric_check = Checkbutton(function_frame, text='2sin(x)', variable=var_trygonometric, onvalue=1, offvalue=0)
trygonometric_check.pack(anchor='w')
function_error_label = Label(function_frame, text="", font=('Helvetica', 12), fg='red')
function_error_label.pack()
function_frame.pack(pady=10)

#range
range_header_label = Label(window, text='Przedział aproksymacji:', font=('Helvetica', 10))
range_header_label.pack()
# range frame
# a
a_label = Label(range_frame, padx=1, text="a: ")
a_label.grid(row=0, column=0)
a_entry = Entry(range_frame, width=4)
a_entry.grid(row=0, column=1, ipady=1)
# b
b_label = Label(range_frame, padx=1, text="b: ")
b_label.grid(row=1, column=0)
b_entry = Entry(range_frame, width=4)
b_entry.grid(row=1, column=1, ipady=1)
range_frame.pack()


# degree frame
degree_label = Label(degree_frame, padx=1, text="stopień wielomianu:")
degree_label.grid(row=0, column=0)
degree_entry = Entry(degree_frame, width=8)
degree_entry.grid(row=0, column=1)


# nodes
node_label = Label(degree_frame, padx=1, text="liczba węzłów:")
node_label.grid(row=1, column=0)
node_entry = Entry(degree_frame, width=8)
node_entry.grid(row=1, column=1)
degree_frame.pack()

#error
error_label = Label(window, text="", font=('Helvetica', 12), fg='red')
error_label.pack()

# result
approximate_button = Button(window, text='APROKSYMACJA', width=25, font=('Helvetica', 12), 
                            command=lambda: approximate(a_entry.get(), b_entry.get(), degree_entry.get(), node_entry.get(), error_label))
approximate_button.pack(pady=10, anchor='s')
approximation_error_label = Label(window, text='Błąd aproksymacji: ', font=('Helvetica', 12), pady=5)
approximation_error_label.pack()

mainloop()