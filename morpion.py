import tkinter
import tkinter as tk
from tkinter import ttk, Canvas
from PIL import ImageTk, Image

class Morpion:
    def __init__(self, main_win):
        self.main_win = main_win
        main_win.title('Morpion')
        # variables morpions

        self.win = False
        self.boutons = []
        #integration des images
        image_attente = Image.open("./assets/blanc.png").resize((150, 200), Image.NEAREST)
        imageR = Image.open("./assets/raton.jpg").resize((150, 200), Image.NEAREST)
        imageT = Image.open("./assets/tacos.jpg").resize((150, 200), Image.NEAREST)
        main_win.blanc = ImageTk.PhotoImage(image=image_attente)
        main_win.raton = ImageTk.PhotoImage(imageR)
        main_win.tacos = ImageTk.PhotoImage(imageT)

        self.current_player = main_win.raton

        self.morpion()

    def winner(self):
        if self.win is False:
            self.win = True
            self.main_win.label.destroy()
            self.main_win.label = tk.Label(self.main_win, text='le Gagnant est ' + str(self.current_player))
            print(self.current_player, "win")
            self.delete_button_worker(self.boutons)
            self.main_win.label.grid(column=0)

            self.bouton = ttk.Button(
                self.main_win,
                text="teuteu",
                command=self.main_win.main,
                image=self.current_player
            )

            self.bouton.grid()



    def swi_player(self):
        if self.current_player == self.main_win.raton:
            self.current_player = self.main_win.tacos
        else:
            self.current_player = self.main_win.raton


    def verif_win(self, click_row, click_col, boutons):
        # detec ligne gagnante
        i=0
        checks = (
            lambda x, y: x[y][click_row],
            lambda x, y: x[click_col][y],
            lambda x, y: x[y][y],
            lambda x, y: x[2-y][y],
        )
        for expr in checks:
            count = 0
            for i in range(3):
                current_bouton = expr(boutons, i)
                # Si on est pas sur une série gagnante, on skip jusqu'à la suivante
                if current_bouton["image"][0] != str(self.current_player):
                    break
            else:
                self.winner()
                return count
        # Aucun gagnant de trouvé
        else:
            count = 0
            for col in range(3):
                for row in range(3):
                    current_bouton = boutons[col][row]
                    if current_bouton["image"][0] != str(self.main_win.blanc):
                        count += 1
            # Toutes les cases sont remplies
            if count == 9:
                print('match nul')
        return 3


    def place_symb(self, row, column, boutons):
        action = boutons[column][row]
        if action["text"] == "":
            action.config(image=self.current_player)
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
                    command=lambda r=row, c=column: self.place_symb(r, c, self.boutons),
                    image=self.main_win.blanc
                    )
                self.bouton.grid(row=row+1, column=column)
                bouton_column.append(self.bouton)
            self.boutons.append(bouton_column)

