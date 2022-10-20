from tkinter import *

from health.bmicalculator import User, BmiCalculator


class Rahmen(Frame):
    def __init__(self, master=None, lblText=""):
        Frame.__init__(self, master)
        self.pack()
        self.label = Label(self, text=lblText, width=30, anchor=W)
        self.label.pack(side="left")
        self.text = StringVar()
        self.entry = Entry(self, width=30, textvariable=self.text)
        self.entry.pack(side="right")


def calculate(wh, hg):
    # weight = input("Gewicht in kg: ")
    if not wh:
        return
    return round(float(wh) / (float(hg) ** 2), 2)


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
            self.btnFrame, text="OK", width=20, command=self.action)
        self.cancelBtn = Button(
            self.btnFrame, text="Cancel", width=20, command=root.destroy)
        self.okBtn.pack(side="left")
        self.cancelBtn.pack(side="right")
        self.listbox = Listbox(master)
        self.listbox.pack(fill=BOTH)

    def action(self):
        user = User(self.nameFrame.text.get(), self.firstFrame.text.get(), self.heightFrame.text.get())
        bmicalculator = BmiCalculator()
        bmi = bmicalculator.calculate(user.height, self.weightFrame.text.get())
        bmicalculator.adding(user.name, user.firstName, bmi)
        self.listbox.delete(0, END)
        if user.name in bmicalculator.dataspace:
            bmis = bmicalculator.dataspace[user.name]
            for bmi in bmis:
                self.listbox.insert(END, user.name + " " + user.firstName + " => " + str(bmi) +
                                    " => " + bmicalculator.analyse(bmi))


root = Tk()
Application(master=root)
root.mainloop()
