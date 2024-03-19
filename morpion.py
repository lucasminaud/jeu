import tkinter
import tkinter as tk
from tkinter import ttk, Canvas
from PIL import ImageTk, Image

class Morpion:
    def __init__(self, main_win):
        self.main_win = main_win
        main_win.title('Morpion')
        # variables morpions
        self.current_player = "X"
        self.win = False
        self.boutons = []


        self.morpion()

    def winner(self):
        if self.win is False:
            self.win = True
            self.main_win.label.destroy()
            self.main_win.label = tk.Label(self.main_win, text='le Gagnant est ' + self.current_player)
            print(self.current_player, "win")
            self.delete_button_worker(self.boutons)
            self.main_win.label.grid(column=0)


            image = Image.open("./assets/raton.jpg")
            image = image.resize((400,300), Image.NEAREST)

            self.bouton = ttk.Button(
                self.main_win,
                text="teuteu",
                command=self.main_win.main,
                image=ImageTk.PhotoImage(image)
            )
            canvas = Canvas(self.bouton, width=400, height=300)
            canvas.image = ImageTk.PhotoImage(image)
            canvas.create_image(0, 0, image=canvas.image, anchor='nw')

            self.bouton.grid()



    def swi_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"


    def verif_win(self, click_row, click_col, boutons):
        # detec ligne gagnante
        count = 0
        for i in range(3):
            current_bouton = boutons[i][click_row]
            if current_bouton["text"] == self.current_player:
                count += 1
        if count == 3:
            self.winner()
            return 3
        # detec ligne gagnante
        count = 0
        for i in range(3):
            current_bouton = boutons[click_col][i]
            if current_bouton["text"] == self.current_player:
                count += 1
        if count == 3:
            self.winner()
            return 3
        # detec ligne gagnante
        count = 0
        for i in range(3):
            current_bouton = boutons[i][i]
            if current_bouton["text"] == self.current_player:
                count += 1
        if count == 3:
            self.winner()
            return 3
        # detec ligne gagnante
        count = 0
        for i in range(3):
            current_bouton = boutons[2 - i][i]
            if current_bouton["text"] == self.current_player:
                count += 1
        if count == 3:
            self.winner()
            return 3

        if self.win is False:
            count = 0
            for col in range(3):
                for row in range(3):
                    current_bouton = boutons[col][row]
                    if current_bouton["text"] == "X" or current_bouton["text"] == "O":
                        count += 1
            if count == 9:
                print('match nul')
                return 3
        else:
            return 3


    def place_symb(self, row, column, boutons):
        action = boutons[column][row]
        if action["text"] == "":
            action.config(text=self.current_player)
            fin = self.verif_win(row, column, boutons)
            if fin == 3:
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
        self.main_win.label = tk.Label(self.main_win, text='Morpion')
        self.main_win.label.grid(column=1)
        self.boutons.clear()
        for column in range(3):
            bouton_column = []
            for row in range(3):
                self.bouton = ttk.Button(
                    self.main_win,
                    padding=15,
                    command=lambda r=row, c=column: self.place_symb(r, c, self.boutons)
                    )
                self.bouton.grid(row=row+1, column=column)
                bouton_column.append(self.bouton)
            self.boutons.append(bouton_column)

