from tkinter import *


root = Tk()
root.title("Kantor")
root.geometry('450x300+200+200')
Listbox(root).grid(row=1, column =1, sticky=W)

Label(root,text="Waluta źródłowa").grid(row=0, column =0, sticky = E, pady = 4)
Label(root,text="Waluta końcowa").grid(row=0, column =4, sticky = S, pady = 4)
#Label(root,text="Imię").grid(row=0)
#Label(root,text="Nazwisko").grid(row=1,sticky=W)

#e1 = Entry(root)
#e2 = Entry(root)
#e1.grid(row=0,column=0)
#e2.grid(row=1,column=1)

root.mainloop()

