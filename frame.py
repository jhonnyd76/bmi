from tkinter import *
master = Tk()
mainFrame = Frame(master, width=300, height=200, bg="red")

secondFrame = Frame(master, width=300, height=200, bg="blue")

thirdFrame = Frame(master, width=200, height=200, bg="yellow")

Label(secondFrame, text="Hallo Welt").place(x=10, y=10)

mainFrame.pack()

secondFrame.pack()
thirdFrame.pack()
master.mainloop()