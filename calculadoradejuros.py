from tkinter import *

def clear_all():
    
    princeple_field.delete(0,END)
    rate_field.delete(0,END)
    time_field.delete(0,END)
    compound_field.delete(0,END)

    princeple_field.focus_set()

def calculate_ci():
    princeple = int(princeple_field.get())
    rate = float(rate_field.get())
    time = int(time_field.get())

    CI = princeple *(pow((1+rate/100),time))

    compound_field.insert(10,CI)


if __name__ == "__main__":

    gui = Tk()

    gui.config(background="light green")
    gui.title("Calculadora de taxa")
    gui.geometry("400x250")


    label1 = Label(gui, text="TOTAL DINHEIRO : ", fg='black', bg='red')
    label2 = Label(gui, text="TAXA : ", fg='black', bg='red')
    label3 = Label(gui, text="TEMPO : ", fg='black', bg='red')
    label4 = Label(gui, text="TOTAL COM JUROS : ", fg='black', bg='red')

    label1.grid(row=1, column=0, padx=10, pady=10)
    label2.grid(row=2, column=0, padx=10, pady=10)
    label3.grid(row=3, column=0, padx=10, pady=10)
    label4.grid(row=4, column=0, padx=10, pady=10)

    princeple_field = Entry(gui)
    rate_field = Entry(gui)
    time_field = Entry(gui)
    compound_field = Entry(gui)

    princeple_field.grid(row=1, column=1, padx=10, pady=10)
    rate_field.grid(row=2, column=1, padx=10, pady=10)
    time_field.grid(row=3, column=1, padx=10, pady=10)
    compound_field.grid(row=4, column=1, padx=10, pady=10)


    button1 = Button(gui, text="CALCULAR", bg="red", fg="black", command=calculate_ci)
    button2 = Button(gui, text="LIMPAR TUDO", bg="red", fg="black", command=clear_all)

    button1.grid(row=5, column=1, pady=10)
    button2.grid(row=6, column=1, pady=10)

gui.mainloop()