from tkinter import *

master = Tk()
master.focus = True

nameFrame = Frame(master)
firstFrame = Frame(master)
btnFrame = Frame(master)
nameFrame.pack()
firstFrame.pack()
btnFrame.pack()
lblName = Label(nameFrame, text="Name:", width=30,anchor=W)
lblFirstname = Label(firstFrame, text="Firstname:", width=30, anchor=W)
entName = Entry(nameFrame, width=30)
entFirstname = Entry(firstFrame, width=30)

lblName.pack(side="left")
lblFirstname.pack(side="left")
entName.pack(side="right")
entFirstname.pack(side="right")

okBtn = Button(btnFrame, text="OK",width=20)
cancelBtn = Button(btnFrame, text="Cancel", width=20)

okBtn.pack(side="left")
cancelBtn.pack(side="right")

master.mainloop()