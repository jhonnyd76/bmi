from tkinter import *


class MainFrame(Frame):
    def __init__(self, master=None, lblText="", lblSide="", entrySide="", lblAnchor=ANCHOR):
        Frame.__init__(self, master)
        self.pack()
        self.label = Label(self, text=lblText, width=30, anchor=lblAnchor)
        self.label.pack(side=lblSide)
        self.text = StringVar()
        self.entry = Entry(self, width=30, textvariable=self.text)
        self.entry.pack(side=entrySide)
