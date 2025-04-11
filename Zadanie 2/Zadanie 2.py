from tkinter import *
from timeit import default_timer as timer

def show_results(vector, row_count, result_frame, result_label, results):
    results.clear()
    result_label.config(text='', font=14)
    for i in range(row_count):
        text = str(vector[i])
        l = Label(result_frame, text='x%d = ' % (i+1) + text, font=14)
        l.grid(row=0, column=i)
        results.append(l)
    
def get_input(row_count, rows, vector_rows, matrix, vector):
    counter = 0
    for i in range(row_count):
        for j in range(row_count):
            matrix[i][j] = float(rows[counter].get())
            counter += 1
    for i in range(row_count):
        vector[i] = float(vector_rows[i].get())

def jordan_generate_results(rows, vector_rows, matrix, vector, result_label, result_frame, results, time_label):
    for label in results:
        label.destroy()
    row_count = len(vector)
    get_input(row_count, rows, vector_rows, matrix, vector)
    row_buf = [0] * row_count # przechowywanie współczynników wiersza macierzy
    start = timer()
    for n in range(row_count):
        for row in matrix:
            row_copy = [round(x, 8) for x in row]     # kopia wiersza z zaokrągleniem wartości do 8. miejsca po przecinku
            if row_copy == [0] * row_count:        # sprawdzenie czy współczynniki macierzy są zerowe
                vector_copy = [round(x, 8) for x in vector] # kopia przybliżonego wektora
                if vector_copy[matrix.index(row)] == 0: # sprawdzenie czy wektor jest zerowy
                    result_label.config(text='Układ nieoznaczony', font=14)
                    result_label.grid(row=0, column=0)
                    return
                else:
                    result_label.config(text='Układ sprzeczny', font=14)
                    result_label.grid(row=0, column=0)
                    return
        max = abs(matrix[n][n])
        index = n   # indeks aktualnego wiersza
        for i in range(row_count - n): # iteracje po wartościach wiersza macierzy w celu znalezienia elementu podstawowego (max) w kolumnie
            if abs(matrix[n + i][n]) > max:
                max = abs(matrix[n + i][n])
                index = n + i
        if index != n: # jeżeli indeks elementu podstawowego nie jest tożsamy z indeksem aktualnego wiersza to wiersz z elementem podstawowym zamieniamy z aktualnym wierszem macierzy
            for i in range(row_count):
                row_buf[i] = matrix[n][i]
                matrix[n][i] = matrix[index][i]
                matrix[index][i] = row_buf[i]
            vector[index], vector[n] = vector[n], vector[index] # zamiana aktualnego wiersza macierzy z wierszem z elementem podstawowym
        primary = matrix[n][n]  # zapis wartości elementu podstawowego do zmiennej primary
        vector[n] /= primary    # dzielenie wiersza wektora przez element podstawowy
        for i in range(row_count - n):
            matrix[n][n + i] /= primary   # dzielenie wiersza macierzy przez element podstawowy
        for i in range(row_count):
            if i != n:      # odejmowanie od pozostałych wierszy
                matrix_in = matrix[i][n]
                vector[i] -= vector[n] * matrix_in
                for j in range(row_count):
                    matrix[i][j] -= matrix[n][j] * matrix_in
    end = timer()
    time = "Czas wykonania: " + str(end - start) + " sec"
    time_label.config(text=time, font=14)
    vector = [round(x, 8) for x in vector] # przybliżenie wartości
    show_results(vector, row_count, result_frame, result_label, results)

def show_matrix(rows, vector_rows, size, matrix, matrix_frame, vector, vector_frame):
    rows.clear()
    vector_rows.clear()
    for i in range(size):
        for j in range(size):
            e = Entry(matrix_frame, relief=GROOVE)
            e.grid(row=i, column=j, sticky=NSEW)
            e.insert(END, matrix[i][j])
            rows.append(e)
    matrix_frame.pack(side=LEFT)
    for i in range(size):
        e = Entry(vector_frame, relief=GROOVE)
        e.grid(row=i, column=0, sticky=NSEW)
        e.insert(END, vector[i])
        vector_rows.append(e)
    vector_frame.pack(side=LEFT)
        
def load_matrix(rows, vector_rows, matrix, vector, size, matrix_frame, vector_frame):
    matrix.clear()
    vector.clear()
    for entry in rows:
        entry.destroy()
    for entry in vector_rows:
        entry.destroy()
    with open("dane.txt", 'r') as data:
        file_line = data.read().splitlines()
    file_line_copy = file_line.copy()
    for item in file_line_copy:
        if item in '':
            del file_line[file_line.index(item)]
    size = len(file_line)
    lines = []
    for line_number in file_line:
        number = ""
        for digit in line_number[:line_number.index("|")+1]:
            if digit in ".-0123456789":
                number += digit
            else:
                if number:
                    lines.append(float(number))
                number = ""
        for digit in line_number[line_number.index("|") + 1:]:
            if digit in ".-0123456789":
                number += digit
            else:
                if number:
                    vector.append(float(number))
                number = ""
        vector.append(float(number))

    for i in range(size):
        matrix.append(list(lines[(i * size):((i + 1) * size)]))
    show_matrix(rows, vector_rows, size, matrix, matrix_frame, vector, vector_frame)

matrix = []
vector = []
size = 0
rows = []
vector_rows = []
results = []

window = Tk()
window.title('Metody numeryczne - zadanie 2')
window.geometry('1000x600')

button_frame = Frame(window, height=200, width=600, pady=20)
label_frame = Frame(window, height=200, width=600, pady=20)
input_frame = Frame(window, height=400, width=600, pady=20)
matrix_frame = Frame(input_frame, height=800, width=500)
vector_frame = Frame(input_frame, height=800, width=100)
result_title_frame = Frame(window, height=50, width=600)
result_info_frame = Frame(window, height=50, width=600)
result_frame = Frame(window, height=50, width=600)
time_frame = Frame(window, height=50, width=600, pady=20)

load_button = Button(button_frame, text='WCZYTAJ DANE Z PLIKU', width=25, font=('Helvetica bold', 12), command=lambda:load_matrix(rows, vector_rows, matrix, vector, size, matrix_frame, vector_frame))
load_button.grid(row=0, column=0, padx=50)
results_button = Button(button_frame, text='GENERUJ WYNIKI', width=25, font=('Helvetica bold', 12), command=lambda:jordan_generate_results(rows, vector_rows, matrix, vector, result_label, result_frame, results, time_label))
results_button.grid(row=0, column=1, padx=50)
matrix_label = Label(label_frame, text='Macierz:', font=('Helvetica bold', 14))
matrix_label.grid(row=0, column=0, padx=(0,500))
vector_label = Label(label_frame, text='Wektor:', font=('Helvetica bold', 14))
vector_label.grid(row=0, column=1, padx=(0,50))
result_title_label = Label(result_title_frame, text='WYNIKI:', font=('Helvetica bold', 14))
result_title_label.pack()
result_label = Label(result_info_frame, text='')
time_label = Label(time_frame, text='', font=14)
time_label.pack()


button_frame.pack()
label_frame.pack()
matrix_frame.pack(side=LEFT, padx=20)
vector_frame.pack(side=LEFT, padx=20)
input_frame.pack()
result_title_frame.pack()
result_info_frame.pack()
result_frame.pack()
time_frame.pack()
mainloop()