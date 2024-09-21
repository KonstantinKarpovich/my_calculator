from tkinter import *
from tkinter import ttk
import pyperclip


def press_key(event):
    if event.char in "+-*/.":
        add_operation(event.char)
    elif event.char.isdigit():
        click_button(event.char)
    elif event.char == "=" or event.char == "\r":
        total_results()
    elif event.char == "\x08":
        clear_last()
    elif event.char in "vVмМ":
        add_clipboard()


def add_clipboard():
    flag = True
    for i in pyperclip.paste():
        if i in "01234567890+-*/.=":
            flag = True
        else:
            flag = False
            field['state'] = "normal"
            field.delete(0, END)
            field.insert(END, "Ошибка ввода")
            field['state'] = "disabled"
    if flag == True:
        clipboard = pyperclip.paste()
        for i in clipboard:
            if i in "+-*/.":
                add_operation(i)
            elif i == "=":
                # total_results()
                return "break"
            else:
                click_button(i)


def click_button(value):
    if field.get() == "0":
        field['state'] = "normal"
        field.delete(0, END)
        field.insert(END, value)
        field['state'] = "disabled"
    elif field.get() == "Ошибка" or field.get() == "Делить на 0 нельзя" or field.get() == "Ошибка ввода":
        field['state'] = "normal"
        field.delete(0, END)
        field.insert(END, value)
        field['state'] = "disabled"
    else:
        field['state'] = "normal"
        field.insert(END, value)
        field['state'] = "disabled"


def add_operation(operation):
    expression = field.get()
    if expression[-1] in "+-*/.":
        expression = expression[:-1]
        field['state'] = "normal"
        field.delete(0, END)
        field.insert(END, expression + operation)
        field['state'] = "disabled"
    elif field.get() == "Ошибка" or field.get() == "Делить на 0 нельзя" or field.get() == "Ошибка ввода":
        field['state'] = "normal"
        field.delete(0, END)
        field.insert(END, "0" + operation)
        field['state'] = "disabled"
    else:
        field['state'] = "normal"
        field.insert(END, operation)
        field['state'] = "disabled"


def clear_last():
    if field.get() == "":
        field['state'] = "normal"
        field.insert(0, "0")
        field['state'] = "disabled"
    elif len(field.get()) == 1:
        field['state'] = "normal"
        field.delete(0, END)
        field.insert(0, "0")
        field['state'] = "disabled"
    elif field.get() == "Ошибка" or field.get() == "Делить на 0 нельзя" or field.get() == "Ошибка ввода":
        field['state'] = "normal"
        field.delete(0, END)
        field.insert(0, "0")
        field['state'] = "disabled"
    else:
        field['state'] = "normal"
        field.delete(len(field.get()) - 1)
        field['state'] = "disabled"


def clear_all():
    field['state'] = "normal"
    field.delete(0, END)
    field.insert(0, "0")
    field['state'] = "disabled"


def total_results():
    expression = field.get()
    if expression == "Ошибка" or expression == "Делить на 0 нельзя" or field.get() == "Ошибка ввода":
        clear_last()
    else:
        try:
            field['state'] = "normal"
            total = (eval(expression))
            field.delete(0, END)
            field.insert(END, total)
            field['state'] = "disabled"

        except ZeroDivisionError:
            field['state'] = "normal"
            field.delete(0, END)
            field.insert(0, 'Делить на 0 нельзя')
            field['state'] = "disabled"

        except SyntaxError:
            field['state'] = "normal"
            field.delete(0, END)
            field.insert(0, 'Ошибка')
            field['state'] = "disabled"


window = Tk()
window.title("Калькулятор")
x = window.winfo_screenwidth() // 2 - 200
y = window.winfo_screenheight() // 2 - 300
window.geometry(f"400x600+{x}+{y}")
window.resizable(False, False)

window.bind("<Key>", press_key)

field = ttk.Entry(window, state=DISABLED, justify=RIGHT, font=("Arial", 30), foreground="#000000")
field['state'] = "normal"
field.insert(0, "0")
field['state'] = "disabled"
field.place(x=0, y=0, width=400, height=100)

s = ttk.Style()
s.configure('TButton', font=('Arial', 15))

btn_1_1 = ttk.Button(window, text="C", command=lambda: clear_all())
btn_1_1.place(x=0, y=100, width=100, height=100)

btn_1_2 = ttk.Button(window, text="⤆", command=lambda: clear_last())
btn_1_2.place(x=100, y=100, width=100, height=100)

btn_1_3 = ttk.Button(window, text="(", command=lambda: click_button("("))
btn_1_3.place(x=200, y=100, width=100, height=100)

btn_1_4 = ttk.Button(window, text="/", command=lambda: add_operation("/"))
btn_1_4.place(x=300, y=200, width=100, height=100)

btn_2_1 = ttk.Button(window, text="7", command=lambda: click_button(7))
btn_2_1.place(x=0, y=200, width=100, height=100)

btn_2_2 = ttk.Button(window, text="8", command=lambda: click_button(8))
btn_2_2.place(x=100, y=200, width=100, height=100)

btn_2_3 = ttk.Button(window, text="9", command=lambda: click_button(9))
btn_2_3.place(x=200, y=200, width=100, height=100)

btn_2_4 = ttk.Button(window, text="*", command=lambda: add_operation("*"))
btn_2_4.place(x=300, y=300, width=100, height=100)

btn_3_1 = ttk.Button(window, text="4", command=lambda: click_button(4))
btn_3_1.place(x=0, y=300, width=100, height=100)

btn_3_2 = ttk.Button(window, text="5", command=lambda: click_button(5))
btn_3_2.place(x=100, y=300, width=100, height=100)

btn_3_3 = ttk.Button(window, text="6", command=lambda: click_button(6))
btn_3_3.place(x=200, y=300, width=100, height=100)

btn_3_4 = ttk.Button(window, text="-", command=lambda: add_operation("-"))
btn_3_4.place(x=300, y=400, width=100, height=100)

btn_4_1 = ttk.Button(window, text="1", command=lambda: click_button(1))
btn_4_1.place(x=0, y=400, width=100, height=100)

btn_4_2 = ttk.Button(window, text="2", command=lambda: click_button(2))
btn_4_2.place(x=100, y=400, width=100, height=100)

btn_4_3 = ttk.Button(window, text="3", command=lambda: click_button(3))
btn_4_3.place(x=200, y=400, width=100, height=100)

btn_4_4 = ttk.Button(window, text="+", command=lambda: add_operation("+"))
btn_4_4.place(x=300, y=500, width=100, height=100)

btn_5_1 = ttk.Button(window, text=".", command=lambda: add_operation("."))
btn_5_1.place(x=0, y=500, width=100, height=100)

btn_5_2 = ttk.Button(window, text="0", command=lambda: click_button(0))
btn_5_2.place(x=100, y=500, width=100, height=100)

btn_5_3 = ttk.Button(window, text=")", command=lambda: click_button(")"))
btn_5_3.place(x=300, y=100, width=100, height=100)

btn_5_4 = ttk.Button(window, text="=", command=lambda: total_results())
btn_5_4.place(x=200, y=500, width=100, height=100)

window.mainloop()
