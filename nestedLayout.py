from tkinter import *

master = Tk()
mF = Frame(master)
mF.pack(fill=X)
hF = Frame(mF, width=500, height=50)
fF = Frame(mF, width=500, height=50)
cF = Frame(mF, width=500, height=300)
lb1 = Label(hF, text="Titel", bg="red", fg="black")
lb1.pack(fill=X, pady=20)
lb2 = Label(cF, text="Hauptinhalt", bg="yellow", fg="red")
lb2.place(x=50, y=20, width=200, height=50)
btn1 = Button(fF, text="OK", bg="yellow")
btn2 = Button(fF, text="Ende", bg="green")
btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
hF.pack(fill=X)
cF.pack(fill=X)

fF.pack(pady=20)
master.mainloop()
