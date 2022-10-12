from tkinter import *


class Rahmen(Frame):
    def __init__(self, master=None, lblText=""):
        Frame.__init__(self, master)
        self.pack()
        self.label = Label(self, text=lblText, width=30, anchor=W)
        self.label.pack(side="left")
        self.text = StringVar()
        self.entry = Entry(self, width=30, textvariable=self.text)
        self.entry.pack(side="right")


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        master.focus = True
        self.nameFrame = Rahmen(master, "Name:")
        self.firstFrame = Rahmen(master, "Firstname:")
        self.heightFrame = Rahmen(master, "Grösse:")
        self.weightFrame = Rahmen(master, "Gewicht:")
        self.btnFrame = Frame(master)
        self.btnFrame.pack()
        self.okBtn = Button(
            self.btnFrame, text="OK", width=20)
        self.okBtn['command'] = self.action
        self.cancelBtn = Button(
            self.btnFrame, text="Cancel", width=20, command=root.destroy)
        self.okBtn.pack(side="left")
        self.cancelBtn.pack(side="right")

    def action(self):
        print(self.nameFrame.text.get())


root = Tk()
Application(master=root)
root.mainloop()
