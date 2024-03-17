import tkinter
import tkinter as tk
from tkinter import ttk



class Puissance(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title('Puissance 4')

        self.boutons = []

        self.puissance4()

    def puissance4(self):
        print("Puissance4")
        self.label = tk.Label(self, text='Puissance4')
        self.label.grid(column=3)
        self.boutons.clear()
        for self.column in range(7):
            self.bouton_column = []
            for self.row in range(6):
                self.bouton = ttk.Button(
                    self,
                    padding=20,
                    text="alled",
                    command=print("teutue")
                )
                self.bouton.grid(row=self.row + 1, column=self.column)
                self.bouton_column.append(self.bouton)
            self.boutons.append(self.bouton_column)
