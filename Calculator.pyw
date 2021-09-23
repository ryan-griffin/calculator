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
 
if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="grey")
    gui.title("Calculator")

    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation, font=("Arial", 30), width=15,)
    expression_field.grid(columnspan=4, pady=13)
 
    button1 = Button(gui, text=' 1 ', fg='black', bg='white',
                    command=lambda: press(1), font=("Arial", 20), height=1, width=5)
    button1.grid(row=2, column=0)
 
    button2 = Button(gui, text=' 2 ', fg='black', bg='white',
                    command=lambda: press(2), font=("Arial", 20), height=1, width=5)
    button2.grid(row=2, column=1)
 
    button3 = Button(gui, text=' 3 ', fg='black', bg='white',
                    command=lambda: press(3), font=("Arial", 20), height=1, width=5)
    button3.grid(row=2, column=2)
 
    button4 = Button(gui, text=' 4 ', fg='black', bg='white',
                    command=lambda: press(4), font=("Arial", 20), height=1, width=5)
    button4.grid(row=3, column=0)
 
    button5 = Button(gui, text=' 5 ', fg='black', bg='white',
                    command=lambda: press(5), font=("Arial", 20), height=1, width=5)
    button5.grid(row=3, column=1)
 
    button6 = Button(gui, text=' 6 ', fg='black', bg='white',
                    command=lambda: press(6), font=("Arial", 20), height=1, width=5)
    button6.grid(row=3, column=2)
 
    button7 = Button(gui, text=' 7 ', fg='black', bg='white',
                    command=lambda: press(7), font=("Arial", 20), height=1, width=5)
    button7.grid(row=4, column=0)
 
    button8 = Button(gui, text=' 8 ', fg='black', bg='white',
                    command=lambda: press(8), font=("Arial", 20), height=1, width=5)
    button8.grid(row=4, column=1)
 
    button9 = Button(gui, text=' 9 ', fg='black', bg='white',
                    command=lambda: press(9), font=("Arial", 20), height=1, width=5)
    button9.grid(row=4, column=2)
 
    button0 = Button(gui, text=' 0 ', fg='black', bg='white',
                    command=lambda: press(0), font=("Arial", 20), height=1, width=5)
    button0.grid(row=5, column=1)
 
    plus = Button(gui, text=' + ', fg='black', bg='white',
                command=lambda: press("+"), font=("Arial", 20), height=1, width=5)
    plus.grid(row=2, column=3)
 
    minus = Button(gui, text=' - ', fg='black', bg='white',
                command=lambda: press("-"), font=("Arial", 20), height=1, width=5)
    minus.grid(row=3, column=3)
 
    multiply = Button(gui, text=' * ', fg='black', bg='white',
                    command=lambda: press("*"), font=("Arial", 20), height=1, width=5)
    multiply.grid(row=4, column=3)
 
    divide = Button(gui, text=' / ', fg='black', bg='white',
                    command=lambda: press("/"), font=("Arial", 20), height=1, width=5)
    divide.grid(row=5, column=3)
 
    equal = Button(gui, text=' = ', fg='black', bg='white',
                command=equalpress, font=("Arial", 20), height=1, width=5)
    equal.grid(row=6, column=3)
 
    clear = Button(gui, text='Clear', fg='black', bg='white',
                command=clear, font=("Arial", 20), height=1, width=5)
    clear.grid(row=5, column=0)
 
    Decimal= Button(gui, text='.', fg='black', bg='white',
                    command=lambda: press('.'), font=("Arial", 20), height=1, width=5)
    Decimal.grid(row=5, column=2)

    gui.mainloop()