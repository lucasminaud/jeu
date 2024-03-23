import tkinter
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


class Puissance:
    def __init__(self, main_win):
        self.main_win = main_win
        main_win.title('Puissance 4')

        self.boutons = []

        # integration des images
        image_attente = Image.open("./assets/blanc.png").resize((30, 40), Image.NEAREST)
        imageR = Image.open("./assets/raton.jpg").resize((30, 40), Image.NEAREST)
        imageT = Image.open("./assets/tacos.jpg").resize((30, 40), Image.NEAREST)
        main_win.blanc = ImageTk.PhotoImage(image=image_attente)
        main_win.raton = ImageTk.PhotoImage(imageR)
        main_win.tacos = ImageTk.PhotoImage(imageT)

        self.current_player = main_win.raton
        self.puissance4()

    def swi_player(self):
        if self.current_player == self.main_win.raton:
            self.current_player = self.main_win.tacos
        else:
            self.current_player = self.main_win.raton

    def verif_win(self, click_row, click_col, boutons):
        # detec ligne gagnante
        count = 0
        i = 0
        for i in range(4):
            current_bouton = boutons[click_row-i][click_col-i]
            if current_bouton["image"][0] != str(self.current_player):
                print(current_bouton["text"])
                break
            else:
                count += 1
                print(count)
                print(current_bouton["text"])



    def place_symb(self,column, row, boutons):
        for i in range(6):
            rowP = 5-i
            action = boutons[rowP][column]
            if action["image"][0] == str(self.main_win.blanc):
                action.config(image=self.current_player)
                fin = self.verif_win(rowP, column, boutons)
                if fin == 3:
                    pass
                self.swi_player()
                break


    def puissance4(self):
        print("Puissance4")
        i = 0
        self.main_win.label = tk.Label(self.main_win, text='puissance4')
        self.main_win.label.grid(column=3)
        self.boutons.clear()
        for row in range(6):
            self.bouton_column = []
            for column in range(7):
                self.bouton = ttk.Button(
                    self.main_win,
                    text=str(i),
                    padding=15,
                    command=lambda r=row, c=column: self.place_symb(c, r, self.boutons),
                    image=self.main_win.blanc
                )
                i += 1
                self.bouton.grid(row=row + 1, column=column)
                self.bouton_column.append(self.bouton)
            self.boutons.append(self.bouton_column)
