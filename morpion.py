import tkinter
import tkinter as tk
from tkinter import ttk

class Morpion(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title('Morpion')
        # variables morpions
        self.current_player = "X"
        self.win = False
        self.boutons = []

        self.morpion()

    def winner(self):
        if self.win is False:
            self.win = True
            self.label = tk.Label(self, text='le Gagnant est ' + self.current_player)
            print(self.current_player, "win")
            self.delete_button_worker(self.boutons)


    def swi_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"


    def verif_win(self, click_row, click_col, boutons):
        # detec ligne gagnante
        self.count = 0
        for self.i in range(3):
            self.current_bouton = boutons[self.i][click_row]
            if self.current_bouton["text"] == self.current_player:
                self.count += 1
        if self.count == 3:
            self.winner()
            return 3
        # detec ligne gagnante
        self.count = 0
        for self.i in range(3):
            self.current_bouton = boutons[click_col][self.i]
            if self.current_bouton["text"] == self.current_player:
                self.count += 1
        if self.count == 3:
            self.winner()
            return 3
        # detec ligne gagnante
        self.count = 0
        for self.i in range(3):
            self.current_bouton = boutons[self.i][self.i]
            if self.current_bouton["text"] == self.current_player:
                self.count += 1
        if self.count == 3:
            self.winner()
            return 3
        # detec ligne gagnante
        count = 0
        for self.i in range(3):
            self.current_bouton = boutons[2 - self.i][self.i]
            if self.current_bouton["text"] == self.current_player:
                self.count += 1
        if self.count == 3:
            self.winner()
            return 3

        if self.win is False:
            self.count = 0
            for self.col in range(3):
                for self.row in range(3):
                    self.current_bouton = boutons[self.col][self.row]
                    if self.current_bouton["text"] == "X" or self.current_bouton["text"] == "O":
                        self.count += 1
            if self.count == 9:
                print('match nul')
                return 3
        else:
            return 3


    def place_symb(self, row, column, boutons):
        self.action = boutons[column][row]
        if self.action["text"] == "":
            self.action.config(text=self.current_player)
            self.fin = self.verif_win(row, column, boutons)
            if self.fin == 3:
                pass
            self.swi_player()

    def delete_button_worker(self, cursed_data_structure):

        if isinstance(cursed_data_structure, ttk.Button):
            cursed_data_structure.destroy()
        else:
            for cursed_container in cursed_data_structure:
                self.delete_button_worker(cursed_container)
    def morpion(self):
        #mise en place du plateau morpion
        self.label = tk.Label(self, text='Morpion')
        self.label.grid(column=1)
        self.boutons.clear()
        for self.column in range(3):
            self.bouton_column = []
            for self.row in range(3):
                self.bouton = ttk.Button(
                    self,
                    padding=15,
                    command=lambda r=self.row, c=self.column: self.place_symb(r, c, self.boutons)
                    )
                self.bouton.grid(row=self.row+1, column=self.column)
                self.bouton_column.append(self.bouton)
            self.boutons.append(self.bouton_column)

