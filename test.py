from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('500x400')
ws.config(bg='#F2B33D')



Entry(ws, width=4,).grid(row=0, column=0, ipady=1)
Label(ws, padx=1, text="x^6 +").grid(row=0, column=1)
Entry(ws, width=4).grid(row=0, column=2, ipady=1)
Label(ws, text="x^5 +").grid(row=0, column=3)
Entry(ws, width=4).grid(row=0, column=4, ipady=1)
Label(ws, text="x^4 +").grid(row=0, column=5)
Entry(ws, width=4).grid(row=0, column=6, ipady=1)
Label(ws, text="x^3 +").grid(row=0, column=7)
Entry(ws, width=4).grid(row=0, column=8, ipady=1)
Label(ws, text="x^2 +").grid(row=0, column=9)
Entry(ws, width=4).grid(row=0, column=10, ipady=1)
Label(ws, text="x +").grid(row=0, column=11)
Entry(ws, width=4).grid(row=0, column=12, ipady=1)

ws.mainloop()