from tkinter import *

root = Tk()

opChoose = ""

def addNumber(number):
    currentValue = str(input.get())
    input.delete(0, END)
    input.insert(0, currentValue + number)

def sumBtn():
    global firstNumber
    firstNumber = int(input.get())
    input.delete(0, END)
    global opChoose
    opChoose = "+"


def minusBtn():
    global firstNumber
    firstNumber = int(input.get())
    input.delete(0, END)
    global opChoose
    opChoose = "-"

def multBtn():
    global firstNumber
    firstNumber = int(input.get())
    input.delete(0, END)
    global opChoose
    opChoose = "*"

def dividBtn():
    global firstNumber
    firstNumber = int(input.get())
    input.delete(0, END)
    global opChoose
    opChoose = "/"

def equalBtn():
    secondNumber = int(input.get())
    input.delete(0, END)
    if (opChoose == "+"):
        input.insert(0, firstNumber + secondNumber)
    if (opChoose == "-"):
        input.insert(0, firstNumber - secondNumber)
    if (opChoose == "*"):
        input.insert(0, firstNumber * secondNumber)
    if (opChoose == "/"):
        input.insert(0, firstNumber / secondNumber)


#Input
input = Entry(root, border=5, width=35)
input.grid(row=0, column=0, columnspan=3)

#Buttons number
button1 = Button(root, text="1", padx=30, pady=10, command= lambda: addNumber("1"))
button2 = Button(root, text="2", padx=30, pady=10, command= lambda: addNumber("2"))
button3 = Button(root, text="3", padx=30, pady=10, command= lambda: addNumber("3"))
button4 = Button(root, text="4", padx=30, pady=10, command= lambda: addNumber("4"))
button5 = Button(root, text="5", padx=30, pady=10, command= lambda: addNumber("5"))
button6 = Button(root, text="6", padx=30, pady=10, command= lambda: addNumber("6"))
button7 = Button(root, text="7", padx=30, pady=10, command= lambda: addNumber("7"))
button8 = Button(root, text="8", padx=30, pady=10, command= lambda: addNumber("8"))
button9 = Button(root, text="9", padx=30, pady=10, command= lambda: addNumber("9"))
button0 = Button(root, text="0", padx=67, pady=10, command= lambda: addNumber("0"))

#Operators numbers
buttonPlus = Button(root, text="+", padx=30, pady=10, command=sumBtn)
buttonMinus = Button(root, text="-", padx=30, pady=10, command=minusBtn)
buttonMult = Button(root, text="x", padx=30, pady=10, command=multBtn)
buttonDivi = Button(root, text="÷", padx=30, pady=10, command=dividBtn)

#Equal button
buttonEqual = Button(root, text="=", padx= 105, pady=10, command=equalBtn)

#Buttons positions
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button0.grid(row=4, column=0, columnspan=2)
buttonPlus.grid(row=4, column=2)
buttonMinus.grid(row=5, column=0)
buttonMult.grid(row=5, column=1)
buttonDivi.grid(row=5, column=2)
buttonEqual.grid(row=6, columnspan=3)


root.resizable(False, False)
root.title("Calculator")
root.mainloop()
