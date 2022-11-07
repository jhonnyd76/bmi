from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.lbl = Label(master, text="Hallo Welt")
        self.lbl.pack()


root = Tk()
app = Application(master=root)
app.mainloop()
