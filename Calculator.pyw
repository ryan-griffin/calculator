from tkinter import *
 
expression = ""
 
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
 
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
 
    except:
        equation.set(" error ")
        expression = ""
 
def clear():
    global expression
    expression = ""
    equation.set("")

root = Tk()
root.title("Calculator")
root.configure(bg="#35363A")

equation = StringVar()
expression_field = Entry(root, textvariable=equation, font=("Arial", 30), width=15, borderwidth=0, fg="white", bg="#35363A")
expression_field.grid(columnspan=4, pady=10)
 
button1 = Button(root, text=" 1 ", fg="white", bg="#202124", activeforeground="white", activebackground="#666871", command=lambda: press(1), font=("Arial", 20), height=1, width=5, borderwidth=0)
button1.grid(row=4, column=0, padx=2, pady=2)
 
button2 = Button(root, text=" 2 ", fg="white", bg="#202124", activeforeground="white", activebackground="#666871", command=lambda: press(2), font=("Arial", 20), height=1, width=5, borderwidth=0)
button2.grid(row=4, column=1, padx=2, pady=2)
 
button3 = Button(root, text=" 3 ", fg="white", bg="#202124", activeforeground="white", activebackground="#666871", command=lambda: press(3), font=("Arial", 20), height=1, width=5, borderwidth=0)
button3.grid(row=4, column=2, padx=2, pady=2)
 
button4 = Button(root, text=" 4 ", fg="white", bg="#202124", activeforeground="white", activebackground="#666871", command=lambda: press(4), font=("Arial", 20), height=1, width=5, borderwidth=0)
button4.grid(row=3, column=0, padx=2, pady=2)
 
button5 = Button(root, text=" 5 ", fg="white", bg="#202124", activeforeground="white", activebackground="#666871", command=lambda: press(5), font=("Arial", 20), height=1, width=5, borderwidth=0)
button5.grid(row=3, column=1, padx=2, pady=2)
 
button6 = Button(root, text=" 6 ", fg="white", bg="#202124", activeforeground="white", activebackground="#666871", command=lambda: press(6), font=("Arial", 20), height=1, width=5, borderwidth=0)
button6.grid(row=3, column=2, padx=2, pady=2)
 
button7 = Button(root, text=" 7 ", fg="white", bg="#202124", activeforeground="white", activebackground="#666871", command=lambda: press(7), font=("Arial", 20), height=1, width=5, borderwidth=0)
button7.grid(row=2, column=0, padx=2, pady=2)
 
button8 = Button(root, text=" 8 ", fg="white", bg="#202124", activeforeground="white", activebackground="#666871", command=lambda: press(8), font=("Arial", 20), height=1, width=5, borderwidth=0)
button8.grid(row=2, column=1, padx=2, pady=2)
 
button9 = Button(root, text=" 9 ", fg="white", bg="#202124", activeforeground="white", activebackground="#666871", command=lambda: press(9), font=("Arial", 20), height=1, width=5, borderwidth=0)
button9.grid(row=2, column=2, padx=2, pady=2)
 
button0 = Button(root, text=" 0 ", fg="white", bg="#202124", activeforeground="white", activebackground="#666871", command=lambda: press(0), font=("Arial", 20), height=1, width=5, borderwidth=0)
button0.grid(row=5, column=1, padx=2, pady=2)
 
plus = Button(root, text=" + ", fg="white", bg="#202124", activeforeground="white", activebackground="#666871", command=lambda: press("+"), font=("Arial", 20), height=1, width=5, borderwidth=0)
plus.grid(row=2, column=3, padx=2, pady=2)
 
minus = Button(root, text=" - ", fg="white", bg="#202124", activeforeground="white", activebackground="#666871", command=lambda: press("-"), font=("Arial", 20), height=1, width=5, borderwidth=0)
minus.grid(row=3, column=3, padx=2, pady=2)
 
multiply = Button(root, text=" * ", fg="white", bg="#202124", activeforeground="white", activebackground="#666871", command=lambda: press("*"), font=("Arial", 20), height=1, width=5, borderwidth=0)
multiply.grid(row=4, column=3, padx=2, pady=2)
 
divide = Button(root, text=" / ", fg="white", bg="#202124", activeforeground="white", activebackground="#666871", command=lambda: press("/"), font=("Arial", 20), height=1, width=5, borderwidth=0)
divide.grid(row=5, column=3, padx=2, pady=2)
 
equal = Button(root, text=" = ", fg="white", bg="#202124", activeforeground="white", activebackground="#666871", command=equalpress, font=("Arial", 20), height=1, width=5, borderwidth=0)
equal.grid(row=6, column=3, padx=2, pady=2)
 
clear = Button(root, text="C", fg="white", bg="#202124", activeforeground="white", activebackground="#666871", command=clear, font=("Arial", 20), height=1, width=5, borderwidth=0)
clear.grid(row=5, column=0, padx=2, pady=2)
 
Decimal= Button(root, text=".", fg="white", bg="#202124", activeforeground="white", activebackground="#666871", command=lambda: press("."), font=("Arial", 20), height=1, width=5, borderwidth=0)
Decimal.grid(row=5, column=2, padx=2, pady=2)

root.mainloop()